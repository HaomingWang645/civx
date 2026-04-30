#!/usr/bin/env python3
"""Add 10 physics-related techs:
  Set 1 (fusion):       fusion-materials, aneutronic-fusion
  Set 2 (accelerators): cyclotron, synchrotron, lhc, higgs-factory
  Set 3 (theories):     quantum-electrodynamics, standard-model,
                        higgs-discovery, string-theory
"""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Particle physics & fusion engineering ───
  { id: "cyclotron", name: "Cyclotron", era: "modern", category: "knowledge",
    year: "1932", prereqs: ["electron-discovery", "electromagnetism"],
    desc: "Ernest Lawrence's 1932 cyclotron (UC Berkeley) accelerated charged particles in a spiral by alternating an electric field synchronized with the ion's circular motion in a uniform magnetic field. The 27-inch (1932) and successive 60-inch (1939) and 184-inch (1946) machines reached energies sufficient to disintegrate atomic nuclei, producing artificial radioisotopes (medical and physics use), discovering carbon-14, and seeding nuclear physics as an experimental discipline. Lawrence won the 1939 Nobel. Modern medical cyclotrons produce isotopes for PET scans daily. The principle — circular acceleration in a magnetic field — descends through synchrotrons to the LHC." },
  { id: "synchrotron", name: "Synchrotron", era: "atomic", category: "knowledge",
    year: "1952", prereqs: ["cyclotron", "quantum-mechanics"],
    desc: "Synchrotrons increase the magnetic field strength as particles gain energy, keeping them on a fixed-radius orbit instead of spiraling outward — overcoming the relativistic mass-energy growth that limits cyclotrons. The Cosmotron (Brookhaven, 1952, 3 GeV) was the first GeV-class machine; Bevatron (Berkeley, 1954) discovered the antiproton (1955); the AGS, CERN PS, Tevatron (Fermilab, 1983, ~1 TeV), and LEP/LHC at CERN form the lineage. Each generation roughly an order of magnitude more energetic. Synchrotron radiation — initially a nuisance — became its own scientific tool, producing X-ray light sources used across biology, materials science, and chemistry." },
  { id: "quantum-electrodynamics", name: "Quantum Electrodynamics", era: "atomic", category: "knowledge",
    year: "1948", prereqs: ["quantum-mechanics", "relativity"],
    desc: "The first relativistic quantum field theory, describing the electromagnetic interaction between charged particles via virtual-photon exchange. Richard Feynman, Julian Schwinger, and Shin'ichirō Tomonaga independently formulated the renormalized theory (1947–48), each receiving the 1965 Nobel. Feynman diagrams turned arbitrarily complex calculations into a graphical perturbation expansion. QED predicts the electron magnetic moment to 12 decimal places — the most accurately verified theory in all of science. As the template for renormalizable quantum field theory, QED set the methodology that produced the Standard Model two decades later." },
  { id: "standard-model", name: "Standard Model", era: "information", category: "knowledge",
    year: "1973", prereqs: ["quantum-electrodynamics", "synchrotron"],
    desc: "The unified quantum field theory of all known elementary particles and three of the four fundamental forces (electromagnetic, weak, strong; gravity excluded). Glashow-Weinberg-Salam electroweak unification (1967) and Gross-Politzer-Wilczek's asymptotic freedom in QCD (1973) brought the pieces together. Six quarks, six leptons, four gauge bosons, the Higgs — every prediction has held. Limitations are the open problems: gravity, dark matter, neutrino mass mechanism, matter-antimatter asymmetry, the gauge-hierarchy problem. The Standard Model is simultaneously physics's greatest achievement and the puzzle whose limits define current frontier research." },
  { id: "string-theory", name: "String Theory", era: "information", category: "knowledge",
    year: "1984", prereqs: ["standard-model", "quantum-mechanics"],
    desc: "Frameworks describing fundamental constituents as one-dimensional vibrating strings rather than point particles, with different vibrational modes giving rise to different particles. The 1984 Green-Schwarz anomaly cancellation triggered the 'first superstring revolution'; Witten's 1995 M-theory unified the five competing superstring formulations. Strings naturally include a graviton-like mode, suggesting a path to quantum gravity. After 40 years, no experimentally distinguishing prediction has been confirmed; the theory's standing as physics-versus-mathematics remains contested. Its mathematical machinery has nonetheless transformed adjacent areas (mirror symmetry, AdS/CFT correspondence, condensed matter) regardless of physical truth." },
  { id: "lhc", name: "Large Hadron Collider", era: "information", category: "knowledge",
    year: "2008", prereqs: ["synchrotron", "semiconductor"],
    desc: "CERN's 27-km-circumference proton-proton collider (Geneva, first beam September 2008, design energy 14 TeV). The energy frontier of accelerator-based physics: 1232 superconducting dipole magnets, ~10,000 tons of liquid helium cooling them to 1.9 K. Four major detectors — ATLAS, CMS, ALICE, LHCb — observe collision products. The 2012 Higgs boson discovery confirmed the Standard Model's last predicted particle. Successor proposals: HL-LHC (2030+, 10× luminosity), FCC (~100 km, 100 TeV), and dedicated Higgs factories. The LHC is humanity's most expensive ($5+B) and complex single instrument." },
  { id: "higgs-discovery", name: "Higgs Boson Discovery", era: "information", category: "knowledge",
    year: "2012", prereqs: ["standard-model", "lhc"],
    desc: "On July 4, 2012, the ATLAS and CMS collaborations at the LHC jointly announced observation of a new boson at ~125 GeV, with properties consistent with the Standard Model Higgs predicted by Peter Higgs and others in 1964. Subsequent measurements (spin 0, parity even, decays in the predicted ratios) confirmed the identification. Higgs and François Englert received the 2013 Nobel; Peter Higgs's mechanism for electroweak symmetry breaking, theorized 48 years earlier, was finally observed. The Higgs was the last unobserved Standard Model particle; its discovery completed the model and shifted the frontier to what lies beyond it." },
  { id: "higgs-factory", name: "Higgs Factory", era: "future", category: "knowledge",
    year: "2045", prereqs: ["lhc", "advanced-chip-manufacturing"],
    desc: "Next-generation electron-positron colliders dedicated to precision Higgs-boson measurements: International Linear Collider (ILC, Japan, proposed), Future Circular Collider electron-positron stage (FCC-ee, CERN, 91 km), and the Circular Electron Positron Collider (CEPC, China, 100 km). Unlike the LHC's 'discovery machine' role, Higgs factories produce ~10⁶ Higgs bosons in clean e⁺e⁻ environments, enabling sub-percent measurement of Higgs couplings — sensitive to subtle deviations that would point to physics beyond the Standard Model. Operational mid-2040s. Cost ~$15-30B; the gating decision is political-economic, not technical." },
  { id: "fusion-materials", name: "Fusion Materials", era: "future", category: "tools",
    year: "2045", prereqs: ["machine-tool", "magnetic-confinement-fusion"],
    desc: "Engineered structural materials that survive the unique stress of a fusion reactor: 14 MeV neutron flux causing transmutation and embrittlement, multi-MW/m² heat loads on plasma-facing surfaces, and tritium permeation. Tungsten plasma-facing armor (low sputtering, high melting point), reduced-activation ferritic-martensitic steels (Eurofer-97), oxide-dispersion-strengthened alloys, and SiC/SiC composites for blanket structures. The IFMIF-DONES neutron-source facility (Spain, ~2032) provides the testing environment. Fusion materials gate the transition from physics demonstrators (ITER) to electricity-producing reactors (DEMO, commercial)." },
  { id: "aneutronic-fusion", name: "Aneutronic Fusion", era: "future", category: "energy",
    year: "2085", prereqs: ["fusion-power", "lunar-industrial-base"],
    desc: "Fusion reactions that produce charged particles (helium nuclei) rather than energetic neutrons: deuterium-helium-3 (D + ³He → ⁴He + p) and proton-boron-11 (p + ¹¹B → 3 ⁴He). Aneutronic reactions avoid the neutron-induced material damage and tritium fuel-cycle problems of D-T fusion, and enable direct conversion of charged-particle kinetic energy to electricity (~80% efficiency vs ~33% steam cycle). The catch: required temperatures are 5–10× higher than D-T (~1 billion °C), and ³He is essentially absent on Earth — making lunar regolith mining (helium-3 implanted by solar wind) a long-term economic premise. TAE Technologies and Helion pursue the engineering through the 2050s–2080s." },
"""

TRANSLATIONS = {
    "cyclotron":                  "回旋加速器",
    "synchrotron":                "同步加速器",
    "quantum-electrodynamics":    "量子电动力学",
    "standard-model":             "粒子物理标准模型",
    "string-theory":              "弦理论",
    "lhc":                        "大型强子对撞机",
    "higgs-discovery":            "希格斯玻色子发现",
    "higgs-factory":              "希格斯工厂",
    "fusion-materials":           "聚变材料",
    "aneutronic-fusion":          "无中子聚变",
}

UNLOCKS = {
    "cyclotron": [
        ("person",   "Ernest Lawrence",          "欧内斯特·劳伦斯",      "Ernest Lawrence"),
        ("unit",     "184-inch Cyclotron",       "184 英寸回旋加速器",    "184-inch Cyclotron"),
        ("org",      "Lawrence Berkeley National Laboratory", "劳伦斯伯克利国家实验室", "Lawrence Berkeley National Laboratory"),
        ("resource", "Carbon-14",                "碳-14",                "Carbon-14"),
    ],
    "synchrotron": [
        ("unit",     "Cosmotron",                "宇宙级加速器",          "Cosmotron"),
        ("unit",     "Bevatron",                 "高能质子同步加速器",    "Bevatron"),
        ("unit",     "Tevatron",                 "万亿电子伏特加速器",    "Tevatron"),
        ("org",      "Brookhaven National Laboratory", "布鲁克黑文国家实验室", "Brookhaven National Laboratory"),
        ("org",      "Fermilab",                 "费米国家加速器实验室",  "Fermilab"),
        ("resource", "Antiproton",               "反质子",               "Antiproton"),
    ],
    "quantum-electrodynamics": [
        ("person",   "Richard Feynman",          "理查德·费曼",         "Richard Feynman"),
        ("person",   "Julian Schwinger",         "朱利安·施温格",       "Julian Schwinger"),
        ("person",   "Shin'ichirō Tomonaga",     "朝永振一郎",          "Shin'ichirō Tomonaga"),
        ("resource", "Feynman diagram",          "费曼图",               "Feynman diagram"),
        ("resource", "Renormalization",          "重正化",               "Renormalization"),
    ],
    "standard-model": [
        ("person",   "Steven Weinberg",          "史蒂文·温伯格",       "Steven Weinberg"),
        ("person",   "Sheldon Glashow",          "谢尔顿·格拉肖",       "Sheldon Lee Glashow"),
        ("person",   "Abdus Salam",              "阿卜杜勒·萨拉姆",     "Abdus Salam"),
        ("resource", "Quantum chromodynamics",   "量子色动力学",         "Quantum chromodynamics"),
        ("resource", "Electroweak interaction",  "电弱相互作用",         "Electroweak interaction"),
        ("resource", "Higgs mechanism",          "希格斯机制",           "Higgs mechanism"),
    ],
    "string-theory": [
        ("person",   "Edward Witten",            "爱德华·威滕",          "Edward Witten"),
        ("person",   "Michael Green",            "迈克尔·格林",          "Michael Green (physicist)"),
        ("person",   "John Schwarz",             "约翰·施瓦茨",          "John Henry Schwarz"),
        ("resource", "M-theory",                 "M 理论",                "M-theory"),
        ("resource", "Superstring theory",       "超弦理论",              "Superstring theory"),
        ("resource", "AdS/CFT correspondence",   "AdS/CFT 对应",          "AdS/CFT correspondence"),
    ],
    "lhc": [
        ("unit",     "ATLAS experiment",         "ATLAS 实验",            "ATLAS experiment"),
        ("unit",     "CMS experiment",           "CMS 实验",              "Compact Muon Solenoid"),
        ("unit",     "ALICE experiment",         "ALICE 实验",            "ALICE experiment"),
        ("unit",     "LHCb",                     "LHCb 实验",             "LHCb experiment"),
        ("org",      "CERN",                     "欧洲核子研究组织",       "CERN"),
        ("resource", "Superconducting magnet",   "超导磁体",              "Superconducting magnet"),
    ],
    "higgs-discovery": [
        ("unit",     "Higgs boson",              "希格斯玻色子",          "Higgs boson"),
        ("person",   "Peter Higgs",              "彼得·希格斯",          "Peter Higgs"),
        ("person",   "François Englert",         "弗朗索瓦·恩格勒特",   "François Englert"),
        ("org",      "ATLAS Collaboration",      "ATLAS 合作组",          "ATLAS experiment"),
        ("work",     "Higgs boson observation",  "希格斯玻色子观测",       "Higgs boson"),
    ],
    "higgs-factory": [
        ("unit",     "International Linear Collider", "国际直线对撞机",   "International Linear Collider"),
        ("unit",     "Future Circular Collider", "未来环形对撞机",        "Future Circular Collider"),
        ("unit",     "CEPC",                     "中国环形正负电子对撞机", "Circular Electron Positron Collider"),
        ("unit",     "FCC-ee",                   "FCC-ee 正负电子环",     "Future Circular Collider"),
    ],
    "fusion-materials": [
        ("resource", "Plasma-facing material",   "等离子体面对材料",       "Plasma-facing material"),
        ("resource", "Tungsten armor",           "钨装甲",                 "Tungsten"),
        ("resource", "Eurofer-97 steel",         "Eurofer-97 钢",         False),
        ("org",      "IFMIF-DONES",              "IFMIF-DONES 中子源",     "IFMIF"),
    ],
    "aneutronic-fusion": [
        ("resource", "Helium-3 fuel cycle",      "氦-3 燃料循环",          "Helium-3"),
        ("resource", "Proton-boron-11 reaction", "质子-硼-11 反应",        "Aneutronic fusion"),
        ("org",      "TAE Technologies",         "TAE 技术公司",           "TAE Technologies"),
        ("org",      "Helion Energy",            "氦聚变能源",             "Helion Energy"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "quantum-electrodynamics" in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} techs")


def splice_translations():
    src = TRANS.read_text()
    if '"quantum-electrodynamics"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Particle physics & fusion engineering ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"quantum-electrodynamics"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Particle physics & fusion engineering ───\n"
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
