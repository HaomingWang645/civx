#!/usr/bin/env python3
"""Add 12 late-Future-Age techs (2065-2095) — medicine, governance, space."""

import json, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

TECHS = [
    ("artificial-womb", "Artificial Womb", "future", "medicine", "2065",
     ["tissue-engineering", "gene-therapy", "ivf"],
     "Ectogenesis — fetal development entirely outside the human body in engineered artificial uteri. Children's Hospital of Philadelphia's biobag for premature lambs (2017) and the EctoLife concept (2022) demonstrate proof of concept; full-term human ectogenesis becomes clinically routine by ~2065. The technology decouples reproduction from biological pregnancy with profound social implications: women's careers, gestational health risks, surrogacy economies, and the legal definition of personhood all shift. Ethical debates over commodification and access intensify alongside adoption.",
     "人工子宫", "Artificial uterus",
     [("unit", "Biobag (CHOP, 2017)", "Biobag生物袋"),
      ("work", "EctoLife (concept)", "EctoLife概念"),
      ("work", "Brave New World (Huxley)", "《美丽新世界》(赫胥黎)"),
      ("person", "Aldous Huxley (literary precursor)", "奥尔德斯·赫胥黎")]),

    ("closed-cycle-cities", "Closed-Cycle Cities", "future", "shelter", "2070",
     ["closed-loop-life-support", "renewable-grid", "robotics"],
     "Megacities operating as fully closed-loop systems — water, nutrients, energy, and materials all cycled internally with zero net waste output. Biosphere 2 (1991) and ISS ECLSS are the small-scale ancestors; Saudi NEOM, Singapore's Eco-Smart City, Songdo (Korea), and Masdar (UAE) attempt partial implementations. By 2070, advanced membranes, AI logistics, robotic recycling, and renewable energy enable closed-cycle cities of millions. The urban form decouples from regional ecological footprint, reversing centuries of city-as-resource-sink dynamics.",
     "闭环循环城市", "Sustainable city",
     [("wonder", "NEOM (Saudi Arabia)", "NEOM新城"),
      ("wonder", "Songdo IBD (Korea)", "松岛国际商务区"),
      ("wonder", "Masdar City (UAE)", "马斯达尔城"),
      ("wonder", "Biosphere 2", "生物圈二号"),
      ("person", "Vincent Callebaut", "文森特·卡勒博")]),

    ("personalized-medicine", "Personalized Medicine", "future", "medicine", "2070",
     ["gene-sequencing", "deep-learning", "cancer-cure"],
     "Treatment plans fully tailored to a patient's genome, microbiome, transcriptome, proteome, and lifestyle history. Whole-genome sequencing at birth becomes routine; AI-driven drug-design platforms (Insilico Medicine, Recursion, Isomorphic Labs) generate patient-specific molecules in hours; pharmacogenomics eliminates trial-and-error prescribing. Drug development shifts from blockbuster small-molecule trials to per-patient biologics manufactured on-demand. The economic model upends the pharmaceutical industry: from mass-market drugs to individualized therapies. Equity and cost remain central concerns.",
     "个性化医疗", "Personalized medicine",
     [("work", "Whole-genome sequencing at birth", "新生儿全基因组测序"),
      ("work", "Pharmacogenomics", "药物基因组学"),
      ("org", "Isomorphic Labs", "Isomorphic Labs"),
      ("org", "Insilico Medicine", "Insilico Medicine"),
      ("unit", "AlphaFold-derived drug design", "AlphaFold药物设计")]),

    ("printable-organs-on-demand", "Printable Organs on Demand", "future", "medicine", "2075",
     ["lab-grown-organs", "3d-printing", "tissue-engineering"],
     "3D-printable organs available within hours from a patient's own cells. United Therapeutics' organ-printing initiative, Prellis Biologics' high-resolution bioprinting, and organoid bioreactors converge into mature clinical capacity. Heart, kidney, liver, pancreas, lung, and even segments of bone and skin become routine prints; brain remains unprintable. Organ scarcity ends; transplant waiting lists become historical artifacts. The economic structure of organ donation, dialysis, and chronic disease management transforms entirely within a generation of wider deployment.",
     "按需打印器官", "3D bioprinting",
     [("org", "Prellis Biologics", "Prellis Biologics"),
      ("org", "United Therapeutics", "United Therapeutics"),
      ("org", "Organovo", "Organovo"),
      ("resource", "Bioink", "生物墨水"),
      ("person", "Anthony Atala (continuation)", "安东尼·阿塔拉")]),

    ("ai-coordination-treaty", "AI Coordination Treaty", "future", "economy", "2075",
     ["agi", "ai-governance", "large-language-model"],
     "Multilateral framework limiting AI capability development and deployment, modeled on nuclear non-proliferation. The 2023 Bletchley Declaration on AI Safety was the first international AI summit; the EU AI Act, U.S. Executive Order on AI, and Chinese AI regulations established competing models. By the 2070s, a binding treaty regulates frontier AI training runs above some compute threshold, mandates safety auditing, and establishes shared compute monitoring — analogous to IAEA inspections. Compliance verification through technical means (capability evaluations, mechanistic interpretability) is the gating challenge.",
     "人工智能协调条约", "Bletchley Declaration",
     [("work", "Bletchley Declaration (2023)", "布莱切利宣言"),
      ("work", "EU AI Act", "欧盟人工智能法案"),
      ("org", "International Atomic Energy Agency (model)", "国际原子能机构(模板)"),
      ("person", "Stuart Russell", "斯图尔特·罗素"),
      ("person", "Yoshua Bengio", "约书亚·本吉奥")]),

    ("direct-ai-democracy", "Direct AI-Mediated Democracy", "future", "economy", "2075",
     ["liquid-democracy", "agi", "large-language-model"],
     "Continuous citizen participation in policy decisions, mediated by AI assistants that translate technical questions into terms each citizen can engage with. Audrey Tang's vTaiwan and Colin Megill's Pol.is platform (2014–) demonstrate small-scale forerunners; by the 2070s, AI-mediated direct democracy operates at national scale. AI maintains discourse quality (filters bots, summarizes positions, identifies common ground) without replacing human judgment. Critics worry about AI-shaped opinion formation and capture; advocates argue it solves classic representative-democracy failures around scale and complexity.",
     "AI辅助直接民主", "Pol.is",
     [("unit", "vTaiwan platform", "vTaiwan平台"),
      ("unit", "Pol.is", "Pol.is"),
      ("person", "Audrey Tang", "唐凤"),
      ("person", "Colin Megill (Pol.is)", "科林·梅吉尔"),
      ("work", "Deliberative democracy", "审议民主")]),

    ("lunar-industrial-base", "Lunar Industrial Base", "future", "shelter", "2075",
     ["moon-base", "asteroid-mining", "advanced-chip-manufacturing"],
     "The Moon transitions from science outpost to primary heavy-industry origin — vacuum-friendly chip fabrication, low-gravity launch, in-situ regolith refining for solar-panel silicon and structural materials. Helium-3 mining for fusion fuel becomes economic if D-He³ reactors mature. Lunar-built spacecraft launch from a 1/6 g gravity well, reaching Mars or the asteroid belt without Earth's escape-velocity penalty. Population grows from hundreds to tens of thousands by mid-century; ISRU (in-situ resource utilization) becomes mature engineering rather than research.",
     "月球工业基地", "Colonization of the Moon",
     [("resource", "Helium-3 (lunar)", "氦-3(月球)"),
      ("unit", "Mass driver (electromagnetic launch)", "电磁质量驱动器"),
      ("resource", "Lunar regolith", "月壤"),
      ("org", "Moon Village (ESA)", "月球村(欧空局)"),
      ("work", "ISRU (in-situ resource utilization)", "原位资源利用")]),

    ("asteroid-belt-settlement", "Asteroid Belt Settlement", "future", "shelter", "2080",
     ["asteroid-mining", "mars-colony", "fusion-rocket", "closed-loop-life-support"],
     "Permanent human settlements on Ceres, Vesta, and major asteroid belt bodies. Ceres (largest belt body, dwarf planet) offers water ice, modest gravity, and a stable orbit; Vesta provides rare-earth-rich differentiated mantle material. Population in the tens of thousands by century-end, primarily mining and refining for trans-system trade. The Belt develops a culturally distinct identity — long communication delays from Earth, low gravity, dependence on mutual support — generating Earth/Mars/Belt identity politics that James S.A. Corey's The Expanse pre-figured.",
     "小行星带定居", "Colonization of the asteroids",
     [("wonder", "Ceres (dwarf planet)", "谷神星"),
      ("wonder", "4 Vesta", "灶神星"),
      ("work", "The Expanse (Corey, novels)", "《苍穹浩瀚》"),
      ("unit", "Belters (cultural identity)", "带客(文化身份)")]),

    ("memory-editing", "Memory Editing", "future", "medicine", "2085",
     ["brain-computer-interface", "neuroscience", "deep-learning"],
     "Selective insertion, deletion, or modification of human memories using targeted neural stimulation, optogenetic-class precision, and AI-mapped engrams. Karim Nader's reconsolidation work (2000) and Susumu Tonegawa's optogenetic memory engineering in mice (2014) are precursors; clinical use begins for PTSD, severe phobias, and addiction. Recreational memory editing — implanting experiences not lived, deleting unwanted memories — drives ethics debates rivaling early genetic engineering. Total Recall and Eternal Sunshine become operational concerns rather than thought experiments.",
     "记忆编辑", "Optogenetics",
     [("person", "Karim Nader", "卡里姆·纳德"),
      ("person", "Susumu Tonegawa", "利根川进"),
      ("work", "Optogenetics", "光遗传学"),
      ("work", "Eternal Sunshine of the Spotless Mind", "《暖暖内含光》"),
      ("work", "Total Recall (Dick / Verhoeven)", "《全面回忆》(迪克 / 范霍文)")]),

    ("cybernetic-enhancement", "Cybernetic Enhancement", "future", "medicine", "2090",
     ["brain-computer-interface", "lab-grown-organs", "robotics"],
     "Body augmentation via integrated mechanical, electronic, and biological components — replacement limbs stronger and more dexterous than biological originals, sensory enhancements (infrared vision, ultrasound hearing), implanted compute. Hugh Herr's MIT prosthetics, DARPA's HAPTIX program, and Neuralink-class BCIs converge into a mass-market enhancement industry. The cultural shift from medical-rehabilitation prosthetics to elective enhancement raises questions about athletic competition (Paralympics-vs-Olympics), military service, and the meaning of 'human' physical capability.",
     "赛博格增强", "Cyborg",
     [("person", "Hugh Herr", "休·赫尔"),
      ("person", "Neil Harbisson (cyborg artist)", "尼尔·哈比森"),
      ("work", "DARPA HAPTIX program", "DARPA HAPTIX项目"),
      ("unit", "Powered exoskeleton", "动力外骨骼"),
      ("unit", "Bionic limb", "仿生肢体")]),

    ("orbital-ring", "Orbital Ring", "future", "transport", "2090",
     ["room-temp-superconductor", "advanced-chip-manufacturing", "fusion-power"],
     "A continuous ring structure in low Earth orbit, supported by electromagnetic levitation against the rotating mass below it, providing tethered space access at near-zero marginal cost. Paul Birch (1982) proposed the design; Isaac Arthur and modern engineers refined the details. An orbital ring effectively eliminates the rocket equation — payloads ride elevators up the supports, then accelerate along the ring to orbital velocity. Construction takes decades and astronomical capital, but operating costs are then near zero, making cislunar industry economically transformative.",
     "轨道环", "Orbital ring",
     [("person", "Paul Birch", "保罗·伯奇"),
      ("person", "Isaac Arthur (futurist)", "艾萨克·亚瑟"),
      ("unit", "Skyhook (megastructure)", "天钩"),
      ("unit", "Lofstrom loop", "洛夫斯特罗姆环")]),

    ("universal-disease-eradication", "Universal Disease Eradication", "future", "medicine", "2095",
     ["vaccines-modern", "antibiotics", "mrna-vaccine", "crispr"],
     "Elimination of all major endemic infectious diseases — malaria, HIV, tuberculosis, schistosomiasis, dengue, hepatitis, neglected tropical diseases. Mass administration of broad-spectrum mRNA vaccines, gene-drive mosquito eradication (Anopheles gambiae), and AI-coordinated public-health surveillance close the gaps that smallpox eradication (1980) only began. Infectious disease shifts from leading global mortality cause to historical curiosity; the burden of disease moves to chronic and aging-related conditions. Engineered bioweapon reemergence remains the residual existential risk.",
     "普遍疾病根除", "Eradication of infectious diseases",
     [("wonder", "Smallpox eradication (1980)", "天花根除"),
      ("wonder", "Polio eradication (in progress)", "脊髓灰质炎根除"),
      ("work", "Gene drive (Anopheles)", "基因驱动(按蚊)"),
      ("org", "Bill & Melinda Gates Foundation", "比尔及梅琳达·盖茨基金会"),
      ("org", "World Health Organization (WHO)", "世界卫生组织")]),
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
    blocks = ["\n  // ─── Future Age (late, 2065-2095) ───"]
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
    insertion = "\n  // ─── Future Age (late) ───\n"
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
    insertion = "\n  // ─── Future Age (late) ───\n"
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
