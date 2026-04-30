#!/usr/bin/env python3
"""Add 6 arts/entertainment techs (3 atomic, 3 information). Updates data.js,
translations.js, unlocks.js atomically."""

import json, re
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Arts & Entertainment (atomic / information) ───
  { id: "abstract-expressionism", name: "Abstract Expressionism", era: "atomic", category: "social",
    year: "1947", prereqs: ["oil-painting", "photography"],
    desc: "First American-led international art movement: Jackson Pollock's drip paintings (Number 1A, 1948), Mark Rothko's color fields, Willem de Kooning's gestural figuration, Barnett Newman's zips. Centered around the New York School and Peggy Guggenheim's Art of This Century gallery, the movement displaced Paris as the world's art capital after WWII. CIA-funded covert promotion (the Congress for Cultural Freedom) used it as Cold War soft power against socialist realism. Abstract Expressionism redefined what painting could be — process, scale, emotional intensity — and set the agenda for postwar visual art." },
  { id: "lp-vinyl-record", name: "LP / Vinyl Record", era: "atomic", category: "communication",
    year: "1948", prereqs: ["radio-wireless", "plastic-polymer"],
    desc: "Columbia Records' 33⅓ rpm long-playing microgroove disc (June 1948) replaced fragile 78 rpm shellac records with vinyl polymer offering ~22 minutes per side. RCA's competing 45 rpm single (1949) settled into the singles slot. Stereo recording arrived in 1958. The LP made the album — not the song — the artistic unit, enabling concept albums (Sgt. Pepper, 1967), gatefold cover art, and album-side dramaturgy. Vinyl dominated music distribution until cassette and CD displaced it; analog warmth and physical artifact value drove a 21st-century revival." },
  { id: "color-television", name: "Color Television", era: "atomic", category: "communication",
    year: "1954", prereqs: ["television", "transistor"],
    desc: "RCA's NTSC compatible color system (FCC approved December 1953, mass production from 1954) broadcast color while remaining compatible with existing black-and-white sets. PAL (Europe, 1967) and SECAM (France/USSR, 1967) followed with regional variants. Color penetration grew slowly — 1% of U.S. households in 1962, 50% in 1972 — limited by set price. Color transformed advertising effectiveness, news immediacy (Vietnam coverage), and the visual grammar of mass culture; sports, soap operas, and political conventions reshape themselves around the color-saturated screen." },
  { id: "video-games", name: "Video Games", era: "information", category: "social",
    year: "1972", prereqs: ["digital-computer", "transistor"],
    desc: "Atari's Pong (November 1972) and the Magnavox Odyssey (September 1972) launched the commercial video-game industry. Spacewar! (1962) was the technical precursor; Computer Space (1971) the first coin-op. Within a decade arcade games (Space Invaders 1978, Pac-Man 1980) and home consoles (Atari 2600, NES 1985) had created an entirely new mass medium with no historical precedent — interactive, visual, narrative. By the 2020s the global games industry exceeded film and music combined; gaming reshaped childhood, social interaction, and the development of computer hardware itself." },
  { id: "cgi-cinema", name: "CGI Cinema", era: "information", category: "communication",
    year: "1993", prereqs: ["cinema", "personal-computer"],
    desc: "Computer-generated imagery enters mainstream filmmaking: The Abyss (1989, ILM water tentacle), Terminator 2's liquid-metal T-1000 (1991), Jurassic Park's photorealistic dinosaurs (1993), and Toy Story's first fully-CG feature (1995, Pixar) marked the transition. By 2010 most studio films used CGI extensively; by 2020 photorealistic synthetic actors and entire CG environments were routine. Industrial Light & Magic, Weta Digital, and Pixar set the technical and artistic standards. CGI dissolved physical-effects constraints on storytelling but also enabled the spectacle-bloat tendencies of contemporary blockbuster cinema." },
  { id: "anime-globalization", name: "Anime Globalization", era: "information", category: "social",
    year: "1995", prereqs: ["sound-film", "mass-media"],
    desc: "Japanese animation breaks out of regional market into global cultural force: Akira (1988) opened Western critical attention; Pokémon (1996) hit children's TV worldwide; Studio Ghibli's Princess Mononoke (1997) and Spirited Away (2001, Oscar) won Western prestige; Cowboy Bebop (1998) and Neon Genesis Evangelion (1995) defined adult anime fandom abroad. Crunchyroll (2006) and Netflix anime licensing (2016+) made Japanese productions globally available. Anime aesthetics — large eyes, frenetic action, melancholic tones — propagate into Western animation, comics, fashion, and music videos." },
"""

TRANSLATIONS = {
    "abstract-expressionism": "抽象表现主义",
    "lp-vinyl-record":        "黑胶唱片",
    "color-television":       "彩色电视",
    "video-games":            "电子游戏",
    "cgi-cinema":             "计算机生成图像电影",
    "anime-globalization":    "日本动画全球化",
}

UNLOCKS = {
    "abstract-expressionism": [
        ("person",   "Jackson Pollock",      "杰克逊·波洛克", "Jackson Pollock"),
        ("person",   "Mark Rothko",          "马克·罗斯科",   "Mark Rothko"),
        ("person",   "Willem de Kooning",    "威廉·德·库宁", "Willem de Kooning"),
        ("work",     "Number 1A, 1948",      "《1A 号,1948》", "Number 1A, 1948"),
        ("org",      "New York School",      "纽约画派",       "New York School (art)"),
    ],
    "lp-vinyl-record": [
        ("resource", "33⅓ rpm microgroove",  "33⅓ 转长播放唱片", "LP record"),
        ("resource", "45 rpm single",        "45 转单曲唱片",   "Single (music)"),
        ("org",      "Columbia Records",     "哥伦比亚唱片公司", "Columbia Records"),
        ("work",     "Sgt. Pepper's Lonely Hearts Club Band", "《佩珀军士的孤独之心俱乐部乐队》", "Sgt. Pepper's Lonely Hearts Club Band"),
    ],
    "color-television": [
        ("resource", "NTSC standard",        "NTSC 制式",       "NTSC"),
        ("resource", "PAL standard",         "PAL 制式",        "PAL"),
        ("org",      "RCA",                  "美国无线电公司",  "RCA"),
        ("unit",     "RCA CT-100",           "RCA CT-100 彩色电视机", "RCA CT-100"),
    ],
    "video-games": [
        ("work",     "Pong",                 "《乓》",           "Pong"),
        ("work",     "Space Invaders",       "《太空侵略者》",   "Space Invaders"),
        ("work",     "Pac-Man",              "《吃豆人》",       "Pac-Man"),
        ("unit",     "Magnavox Odyssey",     "美格福斯奥德赛",   "Magnavox Odyssey"),
        ("unit",     "Atari 2600",           "雅达利 2600",      "Atari 2600"),
        ("org",      "Nintendo",             "任天堂",           "Nintendo"),
    ],
    "cgi-cinema": [
        ("work",     "Jurassic Park",        "《侏罗纪公园》",   "Jurassic Park (film)"),
        ("work",     "Terminator 2: Judgment Day", "《终结者2:审判日》", "Terminator 2: Judgment Day"),
        ("work",     "Toy Story",            "《玩具总动员》",   "Toy Story"),
        ("org",      "Industrial Light & Magic", "工业光魔",     "Industrial Light & Magic"),
        ("org",      "Pixar",                "皮克斯",           "Pixar"),
    ],
    "anime-globalization": [
        ("work",     "Akira",                "《阿基拉》",       "Akira (1988 film)"),
        ("work",     "Spirited Away",        "《千与千寻》",     "Spirited Away"),
        ("work",     "Neon Genesis Evangelion", "《新世纪福音战士》", "Neon Genesis Evangelion"),
        ("work",     "Pokémon",              "《精灵宝可梦》",   "Pokémon"),
        ("org",      "Studio Ghibli",        "吉卜力工作室",     "Studio Ghibli"),
        ("org",      "Crunchyroll",          "Crunchyroll",      "Crunchyroll"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "abstract-expressionism" in src:
        print("data.js: already inserted")
        return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    new_src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")
    DATA.write_text(new_src)
    print(f"data.js: +{len(TRANSLATIONS)} arts techs")


def splice_translations():
    src = TRANS.read_text()
    if '"abstract-expressionism"' in src:
        print("translations.js: already inserted")
        return
    block = "\n  // ─── Arts & Entertainment (atomic / information) ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip()
    assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"abstract-expressionism"' in src:
        print("unlocks.js: already inserted")
        return
    block = "\n  // ─── Arts & Entertainment (atomic / information) ───\n"
    for tid, items in UNLOCKS.items():
        block += f'  "{tid}": [\n'
        for typ, name, name_zh, wiki in items:
            block += (f'    {{ type: "{typ}", '
                      f'name: {json.dumps(name, ensure_ascii=False)}, '
                      f'name_zh: {json.dumps(name_zh, ensure_ascii=False)}, '
                      f'wiki: {json.dumps(wiki, ensure_ascii=False)} }},\n')
        block += '  ],\n'
    rs = src.rstrip()
    assert rs.endswith("};")
    UNLOCKS_PATH.write_text(rs[:-2] + block + "};\n")
    print(f"unlocks.js: +{len(UNLOCKS)}")


if __name__ == "__main__":
    splice_data()
    splice_translations()
    splice_unlocks()
