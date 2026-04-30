#!/usr/bin/env python3
"""Add 6 techs:
  Set 1 (interstellar propulsion):
    beamed-sail-propulsion, nuclear-pulse-propulsion,
    bussard-ramjet, antimatter-propulsion
  Set 2 (quantum sensing/timing):
    optical-atomic-clock, quantum-sensing
"""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Interstellar propulsion + quantum precision ───
  { id: "optical-atomic-clock", name: "Optical Atomic Clock", era: "information", category: "knowledge",
    year: "2014", prereqs: ["quantum-mechanics", "semiconductor"],
    desc: "Atomic clocks based on optical (rather than microwave) transitions in laser-cooled atoms or ions. Strontium and ytterbium optical lattice clocks (Jun Ye / NIST-JILA, 2014) achieved fractional accuracy below 10⁻¹⁸ — equivalent to losing or gaining one second over the age of the universe. The clocks are sensitive enough to detect gravitational time dilation across height differences of 1 cm. Applications include redefinition of the SI second (proposed for 2030), tests of fundamental physics (variation of constants, dark-matter detection), and chronometric geodesy — measuring tiny gravitational potential differences for geophysics and resource prospecting." },
  { id: "quantum-sensing", name: "Quantum Sensing", era: "information", category: "knowledge",
    year: "2015", prereqs: ["quantum-mechanics", "semiconductor"],
    desc: "Measurement of physical quantities (magnetic field, gravity, time, rotation, temperature) using quantum coherence as the sensing element. Nitrogen-vacancy (NV) centers in diamond enable nanometer-scale magnetometry; cold-atom interferometers measure gravity with sub-microGal precision; squeezed light extends LIGO's gravitational-wave sensitivity. Quantum sensors achieve precisions classically forbidden by the Heisenberg limit. Commercial deployment from the late 2010s onward — quantum gravimeters for oil/mineral prospecting, atomic-clock GPS-alternatives for navigation in GPS-denied environments, and biological NV magnetometry for neuroimaging." },
  { id: "beamed-sail-propulsion", name: "Beamed-Sail Propulsion", era: "future", category: "transport",
    year: "2050", prereqs: ["directed-energy-weapons", "reusable-rocket"],
    desc: "Earth- or orbit-based phased-laser arrays accelerate gram-scale lightsail probes to a meaningful fraction of c, enabling decades-rather-than-millennia interstellar transit. Robert Forward proposed the concept in 1962; Breakthrough Starshot (Yuri Milner, Stephen Hawking, 2016) initiated serious engineering toward a $10B prototype targeting Alpha Centauri at 0.2c with ~20-year transit. The challenge stack: 100-GW phased laser array, 4×4 m sail surviving the beam, gram-scale electronics surviving deep space and arrival flyby, communication of the data back. Beamed-sail probes are humanity's first plausible interstellar reach." },
  { id: "nuclear-pulse-propulsion", name: "Nuclear Pulse Propulsion", era: "future", category: "transport",
    year: "2060", prereqs: ["nuclear-weapon", "reusable-rocket"],
    desc: "Project Orion (Ted Taylor, Freeman Dyson, 1958–65): a spaceship driven forward by detonating shaped nuclear charges behind a massive pusher plate. The 1963 Partial Test Ban Treaty (banning atmospheric nuclear tests) effectively killed Orion. Project Daedalus (BIS, 1973–78) and Project Longshot (USNA/NASA, 1988) refined into staged-fusion and antimatter-catalyzed variants. Nuclear pulse remains the only known propulsion physics that can deliver large payloads (10,000+ tons) to other star systems within human lifetimes — but the political and environmental constraints have kept it permanently theoretical until any serious interstellar program forces the question." },
  { id: "bussard-ramjet", name: "Bussard Ramjet", era: "far-future", category: "transport",
    year: "2300", prereqs: ["fusion-rocket", "interstellar-probe"],
    desc: "Robert Bussard's 1960 proposal: an interstellar vehicle scoops interstellar hydrogen with a vast magnetic 'ramjet' funnel, fuses it for thrust, and carries no propellant. Theoretically, a Bussard ramjet could accelerate continuously at 1g, reaching arbitrary speeds limited only by relativity. Subsequent analysis (Whitmire 1975, Fishback 1969) revealed the proton-proton fusion cross-section is too small for practical thrust, and magnetic-funnel drag exceeds thrust at most realistic configurations. Despite the engineering pessimism, the Bussard ramjet remains an iconic interstellar concept and the basis for variants (catalyzed CNO-cycle ramjet, ram-augmented interstellar rocket) that may yet prove viable." },
  { id: "antimatter-propulsion", name: "Antimatter Propulsion", era: "far-future", category: "transport",
    year: "2500", prereqs: ["antimatter-production", "fusion-rocket"],
    desc: "Spacecraft propulsion using matter-antimatter annihilation as energy source. Annihilation reactions release ~9×10¹⁶ J/kg — the maximum theoretically possible energy density — giving specific impulses of ~10⁷ seconds, two orders of magnitude beyond fusion. NASA's Robert Frisbee studied antimatter rocket designs; Steven Howe at Los Alamos proposed antiproton-catalyzed micro-fusion as a near-term variant. The gating constraint is antimatter production (~$10¹⁵/gram currently); once that economic barrier falls (post-2400 in this tree), antimatter propulsion enables decade-scale crewed interstellar voyages without warp-class physics." },
"""

TRANSLATIONS = {
    "optical-atomic-clock":     "光学原子钟",
    "quantum-sensing":          "量子传感",
    "beamed-sail-propulsion":   "光帆推进",
    "nuclear-pulse-propulsion": "核脉冲推进",
    "bussard-ramjet":           "巴萨德冲压发动机",
    "antimatter-propulsion":    "反物质推进",
}

UNLOCKS = {
    "optical-atomic-clock": [
        ("person",   "Jun Ye",                        "叶军",                "Jun Ye (physicist)"),
        ("person",   "David Wineland",                "戴维·瓦恩兰",         "David J. Wineland"),
        ("resource", "Optical lattice clock",         "光晶格钟",            "Optical lattice"),
        ("unit",     "Strontium-87 clock",            "锶-87 光钟",          "Strontium"),
        ("resource", "Chronometric geodesy",          "时频大地测量",        "Chronometric leveling"),
    ],
    "quantum-sensing": [
        ("resource", "Nitrogen-vacancy center",       "金刚石氮空位中心",    "Nitrogen-vacancy center"),
        ("resource", "Atom interferometry",           "原子干涉术",          "Atom interferometer"),
        ("resource", "Squeezed light",                "压缩光",              "Squeezed states of light"),
        ("unit",     "Quantum gravimeter",            "量子重力仪",          "Gravimeter"),
        ("unit",     "Quantum magnetometer",          "量子磁力计",          "Magnetometer"),
    ],
    "beamed-sail-propulsion": [
        ("org",      "Breakthrough Starshot",         "突破摄星计划",         "Breakthrough Starshot"),
        ("person",   "Robert L. Forward",             "罗伯特·L·福沃德",     "Robert L. Forward"),
        ("unit",     "Lightsail probe",               "光帆探测器",          "Solar sail"),
        ("resource", "Phased laser array",            "相控阵激光",          "Phased array"),
    ],
    "nuclear-pulse-propulsion": [
        ("unit",     "Project Orion",                 "猎户座计划",          "Project Orion (nuclear propulsion)"),
        ("unit",     "Project Daedalus",              "代达罗斯计划",        "Project Daedalus"),
        ("unit",     "Project Longshot",              "长射计划",            "Project Longshot"),
        ("person",   "Freeman Dyson",                 "弗里曼·戴森",         "Freeman Dyson"),
        ("person",   "Ted Taylor",                    "西奥多·泰勒",         "Ted Taylor (physicist)"),
    ],
    "bussard-ramjet": [
        ("person",   "Robert W. Bussard",             "罗伯特·W·巴萨德",     "Robert W. Bussard"),
        ("resource", "Magnetic ramscoop",             "磁性冲压舀斗",        False),
        ("work",     "Catalyzed CNO ramjet",          "催化 CNO 冲压发动机", False),
        ("work",     "Tau Zero",                      "《时间零》",          "Tau Zero"),
    ],
    "antimatter-propulsion": [
        ("resource", "Antiproton-catalyzed micro-fusion","反质子催化微聚变",  False),
        ("unit",     "Antimatter rocket",             "反物质火箭",          "Antimatter rocket"),
        ("person",   "Robert Frisbee",                "罗伯特·弗里斯比",     False),
        ("org",      "NASA Institute for Advanced Concepts", "NASA 先进概念研究院", "NASA Institute for Advanced Concepts"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "optical-atomic-clock" in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} techs")


def splice_translations():
    src = TRANS.read_text()
    if '"optical-atomic-clock"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Interstellar propulsion + quantum precision ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"optical-atomic-clock"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Interstellar propulsion + quantum precision ───\n"
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
