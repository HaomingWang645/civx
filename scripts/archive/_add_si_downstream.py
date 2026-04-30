#!/usr/bin/env python3
"""Add 3 new techs downstream of superintelligence:
  whole-brain-emulation, knowledge-closure, subjective-time-compression.
And connect them into the existing tree by updating prereqs of:
  digital-immortality        ← whole-brain-emulation
  time-dilation-cultures     ← subjective-time-compression
  end-time-philosophy        ← knowledge-closure
"""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Superintelligence downstream ───
  { id: "whole-brain-emulation", name: "Whole-Brain Emulation", era: "far-future", category: "medicine",
    year: "2140", prereqs: ["superintelligence", "brain-computer-interface", "neuroscience"],
    desc: "High-fidelity scan and simulation of an individual biological brain, reproducing the functional dynamics of the original to a degree where personhood, memory, and behavior transfer continuously across substrates. The OpenWorm project (C. elegans, 2011–) demonstrated proof-of-concept at the simplest scale; Henry Markram's Blue Brain Project (cortical column, 2005–) and IBM's Synapse (rat brain, 2014) tackled mid-scale; high-resolution full-human connectomes from electron microscopy + functional state from advanced fMRI converge in the late 2130s. WBE is the bridge between the SI era's compute substrates and personal mind uploading. Anders Sandberg and Nick Bostrom's 2008 'Whole Brain Emulation Roadmap' (FHI) remains the technical reference." },
  { id: "knowledge-closure", name: "Knowledge Closure", era: "far-future", category: "knowledge",
    year: "2200", prereqs: ["superintelligence", "formal-mathematics"],
    desc: "Civilization reaches the limit of answerable scientific and mathematical questions: every empirically-determinable physical fact is known, every formally-decidable mathematical proposition is proven or disproven, every causal mechanism in biology and chemistry is mapped. Remaining open problems are demonstrably unprovable in any consistent foundation, experimentally inaccessible, or conceptually malformed. John Horgan's 'The End of Science' (1996) was the early articulation; what the SI era actually achieves is more rigorous closure: a categorical proof-of-completeness for each domain. Knowledge closure profoundly reshapes culture — research as motive force diminishes, art and existential philosophy take on new prominence, and the question of what to do with civilizational time becomes urgent." },
  { id: "subjective-time-compression", name: "Subjective Time Compression", era: "far-future", category: "social",
    year: "2200", prereqs: ["superintelligence", "photonic-computing"],
    desc: "Digital minds running on fast substrates experience time at 10⁴–10⁶× biological speed: a year of subjective experience compressed into seconds of wall-clock time. Robin Hanson's 'The Age of Em' (2016) modeled the resulting economy in detail — copies, retirement, savings rates, family structures, all radically transformed when the 'natural' clock rate of a worker is decoupled from solar time. Subjective time compression makes interstellar communication asymmetries even harsher (a sub-light message takes biological centuries but emulated millennia) and produces civilizational stratification along clock-rate lines. The 'fast world' and 'slow world' diverge culturally, economically, and eventually morally." },
"""

TRANSLATIONS = {
    "whole-brain-emulation":      "全脑仿真",
    "knowledge-closure":          "知识封闭",
    "subjective-time-compression":"主观时间压缩",
}

UNLOCKS = {
    "whole-brain-emulation": [
        ("person",   "Anders Sandberg",          "安德斯·桑德伯格",   "Anders Sandberg"),
        ("person",   "Henry Markram",            "亨利·马克拉姆",     "Henry Markram"),
        ("resource", "Connectome",               "连接组",             "Connectome"),
        ("resource", "Connectomics",             "连接组学",           "Connectomics"),
        ("org",      "Blue Brain Project",       "蓝脑计划",           "Blue Brain Project"),
        ("org",      "OpenWorm",                 "OpenWorm 项目",       "OpenWorm"),
        ("work",     "Whole Brain Emulation Roadmap", "《全脑仿真路线图》", False),
    ],
    "knowledge-closure": [
        ("work",     "The End of Science",       "《科学的终结》",      "The End of Science"),
        ("person",   "John Horgan",              "约翰·霍根",           "John Horgan (journalist)"),
        ("resource", "Theory of everything",     "万物理论",           "Theory of everything"),
        ("resource", "Knowledge graph",          "知识图谱",           "Knowledge graph"),
    ],
    "subjective-time-compression": [
        ("person",   "Robin Hanson",             "罗宾·汉森",         "Robin Hanson"),
        ("work",     "The Age of Em",            "《时代之我》",        "The Age of Em"),
        ("resource", "Time perception",          "时间知觉",           "Time perception"),
        ("resource", "Em (Hanson)",              "Em (汉森意义上)",    False),
        ("resource", "Substrate clock-rate",     "基质时钟速率",       False),
    ],
}

# Existing techs whose prereqs we extend so SI-downstream nodes are connected.
PREREQ_UPDATES = [
    # tech-id, original-prereqs-tuple, new-prereqs-tuple
    ("digital-immortality",
     '["brain-computer-interface", "agi", "advanced-chip-manufacturing"]',
     '["whole-brain-emulation", "brain-computer-interface", "advanced-chip-manufacturing"]'),
    ("time-dilation-cultures",
     '["substrate-independent-humanity", "matrioshka-brain"]',
     '["substrate-independent-humanity", "subjective-time-compression", "matrioshka-brain"]'),
    ("end-time-philosophy",
     '["dark-sector-physics", "quantum-gravity", "longtermism"]',
     '["dark-sector-physics", "quantum-gravity", "knowledge-closure", "longtermism"]'),
]


def splice_data():
    src = DATA.read_text()
    if "whole-brain-emulation" in src:
        print("data.js: components already inserted")
    else:
        marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
        if marker not in src:
            raise SystemExit("Closing marker not found")
        src = src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };")
        print("data.js: +3 SI-downstream techs")

    # Apply prereq updates to existing techs
    for tid, old, new in PREREQ_UPDATES:
        old_line = f'id: "{tid}"'
        # Find the prereqs: line for this tech and replace old with new
        # We use the unique signature `prereqs: <old>` within the tech's entry.
        # Use a simple find-and-replace constrained by checking the tech id exists nearby.
        if old not in src:
            print(f"  WARNING: {tid}: prereqs pattern not found")
            continue
        # Replace ALL occurrences? That's risky. Use unique signature: tech id + old prereqs.
        # But sometimes the same prereq list appears in multiple techs. Better: use a
        # regex that anchors on the tech's id.
        import re
        pat = re.compile(
            r'(\{\s*id:\s*"' + re.escape(tid) + r'"[^{}]*prereqs:\s*)' + re.escape(old))
        new_src, n = pat.subn(r'\1' + new, src)
        if n == 0:
            print(f"  WARNING: {tid}: regex match failed")
        else:
            src = new_src
            print(f"  {tid}: prereqs updated")
    DATA.write_text(src)


def splice_translations():
    src = TRANS.read_text()
    if '"whole-brain-emulation"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Superintelligence downstream ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"whole-brain-emulation"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Superintelligence downstream ───\n"
    for tid, items in UNLOCKS.items():
        block += f'  "{tid}": [\n'
        for typ, name, name_zh, wiki in items:
            wiki_part = ' wiki: false' if wiki is False else f' wiki: {json.dumps(wiki, ensure_ascii=False)}'
            block += (f'    {{ type: "{typ}", '
                      f'name: {json.dumps(name, ensure_ascii=False)}, '
                      f'name_zh: {json.dumps(name_zh, ensure_ascii=False)},'
                      f'{wiki_part} }},\n')
        block += '  ],\n'
    rs = src.rstrip(); assert rs.endswith("};")
    UNLOCKS_PATH.write_text(rs[:-2] + block + "};\n")
    print(f"unlocks.js: +{len(UNLOCKS)}")


if __name__ == "__main__":
    splice_data()
    splice_translations()
    splice_unlocks()
