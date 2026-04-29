#!/usr/bin/env python3
"""Insert 10 future / far-future weapons techs before the closing `];` of
the TECHS array in data.js. Atomic: read once, splice, write once."""

from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")

NEW_BLOCK = """
  // ─── Future / Far-Future weapons ───
  { id: "cyber-kinetic-warfare", name: "Cyber-Kinetic Warfare", era: "future", category: "weapons",
    year: "2030", prereqs: ["cloud-computing", "arpanet-internet"],
    desc: "Cyberattacks producing physical destruction at industrial scale: corrupted PLCs spinning centrifuges to failure, falsified telemetry crashing autonomous fleets, ransomware locking power grids and water-treatment plants. Stuxnet (2010) was the proof of concept; the 2015 Ukraine grid attack, the 2017 NotPetya wiper (~$10 billion damage), and the 2021 Colonial Pipeline ransomware showed the trajectory. By 2030, cyber-kinetic operations are integral to peer warfare doctrine and the legal threshold for armed-conflict response is permanently blurred. Critical-infrastructure hardening becomes a national-security priority on the scale of nuclear deterrence." },
  { id: "directed-energy-weapons", name: "Directed-Energy Weapons", era: "future", category: "weapons",
    year: "2035", prereqs: ["advanced-chip-manufacturing", "lithium-battery"],
    desc: "Kilowatt- to megawatt-class lasers, high-power microwaves, and particle beams replacing kinetic projectiles for selected roles. The U.S. Navy's HELIOS (60 kW solid-state laser, deployed on USS Preble 2022), the British DragonFire (50 kW, 2024), and Israel's Iron Beam mark the early generation. By the 2030s ship- and vehicle-mounted systems engage drones, mortars, and small boats at the speed of light at marginal cost per shot. Directed energy reshapes air defense and counter-UAS, and pushes attackers toward saturation tactics — drone swarms — to overwhelm beam-on-target rates." },
  { id: "drone-swarms", name: "Autonomous Drone Swarms", era: "future", category: "weapons",
    year: "2035", prereqs: ["machine-learning", "autonomous-vehicle"],
    desc: "Cooperative swarms of hundreds to thousands of cheap autonomous drones, coordinated by edge-AI without continuous human supervision. The 2020 Nagorno-Karabakh war (TB2 Bayraktar) and Ukraine's 2022–25 mass FPV-drone campaigns demonstrated the disruption; the Pentagon's Replicator Initiative (2023) and Chinese counterpart programs scale it. By 2035, swarm tactics dominate battlefield reconnaissance, suppression of enemy air defense, and precision strike. Cheap autonomy inverts the cost curve: a $1,000 drone can disable a $10 million tank, forcing armored, naval, and air doctrine to rebuild around mass and dispersion." },
  { id: "anti-satellite-warfare", name: "Anti-Satellite Warfare", era: "future", category: "weapons",
    year: "2040", prereqs: ["satellite", "reusable-rocket"],
    desc: "Mature kinetic and non-kinetic anti-satellite (ASAT) capabilities. China's 2007 Fengyun-1C kinetic test, India's 2019 Mission Shakti, and Russia's 2021 Cosmos 1408 strike showed early kinetic ASAT — at the cost of debris fields lasting decades (Kessler-syndrome risk). By the 2040s, non-kinetic ASAT (jammers, dazzlers, co-orbital grapplers) dominate; kinetic strikes are reserved for terminal-phase doctrine. The first day of any peer conflict opens with a strike on the adversary's ISR, GPS, and communications constellations — making space the decisive contested domain." },
  { id: "engineered-pathogen-defense", name: "Engineered Pathogen Defense", era: "future", category: "weapons",
    year: "2055", prereqs: ["synthetic-biology", "mrna-vaccine"],
    desc: "Continuous biosurveillance plus rapid-response countermeasure pipelines: metagenomic sewage and air sampling, AI-flagged anomaly detection, and on-demand mRNA vaccine and monoclonal-antibody manufacture within days of pathogen identification. Operation Warp Speed (2020) compressed COVID-19 vaccine development from years to months; by the 2050s the pipeline operates in weeks for any sequenced novel agent. Defense against engineered pathogens — released by state programs, terrorists, or accidents — joins nuclear and cyber as a tier-one national-security capability. The same technology lowers the barrier to offensive bioweapons, making the regime fragile." },
  { id: "strategic-memetic-warfare", name: "Strategic Memetic Warfare", era: "far-future", category: "weapons",
    year: "2150", prereqs: ["large-language-model", "agi", "social-media"],
    desc: "Industrial-scale narrative warfare conducted by AGI: adversary populations are subjected to continuous, individualized persuasion campaigns generating tailored disinformation, synthetic relationships, and strategic memes calibrated to shift voting, recruitment, social cohesion, and policy preferences. Russian Internet Research Agency activity (2014–) and the 2024 election deepfake era are the crude precursors. By 2150 a peer civilization without comparable AI defenses can be destabilized within years through narrative attack alone — a more durable form of conquest than military occupation. Defensive epistemic infrastructure becomes a strategic capability." },
  { id: "self-replicating-combat-drones", name: "Self-Replicating Combat Drones", era: "far-future", category: "weapons",
    year: "2200", prereqs: ["self-replicating-machines", "nanotechnology"],
    desc: "Autonomous combat drones that gather raw materials from the environment and manufacture copies of themselves, deploying as self-sustaining military forces without resupply. John von Neumann's universal constructor (1948) provided the theoretical basis; nanomanufacturing and autonomous AI close the practical loop. Once released, a self-replicating fleet's growth becomes exponential and difficult to recall — ergodic conflict where strategic decisions cannot be reversed. International accords prohibit unbounded replicators (1990s-style biological-weapons analogue), but verification challenges and breakaway state programs make compliance fragile." },
  { id: "planetary-defense-system", name: "Planetary Defense System", era: "far-future", category: "weapons",
    year: "2200", prereqs: ["anti-satellite-warfare", "asteroid-mining"],
    desc: "Coordinated multi-layer defense grid for an entire planet: distributed orbital sensors detecting both natural threats (asteroids, comets) and hostile artifacts; kinetic-impactor and gravity-tractor deflection assets on standing alert; directed-energy and missile interceptors for terminal-phase engagements. NASA's 2022 DART mission (the first operational kinetic asteroid deflection) and the planned NEO Surveyor telescope are the early elements. By 2200 humanity operates an integrated grid covering the inner solar system, treating planetary survival as routine infrastructure rather than catastrophic-risk hedging." },
  { id: "relativistic-kinetic-weapon", name: "Relativistic Kinetic Weapon", era: "far-future", category: "weapons",
    year: "2300", prereqs: ["fusion-rocket", "interstellar-probe"],
    desc: "Projectiles accelerated to a meaningful fraction of the speed of light — a one-ton mass at 0.1c carries kinetic energy comparable to the Chicxulub impactor. The Casaba-Howitzer (1960s nuclear-pulse-propelled fragments) and Project Longshot studies provide the theoretical lineage. At interstellar distances RKWs are nearly impossible to defend against — detection at multi-light-day range gives only hours of warning before impact, and even a near-miss imparts catastrophic gamma-ray bursts to the target. Once any star-faring civilization develops the capability, mutual assured destruction goes interstellar." },
  { id: "antimatter-weapon", name: "Antimatter Weapon", era: "far-future", category: "weapons",
    year: "2450", prereqs: ["antimatter-production"],
    desc: "Weapons using positron-electron or proton-antiproton annihilation, with energy densities ~10⁴ times nuclear fission and no critical-mass threshold. A single milligram of antimatter releases ~43 kilotons; gram-scale yields rival the largest thermonuclear devices. Air Force Research Laboratory (2003–) studied positron-catalyzed micro-fusion; practical weaponization remains gated by antimatter production cost (currently ~$10¹⁵ per gram) and trap stability. If those barriers fall, antimatter weapons enable arsenals that fit in a briefcase — collapsing the deterrence architecture that prevented great-power war since 1945." },
"""

TRANSLATIONS = {
    "cyber-kinetic-warfare":         "网络-动能战争",
    "directed-energy-weapons":       "定向能武器",
    "drone-swarms":                  "无人机蜂群",
    "anti-satellite-warfare":        "反卫星战",
    "engineered-pathogen-defense":   "工程病原体防御",
    "strategic-memetic-warfare":     "战略迷因战",
    "self-replicating-combat-drones":"自我复制战斗无人机",
    "planetary-defense-system":      "行星防御系统",
    "relativistic-kinetic-weapon":   "相对论性动能武器",
    "antimatter-weapon":             "反物质武器",
}

UNLOCKS = {
    "cyber-kinetic-warfare": [
        ("unit",     "Stuxnet",                                    "震网病毒"),
        ("unit",     "NotPetya",                                    "NotPetya 蠕虫"),
        ("org",      "U.S. Cyber Command",                          "美国网络司令部"),
        ("work",     "Tallinn Manual",                              "《塔林手册》"),
    ],
    "directed-energy-weapons": [
        ("unit",     "HELIOS Laser",                                "HELIOS 高能激光"),
        ("unit",     "DragonFire",                                  "龙火激光武器"),
        ("unit",     "Iron Beam",                                   "铁束激光"),
        ("org",      "U.S. Naval Research Laboratory",              "美国海军研究实验室"),
    ],
    "drone-swarms": [
        ("unit",     "Bayraktar TB2",                               "拜拉克塔尔 TB2"),
        ("unit",     "Switchblade 600",                             "弹簧刀 600 巡飞弹"),
        ("org",      "Pentagon Replicator Initiative",              "五角大楼复制者计划"),
        ("org",      "Anduril Industries",                          "Anduril 工业"),
    ],
    "anti-satellite-warfare": [
        ("unit",     "Fengyun-1C ASAT Test",                        "风云一号 C 反卫星试验"),
        ("unit",     "Mission Shakti",                              "印度沙克提行动"),
        ("org",      "U.S. Space Force",                            "美国太空军"),
        ("org",      "China PLA Strategic Support Force",           "中国人民解放军战略支援部队"),
    ],
    "engineered-pathogen-defense": [
        ("org",      "BARDA",                                       "美国生物医学高级研究开发管理局"),
        ("org",      "DARPA Pandemic Prevention Platform",          "DARPA 大流行病预防平台"),
        ("resource", "Metagenomic biosurveillance",                 "宏基因组生物监测"),
        ("work",     "Biological Weapons Convention",               "《禁止生物武器公约》"),
    ],
    "strategic-memetic-warfare": [
        ("unit",     "AI persuasion campaign",                      "AI 说服运动"),
        ("org",      "Internet Research Agency",                    "互联网研究机构"),
        ("resource", "Synthetic media saturation",                  "合成媒体饱和攻击"),
        ("work",     "Active Measures doctrine",                    "积极措施学说"),
    ],
    "self-replicating-combat-drones": [
        ("unit",     "Von Neumann combat probe",                    "冯·诺依曼战斗探测器"),
        ("resource", "Autonomous weapons accord",                   "自主武器公约"),
        ("work",     "Convention on Self-Replicating Systems",      "《自复制系统公约》"),
    ],
    "planetary-defense-system": [
        ("unit",     "DART Spacecraft",                             "DART 双小行星撞击试验"),
        ("unit",     "NEO Surveyor",                                "近地天体测量探测器"),
        ("org",      "UN Office for Outer Space Affairs",           "联合国外层空间事务厅"),
        ("wonder",   "Solar System Defense Grid",                   "太阳系防御网格"),
    ],
    "relativistic-kinetic-weapon": [
        ("unit",     "Casaba-Howitzer",                             "卡萨巴榴弹炮"),
        ("unit",     "Project Longshot",                            "长射计划"),
        ("resource", "Interstellar deterrence",                     "星际威慑"),
    ],
    "antimatter-weapon": [
        ("resource", "Positron annihilation device",                "正电子湮灭装置"),
        ("resource", "Antiproton arsenal",                          "反质子军火库"),
        ("org",      "Air Force Research Laboratory",               "美国空军研究实验室"),
    ],
}


def insert_translations():
    """Append translations into translations.js before the closing brace."""
    path = Path("/Users/haomingwang/Desktop/Python/tech-tree/translations.js")
    src = path.read_text()
    if '"cyber-kinetic-warfare"' in src:
        print("translations.js: already inserted")
        return
    block = "\n  // ─── Future / Far-Future weapons ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    # Insert before the final "};"
    rs = src.rstrip()
    assert rs.endswith("};"), "translations.js end marker missing"
    new_src = rs[:-2] + block + "};\n"
    path.write_text(new_src)
    print(f"translations.js: +{len(TRANSLATIONS)}")


def insert_unlocks():
    path = Path("/Users/haomingwang/Desktop/Python/tech-tree/unlocks.js")
    src = path.read_text()
    if '"cyber-kinetic-warfare"' in src:
        print("unlocks.js: already inserted")
        return
    import json
    block = "\n  // ─── Future / Far-Future weapons ───\n"
    for tid, items in UNLOCKS.items():
        block += f'  "{tid}": [\n'
        for typ, name, name_zh in items:
            block += (f'    {{ type: "{typ}", '
                      f'name: {json.dumps(name, ensure_ascii=False)}, '
                      f'name_zh: {json.dumps(name_zh, ensure_ascii=False)} }},\n')
        block += '  ],\n'
    rs = src.rstrip()
    assert rs.endswith("};"), "unlocks.js end marker missing"
    new_src = rs[:-2] + block + "};\n"
    path.write_text(new_src)
    print(f"unlocks.js: +{len(UNLOCKS)}")


def main():
    src = DATA.read_text()
    if "cyber-kinetic-warfare" in src:
        print("data.js: already inserted")
    else:
        marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
        if marker not in src:
            raise SystemExit("Closing marker not found in data.js")
        new_src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")
        DATA.write_text(new_src)
        print("data.js: +10 weapons techs")

    insert_translations()
    insert_unlocks()


if __name__ == "__main__":
    main()
