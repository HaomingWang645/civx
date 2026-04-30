#!/usr/bin/env python3
"""Add 6 air-defense / support-doctrine techs."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Air defense + military support ───
  { id: "military-logistics", name: "Military Logistics", era: "industrial", category: "weapons",
    year: "1870", prereqs: ["railroad-network", "telegraph"],
    desc: "Modern military supply, movement, and sustainment as a planned discipline. Helmuth von Moltke the Elder's Prussian General Staff (1857–) institutionalized the railroad-and-telegraph mobilization plan, demonstrated decisively against Austria (1866) and France (1870–71). The American Civil War (1861–65) pioneered industrial-scale rail-based military supply on the Union side. Subsequent generations — WWI's munitions logistics, WWII's Red Ball Express and floating naval supply trains, the Berlin Airlift (1948), Vietnam's helicopter logistics, Gulf War sealift — defined modern war as a logistics-bound activity. 'Amateurs talk strategy, professionals talk logistics.'" },
  { id: "anti-aircraft-artillery", name: "Anti-Aircraft Artillery", era: "modern", category: "weapons",
    year: "1916", prereqs: ["modern-quick-firing-artillery", "airplane"],
    desc: "High-angle, fast-traversing artillery designed to engage aircraft. WWI improvised AA was inadequate; WWII saw mature systems — the German 8.8 cm FlaK 18/36 (the famous 88, equally effective against tanks), Bofors 40 mm, Vickers QF 3.7 inch, U.S. M1 90 mm. Combined with rangefinders, predictors, and (after 1940) radar fire-control, AA artillery shot down enormous numbers of bomber aircraft over Germany, Britain, and the Pacific. Surface-to-air missiles displaced AA guns from the high-altitude role after ~1960; close-in cannon (Phalanx CIWS, AK-630) survived for ship and base defense at short range." },
  { id: "combat-medic", name: "Combat Medic & Medevac", era: "atomic", category: "medicine",
    year: "1951", prereqs: ["helicopter", "antibiotics"],
    desc: "Forward medical care plus rapid casualty evacuation. Korean War MASH (Mobile Army Surgical Hospital) units (1950s) and Bell H-13 helicopter medevacs cut field-mortality dramatically by acting on R Adams Cowley's 'golden hour' concept. Vietnam's Dustoff and Medevac UH-1 squadrons routinely flew under fire to retrieve casualties. The Israeli IDF's TCCC (Tactical Combat Casualty Care, 1996+) standardized prolonged field-care for injuries: tourniquets, hemostatic gauze, needle decompression. Modern doctrine (deployed since Iraq/Afghanistan) keeps wounded alive with field-applied care for 60+ minutes; combat death-rate-from-wound has roughly halved since Vietnam." },
  { id: "spy-satellite", name: "Spy Satellite", era: "atomic", category: "weapons",
    year: "1960", prereqs: ["satellite", "photography"],
    desc: "Orbital reconnaissance: KH-1 Corona (U.S., first successful film return August 1960), KH-11 Kennen (1976+, the first electro-optical real-time satellite). The Soviet Zenit-2 (1961), Yantar (1974+), and modern Resurs-P series; China's Yaogan family (2006+); commercial spinoffs (Maxar, Planet Labs, Capella). Spy satellites replaced manned overflights after the 1960 U-2 shootdown, allowing routine surveillance over closed states without political incident. Modern variants combine sub-30-cm optical, synthetic-aperture radar, and signals intelligence; resolution is now constrained more by atmospheric blur than orbit altitude." },
  { id: "awacs", name: "Airborne Early Warning", era: "atomic", category: "weapons",
    year: "1965", prereqs: ["radar", "jet-engine"],
    desc: "Aircraft carrying long-range radar and battle-management consoles, providing radar coverage that cannot be terrain-masked the way ground radars are. Early TBM Avenger and EC-121 Warning Star adaptations (1950s) led to the modern E-3 Sentry (Boeing 707 with 30-foot rotodome, IOC 1977), Russian A-50 Mainstay, Chinese KJ-2000. AWACS aircraft control fighter operations across hundreds of kilometers, vector interceptors onto incoming raids, and provide the airborne 'eyes' that integrated air-defense systems coordinate around. Loss of an AWACS in a peer war would catastrophically degrade fleet/air defense — making them top-tier targets." },
  { id: "iads", name: "Integrated Air Defense System", era: "information", category: "weapons",
    year: "1980", prereqs: ["ballistic-missile-defense", "awacs"],
    desc: "Networked layered defense combining surface-to-air missile batteries, anti-aircraft artillery, fighter aircraft, and AWACS, all linked by hardened command-and-control. Soviet PVO-Strany (1948–98) was the original; modern variants include Russian S-300/S-400 systems, the IADS that defended Saddam Hussein's Iraq (heavily attrited 1991/2003), Iran's Bavar-373 + S-300 mix, and China's HQ-9 + integrated radar fence. Defeating a peer IADS — Suppression of Enemy Air Defenses (SEAD) — drives much of NATO's stealth, electronic-warfare, and stand-off-weapons inventory." },
"""

TRANSLATIONS = {
    "military-logistics":      "军事后勤",
    "anti-aircraft-artillery": "高射炮",
    "combat-medic":            "战地医护与医疗后送",
    "spy-satellite":           "侦察卫星",
    "awacs":                   "空中预警机",
    "iads":                    "综合防空系统",
}

UNLOCKS = {
    "military-logistics": [
        ("person",   "Helmuth von Moltke the Elder", "老毛奇",        "Helmuth von Moltke the Elder"),
        ("org",      "German General Staff",         "德国总参谋部",   "German General Staff"),
        ("work",     "Berlin Airlift",               "柏林空运",       "Berlin Blockade"),
        ("unit",     "Red Ball Express",             "红球快运",       "Red Ball Express"),
    ],
    "anti-aircraft-artillery": [
        ("unit",     "8.8 cm FlaK 36",               "88 毫米高射炮",  "8.8 cm Flak 18/36/37/41"),
        ("unit",     "Bofors 40 mm",                 "博福斯 40 毫米炮", "Bofors 40 mm gun"),
        ("unit",     "Phalanx CIWS",                 "密集阵近防系统", "Phalanx CIWS"),
        ("resource", "Proximity fuze",               "近炸引信",       "Proximity fuze"),
    ],
    "combat-medic": [
        ("unit",     "Mobile Army Surgical Hospital","流动军外科医院",  "Mobile army surgical hospital"),
        ("unit",     "Bell UH-1 Iroquois",           "贝尔 UH-1 直升机", "Bell UH-1 Iroquois"),
        ("resource", "Tactical Combat Casualty Care","战术伤员救护",   "Tactical Combat Casualty Care"),
        ("resource", "Tourniquet",                   "止血带",         "Tourniquet"),
        ("resource", "Golden hour",                  "黄金救援时间",    "Golden hour (medicine)"),
    ],
    "spy-satellite": [
        ("unit",     "KH-1 Corona",                  "KH-1 科罗娜",     "Corona (satellite)"),
        ("unit",     "KH-11 Kennen",                 "KH-11 凯南",      "KH-11 KENNEN"),
        ("unit",     "Zenit (satellite)",            "天顶号侦察卫星",  "Zenit (satellite)"),
        ("org",      "National Reconnaissance Office","美国国家侦察局",  "National Reconnaissance Office"),
        ("resource", "Synthetic-aperture radar",     "合成孔径雷达",    "Synthetic-aperture radar"),
    ],
    "awacs": [
        ("unit",     "Boeing E-3 Sentry",            "波音 E-3 哨兵",   "Boeing E-3 Sentry"),
        ("unit",     "Beriev A-50",                  "别里耶夫 A-50",   "Beriev A-50"),
        ("unit",     "KJ-2000",                      "空警-2000",       "KJ-2000"),
        ("unit",     "Lockheed EC-121 Warning Star", "EC-121 预警星",   "Lockheed EC-121 Warning Star"),
        ("resource", "Rotodome",                     "圆盘形雷达罩",     "Rotodome"),
    ],
    "iads": [
        ("unit",     "S-400 missile system",         "S-400 防空导弹系统","S-400 missile system"),
        ("unit",     "Patriot missile",              "爱国者导弹",       "MIM-104 Patriot"),
        ("unit",     "HQ-9 missile system",          "红旗-9 防空导弹",  "HQ-9"),
        ("org",      "PVO Strany",                   "苏联国土防空军",   "Soviet Air Defence Forces"),
        ("resource", "Suppression of Enemy Air Defenses", "压制敌防空体系", "Suppression of Enemy Air Defenses"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if 'id: "military-logistics"' in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src: raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} air-defense / support techs")


def splice_translations():
    src = TRANS.read_text()
    if '"military-logistics"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Air defense + military support ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"military-logistics"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Air defense + military support ───\n"
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
