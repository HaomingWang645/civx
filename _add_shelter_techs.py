#!/usr/bin/env python3
"""Add 8 shelter / architecture techs filling era gaps."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Shelter & architecture (gap fill) ───
  { id: "mammoth-bone-hut", name: "Mammoth Bone Hut", era: "upper-paleo", category: "shelter",
    year: "~25 kya", prereqs: ["hide-clothing", "bone-tools"],
    desc: "Engineered cold-climate dwellings built by Gravettian and later Upper Paleolithic hunters from mammoth long-bones, jaws, and tusks lashed into circular frames and covered with hides. Mezhirich, Ukraine (~15 kya) preserves four such structures, each using ~95 mammoth bones — a labor and material investment implying a permanent winter base camp. Other examples are known from Mezin and Kostenki (Ukraine/Russia) and Dolní Věstonice (Czech Republic). The mammoth-bone hut is the earliest evidence of architecture as deliberate engineering — selecting and assembling specific structural elements rather than occupying natural shelter — and prefigures all later constructed dwellings." },
  { id: "roman-insula", name: "Roman Insula", era: "classical", category: "shelter",
    year: "~100 BCE", prereqs: ["arch-vault", "concrete-roman"],
    desc: "Multi-story urban apartment buildings, typically four to six stories with shops at street level and rented dwellings above. Imperial Rome at peak (~200 CE) housed perhaps 90% of its million-person population in insulae; Ostia preserves the form. Construction used opus latericium (concrete + brick facing) and tile floors over wooden beams. Insulae institutionalized the urban form Mediterranean cities have used continuously since: dense, mixed-use, walkable, vertical. The wealthy lived in domus (single-family courtyard houses) on the same street; the poor lived in collapsing wood-and-mudbrick top floors. Modern apartment housing descends directly from this tradition." },
  { id: "renaissance-dome", name: "Renaissance Architecture", era: "renaissance", category: "shelter",
    year: "1436", prereqs: ["gothic-architecture", "arch-vault"],
    desc: "Filippo Brunelleschi's 1436 dome over Florence Cathedral — the largest masonry dome in the world, built without flying buttresses or wooden centering, using a herringbone brick pattern Brunelleschi rediscovered from Roman precedent. The dome opened the Renaissance architectural revolution: classical orders rediscovered (Alberti, *De re aedificatura* 1452), mathematical proportion as design principle, central plans (Bramante's St. Peter's, 1506), villa architecture (Palladio, 1550). Renaissance architects established the role of the architect-as-intellectual and the building-as-design-product — separating design from construction, as opposed to the medieval master-mason tradition." },
  { id: "iron-frame-construction", name: "Iron-Frame Construction", era: "enlightenment", category: "shelter",
    year: "1779", prereqs: ["coke-iron"],
    desc: "Cast and wrought iron used as primary structural members rather than just decorative or auxiliary elements. Abraham Darby III's Iron Bridge (Coalbrookdale, 1779) was the demonstrator; the Crystal Palace (Joseph Paxton, 1851, 564m × 124m of iron and glass for the Great Exhibition) the breakthrough at scale. Iron framing made unprecedented spans (railway sheds, market halls, exhibition halls) and tall buildings (Eiffel Tower, 1889) possible. The structural revolution prepared the way for steel-frame skyscrapers (1885 Home Insurance Building) and reinforced concrete (1880s); modern construction descends entirely from this 18th-century innovation." },
  { id: "reinforced-concrete", name: "Reinforced Concrete", era: "industrial", category: "shelter",
    year: "1880", prereqs: ["bessemer-steel", "concrete-roman"],
    desc: "Concrete cast around steel-bar reinforcement: the steel takes tensile loads (where unreinforced concrete is weak), the concrete takes compression, and the alkaline matrix protects the steel from rust. Joseph Monier (1867 patent, garden tubs) and François Hennebique (1892, full structural system) established the technique. Reinforced concrete enables long-span floor slabs, cantilevered structures, and economical high-rise — Auguste Perret's apartments, Frank Lloyd Wright's Falling Water (1935), and the entire 20th-century postwar building stock. By 2020, ~30 billion tonnes of concrete are produced globally each year, the most-used construction material in human history." },
  { id: "suburban-tract-housing", name: "Suburban Tract Housing", era: "atomic", category: "shelter",
    year: "1947", prereqs: ["assembly-line", "automobile"],
    desc: "Mass-produced single-family detached homes laid out as auto-dependent residential subdivisions. William Levitt's Levittown, New York (1947–1951, ~17,000 homes built using Ford-style assembly-line construction) was the prototype; the postwar US, UK, Australian, and Canadian middle-class housing stock follows the same pattern. Federal mortgage policy (FHA, VA loans, GI Bill) plus the Interstate Highway System (1956) institutionalized suburbs as the dominant North American settlement form. Suburbs reshaped daily life around private automobiles, single-zoned residential land use, and the nuclear family — and locked-in dependencies on oil, road infrastructure, and segregated land use that contemporary urbanism is still wrestling with." },
  { id: "parametric-architecture", name: "Parametric Architecture", era: "information", category: "shelter",
    year: "2000", prereqs: ["personal-computer", "gui-mouse"],
    desc: "Buildings designed through algorithmic and computational rules — parameter spaces explored by software (Rhino + Grasshopper, Dynamo, Maya), construction documented as parametric models (BIM). Frank Gehry's Walt Disney Concert Hall (2003), Zaha Hadid's Heydar Aliyev Center (2012), and Patrik Schumacher's theory of 'parametricism' (2008) define the form. Computational design enables surfaces, structures, and façades that can't be drawn by hand — every panel a unique geometry, every node a custom connection. Critics argue parametric architecture's signature curvy geometries are a stylistic mannerism more than a substantive innovation; advocates argue it is the first building paradigm whose grammar exists only in code." },
  { id: "smart-building", name: "Smart Building", era: "information", category: "shelter",
    year: "2015", prereqs: ["arpanet-internet", "microprocessor"],
    desc: "Buildings integrating dense sensor networks, programmable HVAC and lighting controls, occupancy detection, and predictive analytics into a single building-management system (BMS). Energy use is optimized in real-time, security is continuous, occupants control their environment via smartphone, and operational data feeds back into design improvements. The Edge (Amsterdam, 2015) became the canonical demonstrator with 28,000 sensors and BREEAM rating of 98.36% (highest ever scored). Smart buildings cut typical commercial-building energy consumption by 30–50% and become substrate nodes in the broader smart-city/IoT fabric — but raise persistent privacy and cybersecurity questions." },
"""

TRANSLATIONS = {
    "mammoth-bone-hut":         "猛犸骨屋",
    "roman-insula":             "罗马公寓楼",
    "renaissance-dome":         "文艺复兴建筑",
    "iron-frame-construction":  "铁框架建筑",
    "reinforced-concrete":      "钢筋混凝土",
    "suburban-tract-housing":   "郊区住宅区",
    "parametric-architecture":  "参数化建筑",
    "smart-building":           "智能建筑",
}

UNLOCKS = {
    "mammoth-bone-hut": [
        ("wonder",   "Mezhirich",                "梅日里奇遗址",       "Mezhirich"),
        ("wonder",   "Dolní Věstonice",          "下维斯特尼采",       "Dolní Věstonice"),
        ("resource", "Mammoth-bone framework",   "猛犸骨架",           False),
        ("unit",     "Gravettian camp",          "格拉维特文化营地",    "Gravettian"),
    ],
    "roman-insula": [
        ("unit",     "Insula",                   "罗马公寓 (insula)",   "Insula (building)"),
        ("unit",     "Domus",                    "罗马宅邸 (domus)",    "Domus"),
        ("wonder",   "Ostia Antica",             "奥斯蒂亚古城",       "Ostia Antica"),
        ("resource", "Opus latericium",          "罗马混凝土砖工",     "Opus latericium"),
    ],
    "renaissance-dome": [
        ("person",   "Filippo Brunelleschi",     "菲利波·布鲁内莱斯基", "Filippo Brunelleschi"),
        ("person",   "Andrea Palladio",          "安德烈亚·帕拉第奥",  "Andrea Palladio"),
        ("person",   "Leon Battista Alberti",    "莱昂·巴蒂斯塔·阿尔伯蒂","Leon Battista Alberti"),
        ("wonder",   "Florence Cathedral",       "佛罗伦萨大教堂",     "Florence Cathedral"),
        ("wonder",   "St. Peter's Basilica",     "圣彼得大教堂",       "St. Peter's Basilica"),
        ("work",     "De re aedificatoria",      "《论建筑》",          "De re aedificatoria"),
    ],
    "iron-frame-construction": [
        ("person",   "Abraham Darby III",        "亚伯拉罕·达比三世",  "Abraham Darby III"),
        ("person",   "Joseph Paxton",            "约瑟夫·帕克斯顿",    "Joseph Paxton"),
        ("wonder",   "The Iron Bridge",          "铁桥",               "The Iron Bridge"),
        ("wonder",   "Crystal Palace",           "水晶宫",             "The Crystal Palace"),
        ("wonder",   "Eiffel Tower",             "埃菲尔铁塔",         "Eiffel Tower"),
    ],
    "reinforced-concrete": [
        ("person",   "Joseph Monier",            "约瑟夫·莫尼耶",      "Joseph Monier"),
        ("person",   "François Hennebique",      "弗朗索瓦·埃内比克",  "François Hennebique"),
        ("person",   "Auguste Perret",           "奥古斯特·佩雷",      "Auguste Perret"),
        ("wonder",   "Fallingwater",             "流水别墅",           "Fallingwater"),
        ("resource", "Hennebique system",        "埃内比克体系",       "Hennebique construction company"),
    ],
    "suburban-tract-housing": [
        ("wonder",   "Levittown",                "莱维敦",             "Levittown, New York"),
        ("person",   "William Levitt",           "威廉·莱维特",        "William Levitt"),
        ("org",      "Federal Housing Administration","美国联邦住房管理局","Federal Housing Administration"),
        ("work",     "GI Bill",                  "《退伍军人权利法案》",  "G.I. Bill"),
        ("resource", "Single-family zoning",     "单户住宅分区",        "Single-family zoning"),
    ],
    "parametric-architecture": [
        ("person",   "Zaha Hadid",               "扎哈·哈迪德",        "Zaha Hadid"),
        ("person",   "Frank Gehry",              "弗兰克·盖里",        "Frank Gehry"),
        ("wonder",   "Walt Disney Concert Hall", "沃尔特·迪士尼音乐厅", "Walt Disney Concert Hall"),
        ("wonder",   "Heydar Aliyev Center",     "海达尔·阿利耶夫中心",  "Heydar Aliyev Center"),
        ("unit",     "Grasshopper 3D",           "Grasshopper 参数化设计","Grasshopper 3D"),
        ("resource", "Building information modeling","建筑信息模型",   "Building information modeling"),
    ],
    "smart-building": [
        ("wonder",   "The Edge (Amsterdam)",     "Edge 大楼 (阿姆斯特丹)","The Edge (building)"),
        ("resource", "Building management system","建筑管理系统",      "Building management system"),
        ("resource", "BREEAM",                   "BREEAM 评估体系",      "BREEAM"),
        ("resource", "Internet of things",       "物联网",              "Internet of things"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if 'id: "mammoth-bone-hut"' in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} shelter techs")


def splice_translations():
    src = TRANS.read_text()
    if '"mammoth-bone-hut"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Shelter & architecture (gap fill) ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"mammoth-bone-hut"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Shelter & architecture (gap fill) ───\n"
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
