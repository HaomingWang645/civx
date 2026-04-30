#!/usr/bin/env python3
"""Add 6 math techs:
  Near Future: univalent-foundations, langlands-program-completion
  Far Future:  beyond-zfc-foundations, continuum-hypothesis-resolution,
               hypercomputation, trans-computable-mathematics
"""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Mathematics frontier (near + far future) ───
  { id: "univalent-foundations", name: "Univalent Foundations", era: "future", category: "knowledge",
    year: "2050", prereqs: ["formal-mathematics", "agi"],
    desc: "Vladimir Voevodsky's program (~2009) reformulating mathematics on Homotopy Type Theory rather than Zermelo-Fraenkel set theory: types are interpreted as homotopy types, equivalent structures are formally identified (the univalence axiom), and proof-relevance is built in. By the 2050s, machine-verified mathematics has migrated to univalent foundations as the working substrate for new theorems — the Coq, Lean, and successor proof assistants run natively on HoTT semantics. The shift consolidates a century of category-theoretic development and makes computer-verified mathematics genuinely productive at research frontiers, not just for verifying old results." },
  { id: "langlands-program-completion", name: "Langlands Program Completion", era: "future", category: "knowledge",
    year: "2090", prereqs: ["formal-mathematics", "agi"],
    desc: "Robert Langlands's 1967 letter to André Weil sketched a vast network of conjectures connecting number theory, representation theory, and harmonic analysis — the most ambitious unification program in modern mathematics. Andrew Wiles's 1995 proof of Fermat's Last Theorem solved a Langlands case (modularity for elliptic curves); Peter Scholze's perfectoid spaces (2011) and the geometric Langlands correspondence advances of the 2020s opened the path forward. By the 2090s, AI-assisted theorem provers and decades of Fields-medal-class human work have closed the program — every major Langlands conjecture has either been proven or shown false, with profound implications for arithmetic, automorphic forms, and quantum field theory." },
  { id: "beyond-zfc-foundations", name: "Beyond-ZFC Foundations", era: "far-future", category: "knowledge",
    year: "2200", prereqs: ["univalent-foundations", "superintelligence"],
    desc: "Mathematical foundations beyond Zermelo-Fraenkel set theory with Choice (ZFC, dominant since ~1925) become primary for ongoing research. Candidates include univalent foundations (HoTT, already established), constructive set theories (CZF), New Foundations (Quine), Tarski-Grothendieck, and proposals from large-cardinal hierarchies. The shift is partly driven by the limitations ZFC reveals at very large cardinals, partly by the ergonomic advantages of structural foundations for computer-assisted mathematics. ZFC continues to be taught for historical/pedagogical reasons but is no longer the lingua franca; multiple foundations coexist with translation theorems linking them." },
  { id: "continuum-hypothesis-resolution", name: "Continuum Hypothesis Resolution", era: "far-future", category: "knowledge",
    year: "2250", prereqs: ["beyond-zfc-foundations", "agi"],
    desc: "Cantor's 1878 question — is there a set whose cardinality lies strictly between |ℕ| and |ℝ|? — was shown by Gödel (1940) and Cohen (1963) to be independent of ZFC: it can be assumed true or false without contradiction. By 2250, mathematics' Beyond-ZFC pluralism produces a posthuman consensus on which axiom extension to canonize as 'standard': forcing axioms (Martin's Maximum, MM⁺⁺) become widely adopted, settling CH negatively. The resolution isn't a proof in ZFC but a decision about the foundations themselves — completing a 350-year debate about the nature of mathematical truth and what it means for a question to have an answer." },
  { id: "hypercomputation", name: "Hypercomputation", era: "far-future", category: "knowledge",
    year: "2400", prereqs: ["superintelligence", "p-vs-np-resolved"],
    desc: "Engineered systems performing operations beyond the Turing-computable: oracle queries to undecidable problems, infinite-time computation in finite physical time, hyperarithmetical functions evaluated in bounded resource budgets. Theoretical proposals include Zeno machines (each step takes half the previous time), Malament-Hogarth spacetimes near rotating black holes (where infinite proper time fits inside finite observer-frame time), and quantum oracle constructions. Whether physical hypercomputation is achievable depends on unresolved questions in quantum gravity and the structure of physical law. If it is, the boundary between mathematics and physics shifts: previously uncomputable functions become computable, and entire branches of math become accessible to direct evaluation." },
  { id: "trans-computable-mathematics", name: "Trans-Computable Mathematics", era: "far-future", category: "knowledge",
    year: "2500", prereqs: ["hypercomputation", "beyond-zfc-foundations"],
    desc: "Mathematics that operates with provably uncomputable objects as primary research material: explicit bounds on busy-beaver values up to large indices, direct construction of Π¹ₙ-complete sets, Chaitin's Ω engineered to specified precision. Earlier mathematics could refer to such objects only abstractly (proving them to exist); trans-computable mathematics, enabled by hypercomputation hardware, manipulates them concretely. The arithmetical hierarchy collapses below the new threshold of practical computation. Open problems that were 'merely uncomputable' are now routine; new open problems arise at higher levels (Δ¹ⱼ, indescribable cardinals, the structure of the constructible universe at large ordinals)." },
"""

TRANSLATIONS = {
    "univalent-foundations":          "一价基础",
    "langlands-program-completion":   "朗兰兹纲领完成",
    "beyond-zfc-foundations":         "超 ZFC 基础",
    "continuum-hypothesis-resolution":"连续统假设解决",
    "hypercomputation":               "超图灵计算",
    "trans-computable-mathematics":   "超可计算数学",
}

UNLOCKS = {
    "univalent-foundations": [
        ("person",   "Vladimir Voevodsky",       "弗拉基米尔·沃埃沃德斯基", "Vladimir Voevodsky"),
        ("resource", "Homotopy type theory",     "同伦类型论",             "Homotopy type theory"),
        ("resource", "Univalence axiom",         "一价公理",               "Univalent foundations"),
        ("unit",     "Coq",                      "Coq 证明助手",           "Coq (software)"),
        ("unit",     "Lean theorem prover",      "Lean 定理证明器",        "Lean (proof assistant)"),
    ],
    "langlands-program-completion": [
        ("person",   "Robert Langlands",         "罗伯特·朗兰兹",         "Robert Langlands"),
        ("person",   "Andrew Wiles",             "安德鲁·怀尔斯",         "Andrew Wiles"),
        ("person",   "Peter Scholze",            "彼得·朔尔策",           "Peter Scholze"),
        ("resource", "Langlands program",        "朗兰兹纲领",             "Langlands program"),
        ("resource", "Geometric Langlands",      "几何朗兰兹对应",         "Geometric Langlands correspondence"),
        ("resource", "Perfectoid space",         "完美空间",               "Perfectoid space"),
    ],
    "beyond-zfc-foundations": [
        ("resource", "Zermelo–Fraenkel set theory", "策梅洛-弗兰克尔集合论", "Zermelo–Fraenkel set theory"),
        ("resource", "Constructive set theory",  "构造性集合论",           "Constructive set theory"),
        ("resource", "New Foundations",          "新基础",                 "New Foundations"),
        ("resource", "Tarski–Grothendieck set theory", "塔斯基-格罗滕迪克集合论", "Tarski–Grothendieck set theory"),
        ("person",   "Saharon Shelah",           "萨哈龙·谢拉",            "Saharon Shelah"),
    ],
    "continuum-hypothesis-resolution": [
        ("resource", "Continuum hypothesis",     "连续统假设",             "Continuum hypothesis"),
        ("person",   "Kurt Gödel",               "库尔特·哥德尔",          "Kurt Gödel"),
        ("person",   "Paul Cohen",               "保罗·科恩",              "Paul Cohen"),
        ("resource", "Forcing",                  "力迫法",                 "Forcing (mathematics)"),
        ("resource", "Martin's Maximum",         "马丁极大原理",            "Martin's maximum"),
        ("resource", "Large cardinal",           "大基数",                 "Large cardinal"),
    ],
    "hypercomputation": [
        ("resource", "Hypercomputation",         "超计算",                 "Hypercomputation"),
        ("resource", "Oracle machine",           "神谕机器",               "Oracle machine"),
        ("resource", "Zeno machine",             "芝诺机",                 "Zeno machine"),
        ("resource", "Malament–Hogarth spacetime", "马拉门-霍加思时空",     "Malament–Hogarth spacetime"),
        ("resource", "Halting problem",          "停机问题",               "Halting problem"),
    ],
    "trans-computable-mathematics": [
        ("resource", "Busy beaver function",     "繁忙的海狸函数",         "Busy beaver"),
        ("resource", "Chaitin's constant",       "蔡廷常数",               "Chaitin's constant"),
        ("resource", "Arithmetical hierarchy",   "算术层次",               "Arithmetical hierarchy"),
        ("resource", "Constructible universe",   "可构造宇宙",             "Constructible universe"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "univalent-foundations" in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} math techs")


def splice_translations():
    src = TRANS.read_text()
    if '"univalent-foundations"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Mathematics frontier ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"univalent-foundations"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Mathematics frontier ───\n"
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
