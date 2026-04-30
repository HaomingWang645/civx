#!/usr/bin/env python3
"""Add 8 physically-realistic Near Future / Far Future techs."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Realistic Near / Far Future additions ───
  { id: "engineered-microbiome", name: "Engineered Microbiome", era: "future", category: "medicine",
    year: "2035", prereqs: ["synthetic-biology", "gene-therapy"],
    desc: "Designed bacterial communities for the human gut, skin, and oral microbiome — and parallel agricultural and soil microbiomes. Fecal microbiota transplants (FMT) for *C. difficile* infection (FDA approval 2022) demonstrated proof of concept; by 2035 designed mixtures of 50–500 species are routinely prescribed for inflammatory bowel disease, metabolic syndrome, depression (via the gut-brain axis), and immunological conditioning. Soil-microbiome engineering displaces some synthetic-fertilizer demand; agricultural genomes are paired with their optimal microbial partners. Seres Therapeutics, Pendulum, and Indigo Ag are early commercial efforts." },
  { id: "geothermal-drilling", name: "Geothermal Drilling Revolution", era: "future", category: "energy",
    year: "2040", prereqs: ["advanced-chip-manufacturing", "climate-science"],
    desc: "Plasma- and millimeter-wave-based drills (Quaise Energy's gyrotron-based system) replace conventional rotary bits past ~5 km depth, where rock vaporizes faster than mechanical drilling can cut it. Wells reach 10–20 km / 500°C anywhere on Earth, unlocking enhanced geothermal systems (EGS) globally rather than only at plate boundaries. Closed-loop systems (Eavor's loop) allow heat extraction without seismic risk. Geothermal becomes a baseload renewable rivaling fusion in energy density and dispatchability — but with the gating constraint of high-temperature drill-bit lifetime in superheated rock." },
  { id: "senolytic-longevity-therapy", name: "Senolytic Longevity Therapy", era: "future", category: "medicine",
    year: "2040", prereqs: ["gene-therapy", "crispr"],
    desc: "Drugs and gene therapies that clear senescent cells — non-dividing zombie cells that secrete inflammatory factors and drive much age-related disease. The dasatinib + quercetin combination (D+Q, Mayo Clinic 2015) was the first demonstrated senolytic; UBX0101, navitoclax, and second-generation candidates (Unity Biotechnology, life-biosciences spinouts) follow. By 2040, senolytic protocols compress most age-related morbidity into a brief terminal phase — extending healthspan more than lifespan. Combined with epigenetic reprogramming (Yamanaka factors safely applied to somatic cells) and mTOR inhibitors, this is the realistic core of near-term anti-aging medicine." },
  { id: "brain-brain-communication", name: "Brain-to-Brain Communication", era: "future", category: "communication",
    year: "2075", prereqs: ["brain-computer-interface", "neuroscience"],
    desc: "Direct neural-to-neural transmission of motor commands, sensations, and (eventually) higher-order percepts via paired BCI systems. Miguel Nicolelis's brainet (rats, 2015) and Rajesh Rao's TMS-mediated human-to-human binary signaling (2014) demonstrated proof of concept at vanishingly low bandwidth. By 2075, dense intracortical mesh interfaces support multi-modal real-time signaling — coordinated motor control of shared bodies, shared visual fields, mood/emotion synchronization. Group-mind experiments and consensual hive-mind subcultures emerge; the philosophical and legal question of where one person ends and another begins becomes operational." },
  { id: "theory-of-consciousness", name: "Theory of Consciousness", era: "future", category: "knowledge",
    year: "2080", prereqs: ["neuroscience", "agi"],
    desc: "Empirical resolution of the hard problem: a scientific consensus on what physical configurations give rise to subjective experience and why. Integrated Information Theory (Tononi, 2004), Global Workspace Theory (Baars/Dehaene), Higher-Order Theories, and various successor frameworks compete; AGI-assisted analysis of comprehensive brain emulations and BCI-recorded subjective reports finally produces a falsifiable theory. The implications cascade: legal personhood criteria for AI, ethics of digital minds, animal welfare frameworks, end-of-life criteria, anaesthesia design, and consciousness-engineering all become rigorous practices instead of philosophical debates." },
  { id: "asteroid-capture", name: "Asteroid Capture", era: "far-future", category: "transport",
    year: "2120", prereqs: ["asteroid-mining", "fusion-rocket"],
    desc: "Active relocation of a near-Earth asteroid into stable Earth or lunar orbit for mining and habitation. NASA's Asteroid Redirect Mission concept (2013–2017) was the early study; later proposals use ion thrusters, gravity tractors, mass drivers, or fusion-thermal pushers to apply gentle continuous thrust to a 100–1000 m asteroid over years. Captured into Earth-Moon Lagrangian or distant retrograde orbits, the asteroid becomes a permanent industrial-scale source of platinum-group metals, water (from C-type bodies), and structural mass for in-orbit construction — collapsing launch-cost economics for cislunar industry." },
  { id: "bose-einstein-engineering", name: "Bose-Einstein Engineering", era: "far-future", category: "tools",
    year: "2300", prereqs: ["programmable-matter", "quantum-applications"],
    desc: "Macroscopic Bose-Einstein condensates and other quantum-coherent matter states maintained at engineering scales as practical industrial materials. Eric Cornell and Carl Wieman's first BEC (1995) was µg-scale and required nanokelvin temperatures; by the 24th century engineered BECs persist at room scale and tolerable temperatures via topological protection and active error-correction. Applications: ultra-precise atomic-clock substrates, frictionless bearings (superfluid helium analogues), quantum communication channels with no thermal noise, and atom-laser machining at single-atom precision. Atom-laser interferometers detect picometer displacements over kilometers." },
  { id: "anti-senescence-cellular-substrate", name: "Anti-Senescence Cellular Substrate", era: "far-future", category: "medicine",
    year: "2300", prereqs: ["cybernetic-enhancement", "nanotechnology"],
    desc: "Replacement of biological cells with engineered substrates — molecular machines or hybrid bio-synthetic constructs — that perform the same metabolic and structural roles without undergoing entropic damage. Where senolytic therapy (2040) clears senescent cells and gene-edited longevity slows aging, cellular-substrate replacement makes senescence a non-issue: damaged components are replaced rather than repaired. Bodies become Theseus-ship aggregates of progressively non-biological parts, with continuity of identity preserved by gradual substitution rather than wholesale upload. Effective biological immortality without abandoning embodied form." },
"""

TRANSLATIONS = {
    "engineered-microbiome":             "工程微生物组",
    "geothermal-drilling":               "深层地热钻探",
    "senolytic-longevity-therapy":       "衰老细胞清除疗法",
    "brain-brain-communication":         "脑脑通信",
    "theory-of-consciousness":           "意识科学理论",
    "asteroid-capture":                  "小行星捕获",
    "bose-einstein-engineering":         "玻色-爱因斯坦凝聚态工程",
    "anti-senescence-cellular-substrate":"抗衰老细胞基质",
}

UNLOCKS = {
    "engineered-microbiome": [
        ("resource", "Fecal microbiota transplant", "粪便微生物群移植",  "Fecal microbiota transplant"),
        ("resource", "Human microbiome",            "人类微生物组",       "Human microbiome"),
        ("org",      "Seres Therapeutics",          "Seres Therapeutics 公司", "Seres Therapeutics"),
        ("resource", "Gut-brain axis",              "肠脑轴",             "Gut–brain axis"),
    ],
    "geothermal-drilling": [
        ("org",      "Quaise Energy",               "Quaise 能源公司",    False),
        ("resource", "Enhanced geothermal system",  "增强型地热系统",     "Enhanced geothermal system"),
        ("resource", "Gyrotron drill",              "回旋管钻机",         "Gyrotron"),
        ("unit",     "Eavor-Loop",                  "Eavor 闭环系统",     False),
    ],
    "senolytic-longevity-therapy": [
        ("person",   "David Sinclair",              "大卫·辛克莱尔",      "David A. Sinclair"),
        ("person",   "Aubrey de Grey",              "奥布里·德格雷",     "Aubrey de Grey"),
        ("resource", "Senolytic",                   "衰老细胞清除剂",     "Senolytic"),
        ("resource", "Cellular senescence",         "细胞衰老",            "Cellular senescence"),
        ("resource", "Yamanaka factors",            "山中因子",            "Induced pluripotent stem cell"),
        ("org",      "Unity Biotechnology",         "Unity 生物技术",      "Unity Biotechnology"),
    ],
    "brain-brain-communication": [
        ("person",   "Miguel Nicolelis",            "米格尔·尼科勒利斯", "Miguel Nicolelis"),
        ("resource", "Brain-to-brain interface",    "脑-脑接口",           "Brain-to-brain interface"),
        ("unit",     "Brainet",                     "脑联网",             False),
        ("org",      "Neuralink",                   "Neuralink 神经链接", "Neuralink"),
    ],
    "theory-of-consciousness": [
        ("person",   "Giulio Tononi",               "朱利奥·托诺尼",      "Giulio Tononi"),
        ("person",   "Christof Koch",               "克里斯托夫·科赫",   "Christof Koch"),
        ("person",   "David Chalmers",              "大卫·查尔默斯",      "David Chalmers"),
        ("resource", "Integrated information theory", "整合信息论",       "Integrated information theory"),
        ("resource", "Global workspace theory",     "全局工作空间理论",   "Global workspace theory"),
        ("resource", "Hard problem of consciousness","意识难题",          "Hard problem of consciousness"),
    ],
    "asteroid-capture": [
        ("unit",     "Asteroid Redirect Mission",   "小行星重定向任务",   "Asteroid Redirect Mission"),
        ("resource", "Gravity tractor",             "引力拖船",           "Gravity tractor"),
        ("resource", "Lagrange point",              "拉格朗日点",         "Lagrange point"),
        ("unit",     "Distant retrograde orbit",    "远逆行轨道",         "Distant retrograde orbit"),
    ],
    "bose-einstein-engineering": [
        ("person",   "Eric Cornell",                "埃里克·康奈尔",      "Eric Allin Cornell"),
        ("person",   "Carl Wieman",                 "卡尔·威曼",         "Carl Wieman"),
        ("resource", "Bose–Einstein condensate",    "玻色-爱因斯坦凝聚态","Bose–Einstein condensate"),
        ("resource", "Atom laser",                  "原子激光",            "Atom laser"),
        ("resource", "Superfluid",                  "超流体",              "Superfluid"),
    ],
    "anti-senescence-cellular-substrate": [
        ("resource", "Cellular senescence",         "细胞衰老",           "Cellular senescence"),
        ("resource", "Theseus's ship paradox",      "忒修斯之船悖论",     "Ship of Theseus"),
        ("unit",     "Hybrid bio-synthetic cell",   "混合生物-合成细胞",   False),
        ("resource", "Molecular nanomedicine",      "分子纳米医学",        "Nanomedicine"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if 'id: "engineered-microbiome"' in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src: raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} realistic-future techs")


def splice_translations():
    src = TRANS.read_text()
    if '"engineered-microbiome"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Realistic Near / Far Future ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"engineered-microbiome"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Realistic Near / Far Future ───\n"
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
