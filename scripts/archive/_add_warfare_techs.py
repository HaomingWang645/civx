#!/usr/bin/env python3
"""Add 7 warfare techs: 2 Enlightenment, 5 Industrial.
Updates data.js, translations.js, unlocks.js."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── More warfare (enlightenment / industrial) ───
  { id: "linear-infantry-tactics", name: "Linear Infantry Tactics", era: "enlightenment", category: "weapons",
    year: "1740", prereqs: ["musket", "standing-army"],
    desc: "Massed close-order infantry firing volleys on command in long thin lines two or three ranks deep. Frederick the Great's Prussian army drilled to fire 4–5 rounds per minute (twice the rate of contemporaries) and maneuver in rigid formation under fire — the decisive edge in the Silesian Wars. Linear tactics dominated European battlefields from 1690 through the Napoleonic Wars (1815). The discipline required to stand and reload while under enemy fire was achieved through brutal drill, harsh discipline, and the cohesion of regimental loyalty. Industrial-era rifling and entrenchment eventually rendered the line obsolete." },
  { id: "standardized-field-artillery", name: "Standardized Field Artillery", era: "enlightenment", category: "weapons",
    year: "1765", prereqs: ["artillery", "factory-system"],
    desc: "Jean-Baptiste Vaquette de Gribeauval's reform of French artillery (1765) standardized cannon calibers (4-, 8-, and 12-pounder field guns plus a 6-inch howitzer), introduced interchangeable parts, lightened carriages for road mobility, and trained dedicated artillery officers. The Gribeauval system gave France's revolutionary and Napoleonic armies decisive battlefield artillery superiority — the same gun could be repaired anywhere, ammunition was uniform, and crews could move pieces faster than infantry could redeploy. Other European armies copied the system after 1815. Modern military logistics descends directly from this artillery-reform model." },
  { id: "ironclad-warship", name: "Ironclad Warship", era: "industrial", category: "weapons",
    year: "1859", prereqs: ["naval-warship", "steamship"],
    desc: "Wooden-hulled warships clad in wrought-iron armor, propelled by steam: France's *Gloire* (1859) and Britain's HMS *Warrior* (1860) made every line-of-battle sailing ship instantly obsolete. The American Civil War's *Monitor* vs *Virginia* duel (March 1862) demonstrated ironclad invulnerability to conventional shellfire. Within a decade major navies converted entirely to steam-and-iron; within two, all-iron and then steel hulls. Ironclads transitioned naval warfare from a 300-year era of broadside sailing combat into modern industrial sea power, foreshadowing dreadnoughts and battleship fleets." },
  { id: "bolt-action-rifle", name: "Bolt-Action Rifle", era: "industrial", category: "weapons",
    year: "1867", prereqs: ["musket", "interchangeable-parts"],
    desc: "Breech-loading, magazine-fed rifle operated by a manually cycled bolt: Johann Nikolaus von Dreyse's needle gun (1841) was the prototype, but Mauser's Model 71 (1871) and the magazine-fed Model 98 (1898) defined the form. Bolt actions doubled or tripled the infantry firing rate over muzzle-loaders while remaining accurate to 600+ meters. Combined with smokeless powder and rimless cartridges (1880s), they gave WWI infantry the firepower that made attacking entrenchments suicidal. Variants of Mauser, Lee-Enfield, and Mosin-Nagant designs remained primary infantry weapons through WWII and saw service in some armies into the 21st century." },
  { id: "high-explosives", name: "High Explosives", era: "industrial", category: "weapons",
    year: "1867", prereqs: ["chemistry-modern"],
    desc: "Alfred Nobel's 1867 patent on dynamite — nitroglycerin stabilized in diatomaceous earth — gave engineers and miners a manageable high explosive ten times more powerful than gunpowder. TNT (1863, weaponized 1902), picric acid (Lyddite, 1888), and later RDX (1899) followed. High explosives transformed mining, tunneling, and demolition; militarily, they replaced black powder in artillery shells, enabled torpedo and naval mine warfare, and ultimately drove the explosive shell volume that defined WWI's industrial-scale killing. Nobel's prize (1895) was funded by the dynamite fortune — partly in atonement for premature obituaries calling him 'the merchant of death'." },
  { id: "modern-quick-firing-artillery", name: "Quick-Firing Artillery", era: "industrial", category: "weapons",
    year: "1897", prereqs: ["artillery", "machine-tool", "high-explosives"],
    desc: "The French 75mm field gun (Modèle 1897) introduced the hydropneumatic recoil mechanism: the barrel slid back on cylinders rather than transmitting recoil to the carriage, so the gun could fire 15–30 rounds per minute without needing to be re-aimed between shots. Combined with rapid-loading metallic-cartridge ammunition and high-explosive shells, the Soixante-Quinze made every previous artillery piece obsolete. Other powers raced to match: Krupp's 77mm (1896), the British 13- and 18-pounders, the Russian M1902. Quick-firing artillery dominated WWI battlefields and inflicted the majority of all WWI casualties." },
  { id: "dreadnought-battleship", name: "Dreadnought Battleship", era: "industrial", category: "weapons",
    year: "1906", prereqs: ["ironclad-warship", "modern-quick-firing-artillery"],
    desc: "HMS *Dreadnought* (Royal Navy, commissioned December 1906) consolidated the all-big-gun, steam-turbine-powered battleship: ten 12-inch guns in five centerline turrets, 21-knot turbine propulsion (faster than any prior battleship), heavy belt armor, controlled by central fire-direction. Her launch instantly obsoleted every previous battleship including those still under construction. Britain, Germany, the U.S., Japan, and others joined a furious dreadnought race that strained European budgets and contributed directly to the geopolitical pressure leading to WWI. Jutland (1916) was the only fleet-vs-fleet dreadnought engagement; aircraft carriers displaced battleships within a generation." },
"""

TRANSLATIONS = {
    "linear-infantry-tactics":      "线列步兵战术",
    "standardized-field-artillery": "标准化野战炮",
    "ironclad-warship":             "铁甲舰",
    "bolt-action-rifle":            "栓动步枪",
    "high-explosives":              "高爆炸药",
    "modern-quick-firing-artillery":"速射火炮",
    "dreadnought-battleship":       "无畏舰",
}

UNLOCKS = {
    "linear-infantry-tactics": [
        ("person",   "Frederick the Great",       "腓特烈大帝",       "Frederick the Great"),
        ("unit",     "Prussian Line Infantry",    "普鲁士线列步兵",   "Prussian Army"),
        ("work",     "Reglement of 1743",         "《1743 年训练条令》", False),
        ("resource", "Volley fire",               "齐射",             "Volley fire"),
    ],
    "standardized-field-artillery": [
        ("person",   "Jean-Baptiste de Gribeauval","让-巴蒂斯特·德·格里博瓦尔", "Jean-Baptiste Vaquette de Gribeauval"),
        ("unit",     "12-pounder field gun",      "12 磅野战炮",       "12-pounder long gun"),
        ("resource", "Gribeauval system",         "格里博瓦尔体系",     "Gribeauval system"),
        ("org",      "École d'application de l'artillerie", "炮兵应用学校", False),
    ],
    "ironclad-warship": [
        ("unit",     "HMS Warrior",               "HMS 勇士号",         "HMS Warrior (1860)"),
        ("unit",     "USS Monitor",               "美国海军舰艇监视者号", "USS Monitor"),
        ("unit",     "CSS Virginia",              "CSS 弗吉尼亚号",     "CSS Virginia"),
        ("unit",     "La Gloire",                 "光荣号",             "French ironclad Gloire"),
        ("work",     "Battle of Hampton Roads",   "汉普顿锚地海战",     "Battle of Hampton Roads"),
    ],
    "bolt-action-rifle": [
        ("person",   "Paul Mauser",               "保罗·毛瑟",         "Paul Mauser"),
        ("unit",     "Mauser Model 1898",         "毛瑟 1898 步枪",     "Mauser Model 1898"),
        ("unit",     "Lee-Enfield",               "李-恩菲尔德步枪",   "Lee–Enfield"),
        ("unit",     "Mosin-Nagant",              "莫辛-纳甘步枪",     "Mosin–Nagant"),
        ("unit",     "Dreyse Needle Gun",         "德赖斯针发枪",       "Dreyse needle gun"),
    ],
    "high-explosives": [
        ("person",   "Alfred Nobel",              "阿尔弗雷德·诺贝尔", "Alfred Nobel"),
        ("resource", "Dynamite",                  "硝化甘油炸药",       "Dynamite"),
        ("resource", "TNT",                       "三硝基甲苯",         "TNT"),
        ("resource", "Nitroglycerin",             "硝化甘油",           "Nitroglycerin"),
        ("org",      "Nobel Industries",          "诺贝尔工业",         "Nobel Industries"),
    ],
    "modern-quick-firing-artillery": [
        ("unit",     "French 75mm",               "法国 75 毫米速射炮", "Canon de 75 modèle 1897"),
        ("unit",     "Krupp 77mm",                "克虏伯 77 毫米炮",   "7.7 cm FK 96"),
        ("unit",     "British 18-pounder",        "英军 18 磅野战炮",   "Ordnance QF 18-pounder"),
        ("resource", "Hydropneumatic recoil",     "液气缓冲后座装置",   "Recoil"),
    ],
    "dreadnought-battleship": [
        ("unit",     "HMS Dreadnought",           "HMS 无畏号",         "HMS Dreadnought (1906)"),
        ("unit",     "SMS Bayern",                "SMS 巴伐利亚号",     "SMS Bayern"),
        ("unit",     "USS Texas",                 "USS 德克萨斯号",     "USS Texas (BB-35)"),
        ("work",     "Battle of Jutland",         "日德兰海战",         "Battle of Jutland"),
        ("person",   "John Fisher",               "约翰·费舍尔",       "John Fisher, 1st Baron Fisher"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "linear-infantry-tactics" in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} warfare techs")


def splice_translations():
    src = TRANS.read_text()
    if '"linear-infantry-tactics"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── More warfare (enlightenment / industrial) ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"linear-infantry-tactics"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── More warfare (enlightenment / industrial) ───\n"
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
