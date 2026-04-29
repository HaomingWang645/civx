#!/usr/bin/env python3
"""Surgically edit data.js to:
  1. Add prereq edges so most leaf techs lead somewhere downstream.
  2. Detect and fix year inversions (prereqs dated AFTER their dependent).

Re-runnable: each addition is idempotent (skips if prereq already present)."""
import re, sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data.js"

# Prereq additions: dependent_id -> [new_prereq_id, ...]
ADDITIONS = {
    "wooden-spear":          ["wooden-club"],
    "village":               ["windbreaks"],
    "plow-ard":              ["digging-stick"],
    "trade-networks":        ["shell-beads"],
    "pottery":               ["water-flask"],
    "cuneiform":             ["proto-language"],
    "weaving":               ["needles"],
    "fish-weir":             ["fishing-net"],
    "distillation":          ["fermentation-brewing"],
    "mathematics-arithmetic":["abacus"],
    "medicine-galenic":      ["trepanation"],
    "iron-smelting":         ["iron-meteoric"],
    "alphabet-phoenician":   ["hieroglyphics"],
    "monumental-architecture":["adobe-brick"],
    "paper-mill":            ["millstone"],
    "musket":                ["crossbow", "longbow"],
    "artillery":             ["siege-engine"],
    "galleon":               ["triremes"],
    "bastion-fortification": ["castle"],
    "machine-gun":           ["musket"],
    "cavalry":               ["chariot"],
    "vaccination":           ["hospital"],
    "joint-stock-company":   ["guild"],
    "enlightenment-philosophy":["protestant-reformation"],
    "relativity":            ["gravitation-law"],
    "calculus":              ["cartesian-coordinates"],
    "thermodynamics":        ["thermometer"],
    "green-revolution":      ["crop-rotation-norfolk"],
    "railway-locomotive":    ["canal-system"],
    "highway-system":        ["turnpike-roads", "railroad-network"],
    "welfare-state":         ["labor-union", "separation-of-powers"],
    "modern-corporation":    ["modern-bookkeeping"],
    "assembly-line":         ["power-loom"],
    "printing-press":        ["quill-ink"],
    "cinema":                ["opera-orchestra"],
    "skyscraper":            ["elevator"],
    "bessemer-steel":        ["steel-bloomery"],
}

# Prereq removals: dependent_id -> [prereq_id_to_remove, ...]
# Used to fix year inversions where the prereq isn't strictly required, or
# where the prereq direction was simply backwards.
REMOVALS = {
    "social-media":           ["smartphone"],          # Facebook 2004 predates iPhone 2007
    "megaliths":              ["village"],             # Göbekli Tepe predates village life
    "solar-calendar":         ["astronomy-observation"],# Egyptian cal predates Babylonian astronomy
    "pyramid-ziggurat":       ["mathematics-arithmetic"],# pyramids predate Babylonian math
    "arch-vault":             ["geometry-euclidean"],  # Etruscan arches predate Euclid
    "siege-engine":           ["geometry-euclidean"],  # catapults predate Euclid
    "library":                ["paper-making"],        # Alexandria used scrolls
    "magnetic-compass-marine":["caravel"],             # marine compass on earlier ships
    "vernacular-literature":  ["printing-press"],      # Dante predates Gutenberg
    "colonialism":            ["mercantilism"],        # 1500 colonialism predates 1550 mercantilism
    "calculus":               ["newtonian-mechanics"], # Leibniz 1684 predates Principia 1687
    "electricity-static":     ["chemistry-modern"],    # Franklin 1750 predates Lavoisier 1789
    "crop-rotation-norfolk":  ["agricultural-revolution"], # Norfolk caused, didn't follow
    "separation-of-powers":   ["liberal-democracy"],   # Montesquieu 1748 predates 1789
    "spinning-jenny":         ["factory-system"],      # jenny 1764 predates factory system
    "railway-locomotive":     ["bessemer-steel"],      # 1814 used wrought iron, not steel
    "machine-tool":           ["bessemer-steel"],      # Maudslay 1797–1820 used iron
    "digital-computer":       ["transistor"],          # ENIAC 1945 was vacuum tubes
    "united-nations":         ["decolonization"],      # UN 1945 predates decolonization wave
    "ivf":                    ["gene-sequencing"],     # IVF 1978 predates HGP 2003
    "atomic-theory":          ["periodic-table"],      # Dalton 1808 predates Mendeleev 1869
    "ocean-navigation":       ["galleon"],             # Columbus used caravels, not galleons
}

# Update tech.year strings to fix inversions / clarify timing.
YEAR_CHANGES = {
    "letter-of-credit":  "~1300 CE",  # was ~1200; Italian merchant bills mature with double-entry
    "ocean-navigation":  "1480",      # was 1500; Columbus 1492 used it
    "arpanet-internet":  "1969",      # was 1983; ARPANET first ran 1969 (TCP/IP renamed it later)
    "public-sanitation": "1865",      # was 1858; align after germ theory 1860
}


def parse_year(s):
    """Return numeric year (negative = past), or None if unparseable."""
    if not s: return None
    s = s.strip().lstrip("~").strip()
    # Strip parenthetical aside: "12 kya (widespread)" → "12 kya"
    s = re.sub(r"\s*\(.*?\)\s*", "", s).strip()
    # Range "1300–1500" or "1300-1500": take first
    m = re.match(r"^([\d\.]+)\s*[–\-]\s*([\d\.]+)\s*([A-Za-z]*)$", s)
    if m:
        s = m.group(1) + " " + (m.group(3) or "")
    m = re.match(r"^(-?[\d\.]+)\s*([A-Za-z]*)\s*", s.strip())
    if not m: return None
    num = float(m.group(1)); unit = m.group(2).upper()
    if unit == "MYA":           return -num * 1_000_000
    if unit == "KYA":           return -num * 1000
    if unit in ("BCE", "BC"):   return -num
    if unit in ("CE", "AD", ""): return num
    return num


def parse_techs(src):
    pat = re.compile(
        r'\{\s*id:\s*"([^"]+)"\s*,'
        r'\s*name:\s*"([^"]+)"\s*,'
        r'\s*era:\s*"([^"]+)"\s*,'
        r'\s*category:\s*"([^"]+)"\s*,'
        r'\s*year:\s*"([^"]+)"\s*,'
        r'\s*prereqs:\s*\[([^\]]*)\]', re.S)
    out = []
    for m in pat.finditer(src):
        prereqs = re.findall(r'"([^"]+)"', m.group(6))
        out.append({"id": m.group(1), "name": m.group(2), "era": m.group(3),
                    "category": m.group(4), "year": m.group(5), "prereqs": prereqs,
                    "yearNum": parse_year(m.group(5))})
    return out


def edit_prereqs(src, tech_id, fn):
    """Apply fn(prereqs_list) -> new_prereqs_list to a tech entry in-place."""
    pat = re.compile(
        r'(\{\s*id:\s*"' + re.escape(tech_id) + r'"\s*,'
        r'(?:[^{}]|\{[^{}]*\})*?'
        r'prereqs:\s*\[)([^\]]*)(\])', re.S)
    m = pat.search(src)
    if not m:
        return src, False
    old = re.findall(r'"([^"]+)"', m.group(2))
    new = fn(old)
    if new == old:
        return src, False
    new_str = ", ".join(f'"{p}"' for p in new)
    return src[:m.start(2)] + new_str + src[m.end(2):], True


def main():
    src = DATA.read_text()
    techs = parse_techs(src)
    techs_by_id = {t["id"]: t for t in techs}

    # ── 1. Apply additions ──
    added = 0; skipped = 0
    for dep_id, new_prereqs in ADDITIONS.items():
        if dep_id not in techs_by_id:
            print(f"  ! ADD: unknown tech {dep_id}"); continue
        for np in new_prereqs:
            if np not in techs_by_id:
                print(f"  ! ADD: unknown prereq {np} for {dep_id}"); continue
            def fn(old, np=np):
                if np in old: return old
                return old + [np]
            src, changed = edit_prereqs(src, dep_id, fn)
            if changed: added += 1; print(f"  +  {dep_id:30} ← {np}")
            else: skipped += 1
    print(f"\nAdditions: {added} applied, {skipped} skipped (already present or unchanged)")

    # ── 2. Apply removals ──
    removed = 0
    for dep_id, kill in REMOVALS.items():
        for k in kill:
            def fn(old, k=k):
                return [p for p in old if p != k]
            src, changed = edit_prereqs(src, dep_id, fn)
            if changed: removed += 1; print(f"  -  {dep_id:30} ✗ {k}")
    print(f"\nRemovals: {removed}")

    # ── 3. Apply year changes ──
    year_changed = 0
    for tech_id, new_year in YEAR_CHANGES.items():
        pat = re.compile(
            r'(\{\s*id:\s*"' + re.escape(tech_id) + r'"\s*,'
            r'(?:[^{}]|\{[^{}]*\})*?'
            r'year:\s*)"[^"]*"', re.S)
        new_src, n = pat.subn(lambda m: m.group(1) + '"' + new_year + '"', src)
        if n == 1:
            src = new_src; year_changed += 1
            print(f"  ~  {tech_id:30} year → {new_year}")
        elif n == 0:
            print(f"  ! year change: tech not found {tech_id}")
    print(f"\nYear changes: {year_changed}")

    DATA.write_text(src)

    # ── 3. Re-parse and report ──
    techs = parse_techs(src)
    techs_by_id = {t["id"]: t for t in techs}
    children = {t["id"]: [] for t in techs}
    for t in techs:
        for p in t["prereqs"]:
            if p in children: children[p].append(t["id"])

    leaves = [t for t in techs if not children[t["id"]]]
    print(f"\nLeaves: {len(leaves)} / {len(techs)}")

    # Year inversions
    print("\nYear inversions (prereq dated AFTER its dependent):")
    inv = 0
    for t in techs:
        if t["yearNum"] is None: continue
        for p in t["prereqs"]:
            pt = techs_by_id.get(p)
            if not pt or pt["yearNum"] is None: continue
            if pt["yearNum"] > t["yearNum"]:
                print(f"  ! {p}({pt['year']}) → {t['id']}({t['year']})")
                inv += 1
    print(f"Total inversions: {inv}")


if __name__ == "__main__":
    main()
