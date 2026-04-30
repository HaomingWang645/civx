#!/usr/bin/env python3
"""Add 12 warfare doctrine / tactics techs spanning Classical → Future."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Warfare doctrine & tactics ───
  { id: "phalanx", name: "Phalanx", era: "classical", category: "weapons",
    year: "~700 BCE", prereqs: ["standing-army", "iron-weapons"],
    desc: "Massed close-order infantry formation in 8-deep ranks bristling with overlapping shields and long thrusting spears (dory or sarissa). Greek hoplites perfected the form (~700 BCE) and used it to defeat the Persians at Marathon (490 BCE) and Plataea (479 BCE); Philip II and Alexander's Macedonian phalanx with 6m sarissai conquered the known world. The phalanx required heavy citizen-soldier discipline and worked only on flat terrain — vulnerabilities the more flexible Roman legion exploited. Its conceptual descendants — Swiss pike squares (1400s), Spanish tercios (1500s), modern infantry line — span 2,500 years of Western warfare." },
  { id: "roman-legion", name: "Roman Legion", era: "classical", category: "weapons",
    year: "~100 BCE", prereqs: ["phalanx", "iron-weapons"],
    desc: "Marian-reform legion (~107 BCE): a permanent professional 4,800-man formation organized into 10 cohorts of 6 centuries, each centurion an experienced career officer with extensive delegated authority. Equipment standardized (gladius, pilum, scutum, lorica). The legion's flexibility — fight in line, in maniples, in testudo formation — defeated phalanxes at Cynoscephalae (197 BCE) and Pydna (168 BCE), Gallic warbands, and Carthaginian armies. Roman military organization established the modern Western model: standardized units, professional officers, logistics doctrine, military engineering as an institutional capability. NATO ranks descend directly from centurion (centurio → centuriarius → captain)." },
  { id: "castle-siege-doctrine", name: "Castle & Siege Doctrine", era: "medieval", category: "weapons",
    year: "1100", prereqs: ["castle", "siege-engine"],
    desc: "Mature high-medieval theory of fortification and siege: concentric castle design (motte-and-bailey → stone keep → curtain walls + flanking towers + barbican), supported by sophisticated siege engineering (countermines, mantlets, siege towers, trebuchets capable of throwing 90 kg projectiles 250m). Crusader fortresses (Krak des Chevaliers) and Edward I's Welsh castles (Caernarfon, Conwy) represent peak design. Defensive doctrine emphasized self-sufficient garrisons surviving year-long sieges; offensive doctrine industrialized siegecraft. The trace italienne (1500s, bastion forts) eventually obsoleted high stone walls in response to gunpowder artillery." },
  { id: "pike-square", name: "Pike Square", era: "renaissance", category: "weapons",
    year: "1476", prereqs: ["knight-cavalry", "longbow"],
    desc: "Massed infantry formation of 5–6m pikes in dense squares of 1,000–10,000 men. Swiss confederate pike squares destroyed Charles the Bold's Burgundian heavy cavalry at Grandson, Murten, and Nancy (1476–77), shattering the medieval cavalry-supremacy paradigm. Landsknechts (German imperial mercenaries) and Spanish tercios (combining pikes with crossbowmen, then arquebusiers) institutionalized the form. Pike squares dominated European warfare from 1480 to ~1700, until socket-bayonets let line infantry combine fire and melee in one formation, ending the pike-and-shot era." },
  { id: "trench-warfare", name: "Trench Warfare", era: "modern", category: "weapons",
    year: "1915", prereqs: ["machine-gun", "modern-quick-firing-artillery"],
    desc: "Defensive doctrine of multiple parallel entrenched lines, barbed-wire belts, machine-gun nests, and pre-registered artillery, that paralyzed WWI's Western Front (1914–18) into four years of attritional stasis. The combination of magazine rifles, quick-firing artillery, machine guns, and barbed wire made traditional infantry assault suicidal — the same week, the Battle of Loos (1915) saw 60,000 British casualties for marginal gains. Trench warfare was the immediate trigger for tank development, chemical weapons, infiltration tactics (Hutier 1917), and ultimately the combined-arms doctrine that broke the deadlock in 1918." },
  { id: "combined-arms-warfare", name: "Combined Arms Warfare", era: "modern", category: "weapons",
    year: "1918", prereqs: ["trench-warfare", "tank"],
    desc: "Coordinated employment of infantry, armor, artillery, and aircraft as a single integrated force, each arm protecting the others' weaknesses. The Hundred Days Offensive (August–November 1918) saw the British Army employ tanks under creeping artillery barrages, with infantry close behind, RAF strafing reserves, and intelligence flowing back from sound-ranging — the first mature combined arms operation. Sir John Monash and Ferdinand Foch institutionalized the concept; J.F.C. Fuller and Heinz Guderian extended it into Plan 1919 and ultimately Blitzkrieg. Combined arms remains the foundational doctrine of modern Western armies." },
  { id: "blitzkrieg", name: "Blitzkrieg", era: "modern", category: "weapons",
    year: "1940", prereqs: ["combined-arms-warfare", "tank"],
    desc: "German operational maneuver doctrine: concentrate armor (Panzer divisions) at a chosen breakthrough point (schwerpunkt), penetrate the enemy line, then exploit deeply with motorized infantry to encircle and shatter rear-area cohesion before the defender can react. Heinz Guderian (Achtung—Panzer!, 1937) synthesized it from interwar British and German theory. Poland (1939, 5 weeks), the Low Countries and France (1940, 6 weeks), and Operation Barbarossa's opening months demonstrated the doctrine's power. Soviet deep-battle doctrine (Tukhachevsky) was the parallel theory; both descended from the WWI combined-arms breakthrough thinking." },
  { id: "ballistic-missile-defense", name: "Ballistic Missile Defense", era: "atomic", category: "weapons",
    year: "1970", prereqs: ["icbm", "radar"],
    desc: "Defensive systems against ballistic missiles: early-warning radars detecting launch, midcourse-phase interceptors targeting warheads in space, and terminal-phase interceptors as a last layer. The U.S. Safeguard system (1975, briefly operational) used nuclear-armed Sprint and Spartan interceptors. The Anti-Ballistic Missile Treaty (1972) limited deployments — strategic stability under MAD required mutual vulnerability. The Strategic Defense Initiative (Reagan, 1983, 'Star Wars') reopened the program; modern systems include Aegis BMD, THAAD, and Ground-Based Midcourse Defense. Effectiveness against peer adversary's saturation attack remains contested." },
  { id: "stealth-aircraft-doctrine", name: "Stealth Aircraft Doctrine", era: "information", category: "weapons",
    year: "1990", prereqs: ["jet-engine", "microprocessor"],
    desc: "Aircraft designed for radar-cross-section minimization through faceted geometry, radar-absorbing coatings, internal weapons bays, and IR signature suppression. The Lockheed F-117 Nighthawk (1981, first combat 1989 Panama, decisive in 1991 Gulf War) was the first operational stealth fighter; the B-2 Spirit (1989) the first stealth bomber. Stealth shifted air doctrine: penetrating contested airspace becomes feasible without large supporting strike packages, enabling decapitation and precision strikes against high-value defended targets. The F-22, F-35, J-20, and Su-57 represent the mature generation. Counter-stealth radar (low-frequency, multistatic, IR search-and-track) drives a continuing arms race." },
  { id: "network-centric-warfare", name: "Network-Centric Warfare", era: "information", category: "weapons",
    year: "2000", prereqs: ["arpanet-internet", "gps"],
    desc: "Doctrine in which military forces operate as a single information system: distributed sensors (satellites, drones, ground radars, individual soldier optics) feed a shared common operational picture; distributed shooters (any platform) engage targets identified by any sensor. Vice-Admiral Arthur Cebrowski formalized the concept (1998). The 1991 Gulf War showed precision-guided munitions; the 2003 Iraq War showed real-time information sharing. By the 2010s, Joint All-Domain Command and Control (JADC2) extended the concept across services and domains. Network-centric warfare is the operational substrate that makes drone swarms, cyber-kinetic operations, and AI-driven decision loops possible." },
  { id: "layered-air-missile-defense", name: "Layered Air & Missile Defense", era: "future", category: "weapons",
    year: "2035", prereqs: ["ballistic-missile-defense", "directed-energy-weapons"],
    desc: "Multi-tier interception architecture covering everything from artillery rockets to ICBMs: short-range systems (Iron Dome, Patriot) handle rockets and tactical ballistic missiles; mid-range (THAAD, Arrow-3) handle theater missiles; strategic (GMD, Aegis SM-3) handle ICBMs; directed-energy weapons handle drones, mortars, and cruise missiles at marginal cost per shot. Israel's combined-arms intercepted ~95% of Hamas rocket fire (May 2021). By 2035 the same architecture extends to peer-state defense, with AI fire-control routing each threat to its cheapest viable interceptor in milliseconds. The economics still favor offense for saturation attacks; layered defense buys time and political space, not invulnerability." },
  { id: "ai-decision-loop-compression", name: "AI Decision Loop Compression", era: "future", category: "weapons",
    year: "2045", prereqs: ["agi", "drone-swarms"],
    desc: "OODA loops (observe-orient-decide-act, John Boyd 1976) operating on millisecond timescales by delegating decisions to AI within tightly-scoped rules of engagement. The doctrine arises because human decision speed (~250ms reaction time, multi-second strategic deliberation) becomes the binding constraint when adversaries' loops are AI-compressed. By 2045, frontline weapons platforms execute target identification, threat prioritization, and engagement decisions algorithmically; humans retain strategic authority but tactical loops run autonomously. The doctrine is contested ethically (lethal autonomous weapons debate) and operationally (brittle to spoofing, unintended escalation), but military-competitive logic drives adoption regardless." },
"""

TRANSLATIONS = {
    "phalanx":                       "方阵",
    "roman-legion":                  "罗马军团",
    "castle-siege-doctrine":         "城堡与攻城学说",
    "pike-square":                   "长矛方阵",
    "trench-warfare":                "堑壕战",
    "combined-arms-warfare":         "诸兵种合成战",
    "blitzkrieg":                    "闪电战",
    "ballistic-missile-defense":     "弹道导弹防御",
    "stealth-aircraft-doctrine":     "隐身飞机学说",
    "network-centric-warfare":       "网络中心战",
    "layered-air-missile-defense":   "分层防空反导",
    "ai-decision-loop-compression":  "AI 决策环压缩",
}

UNLOCKS = {
    "phalanx": [
        ("unit",     "Greek hoplite",            "希腊重装步兵",       "Hoplite"),
        ("unit",     "Macedonian phalanx",       "马其顿方阵",         "Macedonian phalanx"),
        ("resource", "Sarissa",                  "萨里沙长矛",         "Sarissa"),
        ("work",     "Battle of Plataea",        "普拉提亚战役",       "Battle of Plataea"),
    ],
    "roman-legion": [
        ("unit",     "Marian Legion",            "马略改革后的军团",   "Marian reforms"),
        ("unit",     "Centurion",                "百夫长",             "Centurion"),
        ("resource", "Gladius",                  "短剑",               "Gladius"),
        ("resource", "Pilum",                    "投枪",               "Pilum"),
        ("resource", "Testudo formation",        "龟甲阵",             "Testudo formation"),
    ],
    "castle-siege-doctrine": [
        ("wonder",   "Krak des Chevaliers",      "骑士堡",             "Krak des Chevaliers"),
        ("wonder",   "Caernarfon Castle",        "卡那封城堡",         "Caernarfon Castle"),
        ("unit",     "Trebuchet",                "投石机",             "Trebuchet"),
        ("unit",     "Siege tower",              "攻城塔",             "Siege tower"),
        ("resource", "Concentric castle design", "同心圆式城堡设计",   "Concentric castle"),
    ],
    "pike-square": [
        ("unit",     "Swiss pikemen",            "瑞士长矛兵",         "Swiss mercenaries"),
        ("unit",     "Landsknecht",              "德意志雇佣兵",       "Landsknecht"),
        ("unit",     "Spanish tercio",           "西班牙方阵",         "Tercio"),
        ("work",     "Battle of Nancy",          "南锡战役",           "Battle of Nancy"),
    ],
    "trench-warfare": [
        ("work",     "Battle of the Somme",      "索姆河战役",         "Battle of the Somme"),
        ("work",     "Battle of Verdun",         "凡尔登战役",         "Battle of Verdun"),
        ("resource", "Barbed wire",              "带刺铁丝网",         "Barbed wire"),
        ("unit",     "Maxim machine gun nest",   "马克沁机枪阵地",     "Maxim gun"),
        ("resource", "Stormtrooper tactics",     "暴风突击队战术",     "Stormtrooper"),
    ],
    "combined-arms-warfare": [
        ("person",   "John Monash",              "约翰·莫纳什",       "John Monash"),
        ("person",   "Ferdinand Foch",           "费迪南·福煦",       "Ferdinand Foch"),
        ("person",   "J.F.C. Fuller",            "J.F.C. 富勒",        "J. F. C. Fuller"),
        ("work",     "Hundred Days Offensive",   "百日攻势",           "Hundred Days Offensive"),
        ("work",     "Plan 1919",                "1919 年计划",        "Plan 1919"),
    ],
    "blitzkrieg": [
        ("person",   "Heinz Guderian",           "海因茨·古德里安",   "Heinz Guderian"),
        ("person",   "Mikhail Tukhachevsky",     "米哈伊尔·图哈切夫斯基","Mikhail Tukhachevsky"),
        ("work",     "Achtung—Panzer!",          "《注意—坦克!》",    "Achtung – Panzer!"),
        ("work",     "Battle of France",         "法国战役",           "Battle of France"),
        ("resource", "Schwerpunkt",              "重点突破",           "Schwerpunkt"),
        ("resource", "Deep battle",              "大纵深作战",         "Deep operation"),
    ],
    "ballistic-missile-defense": [
        ("unit",     "Safeguard Program",        "保障计划",           "Safeguard Program"),
        ("unit",     "Strategic Defense Initiative","战略防御计划",    "Strategic Defense Initiative"),
        ("unit",     "Aegis Combat System",      "宙斯盾作战系统",     "Aegis Combat System"),
        ("unit",     "THAAD",                    "末段高空区域防御系统","Terminal High Altitude Area Defense"),
        ("work",     "Anti-Ballistic Missile Treaty","《反弹道导弹条约》", "Anti-Ballistic Missile Treaty"),
    ],
    "stealth-aircraft-doctrine": [
        ("unit",     "F-117 Nighthawk",          "F-117 夜鹰",         "Lockheed F-117 Nighthawk"),
        ("unit",     "B-2 Spirit",               "B-2 幽灵",           "Northrop Grumman B-2 Spirit"),
        ("unit",     "F-22 Raptor",              "F-22 猛禽",          "Lockheed Martin F-22 Raptor"),
        ("unit",     "F-35 Lightning II",        "F-35 闪电 II",       "Lockheed Martin F-35 Lightning II"),
        ("unit",     "Chengdu J-20",             "成都歼-20",          "Chengdu J-20"),
        ("resource", "Radar-absorbent material", "雷达吸波材料",       "Radar-absorbent material"),
    ],
    "network-centric-warfare": [
        ("person",   "Arthur Cebrowski",         "阿瑟·切布罗夫斯基", "Arthur K. Cebrowski"),
        ("resource", "Common operational picture","共同作战图景",      "Common operational picture"),
        ("resource", "JADC2",                    "联合全域指挥控制",   "Joint All-Domain Command and Control"),
        ("resource", "Sensor-shooter loop",      "传感器-射手回路",    False),
    ],
    "layered-air-missile-defense": [
        ("unit",     "Iron Dome",                "铁穹",               "Iron Dome"),
        ("unit",     "Patriot missile",          "爱国者导弹",         "MIM-104 Patriot"),
        ("unit",     "Arrow 3",                  "箭-3 反导拦截弹",     "Arrow 3"),
        ("unit",     "SM-3 interceptor",         "SM-3 拦截弹",         "RIM-161 Standard Missile 3"),
        ("resource", "Multi-tier intercept",     "多层拦截",           False),
    ],
    "ai-decision-loop-compression": [
        ("person",   "John Boyd",                "约翰·博伊德",       "John Boyd (military strategist)"),
        ("resource", "OODA loop",                "OODA 循环",          "OODA loop"),
        ("resource", "Lethal autonomous weapon", "致命自主武器",       "Lethal autonomous weapon"),
        ("work",     "Stop Killer Robots campaign","禁止杀人机器人运动","Campaign to Stop Killer Robots"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if 'id: "phalanx"' in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} doctrine techs")


def splice_translations():
    src = TRANS.read_text()
    if '"phalanx"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Warfare doctrine & tactics ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"phalanx"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Warfare doctrine & tactics ───\n"
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
