#!/usr/bin/env python3
"""Add 16 subsistence / agriculture techs filling era gaps."""

import json
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
UNLOCKS_PATH = ROOT / "unlocks.js"

NEW_BLOCK = """
  // ─── Subsistence & agriculture (gap fill) ───
  { id: "food-preservation", name: "Food Preservation", era: "upper-paleo", category: "subsistence",
    year: "~25 kya", prereqs: ["cooking", "fire-making"],
    desc: "Smoking, drying, salting, and fermenting techniques that extend perishable food beyond a few days. Smoked salmon caches in Ice-Age Siberia and dried meat (jerky) of mammoth-hunting peoples are the earliest evidence; the same principles underpin pemmican, biltong, jamón, prosciutto, gravlax, kimchi, and miso. Preservation transforms the seasonal feast-and-famine cycle into a continuous food supply, supporting larger group sizes, longer winters in temperate zones, and the surplus needed for sedentism. Without it, no Neolithic agricultural transition is possible." },
  { id: "beekeeping", name: "Beekeeping", era: "bronze", category: "subsistence",
    year: "~3000 BCE", prereqs: ["pottery", "village"],
    desc: "Managed honeybee (Apis mellifera) hives in pottery, woven straw skeps, or hollow logs. Egyptian apiaries (~2400 BCE) used cylindrical clay hives stacked in groves; Hittite and Greek records (Hesiod) document the practice. Honey was the primary sweetener of antiquity, the key fermentation sugar for mead, and a wound antiseptic. Beeswax provided candles, sealing, lost-wax casting media, and writing tablets. The first managed insect domestication; the practice survives largely unchanged in artisan apiaries today, though commercial pollination services (Apis + bumblebees) now drive a global $200+ billion industry tied to almond, blueberry, and orchard agriculture." },
  { id: "cheese-dairy-processing", name: "Cheese & Dairy Processing", era: "bronze", category: "subsistence",
    year: "~3000 BCE", prereqs: ["animal-domestication", "pottery"],
    desc: "Conversion of perishable milk into shelf-stable products through curdling, draining, salting, and aging: butter, yogurt, cheese in dozens of regional varieties. Earliest evidence — milk-fat residues in pottery sieves at Polish Linear Pottery sites (~5500 BCE), confirmed cheese at Kuyavia (~5500 BCE). Rennet (calf-stomach enzyme) curdles casein proteins into solid curd; salt and aging shape the final product. Dairy processing made nomadic pastoralism viable (lactose-tolerance evolution swept Europe in <5000 years) and gave settled agrarian societies a calorie-dense, transportable food. Modern industrial dairying produces ~700 million tonnes of milk annually." },
  { id: "salt-production", name: "Salt Production", era: "bronze", category: "subsistence",
    year: "~3000 BCE", prereqs: ["pottery", "fire-making"],
    desc: "Rock-salt mining (Hallstatt, Austria, ~1200 BCE; Roman salinarum) and brine evaporation in pottery vessels or open pans (Halle in Germany, Sichuan in China). Salt was the only food preservative besides drying available before refrigeration: salt pork, salt cod, salt fish, salted vegetables formed the protein and vitamin reservoir of every pre-modern population through winter. Salt taxes (gabelle in France, Roman annona) financed governments; the Latin 'salarium' (salary) was salt money paid to soldiers. Trans-Saharan salt routes traded salt for gold one-for-one. Industrialization eventually made salt cheap enough to disappear as an economic factor, but the geography of pre-modern civilization tracks salt sources closely." },
  { id: "latifundia", name: "Latifundia", era: "classical", category: "subsistence",
    year: "~200 BCE", prereqs: ["empire", "plow-ard"],
    desc: "Roman large-scale agricultural estates (typically 1,000–10,000 hectares) worked primarily by enslaved labor and producing grain, olive oil, wine, and livestock for the Mediterranean market. The Punic Wars (264–146 BCE) flooded Rome with slaves and bankrupted small farmers; their plots consolidated into latifundia owned by Senatorial elites. Cato's *De Agricultura* (~160 BCE) and Varro's *Rerum Rusticarum* (~37 BCE) document the management practices. The Roman grain trade — North African and Egyptian wheat shipped to feed the city of Rome's million inhabitants — was the first integrated long-distance food market. Latifundia patterns recur in every later large-estate slave economy: Brazilian sugar, U.S. South cotton, Spanish American haciendas." },
  { id: "sugar-plantation", name: "Sugar Plantation", era: "renaissance", category: "subsistence",
    year: "1500", prereqs: ["colonialism", "columbian-exchange"],
    desc: "Caribbean and Brazilian plantation system producing sugar from sugarcane (originally from Southeast Asia, brought by Columbus on his second voyage 1493). The first integrated agro-industrial process: cane cultivation, harvest, milling, boiling, crystallization, and shipping all on a single estate. Hispaniola, Cuba, Barbados, and Brazil became sugar economies by 1600; Saint-Domingue (Haiti) was the world's largest sugar producer by 1789. The plantation system industrialized slavery — ~12 million enslaved Africans were transported to the Americas, the majority to sugar plantations. Sugar's calorie cheapness drove Atlantic-trade wealth into European cities, structured the Triangle Trade, and remained the model for later cash-crop colonial economies." },
  { id: "canning", name: "Canning & Tinned Food", era: "industrial", category: "subsistence",
    year: "1810", prereqs: ["chemistry-modern", "factory-system"],
    desc: "Nicolas Appert's heat-processing of food in glass jars (1810, prize-winning method commissioned by Napoleon to feed his armies); Bryan Donkin's tin-plated steel cans (1813) commercialized the process. Pasteur (1864) supplied the bacteriological understanding 50 years later. Canned food fed Napoleonic and Civil War armies, fueled Arctic exploration (with disastrous lead-soldering side effects), and stocked 19th-century city pantries. By the late 1800s canned tomatoes, fish, milk, and vegetables had transformed working-class diets and decoupled urban populations from local seasonal agriculture. Modern canning (and parallel inventions: Mason jar 1858, retort processing) underpins global food trade." },
  { id: "mechanical-reaper", name: "Mechanical Reaper", era: "industrial", category: "subsistence",
    year: "1831", prereqs: ["machine-tool", "agricultural-revolution"],
    desc: "Cyrus McCormick's horse-drawn reaper (Virginia, 1831) cut grain stalks via reciprocating saw-tooth blade, depositing the crop in windrows for hand-binding. By the 1850s the McCormick Reaper Works in Chicago was producing tens of thousands of units annually; the reaper-binder (1872) added automated binding; the combine harvester (1880s onward) integrated cutting, threshing, and cleaning. Mechanization collapsed the labor cost of grain harvest from 56 hours per acre (hand reaping) to <5 hours (combine), opening prairie agriculture, freeing farm workers for industrial cities, and integrating American grain into the global market alongside Russian and Australian wheat exports." },
  { id: "pasteurization", name: "Pasteurization", era: "industrial", category: "subsistence",
    year: "1864", prereqs: ["germ-theory", "chemistry-modern"],
    desc: "Louis Pasteur's 1864 demonstration that mild heating (60–70 °C, brief duration) kills the microorganisms responsible for milk and beer spoilage without significantly altering taste. Initially saving the French wine industry from contamination, the technique was extended to beer (1876) and milk (1880s+). Compulsory milk pasteurization (Chicago 1908, UK 1949 for milk supplied to schools) eliminated milk-borne tuberculosis, brucellosis, and typhoid as childhood killers. The process was the first practical application of germ theory and made urban milk supply safe at industrial scale, enabling the modern dairy industry. Modern variants — UHT (ultra-high temperature, 1948), HTST (high-temperature short-time, 1893) — extend shelf life from days to months." },
  { id: "refrigerated-transport", name: "Refrigerated Transport", era: "industrial", category: "subsistence",
    year: "1880", prereqs: ["railroad-network", "chemistry-modern"],
    desc: "Refrigerated rail cars (Gustavus Swift's Chicago meatpacking, 1878+) and refrigerated steamships (SS Strathleven from Australia to London, 1880, first frozen-meat shipment) enabled long-distance perishable food trade. Within a generation, Chicago became the world's meatpacking capital; Argentine and Australian beef + lamb undercut British domestic agriculture; Boston and New York supplied Florida oranges year-round. The cold chain — refrigerated storage at every stage from farm to plate — became the substrate of modern food economy. Refrigerants evolved: ammonia (1850s), CFCs (1928, ozone-destroying, banned 1987 Montreal Protocol), HFCs (1990s), now CO₂ and natural refrigerants for climate compatibility." },
  { id: "tractor", name: "Tractor", era: "modern", category: "subsistence",
    year: "1917", prereqs: ["internal-combustion", "automobile"],
    desc: "Henry Ford's Fordson Model F (1917) — first mass-produced gasoline-powered tractor, designed for family farms (~$395, half the price of competitors). Replaced draft horses and oxen for plowing, planting, and harvest, freeing the ~25% of US farmland used to grow horse fodder for human food production. Crawler tractors (Holt 1904, later Caterpillar) extended the form to heavy soils and forestry. Diesel tractors (1932 Caterpillar) became the standard. Mechanization combined with synthetic fertilizer (Haber-Bosch) and hybrid corn collapsed the labor share of agriculture from ~50% of the US workforce in 1900 to <2% today, with proportionate increases in per-farmer output." },
  { id: "synthetic-pesticides", name: "Synthetic Pesticides", era: "modern", category: "subsistence",
    year: "1939", prereqs: ["chemistry-modern", "plastic-polymer"],
    desc: "DDT (Paul Müller, Geigy 1939, Nobel 1948) was the first synthetic chlorinated hydrocarbon insecticide — cheap, persistent, broad-spectrum, and (it seemed) miraculously effective. WHO malaria-eradication campaigns saved tens of millions of lives in the 1950s; agricultural use eliminated countless crop pests. Rachel Carson's *Silent Spring* (1962) documented the ecological costs (bioaccumulation, bird-egg thinning, resistance evolution); DDT was banned for agricultural use in the US (1972) and Stockholm-Convention-restricted globally (2001) for all but vector control. Successor families (organophosphates, pyrethroids, neonicotinoids, glyphosate) continued the trajectory of higher specificity at higher costs and ongoing controversy over pollinator collapse and farmworker exposure." },
  { id: "industrial-aquaculture", name: "Industrial Aquaculture", era: "atomic", category: "subsistence",
    year: "1965", prereqs: ["animal-domestication", "plastic-polymer"],
    desc: "Large-scale fish farming using cages, raceways, and recirculating systems: Norwegian salmon (1970s), Thai shrimp (1980s), Chinese carp (continuous since antiquity but industrialized post-1960). By 2020, aquaculture production exceeded wild-caught fish for the first time (~85 million tonnes farmed vs ~80 million tonnes wild). The industry made fish a cheap, year-round protein staple in many countries while raising problems wild fisheries don't have: antibiotic resistance, escapee genetic pollution of wild stocks, fishmeal demand pressuring lower-trophic-level wild species, and concentrated environmental impact in coastal embayments. Shrimp aquaculture in particular drove tropical mangrove destruction at scale comparable to Amazon deforestation." },
  { id: "frozen-food-supply-chain", name: "Frozen Food Supply Chain", era: "atomic", category: "subsistence",
    year: "1950", prereqs: ["refrigerated-transport", "air-conditioning"],
    desc: "Clarence Birdseye's flash-freezing technique (commercialized 1930) preserved food quality far better than slow freezing; postwar suburban supermarkets (1947+) and home freezers (~1950) closed the cold chain from factory to family freezer. By 1955, frozen TV dinners (Swanson) institutionalized the form; frozen pizza, ice cream, peas, and concentrated orange juice became American staples. The cold chain enabled global frozen-food trade — Argentine beef, New Zealand lamb, Alaskan salmon, Vietnamese shrimp all shipped frozen to distant markets. Cold-chain energy use accounts for ~3-5% of global electricity demand and ~2% of greenhouse-gas emissions, with steadily rising demand from emerging markets." },
  { id: "gmo", name: "Genetic Modification", era: "information", category: "subsistence",
    year: "1996", prereqs: ["genetic-engineering", "green-revolution"],
    desc: "First commercial transgenic crops: Calgene's FlavrSavr tomato (1994, delayed ripening) and Monsanto's Roundup Ready soybean (1996, glyphosate resistance). Bt corn and cotton (Bacillus thuringiensis insecticidal genes) followed. By 2020, ~190 million hectares globally are planted with GM crops — primarily soy, corn, cotton, and canola; primarily in the US, Brazil, Argentina, India, Canada. GMOs delivered measurable yield improvements and pesticide reductions (Bt) but became politically toxic in Europe and adjacent regions; the regulatory split between countries persists. CRISPR-edited crops (2010s+) are typically classified differently than transgenic GM, sometimes escaping the GMO regulatory regime entirely." },
  { id: "vertical-farming", name: "Vertical Farming", era: "information", category: "subsistence",
    year: "2000", prereqs: ["solar-photovoltaic", "gmo"],
    desc: "Stacked indoor crop production using LED lighting, hydroponic or aeroponic nutrient delivery, and AI-controlled environment optimization. Dickson Despommier's *The Vertical Farm* (2010) popularized the concept; AeroFarms (Newark, 2004), Plenty (San Francisco, 2014), Infarm (Berlin, 2013), and Bowery Farming scaled it commercially. Vertical farms produce leafy greens, herbs, and microgreens 100× more efficiently per land area than field agriculture, with no pesticides and 95% less water — but the LED energy budget is currently economically marginal except for high-value crops near urban markets. Solarpunk advocates see vertical farms as a key element of climate-resilient cities; critics call them an energy-intensive distraction from broader food-system reform." },
"""

TRANSLATIONS = {
    "food-preservation":         "食物保存",
    "beekeeping":                "养蜂业",
    "cheese-dairy-processing":   "奶酪与乳制品加工",
    "salt-production":           "盐业生产",
    "latifundia":                "罗马大庄园",
    "sugar-plantation":          "蔗糖种植园",
    "canning":                   "罐头食品",
    "mechanical-reaper":         "机械收割机",
    "pasteurization":            "巴氏消毒法",
    "refrigerated-transport":    "冷藏运输",
    "tractor":                   "拖拉机",
    "synthetic-pesticides":      "合成农药",
    "industrial-aquaculture":    "工业化水产养殖",
    "frozen-food-supply-chain":  "冷冻食品供应链",
    "gmo":                       "转基因作物",
    "vertical-farming":          "垂直农业",
}

UNLOCKS = {
    "food-preservation": [
        ("resource", "Smoking",                   "烟熏",               "Smoking (cooking)"),
        ("resource", "Drying",                    "干燥",               "Drying"),
        ("resource", "Fermentation in food processing", "食品发酵",     "Fermentation in food processing"),
        ("resource", "Pemmican",                  "肉干 (pemmican)",    "Pemmican"),
    ],
    "beekeeping": [
        ("resource", "Apis mellifera",            "西方蜜蜂",            "Western honey bee"),
        ("resource", "Honey",                     "蜂蜜",               "Honey"),
        ("resource", "Beeswax",                   "蜂蜡",               "Beeswax"),
        ("resource", "Mead",                      "蜂蜜酒",             "Mead"),
        ("wonder",   "Egyptian apiary",           "古埃及蜂房",          "Beekeeping"),
    ],
    "cheese-dairy-processing": [
        ("resource", "Rennet",                    "凝乳酶",             "Rennet"),
        ("resource", "Cheese",                    "奶酪",               "Cheese"),
        ("resource", "Yogurt",                    "酸奶",               "Yogurt"),
        ("resource", "Butter",                    "黄油",               "Butter"),
        ("resource", "Lactase persistence",       "乳糖酶持久性",       "Lactase persistence"),
    ],
    "salt-production": [
        ("wonder",   "Hallstatt salt mine",       "哈尔施塔特盐矿",     "Hallstatt"),
        ("resource", "Salt evaporation pond",     "盐田",               "Salt evaporation pond"),
        ("resource", "Salt cod",                  "盐渍鳕鱼",           "Salt cod"),
        ("work",     "Gabelle (salt tax)",        "盐税 (gabelle)",     "Gabelle"),
    ],
    "latifundia": [
        ("work",     "De Agricultura (Cato)",     "《论农业》(老加图)", "De agri cultura"),
        ("work",     "Rerum Rusticarum (Varro)",  "《论农事》(瓦罗)",   "Marcus Terentius Varro"),
        ("resource", "Roman grain trade",         "罗马粮食贸易",       "Cura Annonae"),
        ("unit",     "Slave-worked estate",       "奴隶庄园",           "Slavery in ancient Rome"),
    ],
    "sugar-plantation": [
        ("resource", "Sugarcane",                 "甘蔗",               "Sugarcane"),
        ("wonder",   "Saint-Domingue",            "圣多明各",           "Saint-Domingue"),
        ("resource", "Triangular trade",          "三角贸易",           "Triangular trade"),
        ("org",      "Royal African Company",     "皇家非洲公司",       "Royal African Company"),
    ],
    "canning": [
        ("person",   "Nicolas Appert",            "尼古拉·阿佩尔",      "Nicolas Appert"),
        ("person",   "Bryan Donkin",              "布莱恩·东金",        "Bryan Donkin"),
        ("resource", "Tin can",                   "马口铁罐",           "Tin can"),
        ("resource", "Mason jar",                 "梅森罐",             "Mason jar"),
    ],
    "mechanical-reaper": [
        ("person",   "Cyrus McCormick",           "塞勒斯·麦考密克",    "Cyrus McCormick"),
        ("unit",     "McCormick Reaper",          "麦考密克收割机",     "Mechanical reaper"),
        ("unit",     "Combine harvester",         "联合收割机",         "Combine harvester"),
        ("org",      "International Harvester",   "万国收割机公司",      "International Harvester"),
    ],
    "pasteurization": [
        ("person",   "Louis Pasteur",             "路易·巴斯德",       "Louis Pasteur"),
        ("resource", "UHT processing",            "超高温灭菌",         "Ultra-high-temperature processing"),
        ("resource", "HTST process",              "高温短时灭菌",        "Pasteurization"),
        ("work",     "Compulsory pasteurization", "强制巴氏消毒法",      "Pasteurization"),
    ],
    "refrigerated-transport": [
        ("person",   "Gustavus Swift",            "古斯塔夫斯·斯威夫特","Gustavus Franklin Swift"),
        ("unit",     "Refrigerator car",          "冷藏车",             "Refrigerator car"),
        ("unit",     "SS Strathleven",            "SS 斯特拉斯利文号",   "SS Strathleven"),
        ("resource", "Cold chain",                "冷链",               "Cold chain"),
    ],
    "tractor": [
        ("unit",     "Fordson Model F",           "福特森 F 型拖拉机",  "Fordson"),
        ("unit",     "John Deere Model D",        "约翰迪尔 D 型",       "John Deere"),
        ("org",      "Caterpillar Inc.",          "卡特彼勒公司",       "Caterpillar Inc."),
        ("resource", "Power take-off",            "动力输出装置",        "Power take-off"),
    ],
    "synthetic-pesticides": [
        ("person",   "Paul Hermann Müller",       "保罗·赫尔曼·穆勒",   "Paul Hermann Müller"),
        ("resource", "DDT",                       "DDT",                 "DDT"),
        ("resource", "Glyphosate",                "草甘膦",              "Glyphosate"),
        ("resource", "Neonicotinoid",             "新烟碱类杀虫剂",      "Neonicotinoid"),
        ("work",     "Silent Spring",             "《寂静的春天》",      "Silent Spring"),
        ("work",     "Stockholm Convention",      "《斯德哥尔摩公约》",  "Stockholm Convention on Persistent Organic Pollutants"),
    ],
    "industrial-aquaculture": [
        ("resource", "Atlantic salmon farming",   "大西洋鲑养殖",        "Salmon as food"),
        ("resource", "Shrimp farming",            "对虾养殖",           "Shrimp farming"),
        ("resource", "Recirculating aquaculture system", "循环水养殖",  "Recirculating aquaculture system"),
        ("org",      "Mowi (formerly Marine Harvest)", "美威公司",      "Mowi"),
    ],
    "frozen-food-supply-chain": [
        ("person",   "Clarence Birdseye",         "克拉伦斯·伯兹艾",    "Clarence Birdseye"),
        ("org",      "Birds Eye",                 "Birds Eye 鸟眼食品", "Birds Eye"),
        ("unit",     "TV dinner",                 "电视餐",              "TV dinner"),
        ("resource", "Flash freezing",            "快速冷冻",            "Flash freezing"),
    ],
    "gmo": [
        ("unit",     "FlavrSavr tomato",          "FlavrSavr 番茄",       "FlavrSavr"),
        ("unit",     "Roundup Ready soybean",     "抗草甘膦大豆",         "Roundup Ready"),
        ("unit",     "Bt corn",                   "Bt 玉米",              "Bt corn"),
        ("org",      "Monsanto",                  "孟山都公司",           "Monsanto"),
        ("resource", "CRISPR-edited crop",        "CRISPR 编辑作物",      "Genome editing"),
    ],
    "vertical-farming": [
        ("person",   "Dickson Despommier",        "迪克森·德斯波米耶",   "Dickson Despommier"),
        ("work",     "The Vertical Farm",         "《垂直农场》",        "Vertical farming"),
        ("org",      "AeroFarms",                 "AeroFarms 空中农场",  "AeroFarms"),
        ("org",      "Plenty (company)",          "Plenty 农业公司",     "Plenty (company)"),
        ("resource", "Aeroponics",                "气培",                "Aeroponics"),
    ],
}


def splice_data():
    src = DATA.read_text()
    if 'id: "food-preservation"' in src:
        print("data.js: already inserted"); return
    marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
    if marker not in src:
        raise SystemExit("Closing marker not found")
    DATA.write_text(src.replace(marker, "\n" + NEW_BLOCK + "];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"))
    print(f"data.js: +{len(TRANSLATIONS)} subsistence techs")


def splice_translations():
    src = TRANS.read_text()
    if '"food-preservation"' in src:
        print("translations.js: already inserted"); return
    block = "\n  // ─── Subsistence & agriculture (gap fill) ───\n"
    for tid, zh in TRANSLATIONS.items():
        block += f'  "{tid}": "{zh}",\n'
    rs = src.rstrip(); assert rs.endswith("};")
    TRANS.write_text(rs[:-2] + block + "};\n")
    print(f"translations.js: +{len(TRANSLATIONS)}")


def splice_unlocks():
    src = UNLOCKS_PATH.read_text()
    if '"food-preservation"' in src:
        print("unlocks.js: already inserted"); return
    block = "\n  // ─── Subsistence & agriculture (gap fill) ───\n"
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
