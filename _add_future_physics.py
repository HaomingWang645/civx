#!/usr/bin/env python3
"""Add 5 physics/math future achievements to the Future Age."""

import json, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# (id, name, era, category, year, prereqs, desc, zh, wiki, unlocks)
TECHS = [
    ("formal-mathematics", "Machine-Verified Mathematics", "future", "knowledge", "2035",
     ["programming-language", "deep-learning", "large-language-model"],
     "AI-assisted theorem proving and machine-verified mathematics at scale. Lean, Coq, Isabelle, and Mizar provide formal-proof languages; the Liquid Tensor Experiment (Scholze, 2020), Mathlib's growing library, and DeepMind's AlphaProof (2024 IMO silver) demonstrate the trajectory. By the 2030s, large language models routinely propose and verify proofs, most newly published theorems are machine-checked, and AI systems begin attacking long-open problems beyond unaided human reach. The certainty floor of mathematics rises permanently.",
     "形式化数学", "Lean (proof assistant)",
     [("unit", "Lean theorem prover", "Lean证明助手"),
      ("unit", "Coq", "Coq证明助手"),
      ("unit", "Mathlib", "Mathlib数学库"),
      ("unit", "AlphaProof (DeepMind)", "AlphaProof(DeepMind)"),
      ("person", "Terence Tao", "陶哲轩"),
      ("person", "Peter Scholze", "彼得·朔尔策")]),

    ("gravitational-wave-spectroscopy", "Gravitational-Wave Spectroscopy", "future", "knowledge", "2045",
     ["relativity", "advanced-chip-manufacturing"],
     "Multi-band gravitational-wave astronomy across frequencies from nanohertz (pulsar-timing arrays, NANOGrav 2023) through millihertz (ESA-NASA LISA, ~2035 launch) to kilohertz (LIGO/Virgo/KAGRA and the proposed Einstein Telescope/Cosmic Explorer). Combined with electromagnetic and neutrino observations, gravitational-wave astronomy makes black-hole mergers, neutron-star equations of state, and possibly inflationary echoes routine measurements rather than rare events — extending the electromagnetic spectrum's century of revelations to the geometry of spacetime itself.",
     "引力波光谱学", "Gravitational-wave astronomy",
     [("unit", "LIGO (advanced)", "高级LIGO"),
      ("unit", "LISA (ESA-NASA)", "LISA(欧空局-NASA)"),
      ("unit", "Einstein Telescope", "爱因斯坦望远镜"),
      ("unit", "NANOGrav (pulsar timing)", "NANOGrav脉冲星计时阵列"),
      ("person", "Kip Thorne", "基普·索恩"),
      ("person", "Rainer Weiss", "雷纳·韦斯")]),

    ("dark-sector-physics", "Dark Sector Physics", "future", "knowledge", "2050",
     ["quantum-mechanics", "relativity"],
     "Identification and theoretical understanding of dark matter (~27% of the universe) and dark energy (~68%). Direct detection at xenon time-projection experiments (XENONnT, LZ, DarkSide), axion searches (ADMX, MADMAX), CMB-S4, the Vera Rubin Observatory's LSST, and DESI/Euclid baryon-acoustic-oscillation measurements converge on candidate models — sterile neutrinos, axion fields, modified gravity, or quintessence — becoming testable. Either ΛCDM is robustly confirmed or replaced with a richer dark sector; either way, the largest open question in physics gets a definitive answer.",
     "暗物质与暗能量物理", "Dark matter",
     [("unit", "XENONnT detector", "XENONnT探测器"),
      ("wonder", "Vera C. Rubin Observatory", "薇拉·鲁宾天文台"),
      ("unit", "ADMX axion search", "ADMX轴子探测"),
      ("person", "Vera Rubin (astronomer)", "薇拉·鲁宾"),
      ("person", "Fritz Zwicky", "弗里茨·兹威基"),
      ("work", "ΛCDM concordance cosmology", "ΛCDM协调宇宙学")]),

    ("quantum-gravity", "Quantum Gravity", "future", "knowledge", "2055",
     ["quantum-mechanics", "relativity", "quantum-computing"],
     "Unification of quantum mechanics and general relativity into a single consistent framework — the holy grail of fundamental physics since the 1930s. Candidate theories include string theory and its M-theory unification, loop quantum gravity, causal dynamical triangulations, and asymptotic safety. The AdS/CFT correspondence (Maldacena 1997) and the black-hole information paradox provide indirect anchors; future tabletop experiments with levitated nanoparticles or precision atomic clocks may bridge the experimental gap. A successful theory would resolve singularities, explain the early universe, and reshape physics as profoundly as relativity did a century ago.",
     "量子引力", "Quantum gravity",
     [("work", "String theory", "弦理论"),
      ("work", "Loop quantum gravity", "圈量子引力"),
      ("person", "Edward Witten", "爱德华·威滕"),
      ("person", "Roger Penrose", "罗杰·彭罗斯"),
      ("person", "Carlo Rovelli", "卡洛·罗韦利"),
      ("work", "AdS/CFT correspondence", "反德西特/共形场论对偶"),
      ("person", "Juan Maldacena", "胡安·马尔达塞纳")]),

    ("p-vs-np-resolved", "P versus NP Resolved", "future", "knowledge", "2060",
     ["quantum-computing", "agi", "formal-mathematics"],
     "Definitive resolution of whether P = NP — whether problems whose solutions can be verified quickly can also be solved quickly. Posed by Stephen Cook (1971) and recognized as the deepest open problem in computer science, the question is one of the seven Clay Millennium Problems. P = NP would render most modern cryptography breakable and most optimization tractable; P ≠ NP would set hard limits on what algorithmic intelligence can achieve. AI-driven proof search, quantum-computational results, and machine-verified mathematics may finally settle the question by mid-century.",
     "P/NP问题解决", "P versus NP problem",
     [("person", "Stephen Cook", "斯蒂芬·库克"),
      ("person", "Leonid Levin", "列昂尼德·列文"),
      ("work", "Cook–Levin theorem", "库克-列文定理"),
      ("org", "Clay Mathematics Institute", "克莱数学研究所"),
      ("work", "Millennium Prize Problems", "千禧年大奖难题")]),
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
    blocks = ["\n  // ─── Future Age (physics & math) ───"]
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
    insertion = "\n  // ─── Future Age (physics & math) ───\n"
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
    insertion = "\n  // ─── Future Age (physics & math) ───\n"
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
