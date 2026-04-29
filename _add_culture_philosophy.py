#!/usr/bin/env python3
"""Add 11 cultural / philosophy / sociology techs spanning Modern → Far Future."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Culture / Philosophy / Sociology ───
  { id: "bauhaus", name: "Bauhaus", era: "modern", category: "social",
    year: "1919", prereqs: ["factory-system", "photography"],
    desc: "Walter Gropius's Bauhaus school (Weimar 1919, Dessau 1925, Berlin 1932) integrated fine art, craft, and industrial design under a single curriculum. Faculty included Paul Klee, Wassily Kandinsky, László Moholy-Nagy, Marcel Breuer, and Mies van der Rohe. Bauhaus pedagogy — preliminary course (Vorkurs), workshop training, mass-production aesthetics — established 'form follows function' modernism as the dominant 20th-century design philosophy. The Nazis closed the school in 1933; faculty diaspora carried the principles to Black Mountain College, the Chicago New Bauhaus (IIT), Harvard, and the Ulm school. Modern furniture, typography, architecture, and graphic design all descend from this fifteen-year experiment." },
  { id: "frankfurt-school", name: "Frankfurt School", era: "modern", category: "social",
    year: "1923", prereqs: ["labor-union", "public-education"],
    desc: "The Institute for Social Research (Frankfurt, 1923) brought together Theodor Adorno, Max Horkheimer, Herbert Marcuse, Walter Benjamin, Erich Fromm, and Jürgen Habermas around a Marxist-Freudian critique of industrial mass culture. Their 'Critical Theory' analyzed how the culture industry, instrumental reason, and authoritarian personality structures sustain capitalism even when it harms workers. Forced into U.S. exile by Nazi rise (Columbia, 1934), they shaped postwar American sociology and 1960s student movements. Habermas's later communicative-action theory (1981) extended the program into deliberative democratic theory." },
  { id: "universal-human-rights", name: "Universal Human Rights", era: "atomic", category: "social",
    year: "1948", prereqs: ["liberal-democracy", "womens-suffrage"],
    desc: "The UN Universal Declaration of Human Rights (December 10, 1948), drafted under Eleanor Roosevelt's chairmanship and adopted with no opposing votes. Thirty articles articulating civil, political, economic, social, and cultural rights as universal — independent of state, religion, or culture. The Declaration produced the binding 1966 Covenants, the Helsinki Accords (1975), the European Convention machinery, and the eventual ICC (2002). Real enforcement remains uneven and contested — sovereign noncompliance, cultural relativism critiques, selective Western application — but human-rights discourse has structured every postwar legitimacy claim, from anticolonial movements to dissident cases inside both Communist and capitalist regimes." },
  { id: "cybernetics", name: "Cybernetics", era: "atomic", category: "knowledge",
    year: "1948", prereqs: ["digital-computer", "mathematics-arithmetic"],
    desc: "Norbert Wiener's 1948 'Cybernetics: Or Control and Communication in the Animal and the Machine' synthesized feedback control theory, information theory, and biological homeostasis into a unified framework. Macy Conferences (1946–1953) gathered Wiener, Claude Shannon, John von Neumann, Warren McCulloch, Margaret Mead, and Gregory Bateson around the program. Cybernetics directly produced control engineering, computer science (von Neumann architecture as cybernetic system), early AI research, family-systems therapy, and the systems-theoretic turn in sociology. Stafford Beer's Cybersyn (Chile 1971) was the most ambitious cybernetic state-management experiment; Norbert Wiener's later 'God and Golem' (1964) anticipated the AI alignment problem." },
  { id: "neoliberalism", name: "Neoliberalism", era: "information", category: "economy",
    year: "1980", prereqs: ["liberal-democracy", "modern-corporation"],
    desc: "The political-economic paradigm of Reagan, Thatcher, and the Washington Consensus: market deregulation, privatization, free trade, capital-flow liberalization, and rolling-back of welfare-state provisions. Theoretical roots trace to the Mont Pelerin Society (Hayek, Friedman, 1947) and Chicago School economics. The IMF's structural adjustment programs (1980s) propagated the model globally; the 1989 fall of the Soviet bloc and 'End of History' (Fukuyama 1992) seemed to vindicate it. Critiques range from inequality (Piketty 2013, Stiglitz) to deindustrialization to financialization. The 2008 financial crisis and 2010s populist backlash signaled the model's unraveling without producing a clear successor." },
  { id: "degrowth-economics", name: "Degrowth Economics", era: "future", category: "economy",
    year: "2035", prereqs: ["climate-science", "renewable-grid"],
    desc: "A planned economic contraction of high-income countries' material throughput, on grounds that biophysical limits make perpetual growth ecologically impossible. Roots in Herman Daly's steady-state economics (1977), Nicholas Georgescu-Roegen's bioeconomics, and André Gorz (1972 — first to use 'décroissance'). Jason Hickel's *Less Is More* (2020) and Kate Raworth's Doughnut Economics (2017) brought it into mainstream policy debate. Degrowth advocates work-time reduction, public-service expansion, decommodification of essentials, and bans on planned obsolescence. Critics (including most mainstream economists) argue it cannot deliver on poverty alleviation; advocates respond that growth-as-currently-defined is what's incompatible with planetary limits." },
  { id: "solarpunk", name: "Solarpunk", era: "future", category: "social",
    year: "2030", prereqs: ["renewable-grid", "climate-science"],
    desc: "An optimistic ecological-technological aesthetic and political imaginary, defined in deliberate contrast to cyberpunk dystopia. Originated in a 2008 blog post and codified through anthologies (*Solarpunk: Ecological and Fantastical Stories*, 2018). Core motifs: photovoltaic-integrated architecture, public-transit cities, urban agriculture, decentralized energy, restored ecosystems, multi-cultural communities, art-nouveau aesthetics. Functions as both fictional genre and template for actual policy advocacy — climate-positive futures that aren't either austere apocalypse or technocratic singularity. Influences architecture (NEOM, Masdar City), animation (Studio Ghibli's later films), and climate-movement framing (Sunrise Movement)." },
  { id: "constructed-religions", name: "Constructed Religions", era: "far-future", category: "social",
    year: "2300", prereqs: ["longtermism", "transhumanism"],
    desc: "Engineered spiritual systems designed for posthuman conditions — millennium-scale lifespans, digital-substrate consciousness, mass speciation. Earlier precursors include 19th-century Auguste Comte's positivist 'religion of humanity', Bahá'í universalist project, and 20th-century engineered religions like Scientology and Raëlism. Posthuman-condition religions address questions baseline traditions weren't built for: meaning under unbounded life, ritual across light-year communications gaps, sacred meaning of ancestral biological humanity, ethics of running multiple instances of one mind. Some are open systems revised iteratively; others claim ahistorical authority. Their architects are explicit about constructing them rather than receiving them." },
  { id: "substrate-pluralism", name: "Substrate Pluralism", era: "far-future", category: "social",
    year: "2350", prereqs: ["substrate-independent-humanity", "universal-sentient-rights"],
    desc: "The formal social philosophy of multi-substrate civilization: legal, ethical, and cultural frameworks for societies in which biological humans, digital minds, hybrid cyborgs, engineered organisms, and emergent AGI substrates coexist as full members. Earlier work — David Chalmers on substrate-independence, Susan Schneider on machine consciousness, Eric Schwitzgebel on group minds — laid foundations. Mature substrate pluralism handles voting weight across short- and long-lived minds, citizenship across instances and forks, intellectual-property claims across substrate copies, and the legitimacy of substrate-specific subcultures. The political settlement is fragile and recurringly contested; substrate-chauvinist movements (biological supremacism, digital purism) recur as serious political forces." },
  { id: "galactic-citizenship", name: "Galactic Citizenship", era: "far-future", category: "social",
    year: "2400", prereqs: ["universal-sentient-rights", "interstellar-treaty"],
    desc: "Legal and moral framework articulating rights, obligations, and standing of any sentient being across the colonized galaxy — independent of star system, planet, biological species, or substrate. Builds on the universal-sentient-rights tradition (2200), adapted for light-year separations: distributed jurisdiction, asynchronous adjudication, rights enforcement across communications gaps centuries long. Earlier multinational citizenship analogues (EU passports, UN treaties) are too small-scale to inform the design directly. Some polities accept galactic citizenship as supervening over local law; others operate it only as treaty-level mutual recognition. The philosophical question — what makes a being eligible — remains permanently open as new substrates emerge." },
  { id: "speciation-ethics", name: "Speciation Ethics", era: "far-future", category: "social",
    year: "2400", prereqs: ["substrate-independent-humanity", "universal-sentient-rights"],
    desc: "Moral philosophy addressing what diverged posthuman branches owe each other once they have become genuinely distinct species — biologically, cognitively, or substrate-wise. Earlier ethical frameworks assumed a unified human moral community; once that assumption collapses, fundamental questions emerge: do branches have positive duties of mutual support, or only negative duties of non-aggression? Are merging or unmerging branches a moral wrong? What of branches that no longer recognize each other as morally significant? Olaf Stapledon's *Last and First Men* (1930) and *Star Maker* (1937) anticipated the questions; serious operational ethics emerges only once speciation is actually happening." },
"""

TRANSLATIONS = {
    "bauhaus":                 "包豪斯",
    "frankfurt-school":        "法兰克福学派",
    "universal-human-rights":  "普世人权",
    "cybernetics":             "控制论",
    "neoliberalism":           "新自由主义",
    "degrowth-economics":      "去增长经济学",
    "solarpunk":               "太阳朋克",
    "constructed-religions":   "构造性宗教",
    "substrate-pluralism":     "基质多元主义",
    "galactic-citizenship":    "银河公民身份",
    "speciation-ethics":       "物种分化伦理学",
}

UNLOCKS = {
    "bauhaus": [
        ("person",   "Walter Gropius",       "瓦尔特·格罗皮乌斯",   "Walter Gropius"),
        ("person",   "László Moholy-Nagy",   "拉斯洛·莫霍利-纳吉", "László Moholy-Nagy"),
        ("person",   "Mies van der Rohe",    "密斯·凡·德罗",        "Ludwig Mies van der Rohe"),
        ("work",     "Bauhaus Manifesto",    "《包豪斯宣言》",        "Bauhaus"),
        ("unit",     "Wassily Chair",        "瓦西里椅",              "Wassily Chair"),
        ("org",      "Bauhaus-Universität Weimar", "魏玛包豪斯大学",  "Bauhaus-Universität Weimar"),
    ],
    "frankfurt-school": [
        ("person",   "Theodor Adorno",       "西奥多·阿多诺",       "Theodor W. Adorno"),
        ("person",   "Max Horkheimer",       "马克斯·霍克海默",     "Max Horkheimer"),
        ("person",   "Herbert Marcuse",      "赫伯特·马尔库塞",     "Herbert Marcuse"),
        ("person",   "Walter Benjamin",      "瓦尔特·本雅明",       "Walter Benjamin"),
        ("person",   "Jürgen Habermas",      "于尔根·哈贝马斯",     "Jürgen Habermas"),
        ("work",     "Dialectic of Enlightenment", "《启蒙辩证法》",  "Dialectic of Enlightenment"),
        ("org",      "Institute for Social Research", "社会研究所",   "Institute for Social Research"),
    ],
    "universal-human-rights": [
        ("work",     "Universal Declaration of Human Rights", "《世界人权宣言》", "Universal Declaration of Human Rights"),
        ("person",   "Eleanor Roosevelt",    "埃莉诺·罗斯福",       "Eleanor Roosevelt"),
        ("org",      "United Nations Human Rights Commission", "联合国人权委员会", "United Nations Commission on Human Rights"),
        ("work",     "International Covenant on Civil and Political Rights", "《公民权利和政治权利国际公约》", "International Covenant on Civil and Political Rights"),
        ("org",      "Amnesty International", "国际特赦组织",         "Amnesty International"),
    ],
    "cybernetics": [
        ("person",   "Norbert Wiener",       "诺伯特·维纳",         "Norbert Wiener"),
        ("person",   "Claude Shannon",       "克劳德·香农",         "Claude Shannon"),
        ("work",     "Cybernetics: or Control and Communication in the Animal and the Machine", "《控制论》", "Cybernetics: Or Control and Communication in the Animal and the Machine"),
        ("org",      "Macy Conferences",     "梅西会议",             "Macy conferences"),
        ("unit",     "Project Cybersyn",     "赛博协同工程",         "Project Cybersyn"),
    ],
    "neoliberalism": [
        ("person",   "Milton Friedman",      "米尔顿·弗里德曼",     "Milton Friedman"),
        ("person",   "Friedrich Hayek",      "弗里德里希·哈耶克",   "Friedrich Hayek"),
        ("person",   "Margaret Thatcher",    "玛格丽特·撒切尔",     "Margaret Thatcher"),
        ("person",   "Ronald Reagan",        "罗纳德·里根",         "Ronald Reagan"),
        ("work",     "Capitalism and Freedom", "《资本主义与自由》",  "Capitalism and Freedom"),
        ("org",      "Mont Pelerin Society", "朝圣山学社",           "Mont Pelerin Society"),
        ("resource", "Washington Consensus", "华盛顿共识",           "Washington Consensus"),
    ],
    "degrowth-economics": [
        ("person",   "Herman Daly",          "赫尔曼·戴利",         "Herman Daly"),
        ("person",   "Nicholas Georgescu-Roegen", "尼古拉斯·乔治斯库-罗根", "Nicholas Georgescu-Roegen"),
        ("person",   "Jason Hickel",         "贾森·希克尔",         "Jason Hickel"),
        ("work",     "Less Is More",         "《少即是多》",         "Jason Hickel"),
        ("work",     "Doughnut Economics",   "《甜甜圈经济学》",     "Doughnut (economic model)"),
        ("resource", "Steady-state economy", "稳态经济",             "Steady-state economy"),
    ],
    "solarpunk": [
        ("resource", "Solarpunk aesthetic",  "太阳朋克美学",         "Solarpunk"),
        ("work",     "Solarpunk: Ecological and Fantastical Stories", "《太阳朋克:生态与奇幻故事集》", "Solarpunk"),
        ("unit",     "Photovoltaic façade",  "光伏外立面",           "Photovoltaics"),
        ("org",      "Sunrise Movement",     "日出运动",             "Sunrise Movement"),
    ],
    "constructed-religions": [
        ("resource", "Religion of Humanity", "人性宗教",             "Religion of Humanity"),
        ("org",      "Bahá'í Faith",         "巴哈伊信仰",           "Bahá'í Faith"),
        ("resource", "New religious movement", "新兴宗教运动",       "New religious movement"),
        ("work",     "Posthuman liturgy",    "后人类礼仪",           False),
    ],
    "substrate-pluralism": [
        ("person",   "David Chalmers",       "大卫·查尔默斯",       "David Chalmers"),
        ("person",   "Susan Schneider",      "苏珊·施奈德",         "Susan Schneider (philosopher)"),
        ("resource", "Substrate independence", "基质独立性",         "Substrate independence"),
        ("work",     "Substrate-pluralism charter", "基质多元主义宪章", False),
    ],
    "galactic-citizenship": [
        ("resource", "Cosmopolitanism",      "世界主义",             "Cosmopolitanism"),
        ("work",     "Galactic Constitution","《银河宪法》",         False),
        ("org",      "Pan-Galactic Civic Tribunal", "泛银河公民法庭", False),
    ],
    "speciation-ethics": [
        ("work",     "Last and First Men",   "《最后和最初的人》",   "Last and First Men"),
        ("work",     "Star Maker",           "《造星者》",           "Star Maker (novel)"),
        ("resource", "Posthuman speciation", "后人类物种分化",       "Speciation"),
        ("work",     "Inter-species moral covenant", "种间道德盟约", False),
    ],
}


def splice_data():
    src = DATA.read_text()
    if "frankfurt-school" in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} culture/philosophy techs")


def splice_translations():
    src = TRANS.read_text()
    if '"frankfurt-school"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Culture / Philosophy / Sociology ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"frankfurt-school"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Culture / Philosophy / Sociology ───\n"
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
