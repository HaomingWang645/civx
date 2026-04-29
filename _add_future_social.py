#!/usr/bin/env python3
"""Add 9 social/cultural Future Age techs covering economy, governance,
ideology, and art. Mutates data.js, translations.js, _image_manifest.json,
images.js, unlocks.js."""

import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# id, name, era, category, year, prereqs, desc, zh, wiki_article, unlocks
TECHS = [
    ("universal-basic-income", "Universal Basic Income", "future", "economy", "2035",
     ["agi", "humanoid-robot"],
     "Unconditional cash payments to every citizen sufficient for basic needs, decoupling income from employment. Pilots in Finland (2017–18), Stockton CA (2019), Kenya (GiveDirectly), Iran, and India produced encouraging behavioral data. With AGI and humanoid robots automating most cognitive and physical labor, UBI shifts from contested policy proposal to economic necessity. Funding mechanisms range from negative income tax (Friedman, 1962) and Georgist land-value taxes to AI-output dividends and resource-rent funds (Alaska Permanent Fund as proof of concept).",
     "全民基本收入", "Universal basic income",
     [("person", "Andrew Yang", "杨安泽"),
      ("person", "Milton Friedman (negative income tax)", "米尔顿·弗里德曼"),
      ("org", "GiveDirectly", "GiveDirectly"),
      ("unit", "Alaska Permanent Fund", "阿拉斯加永久基金"),
      ("work", "Universal Basic Income (book, Van Parijs)", "《全民基本收入》(范帕里斯)")]),

    ("liquid-democracy", "Liquid Democracy", "future", "economy", "2040",
     ["cryptocurrency", "agi", "world-wide-web"],
     "Hybrid of direct and representative democracy: citizens vote directly on issues they care about and delegate votes to trusted experts on others, with delegations transitive and revocable in real time. Smart-contract platforms enable continuous vote aggregation; AI assistants help citizens understand policy implications. Taiwan's vTaiwan platform under Audrey Tang's leadership, Estonia's e-Residency, German Pirate Party experiments, and various Iceland deliberative pilots are early instances. Critics worry about manipulability, voter fatigue, and the loss of deliberative space.",
     "流动民主", "Liquid democracy",
     [("person", "Audrey Tang (Taiwan Digital Minister)", "唐凤(台湾数字部长)"),
      ("unit", "vTaiwan platform", "vTaiwan平台"),
      ("org", "e-Estonia", "电子爱沙尼亚"),
      ("org", "Pirate Party", "海盗党"),
      ("work", "Liquid Feedback (software)", "Liquid Feedback软件")]),

    ("network-state", "Network State", "future", "economy", "2040",
     ["cryptocurrency", "world-wide-web", "ecommerce"],
     "Online communities that organize around shared values, accumulate population and capital, and ultimately negotiate for sovereignty — first as charter cities or special economic zones, eventually as recognized states. Balaji Srinivasan's The Network State (2022) outlined the playbook. Próspera (Honduras ZEDE), Nevada Innovation Zones, Zuzalu pop-up cities, Cabin and Cabin Network, and various crypto-funded experiments are early instances. Whether established nation-states permit this without resistance — and whether such communities can deliver real public goods — is the central political question.",
     "网络国家", "The Network State",
     [("person", "Balaji Srinivasan", "巴拉吉·斯里尼瓦桑"),
      ("work", "The Network State (book)", "《网络国家》"),
      ("unit", "Próspera (Honduras ZEDE)", "普罗斯佩拉(洪都拉斯特区)"),
      ("unit", "Zuzalu (pop-up city)", "Zuzalu(实验性城邦)")]),

    ("ai-governance", "Algorithmic Governance", "future", "economy", "2050",
     ["agi", "large-language-model"],
     "State use of AI for policy analysis, regulation drafting, judicial recommendations, and operational decision-making — initially in advisory roles, eventually in execution. Estonia's pilot 'AI judge' for small-claims court, the EU AI Act's risk tiers, China's social credit experiments, Singapore's AI in public-service delivery, and DARPA's AI-policy initiatives are precursors. The legitimacy and accountability questions are profound: who is responsible when an AI denies a visa, sets a tax rate, or recommends a sentence?",
     "算法治理", "Algorithmic regulation",
     [("unit", "Estonia AI judge (pilot)", "爱沙尼亚AI法官(试点)"),
      ("work", "EU AI Act", "欧盟人工智能法案"),
      ("org", "Singapore Smart Nation", "新加坡智慧国家"),
      ("work", "Algorithmic Regulation (Tim O'Reilly)", "《算法监管》(奥莱利)")]),

    ("transhumanism", "Transhumanism", "future", "social", "2030",
     ["brain-computer-interface", "anti-aging"],
     "Cultural and intellectual movement advocating the use of technology to enhance human physical, cognitive, emotional, and longevity capabilities. Roots in Julian Huxley's 1957 essay; FM-2030, Max More, Nick Bostrom, Anders Sandberg, and Ray Kurzweil developed the philosophy. With BCIs, gene editing, and longevity medicine becoming clinical realities, transhumanism transitions from speculation to applied ethics: Who can afford enhancement? Are unenhanced humans disadvantaged? What counts as human? The question stops being academic once the technologies arrive.",
     "超人类主义", "Transhumanism",
     [("person", "Nick Bostrom", "尼克·博斯特罗姆"),
      ("person", "Ray Kurzweil", "雷·库兹韦尔"),
      ("person", "Max More", "马克斯·摩尔"),
      ("person", "FM-2030", "FM-2030"),
      ("org", "Humanity+ (WTA)", "人类+协会")]),

    ("longtermism", "Longtermism", "future", "social", "2030",
     ["enlightenment-philosophy", "climate-science"],
     "Ethical framework arguing the moral importance of future generations — potentially trillions of lives over millennia — outweighs many near-term concerns. Derek Parfit's Reasons and Persons (1984), Nick Beckstead's dissertation, Toby Ord's The Precipice (2020), and William MacAskill's What We Owe the Future (2022) systematized the view. The Future of Humanity Institute, Open Philanthropy, and 80,000 Hours channel longtermist thinking into existential-risk research, AI safety, and pandemic preparedness. Critics argue it discounts present-day suffering and is sensitive to moral uncertainty.",
     "长期主义", "Longtermism",
     [("person", "Derek Parfit", "德里克·帕菲特"),
      ("person", "Toby Ord", "托比·奥德"),
      ("person", "William MacAskill", "威廉·麦卡斯基尔"),
      ("work", "The Precipice (Ord, 2020)", "《悬崖》(奥德,2020)"),
      ("work", "What We Owe the Future", "《我们欠未来的》"),
      ("org", "80,000 Hours", "80,000 Hours")]),

    ("generative-art", "Generative Art", "future", "social", "2030",
     ["large-language-model", "deep-learning"],
     "AI-generated images, music, video, and text treated as a new creative medium rather than a tool. Midjourney and DALL-E (2022), Stable Diffusion, Suno (music), Sora and Veo (video), and Runway opened the floodgates; the same year, Refik Anadol's MoMA installation and Boris Eldagsen winning a Sony Photography prize signaled fine-art recognition. Disruption to human illustrators, voice actors, and stock photographers is acute; copyright cases (Getty v. Stable Diffusion, NYT v. OpenAI) are reshaping IP law in real time.",
     "生成艺术", "Generative art",
     [("org", "Midjourney", "Midjourney"),
      ("unit", "Stable Diffusion", "Stable Diffusion"),
      ("unit", "DALL-E", "DALL·E"),
      ("unit", "Sora (OpenAI)", "Sora(OpenAI)"),
      ("person", "Refik Anadol", "雷菲克·阿纳多尔"),
      ("person", "Holly Herndon", "霍莉·赫顿")]),

    ("metaverse", "Metaverse", "future", "social", "2035",
     ["advanced-chip-manufacturing", "deep-learning", "world-wide-web"],
     "Persistent, networked, immersive virtual worlds with millions of concurrent users, combining VR/AR headsets, AI-driven characters, and economy-bearing digital ownership. Neal Stephenson's Snow Crash (1992) coined the term; Ernest Cline's Ready Player One (2011) popularized it; Roblox, Fortnite, VRChat, Meta's Horizon Worlds, and Apple Vision Pro (2024) are pre-metaverse implementations. Whether the metaverse is the next computing platform or hyped vaporware remains genuinely uncertain after Meta's $40B+ Reality Labs losses.",
     "元宇宙", "Metaverse",
     [("work", "Snow Crash (Neal Stephenson)", "《雪崩》(尼尔·斯蒂芬森)"),
      ("work", "Ready Player One", "《头号玩家》"),
      ("org", "Meta Reality Labs", "Meta现实实验室"),
      ("unit", "Apple Vision Pro", "苹果Vision Pro"),
      ("unit", "VRChat", "VRChat")]),

    ("decentralized-autonomous-org", "Decentralized Autonomous Organization", "future", "economy", "2030",
     ["cryptocurrency", "programming-language"],
     "Organizations whose governance and operations are encoded as smart contracts on a public blockchain, with token-holders voting on proposals and treasury actions without intermediating institutions. The DAO (2016, infamously hacked for $50M), MakerDAO, Uniswap, ConstitutionDAO (which raised $47M in days to bid on a U.S. Constitution copy in 2021), and Friends With Benefits showed varied applications. DAOs promise programmable, trustless coordination at scale; in practice, governance attacks, low voter turnout, plutocratic capture, and regulatory ambiguity have constrained adoption.",
     "去中心化自治组织", "Decentralized autonomous organization",
     [("org", "MakerDAO", "MakerDAO"),
      ("org", "Uniswap", "Uniswap"),
      ("org", "ConstitutionDAO", "ConstitutionDAO"),
      ("person", "Vitalik Buterin", "维塔利克·布特林"),
      ("unit", "Smart contracts", "智能合约")]),
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
    blocks = ["\n  // ─── Future Age (social / economic / cultural) ───"]
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

    # Translations
    tsrc = TRANS.read_text()
    assert tsrc.rstrip().endswith("};")
    insertion = "\n  // ─── Future Age (social) ───\n"
    for tid, _, _, _, _, _, _, zh, *_ in TECHS:
        insertion += f'  "{tid}": "{zh}",\n'
    tsrc = tsrc.rstrip()[:-2] + insertion + "};\n"
    TRANS.write_text(tsrc)
    print(f"translations.js: +{len(TECHS)} entries")

    # Wikipedia images
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

    # Regenerate images.js
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

    # Unlocks
    usrc = UNLOCKS.read_text()
    assert usrc.rstrip().endswith("};")
    insertion = "\n  // ─── Future Age (social) ───\n"
    for tid, _, _, _, _, _, _, _, _, ulocks in TECHS:
        insertion += f'  "{tid}": [\n'
        for typ, ename, ezh in ulocks:
            insertion += (f'    {{ type: "{typ}", '
                          f'name: {json.dumps(ename, ensure_ascii=False)}, '
                          f'name_zh: {json.dumps(ezh, ensure_ascii=False)} }},\n')
        insertion += '  ],\n'
    usrc = usrc.rstrip()[:-2] + insertion + "};\n"
    UNLOCKS.write_text(usrc)
    print(f"unlocks.js: +{len(TECHS)} entries")


if __name__ == "__main__":
    main()
