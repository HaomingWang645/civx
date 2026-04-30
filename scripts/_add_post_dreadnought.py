#!/usr/bin/env python3
"""Add Assault Rifle and Guided Missile Destroyer; update machine-gun and
aircraft-carrier prereqs to chain through their natural predecessors."""

import json, re
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Post-WWI weapons platforms ───
  { id: "assault-rifle", name: "Assault Rifle", era: "modern", category: "weapons",
    year: "1944", prereqs: ["bolt-action-rifle", "machine-gun"],
    desc: "Select-fire infantry rifle firing an intermediate-cartridge round (between pistol and full-rifle in power). The German StG 44 (1944) — Hugo Schmeisser's 'Sturmgewehr' — was the first; the Soviet AK-47 (Mikhail Kalashnikov, 1947) and the U.S. M16 (Eugene Stoner, 1964) became the global infantry standards. Compared to bolt-action rifles, an assault rifle adds full-auto fire; compared to submachine guns, it adds rifle-class range and accuracy. Light, cheap, robust variants of the AK family have armed both state militaries and insurgencies in essentially every conflict since 1947 — over 100 million produced." },
  { id: "guided-missile-destroyer", name: "Guided Missile Destroyer", era: "atomic", category: "weapons",
    year: "1962", prereqs: ["dreadnought-battleship", "guided-missile"],
    desc: "Surface combatant whose primary armament is missiles rather than guns: long-range surface-to-air (Standard, S-300, Sea Dart) for fleet defense, anti-ship and land-attack cruise missiles (Tomahawk, Harpoon, Kalibr), and torpedo + ASW helicopter for sub-hunting. USS Charles F. Adams (DDG-2, commissioned 1960) and the Soviet Kashin class (1962) marked the transition; the Arleigh Burke class (1991+) and Type 052D (China, 2014+) define the modern form, all built around the Aegis or equivalent combat system. The guided-missile destroyer displaced the gun-armed cruiser and battleship as the workhorse surface combatant of every blue-water navy." },
"""

TRANSLATIONS = {
    "assault-rifle":             "突击步枪",
    "guided-missile-destroyer":  "导弹驱逐舰",
}

UNLOCKS = {
    "assault-rifle": [
        ("unit",     "StG 44",                  "StG 44 突击步枪",     "StG 44"),
        ("unit",     "AK-47",                   "AK-47 突击步枪",      "AK-47"),
        ("unit",     "M16 rifle",               "M16 步枪",            "M16 rifle"),
        ("person",   "Mikhail Kalashnikov",     "米哈伊尔·卡拉什尼科夫", "Mikhail Kalashnikov"),
        ("person",   "Hugo Schmeisser",         "雨果·施迈瑟",          "Hugo Schmeisser"),
        ("resource", "Intermediate cartridge",  "中间型弹药",            "Intermediate cartridge"),
    ],
    "guided-missile-destroyer": [
        ("unit",     "Arleigh Burke-class destroyer", "阿利·伯克级驱逐舰", "Arleigh Burke-class destroyer"),
        ("unit",     "USS Charles F. Adams",    "查尔斯·F·亚当斯号",     "USS Charles F. Adams (DDG-2)"),
        ("unit",     "Type 052D destroyer",     "052D 型驱逐舰",          "Type 052D destroyer"),
        ("unit",     "Aegis Combat System",     "宙斯盾作战系统",         "Aegis Combat System"),
        ("resource", "Tomahawk missile",        "战斧巡航导弹",           "Tomahawk (missile)"),
    ],
}

# Existing techs to extend with the new natural prereq.
# (target-id, prereq-to-add)
PREREQ_ADDS = [
    ("machine-gun",       "bolt-action-rifle"),    # 1884 → adds 1867 ✓
    ("aircraft-carrier",  "dreadnought-battleship"),# 1922 → adds 1906 ✓
]


def splice_data():
    src = DATA.read_text()

    # Insert new techs at end (before closing of TECHS array).
    if 'id: "assault-rifle"' in src:
        print("data.js: assault-rifle already present")
    else:
        marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
        if marker not in src: raise SystemExit("Closing marker not found")
        src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")
        print("data.js: +2 weapons techs (assault-rifle, guided-missile-destroyer)")

    # Add prereqs to existing techs.
    for tid, new in PREREQ_ADDS:
        pat = re.compile(r'(\{\s*id:\s*"' + re.escape(tid) + r'"\s*,[^{}]*?prereqs:\s*\[)(?P<plist>[^\]]*)\]', re.S)
        m = pat.search(src)
        if not m:
            print(f"  WARN: {tid} not found"); continue
        plist = m.group("plist")
        if f'"{new}"' in plist:
            print(f"  {tid}: already has {new}"); continue
        new_plist = plist.rstrip().rstrip(",")
        new_plist = (new_plist + f', "{new}"') if new_plist else f'"{new}"'
        src = src[:m.start()] + m.group(1) + new_plist + "]" + src[m.end():]
        print(f"  {tid}: + {new}")

    DATA.write_text(src)


def splice_translations():
    src = TRANS.read_text()
    if '"assault-rifle"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Post-WWI weapons platforms ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"assault-rifle"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Post-WWI weapons platforms ───\n"
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
