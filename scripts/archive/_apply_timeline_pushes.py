#!/usr/bin/env python3
"""Push optimistic future/far-future tech timings later, per consensus
expert estimates. Includes cascade fixes for downstream prereqs."""

import re
from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")

# (id, new_year, new_era_or_None_to_keep)
YEAR_AND_ERA_CHANGES = [
    # ── Future Age year changes (no era change) ──
    ("agi", "2045", None),
    ("liquid-democracy", "2050", None),  # cascade from agi
    ("fusion-power", "2060", None),
    ("fusion-rocket", "2075", None),     # cascade from fusion-power
    ("mars-colony", "2075", None),
    ("room-temp-superconductor", "2070", None),

    # ── Future → Far-Future (era + year change) ──
    ("nanotechnology", "2150", "far-future"),
    ("quantum-gravity", "2200", "far-future"),
    ("p-vs-np-resolved", "2150", "far-future"),
    ("programmable-matter", "2200", "far-future"),
    ("space-elevator", "2250", "far-future"),
    ("orbital-ring", "2200", "far-future"),
    ("superintelligence", "2120", "far-future"),

    # ── Far Future year changes ──
    ("digital-immortality", "2250", None),
    ("substrate-independent-humanity", "2300", None),
    ("post-human-aesthetics", "2350", None),     # cascade from SIH
    ("time-dilation-cultures", "2450", None),    # cascade from matrioshka
    ("dyson-swarm", "2350", None),
    ("matrioshka-brain", "2400", None),
    ("kardashev-type-ii", "2400", None),
    ("generation-ship-colony", "2350", None),
    ("antimatter-production", "2400", None),
    ("warp-drive", "2700", None),
]

# Tech-id -> new prereq list (to override entirely)
PREREQ_OVERRIDES = {
    # metamaterials no longer requires nanotechnology (which moved to 2150) or
    # room-temp superconductor (now 2070). Real metamaterials use ordinary
    # dielectrics / engineered geometry; keep advanced chip manufacturing.
    "metamaterials": ["advanced-chip-manufacturing"],
}


def apply_year_era_change(src, tech_id, new_year, new_era):
    # Match the entry: { id: "X", name: "...", era: "...", category: "...", year: "..."
    pat = re.compile(
        r'(\{\s*id:\s*"' + re.escape(tech_id) + r'"\s*,'
        r'\s*name:\s*"[^"]+"\s*,'
        r'\s*era:\s*")([^"]+)("\s*,'
        r'\s*category:\s*"[^"]+"\s*,'
        r'\s*year:\s*")([^"]+)(")', re.S)
    m = pat.search(src)
    if not m:
        return src, False, f"entry not found"
    old_era = m.group(2); old_year = m.group(4)
    target_era = new_era if new_era else old_era
    new_block = m.group(1) + target_era + m.group(3) + new_year + m.group(5)
    return src[:m.start()] + new_block + src[m.end():], True, f"era={old_era}→{target_era} year={old_year}→{new_year}"


def apply_prereq_override(src, tech_id, new_prereqs):
    pat = re.compile(
        r'(\{\s*id:\s*"' + re.escape(tech_id) + r'"\s*,'
        r'(?:[^{}]|\{[^{}]*\})*?'
        r'prereqs:\s*\[)[^\]]*(\])', re.S)
    m = pat.search(src)
    if not m:
        return src, False
    new_str = ", ".join(f'"{p}"' for p in new_prereqs)
    return src[:m.start(1)] + m.group(1) + new_str + m.group(2) + src[m.end():], True


def main():
    src = DATA.read_text()

    # Extend Far Future era range to fit warp drive at 2700
    old_range = '  { id: "far-future",    name: "Far Future",         range: "2100 – 2500" },'
    new_range = '  { id: "far-future",    name: "Far Future",         range: "2100 – 2800" },'
    if old_range in src:
        src = src.replace(old_range, new_range)
        print("  ✓ Far Future era range: 2100–2500 → 2100–2800")

    # Apply year/era changes
    print("\n── Year and era changes ──")
    for tech_id, new_year, new_era in YEAR_AND_ERA_CHANGES:
        src, ok, msg = apply_year_era_change(src, tech_id, new_year, new_era)
        mark = "✓" if ok else "✗"
        print(f"  {mark} {tech_id:35} {msg}")

    # Apply prereq overrides
    print("\n── Prereq overrides ──")
    for tech_id, new_prereqs in PREREQ_OVERRIDES.items():
        src, ok = apply_prereq_override(src, tech_id, new_prereqs)
        mark = "✓" if ok else "✗"
        print(f"  {mark} {tech_id:35} prereqs → {new_prereqs}")

    DATA.write_text(src)
    print("\nWrote", DATA)


if __name__ == "__main__":
    main()
