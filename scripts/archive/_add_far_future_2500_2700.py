#!/usr/bin/env python3
"""Add 8 Far Future techs filling the 2500-2700 gap, plus update warp-drive
to gate on the new dark-energy-engineering prereq.

Atomically updates data.js, translations.js, unlocks.js. Image fetching is
done separately by _fetch_far_future_2500_images.py."""

import json, re
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Far Future (2500-2700 fill) ───
  { id: "black-hole-engineering", name: "Black Hole Engineering", era: "far-future", category: "energy",
    year: "2550", prereqs: ["stellar-engineering", "kardashev-type-ii"],
    desc: "Active engineering use of black holes — the Penrose process extracting rotational energy from Kerr black holes, Hawking-radiation harvesters around artificial micro black holes, and gravitational confinement reactors. Roger Penrose's 1971 paper showed that up to 29% of a rotating black hole's mass-energy can be extracted via reverse-Compton-style scattering off the ergosphere. By the 26th century an established Type II civilization fields engineered Kerr-class power plants — black holes built or moved into useful orbits, drained over megayear timescales for an output rivaling stellar luminosity in compact form." },
  { id: "galactic-communication-network", name: "Galactic Communication Network", era: "far-future", category: "communication",
    year: "2550", prereqs: ["galactic-civilization", "lingua-galactica"],
    desc: "A galaxy-spanning communications fabric: dedicated relay stations along major Hill-sphere intersections, neutrino-modulated long-baseline links cutting through interstellar dust, and protocol layers that handle century-scale latency as a normal feature rather than a fault. Any single message takes ~100,000 years to traverse the Milky Way at light speed; the network operates as a deeply asynchronous publish-subscribe system rather than as conversation. Cultural and economic life adapts to a permanent communications horizon — local consensus reigns within a few-light-year cluster, while galactic-scale agreements move at glacial pace." },
  { id: "pre-warp-interstellar-trade", name: "Pre-Warp Interstellar Trade", era: "far-future", category: "economy",
    year: "2550", prereqs: ["galactic-civilization", "generation-ship-colony"],
    desc: "Sub-light interstellar commerce: cargoes of unique materials, biological cultivars, and information-dense artifacts shipped at substantial fractions of c with century-scale delivery times. Light-lag arbitrage — pricing at origin vs destination separated by decades of news — becomes the central economic problem; standardized future-delivery contracts and reputation-based clearing replace synchronous markets. Trading polities specialize at scales where shipping is economical (rare isotopes, unique organisms, novel cultural works), while bulk goods stay local. Light-lag economics generates new financial instruments unknown to faster economies." },
  { id: "pan-galactic-coordination-ai", name: "Pan-Galactic Coordination AI", era: "far-future", category: "knowledge",
    year: "2600", prereqs: ["superintelligence", "galactic-civilization"],
    desc: "A civilization-spanning superintelligence substrate replicated and synchronized across thousands of star systems, coordinating Type II → Type III industrial and ecological policy on million-year horizons. Each local instance handles in-system decisions; the substrate as a whole maintains weak galactic consensus through asynchronous reconciliation across light-year distances. Earlier debates about AI alignment reframe into questions of inter-instance value drift, sub-substrate forking, and how a distributed intelligence preserves identity across communications horizons it cannot fully cross. The pan-galactic AI both stabilizes and constrains civilizational evolution." },
  { id: "femto-engineering", name: "Femto-Engineering", era: "far-future", category: "tools",
    year: "2600", prereqs: ["programmable-matter", "nanotechnology"],
    desc: "Manipulation of matter at nuclear (10⁻¹⁵ m) length scales: engineered isotopes, designer atomic nuclei, controlled nuclear isomers as energy storage, and metastable exotic-nucleus structures impossible in natural environments. Robert Forward, Robert Freitas, and Robert Bradbury speculated about femto-tech in the 1990s; by the 26th century it operates as an industrial discipline. Femto-engineering provides energy densities thousands of times nuclear fission, enables matter-recycling at the proton-neutron level, and underpins later strange-matter and dark-energy capabilities." },
  { id: "vacuum-energy-extraction", name: "Vacuum Energy Extraction", era: "far-future", category: "energy",
    year: "2650", prereqs: ["dark-sector-physics", "kardashev-type-ii"],
    desc: "Practical extraction of zero-point energy from the quantum vacuum — Casimir-effect generators harvesting the difference between vacuum states between closely-spaced surfaces, dynamical Casimir effect emitters in oscillating cavities, and engineered vacuum-state transitions releasing energy. Hendrik Casimir's 1948 prediction was confirmed in the 1990s at vanishingly small scales; by the 27th century engineered geometries amplify the effect into useful power. The energy density of the vacuum (estimated 10⁻⁹ J/m³ at minimum, vastly higher in some theories) becomes a practical resource if even a small fraction is harvestable." },
  { id: "strange-quark-matter", name: "Strange / Quark Matter", era: "far-future", category: "tools",
    year: "2650", prereqs: ["femto-engineering", "quantum-gravity"],
    desc: "Engineering with quark-deconfined matter — strange matter (up + down + strange quarks in approximate equilibrium), color-flavor-locked phases, and stable quark-matter macroscopic structures. The strange-matter hypothesis (Bodmer 1971, Witten 1984) holds that strange matter may be the true ground state of QCD; if so, properly stabilized lumps would be denser than nuclear matter and structurally exotic. Quark-matter hulls for relativistic-velocity craft, ultra-dense storage, and gravitational-wave-resistant computing become engineering options once stabilization is mastered." },
  { id: "dark-energy-engineering", name: "Dark Energy Engineering", era: "far-future", category: "energy",
    year: "2680", prereqs: ["vacuum-energy-extraction", "quantum-gravity"],
    desc: "Localized manipulation of the cosmological constant — engineered regions of negative-pressure dark energy producing controlled spacetime expansion or contraction, and stabilized exotic-matter (negative-energy-density) configurations. The 1998 supernova observations of accelerating cosmic expansion established dark energy as ~68% of the universe's energy budget; by the late 27th century engineered analogues become technological. Dark-energy engineering is the immediate precursor to the Alcubierre warp metric — the same exotic-matter machinery, applied at craft scale rather than cosmological scale." },
"""

TRANSLATIONS = {
    "black-hole-engineering":         "黑洞工程",
    "galactic-communication-network": "银河通信网络",
    "pre-warp-interstellar-trade":    "亚光速星际贸易",
    "pan-galactic-coordination-ai":   "泛银河协调智能",
    "femto-engineering":              "飞米工程",
    "vacuum-energy-extraction":       "真空能提取",
    "strange-quark-matter":           "奇异夸克物质",
    "dark-energy-engineering":        "暗能量工程",
}

UNLOCKS = {
    "black-hole-engineering": [
        ("resource", "Penrose process",                   "彭罗斯过程"),
        ("resource", "Hawking-radiation harvester",       "霍金辐射收集器"),
        ("unit",     "Kerr power plant",                  "克尔黑洞电站"),
        ("work",     "Black-hole bomb",                   "黑洞炸弹理论"),
    ],
    "galactic-communication-network": [
        ("unit",     "Neutrino relay station",            "中微子中继站"),
        ("resource", "Long-baseline laser link",          "长基线激光通信"),
        ("work",     "Galactic Asynchronous Protocol",    "《银河异步协议》"),
        ("wonder",   "Sagittarius A* relay hub",          "人马座 A* 中继枢纽"),
    ],
    "pre-warp-interstellar-trade": [
        ("resource", "Slow-trade contract",                "慢速贸易合约"),
        ("resource", "Light-lag arbitrage",                "光速延迟套利"),
        ("org",      "Interstellar Mercantile Consortium", "星际商业联合体"),
        ("unit",     "Sub-light freighter",                "亚光速货船"),
    ],
    "pan-galactic-coordination-ai": [
        ("unit",     "Galactic Mind substrate",           "银河心智基质"),
        ("resource", "Inter-instance value reconciliation","实例间价值校准"),
        ("work",     "Pan-Galactic Coordination Treaty",  "《泛银河协调条约》"),
    ],
    "femto-engineering": [
        ("resource", "Designer atomic nucleus",           "定制原子核"),
        ("resource", "Nuclear-isomer battery",            "核同质异能素电池"),
        ("unit",     "Femto-fabricator",                  "飞米制造机"),
    ],
    "vacuum-energy-extraction": [
        ("unit",     "Casimir-cavity generator",          "卡西米尔腔发电机"),
        ("resource", "Zero-point energy cell",            "零点能电池"),
        ("resource", "Dynamical Casimir emitter",         "动态卡西米尔发射器"),
    ],
    "strange-quark-matter": [
        ("resource", "Strange-matter ingot",              "奇异物质锭"),
        ("resource", "Color-flavor-locked phase",         "色味锁定相"),
        ("unit",     "Quark-matter hull",                 "夸克物质船体"),
    ],
    "dark-energy-engineering": [
        ("resource", "Negative-energy field",             "负能量场"),
        ("resource", "Cosmological-constant modulator",   "宇宙学常数调制器"),
        ("unit",     "Alcubierre precursor coil",         "阿尔库别雷前驱线圈"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "black-hole-engineering" in src:
        print("data.js: already inserted")
        return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    new_src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")

    # Update warp-drive prereqs to include dark-energy-engineering
    old_warp = '{ id: "warp-drive", name: "Alcubierre Warp Drive", era: "far-future", category: "transport",\n    year: "2700", prereqs: ["quantum-gravity", "dark-sector-physics"]'
    new_warp = '{ id: "warp-drive", name: "Alcubierre Warp Drive", era: "far-future", category: "transport",\n    year: "2700", prereqs: ["dark-energy-engineering", "quantum-gravity"]'
    if old_warp in new_src:
        new_src = new_src.replace(old_warp, new_warp)
        print("  warp-drive prereqs updated to gate on dark-energy-engineering")
    else:
        print("  WARNING: warp-drive prereq pattern not found")
    DATA.write_text(new_src)
    print(f"data.js: +{len(TRANSLATIONS)} far-future techs")


def splice_translations():
    src = TRANS.read_text()
    if '"black-hole-engineering"' in src:
        print("translations.js: already inserted")
        return
    block = "\n  // ─── Far Future (2500-2700 fill) ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip()
    assert rs.endswith("};"), "translations.js end marker missing"
    new_src = rs[:-2] + block + "};\n"
    TRANS.write_text(new_src)
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"black-hole-engineering"' in src:
        print("unlocks.js: already inserted")
        return
    block = "\n  // ─── Far Future (2500-2700 fill) ───\n"
    for tid, items in UNLOCKS.items():
        block += f'  "{tid}": [\n'
        for typ, name, name_zh in items:
            block += (f'    {{ type: "{typ}", '
                      f'name: {json.dumps(name, ensure_ascii=False)}, '
                      f'name_zh: {json.dumps(name_zh, ensure_ascii=False)} }},\n')
        block += '  ],\n'
    rs = src.rstrip()
    assert rs.endswith("};"), "unlocks.js end marker missing"
    new_src = rs[:-2] + block + "};\n"
    UNLOCKS_PATH.write_text(new_src)
    print(f"unlocks.js: +{len(UNLOCKS)}")


if __name__ == "__main__":
    splice_data()
    splice_translations()
    splice_unlocks()
