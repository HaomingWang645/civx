#!/usr/bin/env python3
"""Fill the Future Age gap between 2050 and 2100 with 6 new techs."""

import json, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

TECHS = [
    ("space-habitat", "Space Habitat", "future", "shelter", "2055",
     ["mars-colony", "fusion-power", "asteroid-mining"],
     "Orbital habitats spinning to provide artificial gravity, with miles-long pressurized interiors capable of supporting thousands of inhabitants. Gerard K. O'Neill's High Frontier (1976) proposed Lagrange-point colonies built from lunar and asteroid material; the Stanford torus and Bernal sphere are alternative geometries. With cheap reusable-rocket launch, asteroid-mined feedstock, and closed-loop life support, space habitats become economic by mid-century — possibly the dominant form of human off-world presence rather than planetary settlement.",
     "太空居住舱", "O'Neill cylinder",
     [("unit", "O'Neill cylinder", "奥尼尔圆筒"),
      ("unit", "Stanford torus", "斯坦福圆环"),
      ("unit", "Bernal sphere", "贝尔纳球"),
      ("person", "Gerard K. O'Neill", "杰拉德·K·奥尼尔"),
      ("org", "L5 Society", "L5协会"),
      ("work", "The High Frontier (book)", "《高边疆》")]),

    ("artificial-photosynthesis", "Artificial Photosynthesis", "future", "energy", "2060",
     ["nanotechnology", "synthetic-biology", "advanced-chip-manufacturing"],
     "Engineered systems that convert atmospheric CO₂ into fuels, plastics, and food directly using sunlight or electricity, bypassing biological inefficiency. Daniel Nocera's 'artificial leaf' (2011) and the Bionic Leaf 2.0 (2016) demonstrated proof-of-concept; commercial e-fuel plants (Twelve, Air Company, Synhelion) and electrochemical CO₂ reduction reach industrial scale by mid-century. Combined with cheap renewable electricity, artificial photosynthesis closes the carbon cycle and could feed billions on a fraction of current agricultural land.",
     "人工光合作用", "Artificial photosynthesis",
     [("person", "Daniel Nocera", "丹尼尔·诺切拉"),
      ("unit", "Artificial leaf", "人工叶"),
      ("unit", "Bionic Leaf 2.0", "仿生叶 2.0"),
      ("org", "Twelve (company)", "Twelve公司"),
      ("org", "Synhelion", "Synhelion"),
      ("org", "Air Company", "Air Company")]),

    ("genetic-disease-eradication", "Genetic Disease Eradication", "future", "medicine", "2065",
     ["crispr", "gene-therapy", "anti-aging"],
     "Eradication of all major monogenic genetic diseases — sickle cell, cystic fibrosis, Huntington's, Tay-Sachs, hemophilia, beta-thalassemia, muscular dystrophy — through germline editing, mature somatic gene therapy, and population-wide carrier screening. Casgevy (2023, sickle cell + beta-thalassemia) was the first FDA-approved CRISPR therapy; subsequent approvals extend to thousands of mutations. Polygenic risk scoring with embryo selection during IVF further reduces population frequency. By mid-century, inherited single-gene diseases are largely historical, with debates shifting to enhancement and equity of access.",
     "遗传病根除", "Casgevy",
     [("unit", "Casgevy (CRISPR therapy)", "Casgevy(CRISPR疗法)"),
      ("unit", "Luxturna", "Luxturna"),
      ("unit", "Zolgensma", "Zolgensma"),
      ("unit", "Polygenic risk score", "多基因风险评分"),
      ("person", "Jennifer Doudna", "詹妮弗·杜德纳")]),

    ("self-replicating-machines", "Self-Replicating Machines", "future", "tools", "2070",
     ["humanoid-robot", "agi", "asteroid-mining"],
     "Autonomous machines capable of using local materials to manufacture copies of themselves, enabling exponential expansion of industrial capacity. John von Neumann's 1948 universal constructor model is the theoretical foundation; Drexler's molecular assemblers, Freitas's lunar self-replicating-factory studies (NASA 1980), and proposed asteroid-mining swarms apply the principle. Once a self-replicating system bootstraps in space, the solar system's mineral wealth becomes accessible. Earth-bound versions raise gray-goo and runaway-replication safety concerns that constrain deployment.",
     "自我复制机器", "Self-replicating spacecraft",
     [("person", "John von Neumann", "约翰·冯·诺依曼"),
      ("person", "K. Eric Drexler", "K·埃里克·德雷克斯勒"),
      ("person", "Robert Freitas", "罗伯特·弗雷塔斯"),
      ("unit", "Universal constructor", "通用构造机"),
      ("work", "NASA 1980 study (Lunar self-replicating factory)", "NASA 1980年自复制工厂研究")]),

    ("superintelligence", "Superintelligence", "future", "knowledge", "2080",
     ["agi", "advanced-chip-manufacturing", "formal-mathematics"],
     "Artificial intelligence vastly exceeding human cognitive performance across all domains, with strategic, scientific, and creative capabilities qualitatively beyond what humans can achieve. I.J. Good's 1965 'intelligence explosion' argument framed the runaway-improvement scenario; Nick Bostrom's Superintelligence (2014), Stuart Russell's Human Compatible (2019), and Eliezer Yudkowsky's writings sharpened the alignment problem. Whether AGI scales smoothly to superintelligence — and whether humanity can control or align such a system — is the single most consequential open question for civilization.",
     "超级智能", "Superintelligence",
     [("person", "I.J. Good", "I·J·古德"),
      ("person", "Nick Bostrom", "尼克·博斯特罗姆"),
      ("person", "Stuart Russell", "斯图尔特·罗素"),
      ("person", "Eliezer Yudkowsky", "埃利泽·尤德科夫斯基"),
      ("work", "Superintelligence: Paths, Dangers, Strategies", "《超级智能》"),
      ("work", "AI alignment problem", "AI对齐问题")]),

    ("seti-first-contact", "Detection of Extraterrestrial Intelligence", "future", "knowledge", "2090",
     ["gravitational-wave-spectroscopy", "interstellar-probe", "large-language-model"],
     "Confirmed detection of extraterrestrial intelligence — a structured radio or optical signal, a technosignature artifact, a clearly engineered biosignature, or direct contact via interstellar probe. Frank Drake's Project Ozma (1960) inaugurated the search; the SETI Institute, Breakthrough Listen (2015–), and improving exoplanet biosignature detection (JWST and Habitable Worlds Observatory in the 2040s) progressively cover more of the search space. The Drake equation, Fermi paradox, and proposed post-detection protocols become live operational questions rather than thought experiments — and recontextualize humanity's place in the universe.",
     "地外文明探测", "Search for extraterrestrial intelligence",
     [("person", "Frank Drake", "弗兰克·德雷克"),
      ("org", "SETI Institute", "SETI研究所"),
      ("work", "Drake equation", "德雷克方程"),
      ("work", "Fermi paradox", "费米悖论"),
      ("org", "Breakthrough Listen", "突破聆听计划"),
      ("unit", "Project Ozma (1960)", "奥兹玛计划")]),
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
    insertion_marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    assert insertion_marker in src
    blocks = ["\n  // ─── Future Age (mid-century, 2055-2090) ───"]
    for tid, name, era, cat, year, prereqs, desc, *_ in TECHS:
        prq = ", ".join(f'"{p}"' for p in prereqs)
        blocks.append(
            f'  {{ id: "{tid}", name: "{name}", era: "{era}", category: "{cat}",\n'
            f'    year: "{year}", prereqs: [{prq}],\n'
            f'    desc: {json.dumps(desc, ensure_ascii=False)} }},'
        )
    src = src.replace(insertion_marker, "\n".join(blocks) + "\n" + insertion_marker)
    DATA.write_text(src)
    print(f"data.js: +{len(TECHS)} techs")

    tsrc = TRANS.read_text()
    assert tsrc.rstrip().endswith("};")
    insertion = "\n  // ─── Future Age (mid-century) ───\n"
    for tid, _, _, _, _, _, _, zh, *_ in TECHS:
        insertion += f'  "{tid}": "{zh}",\n'
    tsrc = tsrc.rstrip()[:-2] + insertion + "};\n"
    TRANS.write_text(tsrc)
    print(f"translations.js: +{len(TECHS)}")

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

    usrc = UNLOCKS.read_text()
    assert usrc.rstrip().endswith("};")
    insertion = "\n  // ─── Future Age (mid-century) ───\n"
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
