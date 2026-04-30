#!/usr/bin/env python3
"""Add Reversible Computing (Near Future) and Civilizational Entropy
Management (Far Future), and gate matrioshka-brain on reversible-computing."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Entropy / thermodynamic computing ───
  { id: "reversible-computing", name: "Reversible Computing", era: "future", category: "tools",
    year: "2090", prereqs: ["quantum-computing", "photonic-computing"],
    desc: "Computation that avoids erasing bits, escaping the Landauer limit (kT ln 2 of heat dissipated per bit erased) that puts a hard thermodynamic floor under conventional logic. Charles Bennett (1973) proved any computation can in principle be performed reversibly; Edward Fredkin and Tommaso Toffoli's reversible logic gates (1982) and adiabatic CMOS (1990s) provided practical implementations. By 2090 reversible-logic chips become essential at the densest compute scales — the Landauer limit is otherwise the hardest constraint on chips approaching atomic feature sizes. Reversible computing is the gating technology between classical chip scaling and full computronium architectures (matrioshka brains, Jupiter brains)." },
  { id: "civilizational-entropy-management", name: "Civilizational Entropy Management", era: "far-future", category: "energy",
    year: "2400", prereqs: ["dyson-swarm", "reversible-computing"],
    desc: "Engineering the thermodynamic budget of a Type II civilization as a managed resource: nested-temperature compute architectures, controlled radiation patterns at megastructure scale, deliberate use of cosmic background as a heat sink, and operational planning around the entropy cost of every large-scale process. Freeman Dyson's 'Time Without End' (1979) framed the cosmological end-point — that subjectively unbounded civilization can be sustained against heat death by clocking computation progressively slower as the universe cools. Practical entropy management at galactic scale becomes a routine engineering discipline once Type II energy budgets are achieved, with its own institutions, mathematicians, and planning horizons measured in megayears." },
"""

TRANSLATIONS = {
    "reversible-computing":            "可逆计算",
    "civilizational-entropy-management":"文明级熵管理",
}

UNLOCKS = {
    "reversible-computing": [
        ("person",   "Rolf Landauer",        "罗尔夫·兰道尔",       "Rolf Landauer"),
        ("person",   "Charles H. Bennett",   "查尔斯·H·贝内特",     "Charles H. Bennett (computer scientist)"),
        ("person",   "Edward Fredkin",       "爱德华·弗雷德金",     "Edward Fredkin"),
        ("resource", "Landauer's principle", "兰道尔原理",          "Landauer's principle"),
        ("resource", "Toffoli gate",         "Toffoli 门",           "Toffoli gate"),
        ("resource", "Adiabatic logic",      "绝热逻辑",            "Adiabatic logic"),
    ],
    "civilizational-entropy-management": [
        ("person",   "Freeman Dyson",        "弗里曼·戴森",         "Freeman Dyson"),
        ("work",     "Time Without End",     "《无终之时》",         "Heat death of the universe"),
        ("resource", "Black hole thermodynamics","黑洞热力学",       "Black hole thermodynamics"),
        ("resource", "Bekenstein bound",     "贝肯斯坦边界",        "Bekenstein bound"),
        ("unit",     "Cascaded-temperature compute shell", "级联温度计算壳层", False),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "reversible-computing" in src:
        print("data.js: components already inserted")
    else:
        marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
        if marker not in src:
            raise SystemExit("Closing marker not found")
        src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")
        print("data.js: +2 entropy/reversible-computing techs")

    # Update matrioshka-brain prereqs to include reversible-computing.
    old_mb = '"matrioshka-brain", name: "Matrioshka Brain", era: "far-future", category: "tools",\n    year: "2400", prereqs: ["dyson-swarm", "advanced-chip-manufacturing", "agi"]'
    new_mb = '"matrioshka-brain", name: "Matrioshka Brain", era: "far-future", category: "tools",\n    year: "2400", prereqs: ["dyson-swarm", "reversible-computing", "agi"]'
    if old_mb in src:
        src = src.replace(old_mb, new_mb)
        print("  matrioshka-brain prereqs updated to gate on reversible-computing")
    elif new_mb in src:
        print("  matrioshka-brain already updated")
    else:
        print("  WARNING: matrioshka-brain prereq pattern not found")
    DATA.write_text(src)


def splice_translations():
    src = TRANS.read_text()
    if '"reversible-computing"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Entropy / thermodynamic computing ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"reversible-computing"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Entropy / thermodynamic computing ───\n"
    for tid, items in UNLOCKS.items():
        block += f'  "{tid}": [\n'
        for typ, name, name_zh, wiki in items:
            wiki_part = ' wiki: false' if wiki is False else f' wiki: {json.dumps(wiki, ensure_ascii=False)}'
            block += (f'    {{ type: "{typ}", '
                      f'name: {json.dumps(name, ensure_ascii=False)}, '
                      f'name_zh: {json.dumps(name_zh, ensure_ascii=False)},'
                      f'{wiki_part} }},\n')
        block += '  ],\n'
    rs = src.rstrip(); assert rs.endswith("};")
    UNLOCKS_PATH.write_text(rs[:-2] + block + "};\n")
    print(f"unlocks.js: +{len(UNLOCKS)}")


if __name__ == "__main__":
    splice_data()
    splice_translations()
    splice_unlocks()
