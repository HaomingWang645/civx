#!/usr/bin/env python3
"""Add 4 misc techs across the timeline + chain germ-theory through cell-theory."""

import json, re
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Misc additions (industrial → information) ───
  { id: "cell-theory", name: "Cell Theory", era: "industrial", category: "knowledge",
    year: "1839", prereqs: ["microscope", "chemistry-modern"],
    desc: "Matthias Schleiden (plants, 1838) and Theodor Schwann (animals, 1839): all living organisms are composed of cells, the cell is the basic structural unit, and cells arise only from pre-existing cells (the third proposition added by Rudolf Virchow, 1855: 'omnis cellula e cellula'). Cell theory is to biology what atomic theory is to chemistry — the unifying framework that organizes everything else. It made microbiology, embryology, immunology, oncology, and modern molecular biology possible. Pasteur's germ theory (1860s), Koch's postulates (1884), and the entire 20th-century biomedical revolution all rest on cell theory's foundation." },
  { id: "modern-olympics", name: "Modern Olympics", era: "industrial", category: "social",
    year: "1896", prereqs: ["nation-state", "newspaper-mass"],
    desc: "Pierre de Coubertin's revival of the ancient Greek games: Athens 1896 brought 241 athletes from 14 nations. The IOC formalized international competition in standardized sports under shared rules; subsequent Games (Paris 1900, St. Louis 1904, London 1908) institutionalized the four-year cycle, the medal system, and the opening ceremonies. The Winter Olympics (1924), Paralympics (1948/1960), and Youth Olympics (2010) extended the model. The modern Olympics became the largest peacetime international gathering on Earth — Tokyo 2020 had 11,000 athletes from 206 nations — and a recurring stage for political conflicts (1936 Berlin, 1968 Mexico City, 1972 Munich, 1980/1984 boycotts)." },
  { id: "civil-aviation", name: "Civil Aviation", era: "modern", category: "transport",
    year: "1920", prereqs: ["airplane"],
    desc: "Commercial passenger and cargo air transport. KLM (1919, the oldest still-operating airline), Aeroflot (1923), Imperial Airways (1924), and Pan Am (1927) opened scheduled routes. The Douglas DC-3 (1936) made airline operations economically viable; the Boeing 707 (1958) brought long-haul jet travel; the 747 (1969) and the Concorde (1976) defined the supersonic and jumbo eras. The 1944 Chicago Convention created ICAO and the framework for international aviation rights. Civil aviation collapsed travel times by an order of magnitude (London-New York: 5 days by ship → 7 hours by jet) and connected the world economically and culturally." },
  { id: "mobile-internet", name: "Mobile Internet", era: "information", category: "communication",
    year: "2000", prereqs: ["arpanet-internet", "mobile-phone"],
    desc: "Internet access from cellular handsets. WAP (Wireless Application Protocol, 1999) and i-mode (NTT DoCoMo, Japan, 1999) were the first commercial deployments; 3G (2001+), the iPhone (2007), and Android (2008) made it a mass medium. By 2014, mobile internet usage exceeded desktop usage; by 2024, ~5.5 billion people used mobile internet daily. Mobile internet enabled a new wave of platforms — WhatsApp, Instagram, TikTok, ride-sharing, mobile banking, mobile commerce — and brought online connectivity to populations that had skipped over wireline infrastructure (especially in Africa and South Asia: leapfrogging)." },
"""

TRANSLATIONS = {
    "cell-theory":     "细胞学说",
    "modern-olympics": "现代奥林匹克运动会",
    "civil-aviation":  "民用航空",
    "mobile-internet": "移动互联网",
}

UNLOCKS = {
    "cell-theory": [
        ("person",   "Matthias Schleiden",     "马蒂亚斯·施莱登",     "Matthias Jakob Schleiden"),
        ("person",   "Theodor Schwann",        "泰奥多尔·施旺",       "Theodor Schwann"),
        ("person",   "Rudolf Virchow",         "鲁道夫·菲尔绍",       "Rudolf Virchow"),
        ("resource", "Cell (biology)",         "细胞",                "Cell (biology)"),
        ("resource", "Mitosis",                "有丝分裂",            "Mitosis"),
    ],
    "modern-olympics": [
        ("person",   "Pierre de Coubertin",    "皮埃尔·德·顾拜旦",    "Pierre de Coubertin"),
        ("org",      "International Olympic Committee", "国际奥林匹克委员会", "International Olympic Committee"),
        ("work",     "Athens 1896",            "1896 年雅典奥运会",   "1896 Summer Olympics"),
        ("work",     "Olympic Charter",        "《奥林匹克宪章》",     "Olympic Charter"),
    ],
    "civil-aviation": [
        ("unit",     "Douglas DC-3",           "道格拉斯 DC-3",       "Douglas DC-3"),
        ("unit",     "Boeing 707",             "波音 707",            "Boeing 707"),
        ("unit",     "Boeing 747",             "波音 747",            "Boeing 747"),
        ("org",      "KLM",                    "荷兰皇家航空",        "KLM"),
        ("org",      "Pan American World Airways", "泛美航空",         "Pan American World Airways"),
        ("org",      "International Civil Aviation Organization", "国际民用航空组织", "International Civil Aviation Organization"),
    ],
    "mobile-internet": [
        ("unit",     "i-mode",                 "i-mode 移动数据服务",  "I-mode"),
        ("resource", "Wireless Application Protocol", "无线应用协议",  "Wireless Application Protocol"),
        ("resource", "3G",                     "第三代移动通信",       "3G"),
        ("unit",     "iPhone (1st generation)","初代 iPhone",         "IPhone (1st generation)"),
        ("unit",     "Android (operating system)","安卓系统",          "Android (operating system)"),
    ],
}

# Connect cell-theory into germ-theory's lineage.
PREREQ_ADDS = [("germ-theory", "cell-theory")]


def splice_data():
    src = DATA.read_text()
    if 'id: "cell-theory"' in src:
        print("data.js: already inserted")
    else:
        marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
        if marker not in src: raise SystemExit("Closing marker not found")
        src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")
        print(f"data.js: +{len(TRANSLATIONS)} misc techs")

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
    if '"cell-theory"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Misc additions ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"cell-theory"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Misc additions ───\n"
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
