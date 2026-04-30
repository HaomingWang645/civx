#!/usr/bin/env python3
"""Spin off a Far Future era (2100–2500). Move the two existing 2100 techs
out of Future Age into Far Future, then add 10 new far-future technologies."""

import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# 10 new far-future techs.
TECHS = [
    ("dyson-swarm", "Dyson Swarm", "far-future", "energy", "2150",
     ["space-habitat", "asteroid-mining", "fusion-power"],
     "Orbital arrays of solar collectors capturing a significant fraction of the Sun's output. Freeman Dyson's 1960 paper proposed the construct as a signature of advanced civilization; modern refinement holds that loose swarms of statites are mechanically achievable while full rigid shells are not. Building one consumes most of a planet's worth of mass and millennium-scale industrial effort even at exponential growth. A complete Dyson swarm marks the threshold of Kardashev Type II — the energy budget of an entire star at humanity's disposal.",
     "戴森球", "Dyson sphere",
     [("person", "Freeman Dyson", "弗里曼·戴森"),
      ("unit", "Statite (solar sail)", "光力悬浮卫星"),
      ("work", "Kardashev scale", "卡尔达肖夫等级"),
      ("person", "Robert Bradbury", "罗伯特·布拉德伯里"),
      ("work", "Search for Dyson sphere candidates (Tabby's star)", "戴森球候选搜索(塔比之星)")]),

    ("matrioshka-brain", "Matrioshka Brain", "far-future", "tools", "2300",
     ["dyson-swarm", "advanced-chip-manufacturing", "agi"],
     "Solar-system-scale computational substrate: nested Dyson shells use solar energy at progressively cooler temperatures, each layer dedicated to computation. Robert Bradbury proposed the design (1997) as the upper bound of computational density per unit mass, exploiting reversible computing and minimum-Landauer-energy operations. A Matrioshka brain could simulate entire civilizations or run a single intelligence many orders of magnitude beyond any current mind. Whether it can host conscious experience at meaningful subjective rates depends on substrate properties unresolved at this scale.",
     "套娃式大脑", "Matrioshka brain",
     [("person", "Robert Bradbury", "罗伯特·布拉德伯里"),
      ("work", "Reversible computing", "可逆计算"),
      ("work", "Landauer's principle", "兰道尔原理"),
      ("unit", "Jupiter brain", "木星之脑")]),

    ("stellar-engineering", "Stellar Engineering", "far-future", "tools", "2500",
     ["dyson-swarm", "kardashev-type-ii"],
     "Active manipulation of stellar physics — moving stars, extending their lifespans, harvesting their mass. The Shkadov thruster (Leonid Shkadov, 1987) is a partial Dyson mirror whose asymmetric reflection produces net thrust on the host star, navigating it through the galaxy over millions of years. Star-lifting (David Criswell, 1985) involves removing mass from stars to extend their lifespan or harvest fuel. These engineering proposals require no new physics — only thousands of years of Type II infrastructure and patience.",
     "恒星工程", "Stellar engine",
     [("unit", "Shkadov thruster", "希卡多夫推进器"),
      ("unit", "Star lifting", "恒星采矿"),
      ("person", "Leonid Shkadov", "列昂尼德·希卡多夫"),
      ("person", "David Criswell", "大卫·克里斯韦尔")]),

    ("generation-ship-colony", "Generation Ship Colony", "far-future", "shelter", "2200",
     ["space-habitat", "fusion-rocket", "closed-loop-life-support"],
     "First successful establishment of a self-sustaining human colony at another star system. A generation ship — a thousand-person closed-cycle habitat — travels for centuries to Proxima Centauri b, TRAPPIST-1, or Tau Ceti, with descendants of the original crew arriving to terraform a new world. Hollowed-asteroid Rama-class habitats and constant-thrust fusion vessels are the leading designs; the social engineering of a centuries-spanning society in confinement is harder than the propulsion. The first colony is the moment humanity becomes irreversibly multi-stellar.",
     "世代飞船殖民", "Generation ship",
     [("work", "Project Hyperion", "海泊龙计划"),
      ("work", "100 Year Starship initiative", "百年星舰计划"),
      ("unit", "Rama-class habitat (Clarke)", "罗摩级栖息地(克拉克)"),
      ("wonder", "Proxima Centauri b", "比邻星b")]),

    ("galactic-civilization", "Galactic Civilization", "far-future", "economy", "2500",
     ["stellar-engineering", "generation-ship-colony", "agi"],
     "Multi-stellar human or post-human presence across hundreds to millions of star systems — Kardashev Type III civilization commanding the energy budget of an entire galaxy. Light-speed limits make tight political integration impossible; expect instead a constellation of independent or loosely-federated outposts, each with millennium-scale local culture. The Drake equation, Fermi paradox, and simulation argument become operational concerns. Whether a single galactic civilization or a fragmented archipelago is more likely is the open question.",
     "银河文明", "Type III civilization",
     [("work", "Kardashev Type III", "卡尔达肖夫III型"),
      ("work", "Drake equation", "德雷克方程"),
      ("work", "Fermi paradox", "费米悖论"),
      ("work", "Great Filter", "大过滤器"),
      ("person", "Carl Sagan (Cosmos)", "卡尔·萨根(宇宙)")]),

    ("speciation", "Post-Human Speciation", "far-future", "social", "2400",
     ["substrate-independent-humanity", "mars-colony", "anti-aging"],
     "Divergence of post-human descendants into multiple species or substantially distinct populations through natural selection in extreme environments (Mars, space habitats, low-G colonies, deep ocean) and through deliberate genetic engineering. Stephen Hawking, Cixin Liu, and Greg Egan have all explored the scenario. Reproductive isolation between Earth, Mars, asteroid-belt, and digital populations could begin within a few centuries; cross-species rights and cross-population reproduction would be unprecedented political problems. Speciation is the moment 'humanity' becomes a category rather than a species.",
     "物种分化", "Speciation",
     [("person", "Stephen Hawking", "史蒂芬·霍金"),
      ("person", "Cixin Liu", "刘慈欣"),
      ("person", "Greg Egan", "格雷格·伊根"),
      ("work", "The Diamond Age (Stephenson)", "《钻石时代》"),
      ("work", "Cordwainer Smith's Underpeople", "考德怀纳·史密斯笔下的下层人")]),

    ("substrate-independent-humanity", "Substrate-Independent Humanity", "far-future", "social", "2250",
     ["digital-immortality", "agi", "advanced-chip-manufacturing"],
     "Mass shift of human consciousness onto digital or hybrid biological-digital substrates. Whole-brain emulation becomes routine; backup, copying, and merging of minds are normal medical procedures; large fractions of humanity exist primarily in computational form. Continuity-of-self questions, copy-rights, and economic disruption (digital minds running thousands of times faster than biological humans) become live political issues. Hans Moravec, Ray Kurzweil, and Robin Hanson sketched competing visions; Hanson's 'Age of Em' (2016) is the most rigorous economic modeling.",
     "基底无关人类", "Posthuman",
     [("person", "Hans Moravec", "汉斯·莫拉维克"),
      ("person", "Ray Kurzweil", "雷·库兹韦尔"),
      ("person", "Robin Hanson", "罗宾·汉森"),
      ("work", "The Age of Em (book)", "《模拟人类时代》"),
      ("work", "Whole brain emulation", "全脑仿真")]),

    ("antimatter-production", "Antimatter Production", "far-future", "energy", "2200",
     ["fusion-power", "advanced-chip-manufacturing"],
     "Industrial-scale antimatter manufacture and storage. CERN's Penning traps now hold antiprotons for months; the AEgIS, ALPHA, and BASE experiments measure antihydrogen properties to high precision. Mass production at gram scale requires solar-collector–scale energy investment but enables propulsion at relativistic speeds and the most energy-dense physical fuel possible (E = mc² with full mass-conversion efficiency). By the late 22nd century, micrograms-per-year may be achievable; gram-scale by the 23rd; meaningful tonnages remain centuries out. The destructive potential and weaponization risk are profound.",
     "反物质生产", "Antimatter",
     [("org", "CERN", "欧洲核子研究组织"),
      ("unit", "Penning trap", "潘宁离子阱"),
      ("unit", "Antihydrogen", "反氢"),
      ("work", "Antimatter rocket", "反物质火箭"),
      ("work", "AEgIS experiment", "AEgIS实验")]),

    ("warp-drive", "Alcubierre Warp Drive", "far-future", "transport", "2400",
     ["quantum-gravity", "dark-sector-physics"],
     "A spacetime metric that contracts space ahead of a craft and expands it behind, enabling apparent faster-than-light travel without locally exceeding c. Miguel Alcubierre's 1994 General Relativity solution is mathematically valid but requires negative-energy density (exotic matter) and astronomical energy budgets. Recent work by Erik Lentz (2021) and the NASA Eagleworks group reduced energy requirements by orders of magnitude; whether a positive-energy-only solution exists is open. If achievable, warp drive collapses interstellar travel from millennia to days and effectively unifies the galaxy.",
     "曲速引擎", "Alcubierre drive",
     [("person", "Miguel Alcubierre", "米格尔·阿尔库别雷"),
      ("person", "Erik Lentz", "埃里克·伦茨"),
      ("org", "NASA Eagleworks", "NASA Eagleworks实验室"),
      ("work", "Krasnikov tube", "克拉斯尼科夫管"),
      ("resource", "Negative-energy density (exotic matter)", "负能量密度(奇异物质)")]),

    ("kardashev-type-ii", "Kardashev Type II Civilization", "far-future", "economy", "2250",
     ["dyson-swarm", "fusion-power"],
     "Civilization controlling the full energy output of its host star — ~10²⁶ watts, roughly ten billion times current human energy use. Nikolai Kardashev's 1964 scale defined Type II as the threshold of true cosmic engineering; partial Dyson swarms reach this milestone gradually. With Type II energy, terraforming planets, antimatter production, stellar engineering, and computronium fabrication all become tractable on millennium timescales. The transition from Type I (planetary) to Type II is the largest single energy step a civilization will take.",
     "卡尔达肖夫II型文明", "Kardashev scale",
     [("person", "Nikolai Kardashev", "尼古拉·卡尔达肖夫"),
      ("work", "Kardashev Type I (planetary)", "卡尔达肖夫I型(行星级)"),
      ("work", "Kardashev Type II (stellar)", "卡尔达肖夫II型(恒星级)"),
      ("person", "Carl Sagan (extension)", "卡尔·萨根(扩展)")]),
]


def http_json(url, retries=4):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt); continue
            raise


def http_bytes(url, retries=4):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt); continue
            raise


def main():
    src = DATA.read_text()

    # 1) Add far-future era to ERAS array, after future
    old_future_era = '  { id: "future",        name: "Future Age",         range: "2030 – beyond" },'
    new_eras_block = (
        '  { id: "future",        name: "Future Age",         range: "2030 – 2100" },\n'
        '  { id: "far-future",    name: "Far Future",         range: "2100 – 2500" },'
    )
    assert old_future_era in src, "ERAS line shape changed"
    src = src.replace(old_future_era, new_eras_block)

    # 2) Move digital-immortality and terraforming-mars to far-future
    for tid in ("digital-immortality", "terraforming-mars"):
        pat = re.compile(
            r'(\{\s*id:\s*"' + re.escape(tid) + r'"\s*,'
            r'\s*name:\s*"[^"]+"\s*,'
            r'\s*era:\s*")future("\s*,)', re.S)
        new_src, n = pat.subn(r'\1far-future\2', src)
        if n == 1:
            src = new_src
            print(f"  ↦ moved {tid} to far-future")
        else:
            print(f"  ! {tid}: era line not found ({n} replacements)")

    # 3) Insert new tech entries before closing `];`
    insertion_marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    assert insertion_marker in src
    blocks = ["\n  // ─── Far Future ───"]
    for tid, name, era, cat, year, prereqs, desc, *_ in TECHS:
        prq = ", ".join(f'"{p}"' for p in prereqs)
        blocks.append(
            f'  {{ id: "{tid}", name: "{name}", era: "{era}", category: "{cat}",\n'
            f'    year: "{year}", prereqs: [{prq}],\n'
            f'    desc: {json.dumps(desc, ensure_ascii=False)} }},'
        )
    src = src.replace(insertion_marker, "\n".join(blocks) + "\n" + insertion_marker)
    DATA.write_text(src)
    print(f"data.js: +1 era (far-future), +{len(TECHS)} techs, 2 era moves")

    # 4) Translations
    tsrc = TRANS.read_text()
    assert tsrc.rstrip().endswith("};")
    insertion = "\n  // ─── Far Future ───\n"
    for tid, _, _, _, _, _, _, zh, *_ in TECHS:
        insertion += f'  "{tid}": "{zh}",\n'
    tsrc = tsrc.rstrip()[:-2] + insertion + "};\n"
    TRANS.write_text(tsrc)
    print(f"translations.js: +{len(TECHS)}")

    # 5) Wikipedia images
    manifest = json.loads(MANIFEST.read_text())
    fetched = 0
    for tid, name, _, _, _, _, _, _, wiki, _ in TECHS:
        if tid in manifest and manifest[tid].get("status") == "ok":
            continue
        try:
            url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(wiki.replace(' ', '_'))
            j = http_json(url)
            thumb = (j.get("thumbnail") or {}).get("source")
            page = j.get("content_urls", {}).get("desktop", {}).get("page", url)
            if not thumb:
                manifest[tid] = {"name": name, "article": j.get("title"), "page": page,
                                 "status": "no_image", "reason": "no thumbnail"}
                print(f"  ! {tid}: no thumbnail in {wiki!r}")
                continue
            data, ctype = http_bytes(thumb)
            ext = ".jpg" if "jpeg" in ctype or "jpg" in ctype else ".png"
            out = IMG_DIR / f"{tid}{ext}"
            out.write_bytes(data)
            manifest[tid] = {
                "name": name, "article": j.get("title"), "page": page,
                "image_url": thumb, "image_path": str(out.relative_to(ROOT)),
                "extract": (j.get("extract") or "")[:280],
                "status": "ok", "score": 0.9, "reason": "manual override",
            }
            fetched += 1
            print(f"  + {tid:35} {j.get('title')} → {out.name}")
            time.sleep(0.6)
        except Exception as e:
            print(f"  ! {tid}: ERR {e}")
            manifest[tid] = {"name": name, "status": "no_match", "reason": str(e)[:120]}
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"images: {fetched} fetched")

    # 6) Regenerate images.js
    entries, attribution = {}, {}
    for k, v in manifest.items():
        if v.get("image_path"):
            entries[k] = v["image_path"]
            attribution[k] = {"article": v.get("article"), "url": v.get("page")}
    with open(ROOT / "images.js", "w") as f:
        f.write("// Auto-generated from _image_manifest.json. Do not edit by hand.\n")
        f.write("// Maps tech id -> Wikipedia image path + attribution.\n")
        f.write("window.TECH_IMAGES = " + json.dumps(entries, indent=2, ensure_ascii=False) + ";\n")
        f.write("window.TECH_IMAGE_CREDITS = " + json.dumps(attribution, indent=2, ensure_ascii=False) + ";\n")
    print(f"images.js: {len(entries)}")

    # 7) Unlocks
    usrc = UNLOCKS.read_text()
    assert usrc.rstrip().endswith("};")
    insertion = "\n  // ─── Far Future ───\n"
    for tid, _, _, _, _, _, _, _, _, ulocks in TECHS:
        insertion += f'  "{tid}": [\n'
        for typ, ename, ezh in ulocks:
            insertion += (f'    {{ type: "{typ}", '
                          f'name: {json.dumps(ename, ensure_ascii=False)}, '
                          f'name_zh: {json.dumps(ezh, ensure_ascii=False)} }},\n')
        insertion += '  ],\n'
    usrc = usrc.rstrip()[:-2] + insertion + "};\n"
    UNLOCKS.write_text(usrc)
    print(f"unlocks.js: +{len(TECHS)}")


if __name__ == "__main__":
    main()
