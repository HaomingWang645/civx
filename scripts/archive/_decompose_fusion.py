#!/usr/bin/env python3
"""Decompose fusion-power into component techs:
  - magnetic-confinement-fusion (tokamak path)
  - inertial-confinement-fusion (laser-driven path)
  - tritium-breeding (fuel cycle)
And update fusion-power's prereqs to gate on the new chain."""

import json, re
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Fusion power decomposition ───
  { id: "inertial-confinement-fusion", name: "Inertial Confinement Fusion", era: "future", category: "energy",
    year: "2035", prereqs: ["plasma-physics", "advanced-chip-manufacturing"],
    desc: "Compressing a millimeter-scale deuterium-tritium fuel pellet by 192 simultaneous laser pulses faster than it can fly apart, briefly reaching the ~100 million °C and ~100 g/cm³ conditions for fusion. The U.S. National Ignition Facility (Lawrence Livermore) achieved the first laboratory ignition (Q>1) in December 2022, releasing more fusion energy than the lasers delivered to the target. By the mid-2030s repeatable, higher-gain ignition becomes routine; the path to a commercial inertial-fusion power plant remains harder than tokamaks (rep-rate, target-injection, optic damage), but inertial fusion provides invaluable physics data and unlocks pulsed-fusion propulsion concepts." },
  { id: "magnetic-confinement-fusion", name: "Magnetic Confinement Fusion", era: "future", category: "energy",
    year: "2040", prereqs: ["plasma-physics", "advanced-chip-manufacturing"],
    desc: "A toroidal magnetic field bottles a hot deuterium-tritium plasma so it never touches the chamber walls, enabling steady-state fusion at Q>10 (ten times more energy out than in). ITER (Cadarache, France, first plasma 2034) and Commonwealth Fusion Systems' SPARC (high-temperature-superconductor tokamak) target the breakthrough; the Joint European Torus, EAST, and KSTAR provide the operational experience base. By 2040 sustained burning plasma is routine in multiple machines worldwide. The challenge transitions from physics to engineering: divertor heat loads, neutron-induced material damage, and continuous tritium fueling all need solving before commercial reactors are economic." },
  { id: "tritium-breeding", name: "Tritium Breeding", era: "future", category: "energy",
    year: "2050", prereqs: ["magnetic-confinement-fusion", "nuclear-power"],
    desc: "Generating tritium fuel in-situ by capturing fusion neutrons in a lithium-bearing blanket surrounding the reactor: ⁶Li + n → ⁴He + ³T. Natural tritium is essentially nonexistent (a few kg globally, mostly from fission reactors), so any commercial fusion economy must breed its own. The blanket must achieve a tritium breeding ratio >1.05 to compensate for losses, while also extracting useful heat. ITER's test blanket modules (TBM program) and DEMO-class follow-ons mature the technology through the 2040s. Tritium breeding closes the fusion fuel cycle and is the gating engineering capability between magnetic-confinement physics and grid-scale fusion electricity." },
"""

TRANSLATIONS = {
    "inertial-confinement-fusion":  "惯性约束聚变",
    "magnetic-confinement-fusion":  "磁约束聚变",
    "tritium-breeding":             "氚增殖",
}

UNLOCKS = {
    "inertial-confinement-fusion": [
        ("unit",     "National Ignition Facility", "国家点火装置",       "National Ignition Facility"),
        ("org",      "Lawrence Livermore National Laboratory", "劳伦斯利弗莫尔国家实验室", "Lawrence Livermore National Laboratory"),
        ("resource", "Inertial confinement fusion", "惯性约束聚变",      "Inertial confinement fusion"),
        ("unit",     "Laser Mégajoule",            "兆焦耳激光装置",     "Laser Mégajoule"),
    ],
    "magnetic-confinement-fusion": [
        ("unit",     "ITER",                       "国际热核聚变实验堆", "ITER"),
        ("unit",     "Joint European Torus",       "欧洲联合环",         "Joint European Torus"),
        ("unit",     "SPARC",                      "SPARC 紧凑型托卡马克", "SPARC (tokamak)"),
        ("unit",     "EAST",                       "东方超环",           "Experimental Advanced Superconducting Tokamak"),
        ("resource", "Tokamak",                    "托卡马克",           "Tokamak"),
        ("resource", "Stellarator",                "仿星器",             "Stellarator"),
        ("org",      "Commonwealth Fusion Systems","联邦聚变系统公司",   "Commonwealth Fusion Systems"),
    ],
    "tritium-breeding": [
        ("resource", "Tritium",                    "氚",                 "Tritium"),
        ("resource", "Lithium-6",                  "锂-6",               "Lithium-6"),
        ("resource", "Tritium breeding ratio",     "氚增殖比",            "Breeder reactor"),
        ("unit",     "ITER Test Blanket Module",   "ITER 试验包层模块",   "ITER"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "magnetic-confinement-fusion" in src:
        print("data.js: components already inserted")
    else:
        marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
        if marker not in src:
            raise SystemExit("Closing marker not found")
        src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")
        print(f"data.js: +3 fusion component techs")

    # Update fusion-power prereqs to gate on the new chain.
    old_fp = '{ id: "fusion-power", name: "Fusion Power", era: "future", category: "energy",\n    year: "2060", prereqs: ["nuclear-power", "plasma-physics", "advanced-chip-manufacturing"]'
    new_fp = '{ id: "fusion-power", name: "Fusion Power", era: "future", category: "energy",\n    year: "2060", prereqs: ["magnetic-confinement-fusion", "tritium-breeding"]'
    if old_fp in src:
        src = src.replace(old_fp, new_fp)
        print("  fusion-power prereqs updated to gate on magnetic-confinement-fusion + tritium-breeding")
    elif new_fp in src:
        print("  fusion-power prereqs already updated")
    else:
        print("  WARNING: fusion-power prereq pattern not found")
    DATA.write_text(src)


def splice_translations():
    src = TRANS.read_text()
    if '"magnetic-confinement-fusion"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Fusion power decomposition ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"magnetic-confinement-fusion"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Fusion power decomposition ───\n"
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
