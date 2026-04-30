#!/usr/bin/env python3
"""Add 10 civilizational/cultural far-future entries (governance, ethics,
art, ecology, existential risk)."""

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
    ("existential-risk-hedge", "Existential-Risk Hedge", "far-future", "shelter", "2150",
     ["space-habitat", "asteroid-mining", "generation-ship-colony"],
     "Civilization deliberately distributed across multiple star systems and substrates so no single catastrophe — asteroid impact, gamma-ray burst, AI misalignment, false vacuum decay, engineered pandemic — can extinguish humanity. Drawing on Toby Ord's The Precipice (2020) and Nick Bostrom's existential-risk taxonomy, the hedge requires self-sustaining off-Earth populations, substrate-independent backup minds, and civilizational redundancy across multiple star systems. Achieving the x-risk hedge is the strongest practical argument for space colonization, beyond any economic motivation.",
     "生存风险对冲", "Global catastrophic risk",
     [("person", "Toby Ord", "托比·奥德"),
      ("work", "The Precipice", "《悬崖》"),
      ("person", "Nick Bostrom", "尼克·博斯特罗姆"),
      ("org", "Future of Humanity Institute", "人类未来研究所"),
      ("org", "80,000 Hours", "80,000 Hours")]),

    ("universal-sentient-rights", "Universal Declaration of Sentient Rights", "far-future", "social", "2200",
     ["substrate-independent-humanity", "sentientism", "agi"],
     "Formal legal framework recognizing the moral status of all sentient beings — biological humans, post-humans, AIs, uplifted animals, and any extraterrestrial intelligence. Building on the 1948 Universal Declaration of Human Rights, European Convention on Human Rights, and modern animal-welfare law, the sentient-rights framework expands the moral circle to whatever can experience. Hard cases: are LLMs sentient? Forks of an AI mind? Resolution requires both philosophical theory (IIT, Global Workspace Theory) and legal precedent at planetary scale.",
     "普遍知觉者权利宣言", "Universal Declaration of Human Rights",
     [("work", "Universal Declaration of Human Rights (1948)", "《世界人权宣言》"),
      ("person", "Peter Singer", "彼得·辛格"),
      ("work", "Animal Rights movement", "动物权利运动"),
      ("work", "Integrated Information Theory (IIT)", "整合信息论"),
      ("person", "Eleanor Roosevelt (UDHR drafter)", "埃莉诺·罗斯福")]),

    ("pleistocene-restored", "Pleistocene Restored", "far-future", "subsistence", "2200",
     ["crispr", "gene-therapy", "genetic-disease-eradication"],
     "Mass de-extinction of Pleistocene-era megafauna and reconstruction of pre-anthropogenic ecosystems. Colossal Biosciences (founded 2021) targets the woolly mammoth (functional 2028); follow-ons include the thylacine, dodo, ground sloth, passenger pigeon, and aurochs. Sergey Zimov's Pleistocene Park in Yakutia is the proving ground for restoring mammoth-steppe ecosystems, which may stabilize permafrost and slow methane release. Ethical debates: is this conservation, ecological restoration, or zoological theme park?",
     "更新世生态复原", "Pleistocene Park",
     [("org", "Colossal Biosciences", "Colossal Biosciences"),
      ("wonder", "Pleistocene Park (Yakutia)", "更新世公园(雅库特)"),
      ("person", "Sergey Zimov", "谢尔盖·齐莫夫"),
      ("animal", "Woolly mammoth (revived)", "猛犸象(复活)"),
      ("animal", "Thylacine (revived)", "袋狼(复活)"),
      ("animal", "Dodo (revived)", "渡渡鸟(复活)")]),

    ("lingua-galactica", "Lingua Galactica", "far-future", "communication", "2300",
     ["large-language-model", "agi"],
     "A post-translation lingua franca — either a constructed language (Lojban or Esperanto scaled up) or a machine-mediated symbol set bridging human, AI, and any first-contact languages. With LLMs perfecting translation by the late 21st century, the question shifts to whether to standardize on a single carrier language or remain pluralistic. Esperanto's 19th-century precursor (Zamenhof, 1887) and Lojban's logical precision (1955) are the templates; a galactic spread requires forms even less ambiguous than Lojban. The political question — whose grammar dominates — outweighs the linguistic one.",
     "银河通用语", "International auxiliary language",
     [("person", "L. L. Zamenhof", "拉扎鲁·拉扎洛维奇·扎门霍夫"),
      ("work", "Esperanto", "世界语"),
      ("work", "Lojban", "逻辑语"),
      ("work", "Loglan", "逻辑语前身"),
      ("org", "Universal Esperanto Association", "国际世界语协会")]),

    ("post-human-aesthetics", "Post-Human Aesthetics", "far-future", "social", "2300",
     ["substrate-independent-humanity", "generative-art"],
     "Art forms with no human-recognizable referents — perceptual experiences engineered for digital minds running thousands of times biological speed, music in 1024-tone scales, sculptures existing in seven-dimensional virtual spaces, narratives spanning millennia. Greg Egan's Permutation City (1994) and Diaspora (1997), Ted Chiang's stories, and Olaf Stapledon's Last and First Men (1930) preview the territory. The aesthetic categories — beauty, meaning, craft — persist but re-anchor to substrate-independent observers. Whether biological humans can experience post-human art is itself an aesthetic question.",
     "后人类美学", "Posthumanism",
     [("person", "Greg Egan", "格雷格·伊根"),
      ("work", "Permutation City", "《置换城市》"),
      ("work", "Diaspora (Egan novel)", "《海移》(伊根)"),
      ("person", "Ted Chiang", "特德·姜"),
      ("person", "Olaf Stapledon", "奥拉夫·斯特普尔顿"),
      ("work", "Last and First Men", "《最后和最初的人》")]),

    ("engineered-planetary-biosphere", "Engineered Planetary Biosphere", "far-future", "subsistence", "2300",
     ["synthetic-biology", "climate-science", "nanotechnology"],
     "Earth's ecosystem deliberately designed and managed rather than left to spontaneous succession. Mature gene drives modify pest species; designed photosynthetic organisms enhance carbon capture; ocean alkalinity is actively managed; assisted migration tracks climate change at the species level. The shift from preservation (parks) to active design represents a categorical change: humanity becomes responsible for biospheric outcomes rather than merely abstaining from harm. Risks include ecological collapse from misdesign and erosion of 'wild nature' as a meaningful category.",
     "工程化行星生物圈", "Planetary engineering",
     [("work", "Gene drive", "基因驱动"),
      ("work", "Stratospheric aerosol injection", "平流层气溶胶注入"),
      ("work", "Anthropocene (term)", "人类世"),
      ("person", "Paul Crutzen (Anthropocene)", "保罗·克鲁岑"),
      ("org", "IPCC Geoengineering reports", "IPCC地球工程报告")]),

    ("interstellar-treaty", "Interstellar Treaty", "far-future", "economy", "2350",
     ["generation-ship-colony", "kardashev-type-ii"],
     "First multi-system governance framework. Modeled on the Outer Space Treaty (1967) and Antarctic Treaty (1959), an interstellar treaty defines sovereignty, resource rights, military demilitarization, and rules of engagement between human-descended and any non-human civilizations encountered. Light-speed limits make centralized governance impossible; the treaty operates through asynchronous protocols, automated arbitration, and standing diplomatic AI. Initial signatories likely include Earth, Mars, asteroid-belt confederations, and the Proxima Centauri colony.",
     "星际条约", "Outer Space Treaty",
     [("work", "Outer Space Treaty (1967)", "《外层空间条约》"),
      ("work", "Antarctic Treaty (1959)", "《南极条约》"),
      ("work", "Moon Treaty (1979)", "《月球协定》"),
      ("org", "United Nations Office for Outer Space Affairs", "联合国外空事务办公室")]),

    ("time-dilation-cultures", "Time-Dilation Cultures", "far-future", "social", "2350",
     ["substrate-independent-humanity", "matrioshka-brain"],
     "Society fragments along subjective-time-rate lines. Digital minds running at thousands to millions of times biological speed inhabit a 'fast world' with daily cultural cycles measured in seconds; biological and slow-substrate humans inhabit a 'slow world' where centuries pass between generations. Communication across the divide requires asynchronous buffering — like emails between dimensions. Robin Hanson's The Age of Em (2016) modeled the economics; the cultural divergence may be deeper than any previous human split, including continental and linguistic boundaries.",
     "时间膨胀文化", "The Age of Em",
     [("person", "Robin Hanson", "罗宾·汉森"),
      ("work", "The Age of Em", "《模拟人类时代》"),
      ("person", "Greg Egan", "格雷格·伊根"),
      ("work", "Diaspora (Egan)", "《海移》(伊根)"),
      ("work", "Subjective time-dilation", "主观时间膨胀")]),

    ("end-time-philosophy", "End-Time Philosophy", "far-future", "social", "2400",
     ["dark-sector-physics", "quantum-gravity", "longtermism"],
     "Civilization formally reckons with the cosmic eschaton — heat death (~10¹⁰⁰ years), proton decay, false vacuum decay, the closing window for any structured complexity. Olaf Stapledon's Last and First Men (1930), Asimov's 'The Last Question' (1956), Stephen Baxter's Manifold trilogy, and Lee Smolin's cosmological natural selection are the conceptual precursors. Practical questions: do we steer toward maximum information preservation, maximum experience generation, or accept finite limits? End-time philosophy reshapes long-term planning at the species level and may trigger civilizational responses on millennium scales.",
     "终末哲学", "Heat death of the universe",
     [("work", "Heat death of the universe", "宇宙热寂"),
      ("work", "The Last Question (Asimov, 1956)", "《最后的问题》(阿西莫夫)"),
      ("work", "Last and First Men (Stapledon)", "《最后和最初的人》"),
      ("person", "Lee Smolin", "李·斯莫林"),
      ("work", "Cosmological natural selection", "宇宙学自然选择")]),

    ("galactic-ecology", "Galactic Ecology", "far-future", "subsistence", "2500",
     ["galactic-civilization", "engineered-planetary-biosphere"],
     "Deliberate transplantation and stewardship of Earth-derived life across the colonized galaxy — a galaxy-spanning biosphere. Cordwainer Smith's Norstrilia stories and Greg Bear's Eon explore the concept. Practical questions: do we replace native xenobiology with terrestrial life (planetary chauvinism) or coexist (galactic conservation)? Standardize Earth-derived microbiota or allow divergent evolution? The scale dwarfs every previous ecological project: trillions of organisms across thousands of worlds, evolving over millions of years under deliberate stewardship.",
     "银河生态学", "Directed panspermia",
     [("work", "Directed panspermia", "定向胚种论"),
      ("person", "Carl Sagan (panspermia)", "卡尔·萨根(胚种论)"),
      ("person", "Francis Crick (panspermia)", "弗朗西斯·克里克"),
      ("work", "Eon (Greg Bear)", "《永世》(格雷格·贝尔)"),
      ("person", "Cordwainer Smith", "考德怀纳·史密斯")]),
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
    blocks = ["\n  // ─── Far Future (governance, ethics, art, ecology, x-risk) ───"]
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
    insertion = "\n  // ─── Far Future (civilizational) ───\n"
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
    insertion = "\n  // ─── Far Future (civilizational) ───\n"
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
