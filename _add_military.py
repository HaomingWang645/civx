#!/usr/bin/env python3
"""Add 14 military techs spanning Modern → Information era.
Mutates data.js, translations.js, _image_manifest.json, images.js, unlocks.js
in-place. Wikipedia images are fetched and saved into images/."""

import json, re, time, urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# tech_id -> (name, era, year, prereqs, desc, zh, wiki_article, unlocks)
TECHS = [
    ("tank", "Tank", "modern", "1916",
     ["internal-combustion", "machine-gun", "bessemer-steel"],
     "Tracked, armored, internally-powered vehicle carrying its own armament. The British Mark I (1916) at Flers-Courcelette broke the trench-warfare stalemate of WWI; J.F.C. Fuller's Plan 1919 imagined armored breakthrough as the future of warfare. By WWII the T-34, M4 Sherman, Panzer IV, and Tiger I had defined the modern tank, and Soviet deep-battle and German blitzkrieg doctrines made armored maneuver the central form of land warfare for the rest of the 20th century.",
     "坦克", "Tank",
     [("unit","Mark I tank","马克I型坦克"),("unit","T-34","T-34坦克"),("unit","M4 Sherman","M4谢尔曼坦克"),("unit","Tiger I","虎式坦克"),("person","J.F.C. Fuller","J·F·C·富勒")]),

    ("aircraft-carrier", "Aircraft Carrier", "modern", "1922",
     ["steamship", "airplane", "internal-combustion"],
     "Warship with a flight deck, hangars, catapults, and arrestor wires for fixed-wing operations. USS Langley (CV-1, 1922, converted from a collier) was the U.S. Navy's first; Lexington and Saratoga (1927) and Akagi made carriers fleet flagships. Pearl Harbor (1941) and Midway (1942) demonstrated that carriers had displaced the battleship as the capital ship. By the late 20th century carriers were instruments of global power projection rather than fleet engagements.",
     "航空母舰", "Aircraft carrier",
     [("unit","USS Langley (CV-1)","美国海军兰利号航空母舰"),("unit","USS Enterprise (CV-6)","企业号航空母舰"),("unit","HMS Hermes","赫尔墨斯号航空母舰"),("wonder","Battle of Midway","中途岛海战")]),

    ("submarine-warfare", "Submarine Warfare", "modern", "1914",
     ["steamship", "internal-combustion", "electric-battery"],
     "Diesel-electric submarines fielded as strategic weapons of attrition against surface shipping. German U-boats nearly starved Britain in WWI and again in 1942–43 with wolfpack tactics and the Type VII; Allied convoys, sonar, depth-charges, and ULTRA decryption eventually broke the Atlantic campaign. The Type XXI 'Elektroboot' (1944) — high underwater speed, snorkel — pointed toward modern fully submerged operations.",
     "潜艇战", "Submarine warfare",
     [("unit","Type VII U-boat","VII型潜艇"),("unit","Type XXI U-boat","XXI型潜艇"),("person","Karl Dönitz","卡尔·邓尼茨"),("unit","Wolfpack tactics","狼群战术")]),

    ("thermonuclear-weapon", "Thermonuclear Weapon", "atomic", "1952",
     ["nuclear-weapon"],
     "Hydrogen-fusion bomb using a fission primary to compress and ignite a fusion secondary, releasing energies a thousand times that of fission alone. Ivy Mike (1952, 10.4 Mt) was the first true H-bomb test; Castle Bravo (1954, 15 Mt) was the largest U.S. test; the Soviet Tsar Bomba (1961) yielded ~50 Mt. The Teller-Ulam configuration is still classified in detail but shapes every modern strategic warhead, with a single warhead capable of destroying the largest cities.",
     "氢弹", "Thermonuclear weapon",
     [("unit","Ivy Mike","常春藤·麦克氢弹试验"),("unit","Castle Bravo","城堡·布拉沃氢弹试验"),("unit","Tsar Bomba","沙皇炸弹"),("person","Edward Teller","爱德华·泰勒"),("person","Stanislaw Ulam","斯坦尼斯瓦夫·乌拉姆"),("person","Andrei Sakharov","安德烈·萨哈罗夫")]),

    ("icbm", "Intercontinental Ballistic Missile", "atomic", "1957",
     ["rocket", "nuclear-weapon", "digital-computer"],
     "Boost-glide ballistic missile of intercontinental range carrying a nuclear warhead. The Soviet R-7 Semyorka (August 1957) was the first; the U.S. Atlas (1959) and Minuteman (1962) followed; submarine-launched Polaris (1960) added a survivable second strike. ICBMs reduced strategic warning time from hours to ~30 minutes, made every population center on Earth instantly targetable, and underwrote the Cold War's mutually assured destruction.",
     "洲际弹道导弹", "Intercontinental ballistic missile",
     [("unit","R-7 Semyorka","R-7火箭"),("unit","Atlas missile","宇宙神导弹"),("unit","Minuteman III","民兵III型导弹"),("unit","Polaris (submarine-launched)","北极星导弹")]),

    ("nuclear-submarine", "Nuclear Submarine", "atomic", "1954",
     ["nuclear-power", "submarine-warfare"],
     "Submarine driven by a nuclear reactor, capable of remaining submerged for months and circling the globe without refueling. USS Nautilus (SSN-571, 1954) was the first; USS George Washington (SSBN-598, 1959) carried 16 Polaris ballistic missiles, creating the survivable nuclear deterrent. By 1960 the Skipjack class achieved teardrop hulls optimized for underwater operation. SSBNs remain the most invulnerable strategic weapons platform.",
     "核潜艇", "Nuclear submarine",
     [("unit","USS Nautilus (SSN-571)","鹦鹉螺号核潜艇"),("unit","USS George Washington (SSBN-598)","乔治·华盛顿号核潜艇"),("unit","Trident missile","三叉戟导弹"),("person","Hyman G. Rickover","海曼·G·里科弗")]),

    ("nuclear-aircraft-carrier", "Nuclear Aircraft Carrier", "atomic", "1961",
     ["aircraft-carrier", "nuclear-power"],
     "Aircraft carrier driven by nuclear reactors, eliminating fuel-tanker dependence and giving essentially unlimited high-speed range. USS Enterprise (CVN-65, commissioned 1961) was the first, with eight reactors. The Nimitz class (1975 onward) standardized two-reactor 100,000-ton supercarriers as the symbol of American power projection. The Gerald R. Ford class (2017) introduces electromagnetic catapults and reduces crew requirements.",
     "核动力航母", "Nuclear-powered aircraft carrier",
     [("unit","USS Enterprise (CVN-65)","企业号核动力航母"),("unit","Nimitz class","尼米兹级航母"),("unit","Gerald R. Ford class","福特级航母")]),

    ("guided-missile", "Guided Missile", "atomic", "1956",
     ["rocket", "radar"],
     "Missile that adjusts its trajectory in flight using infrared, radar, or wire guidance. The AIM-9 Sidewinder (1956) was the first effective infrared air-to-air missile; the radar-guided AIM-7 Sparrow gave beyond-visual-range engagement; SA-2 Guideline (1957) demonstrated surface-to-air missiles in the U-2 shootdown of 1960. Within twenty years, gun-only fighters had been displaced and most warships became platforms for missiles rather than artillery.",
     "制导导弹", "Guided missile",
     [("unit","AIM-9 Sidewinder","AIM-9响尾蛇导弹"),("unit","AIM-7 Sparrow","AIM-7麻雀导弹"),("unit","SA-2 Guideline","SA-2地空导弹"),("unit","BGM-71 TOW","BGM-71陶式反坦克导弹")]),

    ("precision-guided-munition", "Precision-Guided Munition", "information", "1972",
     ["guided-missile", "microprocessor"],
     "Munitions guided to specific aimpoints by laser, GPS, or imaging seekers, achieving circular error probable of meters rather than tens of meters. Paveway laser-guided bombs in the Linebacker raids on Hanoi (1972) demonstrated the concept; JDAM GPS kits (1997) gave every cheap bomb precision capability; Tomahawk cruise missiles (1991, Desert Storm) added stand-off range. PGMs replaced area bombing with single-target strikes and reshaped the ethics and political tolerance of military operations.",
     "精确制导武器", "Precision-guided munition",
     [("unit","Paveway laser-guided bomb","宝石路激光制导炸弹"),("unit","JDAM","联合直接攻击弹药(JDAM)"),("unit","Tomahawk cruise missile","战斧巡航导弹"),("unit","AGM-114 Hellfire","AGM-114地狱火导弹")]),

    ("stealth-aircraft", "Stealth Aircraft", "information", "1981",
     ["airplane", "radar", "programming-language"],
     "Aircraft designed to minimize radar cross-section through faceted or blended geometry, radar-absorbent materials, infrared masking, and reduced acoustic signature. Lockheed's Have Blue prototype and the F-117 Nighthawk (operational 1983, public 1988) were the first; the B-2 Spirit (1989) extended the principle to a strategic bomber. Stealth requires solving Maxwell's equations on supercomputers — the technology is computational as much as material.",
     "隐形战机", "Stealth aircraft",
     [("unit","F-117 Nighthawk","F-117夜鹰战斗机"),("unit","B-2 Spirit","B-2幽灵轰炸机"),("person","Ben Rich (Skunk Works)","本·里奇(臭鼬工厂)"),("org","Lockheed Skunk Works","洛克希德臭鼬工厂")]),

    ("drone-uav", "Unmanned Aerial Vehicle", "information", "1995",
     ["airplane", "microprocessor", "satellite"],
     "Pilotless aircraft, remotely operated or autonomous, used for reconnaissance, strike, and increasingly logistics. General Atomics MQ-1 Predator (1995) put long-endurance ISR over Bosnia and later Afghanistan; armed Predators conducted the first targeted killings; the MQ-9 Reaper, RQ-4 Global Hawk, and Turkish Bayraktar TB2 (Ukraine 2022) extended drone warfare globally. Cheap quadcopter drones have since reshaped infantry combat from Karabakh to Ukraine.",
     "无人机", "Unmanned aerial vehicle",
     [("unit","MQ-1 Predator","MQ-1捕食者无人机"),("unit","MQ-9 Reaper","MQ-9死神无人机"),("unit","RQ-4 Global Hawk","RQ-4全球鹰无人机"),("unit","Bayraktar TB2","拜拉克塔尔TB2无人机"),("org","General Atomics","通用原子能公司")]),

    ("fifth-gen-fighter", "Fifth-Generation Fighter", "information", "2005",
     ["stealth-aircraft", "jet-engine"],
     "Stealth fighter combining low radar signature, supersonic cruise without afterburner, internal weapons bays, sensor fusion, and high-bandwidth datalinks. The F-22 Raptor (IOC 2005) was first; the F-35 Lightning II (2015) is the largest defense program in history. The Chengdu J-20 (2017) and Sukhoi Su-57 (2020) are non-Western entrants. Fifth-generation aircraft are network nodes as much as airframes, with their advantage as much in data fusion as in the platform itself.",
     "第五代战斗机", "Fifth-generation fighter",
     [("unit","F-22 Raptor","F-22猛禽战斗机"),("unit","F-35 Lightning II","F-35闪电II战斗机"),("unit","Chengdu J-20","成都J-20战斗机"),("unit","Sukhoi Su-57","苏-57战斗机")]),

    ("cyber-warfare", "Cyber Warfare", "information", "2010",
     ["arpanet-internet", "programming-language"],
     "State-directed digital attacks against industrial systems, critical infrastructure, and political targets. Stuxnet (2010, U.S.-Israeli operation against Iranian centrifuges) was the first publicly attributed strategic cyberweapon. NotPetya (2017, Russia targeting Ukraine, then global spillover, $10B+ damage), election interference, ransomware-for-hire, and cyber components of Russia's invasion of Ukraine (2022) make cyber a permanent dimension of state conflict alongside the kinetic ones.",
     "网络战", "Cyberwarfare",
     [("unit","Stuxnet","震网病毒"),("unit","NotPetya","NotPetya勒索软件"),("org","NSA TAO","美国国安局特定入侵行动办公室"),("org","Unit 8200","以色列8200部队")]),

    ("hypersonic-weapon", "Hypersonic Weapon", "information", "2019",
     ["jet-engine", "guided-missile", "advanced-chip-manufacturing"],
     "Maneuverable weapons sustaining Mach 5+ in the atmosphere via hypersonic glide vehicles or air-breathing scramjets. Russia's Avangard HGV (operational 2019), China's DF-17 with the DF-ZF glider (2019), and North Korea's Hwasong-8 (2021) entered service while U.S. systems (HAWC, ARRW) are in development. Their speed and maneuverability defeat conventional ABM systems and compress decision time further than ICBMs did.",
     "高超音速武器", "Hypersonic flight",
     [("unit","Avangard","先锋高超音速导弹"),("unit","DF-17 / DF-ZF","东风-17 / 东风-ZF"),("unit","Hwasong-8","火星-8导弹")]),
]


def parse_year(s):
    s = s.strip().lstrip("~").strip()
    s = re.sub(r'\s*\(.*?\)\s*', '', s)
    m = re.match(r'^(-?[\d.]+)\s*([A-Za-z]*)', s.strip())
    if not m: return None
    num = float(m.group(1)); unit = (m.group(2) or "").upper()
    if unit == "MYA": return -num*1_000_000
    if unit == "KYA": return -num*1000
    if unit in ("BCE","BC"): return -num
    return num


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
    # ── 1. Insert tech entries into data.js (before closing `];`) ──
    src = DATA.read_text()
    insertion_marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    assert insertion_marker in src
    blocks = []
    for tid, name, era, year, prereqs, desc, *_ in TECHS:
        prereq_str = ", ".join(f'"{p}"' for p in prereqs)
        blocks.append(
            f'  {{ id: "{tid}", name: "{name}", era: "{era}", category: "weapons",\n'
            f'    year: "{year}", prereqs: [{prereq_str}],\n'
            f'    desc: {json.dumps(desc, ensure_ascii=False)} }},'
        )
    insert_text = "\n  // ─── Military additions ───\n" + "\n".join(blocks) + "\n"
    src = src.replace(insertion_marker, insert_text + insertion_marker)
    DATA.write_text(src)
    print(f"data.js: added {len(TECHS)} tech entries")

    # ── 2. Translations ──
    tsrc = TRANS.read_text()
    insertion = "\n  // ─── Military additions ───\n"
    for tid, _, _, _, _, _, zh, *_ in TECHS:
        insertion += f'  "{tid}": "{zh}",\n'
    # Insert before the closing `};`
    assert tsrc.rstrip().endswith("};"), "translations.js shape changed"
    tsrc = tsrc.rstrip()[:-2] + insertion + "};\n"
    TRANS.write_text(tsrc)
    print(f"translations.js: added {len(TECHS)} entries")

    # ── 3. Wikipedia images ──
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    fetched = 0
    for tid, name, _, _, _, _, _, wiki_article, _ in TECHS:
        if tid in manifest and manifest[tid].get("status") == "ok":
            continue
        try:
            url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(wiki_article.replace(' ', '_'))
            j = http_json(url)
            thumb = (j.get("thumbnail") or {}).get("source")
            page = j.get("content_urls", {}).get("desktop", {}).get("page", url)
            if not thumb:
                manifest[tid] = {"name": name, "article": j.get("title"), "page": page, "status": "no_image", "reason": "no thumbnail"}
                print(f"  ! {tid}: no thumbnail in {wiki_article}")
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
            print(f"  + {tid:30} {j.get('title')} → {out.name} ({len(data)} bytes)")
            time.sleep(0.6)
        except Exception as e:
            print(f"  ! {tid}: ERR {e}")
            manifest[tid] = {"name": name, "status": "no_match", "reason": str(e)[:120]}
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"images: fetched {fetched}")

    # ── 4. Regenerate images.js ──
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

    # ── 5. Unlocks ──
    usrc = UNLOCKS.read_text()
    assert usrc.rstrip().endswith("};"), "unlocks.js shape changed"
    insertion = "\n  // ─── Military additions ───\n"
    for tid, _, _, _, _, _, _, _, ulocks in TECHS:
        insertion += f'  "{tid}": [\n'
        for typ, ename, ezh in ulocks:
            insertion += f'    {{ type: "{typ}", name: {json.dumps(ename, ensure_ascii=False)}, name_zh: {json.dumps(ezh, ensure_ascii=False)} }},\n'
        insertion += '  ],\n'
    usrc = usrc.rstrip()[:-2] + insertion + "};\n"
    UNLOCKS.write_text(usrc)
    print(f"unlocks.js: added {len(TECHS)} entries")


if __name__ == "__main__":
    main()
