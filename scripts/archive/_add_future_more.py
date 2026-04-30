#!/usr/bin/env python3
"""Add 13 more Future Age techs spanning 2035-2100 across energy, transport,
medicine, computing, governance, and far-future categories."""

import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

TECHS = [
    ("hyperloop", "Hyperloop", "future", "transport", "2035",
     ["electric-motor", "advanced-chip-manufacturing", "machine-tool"],
     "Vacuum-tube transport with magnetically levitated capsules, theoretically reaching 1000+ km/h with low energy use. Elon Musk's 2013 white paper popularized the concept; Virgin Hyperloop ran a passenger test in 2020 before pivoting away. SpaceX's Boring Company, HyperloopTT, and Chinese state programs continue research; Saudi Arabia and India have proposed mainline routes. Engineering and economic challenges — vacuum maintenance, station throughput, capital cost vs. high-speed rail — remain unresolved, but the concept defines the maglev frontier.",
     "超回路列车", "Hyperloop",
     [("work", "Hyperloop white paper (Musk 2013)", "超回路列车白皮书"),
      ("org", "Virgin Hyperloop", "维珍超回路"),
      ("org", "HyperloopTT", "HyperloopTT"),
      ("org", "Boring Company", "Boring公司")]),

    ("neuromorphic-chip", "Neuromorphic Chip", "future", "tools", "2035",
     ["advanced-chip-manufacturing", "neuroscience"],
     "Computer chips with brain-inspired architecture — spiking neurons, in-memory compute, event-driven asynchronous operation — radically more energy-efficient for pattern recognition and adaptive control. Intel Loihi 2 (2021), IBM TrueNorth (2014), the Manchester SpiNNaker board, and BrainChip Akida are leading platforms. Useful where conventional GPUs are wasteful: edge AI, robotics, sensory processing, brain-computer interfaces. Likely complements rather than replaces conventional silicon for the foreseeable future.",
     "神经形态芯片", "Neuromorphic engineering",
     [("unit", "Intel Loihi 2", "英特尔Loihi 2"),
      ("unit", "IBM TrueNorth", "IBM TrueNorth"),
      ("unit", "SpiNNaker (Manchester)", "SpiNNaker(曼彻斯特)"),
      ("person", "Carver Mead", "卡弗·米德"),
      ("org", "BrainChip", "BrainChip公司")]),

    ("lab-grown-organs", "Lab-Grown Organs", "future", "medicine", "2040",
     ["tissue-engineering", "gene-therapy", "3d-printing"],
     "Whole transplant organs grown from a patient's own cells on biocompatible scaffolds, eliminating donor shortages and immune rejection. Anthony Atala's lab grew functional bladders for clinical patients (2006); recent work has produced miniature kidneys, livers, hearts, and lungs as organoids. 3D-bioprinting whole-organ structures with vascularization remains the gating step; United Therapeutics and BioLife Solutions target full clinical organs by 2040. Would end transplant waiting lists and chronic dialysis.",
     "实验室培育器官", "Organ engineering",
     [("person", "Anthony Atala", "安东尼·阿塔拉"),
      ("unit", "Lab-grown bladder (2006)", "实验室培育膀胱"),
      ("org", "United Therapeutics", "United Therapeutics"),
      ("unit", "Organoid", "类器官")]),

    ("sentientism", "Sentientism", "future", "social", "2040",
     ["longtermism", "evolution-darwin"],
     "Ethical framework extending moral consideration to all sentient beings — non-human animals and potentially digital minds — based on capacity for subjective experience rather than species membership. Peter Singer's Animal Liberation (1975) is the foundational text; Donald Watson, Sue Donaldson, Will Kymlicka, and Jeff Sebo extended it to political theory. The framework reshapes debates around factory farming, lab animal use, AI moral status, and far-future digital sentience. Effective animal advocacy organizations operate on these ethics.",
     "感知主义", "Sentientism",
     [("person", "Peter Singer", "彼得·辛格"),
      ("work", "Animal Liberation (1975)", "《动物解放》"),
      ("person", "Jeff Sebo", "杰夫·塞博"),
      ("person", "Donald Watson", "唐纳德·沃森"),
      ("org", "Open Philanthropy (animal welfare)", "Open Philanthropy(动物福利)")]),

    ("dna-data-storage", "DNA Data Storage", "future", "tools", "2045",
     ["synthetic-biology", "gene-sequencing"],
     "Encoding digital information in synthetic DNA strands, achieving theoretical density of ~1 exabyte per cubic millimeter with millennial archival stability. Microsoft Research demonstrated 200 MB storage and retrieval in DNA (2019); Catalog Technologies and Twist Bioscience are commercializing the approach. Reading and writing speeds remain slow and per-bit costs high (~$1000/MB), making DNA storage suitable for cold archival rather than active use. As silicon storage costs plateau and data volumes grow, DNA may become the only viable option for centuries-scale archives.",
     "DNA数据存储", "DNA digital data storage",
     [("org", "Microsoft Research", "微软研究院"),
      ("org", "Catalog Technologies", "Catalog Technologies"),
      ("org", "Twist Bioscience", "Twist Bioscience"),
      ("person", "George Church", "乔治·丘奇")]),

    ("cancer-cure", "Cancer Cure", "future", "medicine", "2045",
     ["crispr", "mrna-vaccine", "deep-learning"],
     "General cancer therapy using personalized mRNA vaccines, CAR-T cell therapy, immune checkpoint inhibitors, and AI-designed targeted molecules to clear tumors with minimal toxicity. Moderna's personalized cancer vaccines (Phase III in melanoma, 2024), Kymriah CAR-T (2017), and Keytruda checkpoint inhibitor (2014) are the building blocks. AlphaFold-class protein structure prediction enables rational drug design at scale. Most cancer types remain only partially treatable today, but the trajectory points to most cancers becoming chronic-but-manageable diseases by mid-century.",
     "癌症治愈", "Cancer immunotherapy",
     [("unit", "CAR-T cell therapy", "CAR-T细胞疗法"),
      ("unit", "Keytruda (pembrolizumab)", "Keytruda(派姆单抗)"),
      ("unit", "Personalized mRNA cancer vaccine", "个性化mRNA癌症疫苗"),
      ("person", "James Allison", "詹姆斯·艾利森")]),

    ("ai-judge", "Algorithmic Justice", "future", "economy", "2045",
     ["ai-governance", "large-language-model"],
     "AI systems making judicial decisions — bail recommendations, small-claims rulings, contract dispute resolution, parole reviews — initially as tools for human judges, eventually as autonomous decision-makers. Estonia's pilot 'AI judge' for €7000 contract disputes was floated in 2019; COMPAS recidivism scoring is used in U.S. criminal sentencing. The bias and transparency questions are profound — algorithmic justice from biased data reproduces injustice — and most legal scholars argue for AI as decision support rather than decision maker for the foreseeable future.",
     "算法司法", "Algorithmic radicalization",
     [("unit", "COMPAS recidivism algorithm", "COMPAS再犯预测算法"),
      ("unit", "Estonia AI judge (pilot)", "爱沙尼亚AI法官(试点)"),
      ("work", "Weapons of Math Destruction", "《数学杀伤性武器》"),
      ("person", "Cathy O'Neil", "凯西·奥尼尔")]),

    ("space-based-solar", "Space-Based Solar Power", "future", "energy", "2050",
     ["solar-photovoltaic", "reusable-rocket"],
     "Orbital arrays of photovoltaics or mirrors collecting solar energy in space and beaming it to Earth as microwaves or laser. The constant insolation (no clouds, no night) gives ~7-8x ground-based solar productivity. Caltech's Space Solar Power Project demonstrated wireless power transfer from orbit (2023); ESA's SOLARIS, China's planned 2028 demonstrator, and U.S. Air Force Research Laboratory programs target commercial systems. Launch costs (now collapsing under SpaceX) and microwave receiver siting are the gating constraints.",
     "空间太阳能发电", "Space-based solar power",
     [("org", "Caltech Space Solar Power Project", "加州理工太空太阳能项目"),
      ("work", "SOLARIS (ESA)", "SOLARIS(欧空局)"),
      ("person", "Peter Glaser (concept, 1968)", "彼得·格拉泽"),
      ("unit", "Microwave power transmission", "微波输电")]),

    ("photonic-computing", "Photonic Computing", "future", "tools", "2050",
     ["advanced-chip-manufacturing", "fiber-optic"],
     "Computers using photons instead of electrons for matrix multiplication, exploiting wavelength-division multiplexing and zero crosstalk. Lightmatter, Lightelligence, Optalysys, and PsiQuantum are commercializing photonic accelerators for AI inference, where photonics excels at parallel linear algebra. Nonlinear operations remain a challenge. Photonic chips may displace GPUs for specific AI workloads in the 2030s, with hybrid electronic-photonic architectures likely dominant rather than pure-photonic.",
     "光子计算", "Photonic computing",
     [("org", "Lightmatter", "Lightmatter"),
      ("org", "Lightelligence", "Lightelligence"),
      ("unit", "Photonic tensor core", "光子张量核"),
      ("org", "PsiQuantum", "PsiQuantum")]),

    ("metamaterials", "Metamaterials", "future", "tools", "2055",
     ["nanotechnology", "room-temp-superconductor"],
     "Engineered composite structures with sub-wavelength features producing optical, acoustic, or electromagnetic properties not found in nature — negative refractive index, perfect lensing, electromagnetic cloaking. John Pendry, David Smith, and Richard Shelby demonstrated the first negative-index materials (2000-2006). Applications include cloaking devices (Duke University demonstration), super-resolution imaging, antenna miniaturization, and structural acoustic absorbers. Industrial use is growing in 5G antennas, automotive radar, and lightweight composites.",
     "超材料", "Metamaterial",
     [("person", "John Pendry", "约翰·彭德里"),
      ("person", "David Smith", "大卫·史密斯"),
      ("unit", "Cloaking device", "隐身斗篷"),
      ("unit", "Negative refractive index lens", "负折射率透镜")]),

    ("programmable-matter", "Programmable Matter", "future", "tools", "2065",
     ["nanotechnology", "robotics"],
     "Material whose physical structure can be reprogrammed under software control — shape, color, conductivity, even function. Carnegie Mellon's claytronics project, MIT's M-Blocks (2019), and various magnetic-particle systems demonstrate millimeter-scale prototypes. Long-term: a brick that becomes a chair, then a table, then a hammer; or a robot reshaping itself for different tasks. Applications would span construction, manufacturing, surgery, and exploration. Self-organizing nano-modules remain the gating capability.",
     "可编程物质", "Programmable matter",
     [("work", "Claytronics (CMU)", "Claytronics项目(CMU)"),
      ("unit", "M-Blocks (MIT)", "M-Blocks机器人模块"),
      ("person", "Seth Goldstein", "塞斯·戈德斯坦"),
      ("person", "Daniela Rus", "丹妮拉·罗斯")]),

    ("interstellar-probe", "Interstellar Probe", "future", "transport", "2080",
     ["fusion-rocket", "agi"],
     "Robotic spacecraft sent on multi-decade voyages to nearby stars (Alpha Centauri, Barnard's Star, TRAPPIST-1) to image exoplanets and search for biosignatures. Breakthrough Starshot (announced 2016) targets a gram-scale solar-sail probe accelerated to 0.2c by ground-based laser arrays — Alpha Centauri in 20 years, signal back in another 4. Project Daedalus (1970s) and Project Longshot (1988) studied larger fusion-driven probes. Communication bandwidth from light-years away and 50-year operating reliability are the engineering walls.",
     "星际探测器", "Interstellar probe",
     [("unit", "Breakthrough Starshot", "突破摄星计划"),
      ("person", "Yuri Milner", "尤里·米尔纳"),
      ("person", "Stephen Hawking", "史蒂芬·霍金"),
      ("unit", "Project Daedalus (1970s)", "代达罗斯计划"),
      ("wonder", "Proxima Centauri b", "比邻星b")]),

    ("terraforming-mars", "Terraforming Mars", "future", "shelter", "2100",
     ["mars-colony", "fusion-power", "asteroid-mining"],
     "Engineered transformation of Mars's atmosphere, surface, and biosphere to support unassisted human life — releasing CO₂ from polar ice and regolith for greenhouse warming, generating an artificial magnetosphere, and seeding genetically engineered photosynthetic organisms. Carl Sagan first quantified the project (1971); recent analyses (Jakosky and Edwards, 2018) suggest insufficient CO₂ remains on Mars for full terraforming. Partial terraforming or paraterraforming (large enclosed habitats) may be more realistic. Even partial success would take centuries.",
     "火星地球化", "Terraforming of Mars",
     [("person", "Carl Sagan", "卡尔·萨根"),
      ("person", "Robert Zubrin", "罗伯特·祖布林"),
      ("work", "The Case for Mars", "《赶往火星》"),
      ("unit", "Paraterraforming (worldhouse)", "局部地球化(世界穹顶)")]),
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
    blocks = ["\n  // ─── Future Age (additional 2035-2100) ───"]
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
    insertion = "\n  // ─── Future Age (additional) ───\n"
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
            print(f"  + {tid:30} {j.get('title')} → {out.name}")
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
    insertion = "\n  // ─── Future Age (additional) ───\n"
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
