#!/usr/bin/env python3
"""Add a Future Age era + 18 speculative-future techs + 5 backfill prereqs.
Mutates data.js, translations.js, _image_manifest.json, images.js, unlocks.js."""

import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# (id, name, era, category, year, prereqs, desc, zh, wiki, unlocks)
# unlocks: list of (type, name_en, name_zh)

PREREQS = [
    ("plasma-physics", "Plasma Physics", "atomic", "knowledge", "1958",
     ["quantum-mechanics", "electromagnetism"],
     "The study of ionized gases — the fourth state of matter — formalized as a discipline by Hannes Alfvén, Lyman Spitzer, and Soviet researchers in the 1950s. Spitzer's stellarator (1951) and the Soviet tokamak (Tamm and Sakharov, 1958) established the two main magnetic-confinement geometries used to study fusion plasmas. Plasma physics also underlies astrophysics (stars, accretion disks), atmospheric reentry, semiconductor processing, and electric propulsion.",
     "等离子体物理学", "Plasma (physics)",
     [("person","Hannes Alfvén","汉尼斯·阿尔芬"),("person","Lyman Spitzer","莱曼·斯皮策"),("unit","Stellarator","仿星器"),("unit","Tokamak","托卡马克装置")]),

    ("neuroscience", "Neuroscience", "atomic", "knowledge", "1952",
     ["evolution-darwin", "electromagnetism"],
     "Systematic study of the nervous system at cellular, circuit, and behavioral levels. Hodgkin and Huxley's squid-axon model of action-potential propagation (1952) is the canonical foundational paper; Wilder Penfield's cortical mapping in conscious patients (1937 onward) defined functional brain regions; Eric Kandel won the 2000 Nobel for the molecular basis of memory in Aplysia. Neuroscience now spans from molecular biology to fMRI to computational models, and is the substrate for any future brain-computer or cognitive-enhancement technology.",
     "神经科学", "Neuroscience",
     [("person","Alan Hodgkin & Andrew Huxley","霍奇金与赫胥黎"),("person","Wilder Penfield","怀尔德·彭菲尔德"),("person","Eric Kandel","埃里克·坎德尔"),("work","Hodgkin–Huxley model","霍奇金-赫胥黎方程")]),

    ("gene-therapy", "Gene Therapy", "information", "medicine", "1990",
     ["genetic-engineering", "dna-structure"],
     "Therapeutic introduction or correction of genes inside patient cells, delivered by viral vectors or nanoparticles. Ashanti DeSilva's 1990 ADA-SCID treatment was the first FDA-approved trial. After early-2000s setbacks, modern AAV vectors enabled Luxturna (2017, hereditary blindness), Zolgensma (2019, spinal muscular atrophy), and Casgevy (2023, sickle-cell disease). Combined with CRISPR, gene therapy is moving from rare monogenic diseases toward broader applications including cancer immunotherapy.",
     "基因疗法", "Gene therapy",
     [("person","French Anderson","威廉·法兰奇·安德森"),("unit","Luxturna","Luxturna基因疗法"),("unit","Zolgensma","Zolgensma基因疗法"),("unit","Casgevy (CRISPR)","Casgevy(CRISPR疗法)")]),

    ("tissue-engineering", "Tissue Engineering", "information", "medicine", "1989",
     ["genetic-engineering", "dna-structure"],
     "Growing functional biological tissue on biocompatible scaffolds seeded with cells. The 'Vacanti mouse' (1989, ear-shaped cartilage on a polymer scaffold) made the field famous. Lab-grown skin (Apligraf 1998), bladders (Atala 2006), and trachea (Macchiarini 2008) entered clinical use. Modern organoids and 3D-bioprinted tissues are inching toward whole organs; meanwhile cultivated-meat companies use the same techniques to grow muscle for food.",
     "组织工程", "Tissue engineering",
     [("person","Robert Langer","罗伯特·兰格"),("person","Joseph Vacanti","约瑟夫·瓦坎蒂"),("unit","Vacanti mouse","瓦坎蒂老鼠"),("person","Anthony Atala","安东尼·阿塔拉")]),

    ("closed-loop-life-support", "Closed-Loop Life Support", "information", "shelter", "1991",
     ["public-sanitation", "synthetic-fertilizer"],
     "Self-sustaining systems that recycle air, water, and waste nutrients within a sealed habitat. Biosphere 2 (Arizona, 1991, $200M, 8 inhabitants for two years) was the most ambitious early attempt and revealed how hard the engineering is — atmospheric balance, microbial succession, food production all proved unstable. The ISS Environmental Control and Life Support System (operational since 2008) is the first proven closed-loop oxygen and water system in space, and the basis for future Moon and Mars habitats.",
     "闭环生命维持系统", "Bioregenerative life support system",
     [("wonder","Biosphere 2","生物圈二号"),("unit","ISS ECLSS","国际空间站环境控制系统"),("unit","BIOS-3 (Soviet)","BIOS-3(苏联生命维持系统)")]),
]

FUTURES = [
    ("fusion-power", "Fusion Power", "future", "energy", "2040",
     ["nuclear-power", "plasma-physics", "advanced-chip-manufacturing"],
     "Commercial electricity from controlled deuterium-tritium fusion at temperatures above 100 million °C. ITER (under construction, France) is targeting Q>10 first plasma in the 2030s; private firms — Commonwealth Fusion Systems, TAE, Helion, Tokamak Energy — are pursuing high-temperature-superconductor tokamaks and alternative concepts. The 2022 NIF inertial-confinement ignition (Q>1) was a milestone but remains far from grid-scale. Practical fusion would essentially solve climate-era energy supply, making electricity abundant and carbon-free.",
     "可控核聚变", "Fusion power",
     [("org","ITER","国际热核聚变实验堆"),("org","Commonwealth Fusion Systems","联邦聚变系统公司"),("unit","SPARC tokamak","SPARC托卡马克"),("unit","Joint European Torus (JET)","欧洲联合环面装置(JET)"),("wonder","National Ignition Facility","国家点火装置")]),

    ("humanoid-robot", "Humanoid Robot", "future", "tools", "2030",
     ["robotics", "deep-learning", "lithium-battery", "advanced-chip-manufacturing"],
     "General-purpose bipedal robots capable of working in human environments without retrofitting them. Boston Dynamics Atlas (electric version 2024), Tesla Optimus, Figure 02, Agility Robotics' Digit, and Chinese makers like Unitree H1 and Fourier GR-1 are entering pilot deployments in factories and warehouses. The combination of cheap actuators, vision-language-action models trained on internet data, and dramatically improved batteries has made physically embodied AI plausible in this decade rather than next century.",
     "人形机器人", "Humanoid robot",
     [("unit","Atlas (Boston Dynamics)","阿特拉斯机器人(波士顿动力)"),("unit","Tesla Optimus","特斯拉Optimus"),("unit","Figure 02","Figure 02机器人"),("unit","Unitree H1","宇树H1机器人"),("org","Boston Dynamics","波士顿动力")]),

    ("agi", "Artificial General Intelligence", "future", "knowledge", "2035",
     ["large-language-model", "deep-learning", "advanced-chip-manufacturing"],
     "AI systems that match or exceed humans across the full breadth of cognitive tasks rather than excelling at narrow domains. Whether large language models scale into AGI, whether multimodal embodied training is required, and how alignment scales remain open. The leading labs — OpenAI, Anthropic, Google DeepMind, Meta AI, xAI — explicitly target AGI; safety research from Bostrom, Russell, Christiano, and Hendrycks frames the alignment problem. The economic and existential implications are unique in the technology tree.",
     "通用人工智能", "Artificial general intelligence",
     [("org","OpenAI","OpenAI"),("org","Anthropic","Anthropic"),("org","Google DeepMind","谷歌DeepMind"),("person","Demis Hassabis","戴密斯·哈萨比斯"),("person","Stuart Russell","斯图尔特·罗素"),("person","Nick Bostrom","尼克·博斯特罗姆")]),

    ("brain-computer-interface", "Brain-Computer Interface", "future", "medicine", "2030",
     ["neuroscience", "advanced-chip-manufacturing", "deep-learning"],
     "Direct neural electrode arrays reading from and writing to the human brain. Utah arrays have been used in research since the 1990s; Neuralink's N1 implant (first human in 2024) and Synchron's stentrode (2022) are bringing high-channel-count implants toward clinical use. BlackRock Neurotech, Paradromics, and Onward (spinal cord) target paralysis, blindness, and depression. Long-term: lossless input/output to the cortex, enabling cognitive augmentation and shared experience.",
     "脑机接口", "Brain–computer interface",
     [("org","Neuralink","Neuralink"),("org","Synchron","Synchron"),("unit","Utah array","犹他电极阵列"),("unit","N1 Implant (Neuralink)","N1脑机接口(Neuralink)"),("person","Miguel Nicolelis","米格尔·尼科莱利斯")]),

    ("moon-base", "Permanent Moon Base", "future", "shelter", "2035",
     ["reusable-rocket", "nuclear-power", "3d-printing", "closed-loop-life-support"],
     "Continuously inhabited human outposts on the lunar surface, leveraging in-situ resource utilization (water ice in shadowed polar craters, regolith for radiation shielding) to reduce dependence on Earth supply. NASA's Artemis program targets the Lunar Gateway and a south-polar surface base by the 2030s; China and Russia are jointly pursuing the International Lunar Research Station; SpaceX's Starship is the heavy lifter that makes the architecture economic. The Moon becomes both science platform and proving ground for Mars.",
     "月球永久基地", "Lunar outpost",
     [("org","NASA Artemis program","NASA阿耳忒弥斯计划"),("unit","Lunar Gateway","月球门户空间站"),("unit","Artemis Base Camp","阿耳忒弥斯基地"),("org","International Lunar Research Station","国际月球科研站")]),

    ("mars-colony", "Mars Colonization", "future", "shelter", "2050",
     ["moon-base", "fusion-power", "closed-loop-life-support"],
     "Self-sustaining human settlements on Mars, capable of growing without continuous resupply from Earth. SpaceX's stated goal is a million people on Mars by ~2070, beginning with cargo Starship landings in the late 2020s; Mars's 24h-37min day and 38% gravity are favorable, while its thin CO₂ atmosphere, 2400 ppm CO₂ in soil, and lack of magnetic field create radiation, dust, and life-support challenges. Mars colonization is the canonical case for humanity becoming a multi-planet species.",
     "火星殖民", "Colonization of Mars",
     [("org","SpaceX","SpaceX"),("unit","Starship","星舰"),("person","Elon Musk","埃隆·马斯克"),("wonder","Olympus Mons","奥林帕斯山"),("plant","Mars potato (The Martian)","火星马铃薯")]),

    ("asteroid-mining", "Asteroid Mining", "future", "subsistence", "2040",
     ["reusable-rocket", "robotics", "autonomous-vehicle"],
     "Robotic extraction of platinum-group metals, water, and rare earths from near-Earth asteroids. NASA's OSIRIS-REx returned 250g from Bennu (2023); Japan's Hayabusa2 from Ryugu (2020). Commercial firms (Planetary Resources, Deep Space Industries) struggled with capital but the architecture remains plausible: water from carbonaceous asteroids becomes orbital propellant, freeing deep-space exploration from Earth's gravity well. Long-term, a single 200m metallic asteroid contains more platinum than has ever been mined on Earth.",
     "小行星采矿", "Asteroid mining",
     [("unit","OSIRIS-REx mission","OSIRIS-REx任务"),("unit","Hayabusa2 mission","隼鸟2号任务"),("wonder","Asteroid 16 Psyche","16灵神星"),("resource","Platinum-group metals","铂族金属"),("resource","Asteroid water ice","小行星水冰")]),

    ("anti-aging", "Longevity Medicine", "future", "medicine", "2040",
     ["crispr", "gene-therapy", "deep-learning"],
     "Therapies targeting the biological mechanisms of aging — cellular senescence, telomere attrition, mitochondrial dysfunction, epigenetic drift — rather than individual age-related diseases. Senolytic drugs (clearing senescent cells), partial cellular reprogramming via Yamanaka factors (Altos Labs, Calico), and rapamycin-class compounds are early clinical efforts. If successful, longevity medicine could compress morbidity and add decades of healthspan, reshaping demographics, pensions, careers, and family structure.",
     "抗衰老医学", "Life extension",
     [("org","Altos Labs","Altos实验室"),("org","Calico (Alphabet)","Calico"),("person","Aubrey de Grey","奥布里·德格雷"),("person","David Sinclair","大卫·辛克莱"),("unit","Yamanaka factors (OSKM)","山中因子(OSKM)")]),

    ("lab-grown-meat", "Cultivated Meat", "future", "subsistence", "2030",
     ["tissue-engineering", "genetic-engineering", "synthetic-fertilizer"],
     "Animal muscle and fat grown from cell culture in bioreactors rather than on farms. Mark Post's 2013 lab-grown burger cost $325,000; by 2024 cultivated chicken was approved for sale in Singapore (Eat Just) and the United States. The economics still require scale-up of cell-line stability, growth-factor cost reduction, and bioreactor engineering. At maturity, cultivated meat could decouple meat consumption from land use, water, and greenhouse-gas footprints of conventional livestock.",
     "实验室培育肉", "Cultured meat",
     [("org","Eat Just (GOOD Meat)","Eat Just (GOOD Meat)"),("org","UPSIDE Foods","UPSIDE Foods"),("person","Mark Post","马克·波斯特"),("unit","Cultivated chicken","培育鸡肉")]),

    ("synthetic-biology", "Synthetic Biology", "future", "knowledge", "2035",
     ["crispr", "gene-sequencing", "deep-learning"],
     "Engineering organisms with novel genetic circuits, redesigned chromosomes, and computer-designed proteins. Craig Venter's synthetic Mycoplasma (2010) booted from a chemically synthesized genome; AlphaFold (2020) and ESM3 (2024) made protein design tractable; bacterial chassis are now used to produce insulin, artemisinin, leather, and silk. The long arc points toward custom organisms for materials, fuels, drug factories, and environmental remediation.",
     "合成生物学", "Synthetic biology",
     [("person","Craig Venter","克雷格·文特尔"),("unit","Synthetic Mycoplasma (JCVI-syn3.0)","合成支原体"),("work","AlphaFold","AlphaFold蛋白结构预测"),("org","Ginkgo Bioworks","Ginkgo Bioworks"),("unit","ESM3 protein model","ESM3蛋白质模型")]),

    ("room-temp-superconductor", "Room-Temperature Superconductor", "future", "tools", "2040",
     ["advanced-chip-manufacturing", "quantum-mechanics"],
     "Materials that conduct electricity with zero resistance at ambient temperature and pressure, eliminating the cryogenic cost that limits superconducting magnets and power lines. Hydrogen-rich high-pressure superconductors (LaH10 at 250 K, 170 GPa) approach room-temperature behavior; high-temperature copper-oxide superconductors operate above liquid-nitrogen temperature. A practical room-temperature, ambient-pressure superconductor would transform power transmission, MRI, maglev, fusion magnets, and quantum computing.",
     "室温超导体", "Room-temperature superconductor",
     [("resource","Lanthanum decahydride (LaH10)","氢化镧(LaH10)"),("resource","YBCO superconductor","钇钡铜氧超导体"),("person","Karl Müller","卡尔·米勒"),("person","J. Georg Bednorz","约翰内斯·贝德诺尔茨")]),

    ("nanotechnology", "Molecular Nanotechnology", "future", "tools", "2050",
     ["3d-printing", "advanced-chip-manufacturing"],
     "Engineered manipulation of matter at the atomic and molecular scale, from DNA origami and nanoscale drug delivery to (in the long-term) molecular assemblers building bulk goods atom by atom. Drexler's Engines of Creation (1986) sketched the speculative endgame; current practice is dominated by self-assembly, atomic force microscopy, and bottom-up chemistry. Carbon nanotubes, graphene, and quantum dots are commercial realities; atom-by-atom manufacturing remains a research goal.",
     "纳米技术", "Molecular nanotechnology",
     [("person","K. Eric Drexler","K·埃里克·德雷克斯勒"),("person","Richard Feynman","理查德·费曼"),("work","Engines of Creation","《创造的发动机》"),("resource","Carbon nanotube","碳纳米管"),("resource","Graphene","石墨烯")]),

    ("quantum-applications", "Practical Quantum Computing", "future", "knowledge", "2040",
     ["quantum-computing", "advanced-chip-manufacturing"],
     "Fault-tolerant quantum computers solving problems classical machines cannot — Shor's algorithm breaking RSA, Grover's algorithm searching unstructured databases, and quantum chemistry simulations of catalyst and drug molecules. Current systems (Google Sycamore, IBM Heron, IonQ) are NISQ-era — noisy, intermediate-scale, error-prone. Crossing the error-corrected threshold (millions of physical qubits per logical qubit) is the gating step. Practical quantum will rewrite cryptography, materials science, and high-energy physics.",
     "实用量子计算", "Quantum supremacy",
     [("org","IBM Quantum","IBM量子"),("org","Google Quantum AI","谷歌量子AI"),("org","IonQ","IonQ"),("unit","Shor's algorithm","秀尔算法"),("unit","Grover's algorithm","格罗弗算法")]),

    ("carbon-capture-scale", "Carbon Capture at Scale", "future", "energy", "2035",
     ["renewable-grid", "climate-science", "synthetic-fertilizer"],
     "Industrial-scale removal of CO₂ from the atmosphere through direct air capture (Climeworks Orca/Mammoth), bioenergy with carbon capture and storage (BECCS), enhanced rock weathering, and ocean alkalinity enhancement. Current global capacity is ~10 megatons CO₂/year vs. the gigatons needed by midcentury for 1.5°C-compatible scenarios. Costs are falling — Climeworks targets $100/ton — but scale-up requires cheap renewable energy, geological storage, and policy support.",
     "大规模碳捕集", "Direct air capture",
     [("org","Climeworks","Climeworks"),("unit","Orca DAC plant","Orca碳捕集工厂"),("unit","Mammoth DAC plant","Mammoth碳捕集工厂"),("org","Carbon Engineering","Carbon Engineering")]),

    ("fusion-rocket", "Fusion Propulsion", "future", "transport", "2060",
     ["fusion-power", "reusable-rocket"],
     "Spacecraft propulsion driven by fusion reactions, achieving specific impulses of 10,000-100,000 seconds — orders of magnitude beyond chemical or fission rockets. Princeton's PFRC reactor and the Direct Fusion Drive concept are the leading studies; the Daedalus interstellar probe study (1970s) and Project Longshot (1988) explored mission profiles. With fusion propulsion, Mars transit drops below a month and outer-planet missions become practical with crew. It is the gating technology for solar-system colonization.",
     "聚变火箭", "Fusion rocket",
     [("unit","Direct Fusion Drive","直接聚变驱动"),("unit","Daedalus probe (study)","代达罗斯探测器(研究)"),("unit","PFRC reactor","PFRC聚变反应堆")]),

    ("space-elevator", "Space Elevator", "future", "transport", "2080",
     ["nanotechnology", "room-temp-superconductor", "reusable-rocket"],
     "A cable from the equatorial surface to a counterweight beyond geostationary orbit, allowing payloads to ride to orbit on electric climbers at a fraction of rocket cost. The concept dates to Tsiolkovsky (1895) and Yuri Artsutanov (1959); modern interest revived with Bradley Edwards's NASA-funded study (2000). The gating technology is the cable: it requires a material with tensile strength 30-100x steel — carbon nanotube fibers, graphene, or boron nitride. None yet exist at the required length.",
     "太空电梯", "Space elevator",
     [("person","Konstantin Tsiolkovsky","康斯坦丁·齐奥尔科夫斯基"),("person","Yuri Artsutanov","尤里·阿尔楚塔诺夫"),("person","Bradley Edwards","布拉德利·爱德华兹"),("resource","Carbon nanotube cable","碳纳米管缆绳")]),

    ("post-scarcity", "Post-Scarcity Economy", "future", "economy", "2080",
     ["agi", "fusion-power", "humanoid-robot"],
     "An economic regime in which automation, abundant clean energy, and AI-driven production reduce the marginal cost of most goods and services toward zero. With AGI handling cognitive work and humanoid robots handling physical work, the historical link between labor and income breaks down, forcing redesigns of taxation, ownership, and meaning. Universal basic income, post-work culture, and new forms of governance become live political questions rather than thought experiments. Whether such a society is utopian or dystopian depends on the politics around the transition.",
     "后稀缺经济", "Post-scarcity economy",
     [("person","Peter Diamandis","彼得·迪亚曼迪斯"),("work","Abundance (book)","《富足》"),("work","Universal Basic Income","全民基本收入(UBI)"),("person","John Maynard Keynes (1930 essay)","凯恩斯(1930年论文)")]),

    ("digital-immortality", "Mind Uploading", "future", "medicine", "2100",
     ["brain-computer-interface", "agi", "advanced-chip-manufacturing"],
     "Whole-brain emulation: the (so-far-speculative) capture of a human nervous system's connectome and dynamics in computational substrate, allowing the person's cognition to continue indefinitely outside the original biological body. Required components — connectomic-scale neural mapping (currently ~1 mm³ of mouse cortex, Lichtman lab 2024), real-time biophysical simulation, and substrate-independent identity preservation — are each plausible long-term but presently far. Mind uploading is the most philosophically consequential entry in the future tree, intersecting personal identity, consciousness, and the meaning of death.",
     "意识上传", "Mind uploading",
     [("person","Hans Moravec","汉斯·莫拉维克"),("person","Ray Kurzweil","雷·库兹韦尔"),("work","The Singularity Is Near","《奇点临近》"),("unit","Whole-brain emulation","全脑仿真")]),
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

    # ── 1. Add "future" era to ERAS array ──
    info_line = '  { id: "information",   name: "Information",        range: "1970 – present" },'
    new_eras = (info_line + '\n'
                '  { id: "future",        name: "Future Age",         range: "2030 – beyond" },')
    assert info_line in src, "ERAS line shape changed"
    src = src.replace(info_line, new_eras)

    # ── 2. Insert all new tech entries before closing `];` ──
    insertion_marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    assert insertion_marker in src
    blocks = ["\n  // ─── Backfill prereqs for Future Age ───"]
    for tid, name, era, cat, year, prereqs, desc, *_ in PREREQS:
        prq = ", ".join(f'"{p}"' for p in prereqs)
        blocks.append(
            f'  {{ id: "{tid}", name: "{name}", era: "{era}", category: "{cat}",\n'
            f'    year: "{year}", prereqs: [{prq}],\n'
            f'    desc: {json.dumps(desc, ensure_ascii=False)} }},'
        )
    blocks.append("\n  // ─── Future Age ───")
    for tid, name, era, cat, year, prereqs, desc, *_ in FUTURES:
        prq = ", ".join(f'"{p}"' for p in prereqs)
        blocks.append(
            f'  {{ id: "{tid}", name: "{name}", era: "{era}", category: "{cat}",\n'
            f'    year: "{year}", prereqs: [{prq}],\n'
            f'    desc: {json.dumps(desc, ensure_ascii=False)} }},'
        )
    src = src.replace(insertion_marker, "\n".join(blocks) + "\n" + insertion_marker)
    DATA.write_text(src)
    print(f"data.js: +1 era, +{len(PREREQS)} prereq techs, +{len(FUTURES)} future techs")

    # ── 3. Translations ──
    tsrc = TRANS.read_text()
    assert tsrc.rstrip().endswith("};"), "translations.js shape changed"
    insertion = "\n  // ─── Future Age + backfill prereqs ───\n"
    for tid, _, _, _, _, _, _, zh, *_ in PREREQS + FUTURES:
        insertion += f'  "{tid}": "{zh}",\n'
    tsrc = tsrc.rstrip()[:-2] + insertion + "};\n"
    TRANS.write_text(tsrc)
    print(f"translations.js: +{len(PREREQS) + len(FUTURES)} entries")

    # ── 4. Wikipedia images ──
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    fetched = 0
    all_techs = PREREQS + FUTURES
    for tid, name, _, _, _, _, _, _, wiki, _ in all_techs:
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
                print(f"  ! {tid}: no thumbnail")
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

    # ── 5. Regenerate images.js ──
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
    print(f"images.js: {len(entries)} entries")

    # ── 6. Unlocks ──
    usrc = UNLOCKS.read_text()
    assert usrc.rstrip().endswith("};"), "unlocks.js shape changed"
    insertion = "\n  // ─── Future Age + backfill prereqs ───\n"
    for tid, _, _, _, _, _, _, _, _, ulocks in all_techs:
        insertion += f'  "{tid}": [\n'
        for typ, ename, ezh in ulocks:
            insertion += (f'    {{ type: "{typ}", '
                          f'name: {json.dumps(ename, ensure_ascii=False)}, '
                          f'name_zh: {json.dumps(ezh, ensure_ascii=False)} }},\n')
        insertion += '  ],\n'
    usrc = usrc.rstrip()[:-2] + insertion + "};\n"
    UNLOCKS.write_text(usrc)
    print(f"unlocks.js: +{len(all_techs)} entries")


if __name__ == "__main__":
    main()
