#!/usr/bin/env python3
"""Fetch Wikipedia lead images for each tech in data.js, with a confidence
score so we can audit matches. Run once; outputs:

  images/{tech_id}.jpg            — saved when match is HIGH confidence
  _image_manifest.json            — full record per tech (status, score, urls)

Status values:
  ok       — article title and extract clearly match the tech; image saved
  review   — article found and image downloaded but the title or extract drift
              from the tech name/description; needs human eyeballing
  no_image — article exists but has no thumbnail
  no_match — search returned nothing relevant
  skip     — search override says don't fetch

Re-runs are incremental: techs already with status=ok are skipped unless --force.
"""

import json, os, re, sys, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_JS = ROOT / "data.js"
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# Per-tech search overrides for cases where tech.name doesn't make a great query.
# Keys are tech ids. Empty string means "skip this tech".
SEARCH_OVERRIDES = {
    "bipedal-gait": "Bipedalism",
    "wooden-club": "Club (weapon)",
    "gestural-communication": "Sign language",
    "scavenging": "Scavenger",
    "persistence-hunting": "Persistence hunting",
    "fire-use": "Control of fire by early humans",
    "fire-making": "Fire making",
    "windbreaks": "Windbreak",
    "wooden-spear": "Schöningen spears",
    "acheulean": "Acheulean",
    "oldowan": "Oldowan",
    "cooking": "Cooking",
    "digging-stick": "Digging stick",
    "levallois": "Levallois technique",
    "hafting": "Hafting",
    "birch-tar": "Birch tar",
    "hide-clothing": "Buckskin (leather)",
    "shellfishing": "Shellfish",
    "pigments": "Pigment",
    "composite-spear": "Clovis point",
    "shell-beads": "Shell jewelry",
    "water-flask": "Diepkloof Rock Shelter",
    "burial": "Burial",
    "proto-language": "Sign language",
    "rafts": "Raft",
    "blade-tech": "Blade (archaeology)",
    "bone-tools": "Bone tool",
    "needles": "Sewing needle",
    "cave-art": "Cave painting",
    "flute": "Divje Babe Flute",
    "bow-drill": "Bow drill",
    "tally-bones": "Ishango bone",
    "oil-lamp": "Oil lamp",
    "spun-fiber": "Spindle (textiles)",
    "figurines": "Venus figurines",
    "microliths": "Microlith",
    "shamanism": "Shamanism",
    "trade-networks": "Long-distance trade",
    "atlatl": "Spear-thrower",
    "lunar-tally": "Lunar calendar",
    "harpoon": "Harpoon",
    "dog": "Origin of the domestic dog",
    "ground-stone": "Ground stone",
    "bow-arrow": "Bow and arrow",
    "spun-fiber-mat": "Mat",
    "basketry": "Basket weaving",
    "semi-sedentism": "Mesolithic",
    "mortar-pestle": "Mortar and pestle",
    "sickle-flint": "Sickle",
    "fishing-net": "Fishing net",
    "fish-weir": "Fish trap",
    "canoe": "Dugout canoe",
    "snowshoe-ski": "Snowshoe",
    "plant-cultivation": "Neolithic Revolution",
    "animal-domestication": "Domestication of animals",
    "polished-stone": "Hand axe",
    "pottery": "Pottery",
    "village": "Çatalhöyük",
    "adobe-brick": "Adobe",
    "megaliths": "Megalith",
    "ritual-religion": "Prehistoric religion",
    "pottery-wheel": "Potter's wheel",
    "weaving": "Weaving",
    "domesticated-flax": "Flax",
    "irrigation": "Irrigation",
    "plow-ard": "Ard (plough)",
    "millstone": "Millstone",
    "fermentation-brewing": "History of beer",
    "granary": "Granary",
    "sledge-runner": "Sled",
    "sail-primitive": "Sail",
    "copper-smelting": "Copper extraction",
    "mathematics-counting": "History of mathematics",
    "proto-writing-tokens": "Proto-writing",
    "bronze-metallurgy": "Bronze",
    "bronze-tools": "Bronze Age",
    "bronze-weapons": "Bronze Age sword",
    "iron-meteoric": "Meteoric iron",
    "spoked-wheel": "Spoke",
    "wheeled-cart": "Cart",
    "horse-domestication": "Horse",
    "chariot": "Chariot",
    "composite-bow": "Composite bow",
    "city-state": "City-state",
    "code-of-law": "Code of Hammurabi",
    "cuneiform": "Cuneiform",
    "hieroglyphics": "Egyptian hieroglyphs",
    "alphabet-phoenician": "Mesha Stele",
    "abacus": "Abacus",
    "mathematics-arithmetic": "Babylonian mathematics",
    "astronomy-observation": "Babylonian astronomy",
    "solar-calendar": "Egyptian calendar",
    "monumental-architecture": "Ancient Egyptian architecture",
    "pyramid-ziggurat": "Egyptian pyramids",
    "glass-making": "History of glass",
    "silver-gold-metallurgy": "Goldsmith",
    "olive-wine": "History of wine",
    "linen-textile": "Linen",
    "standing-army": "Standing army",
    "maritime-trade": "Maritime history",
    "galley-ship": "Galley",
    "pulley-lever": "Pulley",
    "proto-medicine": "Edwin Smith Papyrus",
    "trepanation": "Trepanning",
    "iron-smelting": "Bloomery",
    "iron-tools": "Iron",
    "iron-weapons": "Gladius",
    "steel-bloomery": "Wootz steel",
    "alphabet-greek": "Linear B",
    "alphabet-latin": "Latin alphabet",
    "philosophy": "Plato",
    "geometry-euclidean": "Euclidean geometry",
    "zero-numeral": "Bakhshali manuscript",
    "alchemy": "Alchemy",
    "coinage": "Coin",
    "democracy": "Athenian democracy",
    "republic": "Roman Republic",
    "empire": "Roman Empire",
    "roman-law": "Roman law",
    "roads-paved": "Roman roads",
    "aqueduct": "Roman aqueduct",
    "arch-vault": "Arch",
    "concrete-roman": "Roman concrete",
    "crossbow": "Crossbow",
    "siege-engine": "Siege engine",
    "cavalry": "Cavalry",
    "saddle-stirrup": "Stirrup",
    "silk-production": "History of silk",
    "paper-making": "History of paper",
    "world-religion": "Religious symbol",
    "monasticism": "Mont Saint-Michel",
    "library": "Library of Alexandria",
    "scientific-method-proto": "Aristotle",
    "medicine-galenic": "Galen",
    "water-clock": "Water clock",
    "waterwheel": "Water wheel",
    "compass-early": "South-pointing chariot",
    "triremes": "Trireme",
    "gear-mechanism": "Antikythera mechanism",
    "woodblock-printing": "Woodblock printing",
    "arabic-numerals": "Liber Abaci",
    "algebra": "Al-Khwarizmi",
    "gunpowder": "Gunpowder",
    "moveable-type": "Movable type",
    "mechanical-clock": "History of timekeeping devices",
    "windmill": "Windmill",
    "heavy-plow": "Plough",
    "horse-collar": "Horse collar",
    "three-field-system": "Three-field system",
    "university": "University of Bologna",
    "scholasticism": "Scholasticism",
    "gothic-architecture": "Gothic architecture",
    "castle": "Castle",
    "knight-cavalry": "Knight",
    "longbow": "English longbow",
    "cannon-early": "History of cannon",
    "caravel": "Caravel",
    "hospital": "Bimaristan",
    "guild": "Guild",
    "banking-double-entry": "Luca Pacioli",
    "letter-of-credit": "Bill of exchange",
    "magnetic-compass-marine": "Compass",
    "glass-lens": "Lens",
    "spectacles": "Glasses",
    "distillation": "Distillation",
    "paper-mill": "Paper mill",
    "horizontal-loom": "Loom",
    "quill-ink": "Quill",
    "printing-press": "Printing press",
    "vernacular-literature": "Geoffrey Chaucer",
    "humanism": "Renaissance humanism",
    "linear-perspective": "Perspective (graphical)",
    "oil-painting": "Oil painting",
    "opera-orchestra": "Opera",
    "scientific-method": "Galileo Galilei",
    "heliocentrism": "Heliocentrism",
    "algebra-symbolic": "François Viète",
    "logarithms": "Logarithm",
    "anatomy-vesalius": "De humani corporis fabrica",
    "microscope": "Optical microscope",
    "telescope": "Refracting telescope",
    "pendulum-clock": "Pendulum clock",
    "protestant-reformation": "Martin Luther",
    "nation-state": "Peace of Westphalia",
    "joint-stock-company": "Joint-stock company",
    "mercantilism": "Mercantilism",
    "galleon": "Galleon",
    "ocean-navigation": "Celestial navigation",
    "new-world-encounter": "Voyages of Christopher Columbus",
    "colonialism": "Colonialism",
    "columbian-exchange": "Columbian exchange",
    "musket": "Musket",
    "artillery": "Artillery",
    "bastion-fortification": "Bastion fort",
    "newtonian-mechanics": "Philosophiæ Naturalis Principia Mathematica",
    "calculus": "Isaac Newton",
    "gravitation-law": "Isaac Newton",
    "cartesian-coordinates": "Cartesian coordinate system",
    "probability-theory": "Probability theory",
    "thermometer": "Thermometer",
    "barometer": "Barometer",
    "germ-precursor": "Antonie van Leeuwenhoek",
    "vaccination": "Edward Jenner",
    "chemistry-modern": "Antoine Lavoisier",
    "electricity-static": "Benjamin Franklin",
    "steam-pump": "Newcomen atmospheric engine",
    "steam-engine-watt": "Watt steam engine",
    "coke-iron": "Abraham Darby I",
    "canal-system": "Bridgewater Canal",
    "turnpike-roads": "Turnpike trust",
    "agricultural-revolution": "British Agricultural Revolution",
    "crop-rotation-norfolk": "Crop rotation",
    "selective-breeding": "Selective breeding",
    "enlightenment-philosophy": "Age of Enlightenment",
    "liberal-democracy": "Liberal democracy",
    "separation-of-powers": "Montesquieu",
    "encyclopedia": "Encyclopédie",
    "public-education": "Compulsory education",
    "factory-system": "Factory system",
    "spinning-jenny": "Spinning jenny",
    "power-loom": "Power loom",
    "naval-warship": "Ship of the line",
    "modern-bookkeeping": "Luca Pacioli",
    "central-bank": "Bank of England",
    "bessemer-steel": "Bessemer process",
    "railway-locomotive": "Stephenson's Rocket",
    "telegraph": "Electrical telegraph",
    "railroad-network": "Rail transport",
    "steamship": "Steamship",
    "electric-battery": "Voltaic pile",
    "electromagnetism": "Electromagnetism",
    "electric-motor": "Electric motor",
    "telephone": "Telephone",
    "radio-wireless": "History of radio",
    "photography": "History of photography",
    "cinema": "Lumière brothers",
    "oil-petroleum": "History of the petroleum industry",
    "internal-combustion": "Internal combustion engine",
    "automobile": "Benz Patent-Motorwagen",
    "bicycle": "Safety bicycle",
    "evolution-darwin": "On the Origin of Species",
    "germ-theory": "Germ theory of disease",
    "antiseptic-surgery": "Joseph Lister",
    "anesthesia": "History of general anesthesia",
    "public-sanitation": "Sanitary sewer",
    "vaccination-mass": "Louis Pasteur",
    "thermodynamics": "Thermodynamics",
    "periodic-table": "Periodic table",
    "atomic-theory": "Atomic theory",
    "electron-discovery": "Electron",
    "x-ray": "X-ray",
    "machine-tool": "Machine tool",
    "interchangeable-parts": "Interchangeable parts",
    "assembly-line": "Assembly line",
    "modern-corporation": "John D. Rockefeller",
    "labor-union": "International Workers' Day",
    "newspaper-mass": "New York Tribune",
    "skyscraper": "Burj Khalifa",
    "elevator": "Elevator",
    "machine-gun": "Maxim gun",
    "electrification": "Electrification",
    "airplane": "Wright Flyer",
    "relativity": "Theory of relativity",
    "quantum-mechanics": "Quantum mechanics",
    "radar": "Radar",
    "helicopter": "Helicopter",
    "jet-engine": "Jet engine",
    "rocket": "V-2 rocket",
    "nuclear-fission": "Nuclear fission",
    "nuclear-weapon": "Nuclear weapon",
    "nuclear-power": "Nuclear power",
    "antibiotics": "History of penicillin",
    "vaccines-modern": "Polio vaccine",
    "dna-structure": "DNA",
    "synthetic-fertilizer": "Haber process",
    "green-revolution": "Green Revolution",
    "plastic-polymer": "Plastic",
    "transistor": "Transistor",
    "semiconductor": "Integrated circuit",
    "digital-computer": "ENIAC",
    "programming-language": "Fortran",
    "mainframe": "IBM System/360",
    "television": "History of television",
    "satellite": "Sputnik 1",
    "spaceflight": "Vostok 1",
    "moon-landing": "Apollo 11",
    "mass-media": "Newspaper",
    "consumer-economy": "Consumerism",
    "credit-card": "Credit card",
    "container-shipping": "Containerization",
    "highway-system": "Interstate Highway System",
    "welfare-state": "Welfare state",
    "decolonization": "Indian independence movement",
    "united-nations": "United Nations",
    "birth-control": "Combined oral contraceptive pill",
    "air-conditioning": "Air conditioning",
    "microprocessor": "Intel 4004",
    "personal-computer": "Apple II",
    "gui-mouse": "Graphical user interface",
    "packet-switching": "Donald Davies",
    "arpanet-internet": "ARPANET",
    "email": "Email",
    "world-wide-web": "World Wide Web",
    "search-engine": "Google Search",
    "fiber-optic": "Fiber-optic communication",
    "mobile-phone": "Mobile phone",
    "smartphone": "IPhone (1st generation)",
    "social-media": "Social media",
    "streaming-media": "Streaming media",
    "cloud-computing": "Cloud computing",
    "ecommerce": "Amazon (company)",
    "gps": "Global Positioning System",
    "gene-sequencing": "Human Genome Project",
    "genetic-engineering": "Recombinant DNA",
    "crispr": "CRISPR",
    "mri-imaging": "Magnetic resonance imaging",
    "ivf": "In vitro fertilisation",
    "mrna-vaccine": "Pfizer–BioNTech COVID-19 vaccine",
    "solar-photovoltaic": "Solar cell",
    "wind-turbine": "Wind turbine",
    "lithium-battery": "Lithium-ion battery",
    "electric-vehicle": "Tesla Roadster (first generation)",
    "renewable-grid": "Renewable energy",
    "machine-learning": "TensorFlow",
    "deep-learning": "AlexNet",
    "large-language-model": "ChatGPT",
    "cryptocurrency": "Bitcoin",
    "reusable-rocket": "Falcon 9",
    "autonomous-vehicle": "Waymo",
    "3d-printing": "3D printing",
    "robotics": "Robotics",
    "quantum-computing": "Quantum computing",
    "climate-science": "Climatology",
}


def parse_techs():
    """Parse data.js for [{id, name, era, desc}, ...]."""
    src = DATA_JS.read_text()
    pattern = re.compile(
        r'\{\s*id:\s*"([^"]+)"\s*,'
        r'\s*name:\s*"([^"]+)"\s*,'
        r'\s*era:\s*"([^"]+)"\s*,'
        r'\s*category:\s*"([^"]+)"\s*,'
        r'\s*year:\s*"([^"]+)"\s*,'
        r'\s*prereqs:\s*\[[^\]]*\]\s*,'
        r'\s*desc:\s*"([^"]+)"',
        re.S,
    )
    return [
        {"id": m.group(1), "name": m.group(2), "era": m.group(3),
         "category": m.group(4), "year": m.group(5), "desc": m.group(6)}
        for m in pattern.finditer(src)
    ]


def http_json(url, retries=5):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                backoff = 2 ** attempt
                print(f"  429, sleeping {backoff}s...")
                time.sleep(backoff)
                continue
            raise


def http_bytes(url, retries=5):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                backoff = 2 ** attempt
                print(f"  429 on image, sleeping {backoff}s...")
                time.sleep(backoff)
                continue
            raise


def normalize(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def title_overlap(tech_name, article_title):
    """Fraction of tech-name words present in article title."""
    a = set(normalize(tech_name).split())
    b = set(normalize(article_title).split())
    if not a:
        return 0.0
    stop = {"the", "of", "a", "an", "and", "or", "in", "to"}
    a -= stop
    b -= stop
    if not a:
        return 1.0
    return len(a & b) / len(a)


def fetch_summary(title):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(title.replace(" ", "_"))
    return http_json(url)


def search_article(query):
    url = ("https://en.wikipedia.org/w/api.php"
           "?action=query&list=search&format=json&srlimit=1&srsearch=" + urllib.parse.quote(query))
    j = http_json(url)
    hits = j.get("query", {}).get("search", [])
    return hits[0]["title"] if hits else None


def score(tech, summary, used_override):
    """Return (status, score, reason)."""
    article = summary.get("title", "")
    extract = summary.get("extract") or ""
    desc = summary.get("description") or ""
    if summary.get("type") == "disambiguation":
        return ("review", 0.3, "disambiguation page")

    title_score = title_overlap(tech["name"], article)
    name_words = [w for w in normalize(tech["name"]).split() if len(w) > 3]
    body = (extract + " " + desc).lower()
    body_hits = sum(1 for w in name_words if w in body)
    body_score = body_hits / max(1, len(name_words)) if name_words else 0.0
    s = 0.6 * title_score + 0.4 * body_score
    reason = f"title={title_score:.2f} body={body_score:.2f}{' override' if used_override else ''}"

    # Hand-curated overrides: trust them unless the body completely fails
    # (e.g. picked a wrong article — body would have ~0 overlap with tech words).
    if used_override:
        if body_score >= 0.2 or len(name_words) == 0:
            return ("ok", round(max(s, 0.7), 2), reason)
        return ("review", round(s, 2), reason + " (override but weak body match)")

    if title_score >= 0.6 and body_score >= 0.3:
        return ("ok", round(s, 2), reason)
    if title_score >= 0.3 or body_score >= 0.3:
        return ("review", round(s, 2), reason)
    return ("review", round(s, 2), reason)


def main():
    force = "--force" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]

    techs = parse_techs()
    print(f"Loaded {len(techs)} techs")

    IMG_DIR.mkdir(exist_ok=True)
    manifest = {}
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text())

    counts = {"ok": 0, "review": 0, "no_image": 0, "no_match": 0, "skip": 0, "cached": 0}

    for i, t in enumerate(techs):
        if only and t["id"] != only:
            continue
        existing = manifest.get(t["id"], {})
        if (not force) and existing.get("status") == "ok" and (IMG_DIR / f"{t['id']}.jpg").exists():
            counts["cached"] += 1
            continue

        # Pick query
        override = SEARCH_OVERRIDES.get(t["id"])
        if override == "":
            manifest[t["id"]] = {**existing, "status": "skip", "reason": "explicit skip"}
            counts["skip"] += 1
            continue
        query = override or t["name"]

        try:
            # Use override directly as title if provided; otherwise search.
            title = query if override else (search_article(query) or query)
            summary = fetch_summary(title)
            article_title = summary.get("title", title)
            thumb = (summary.get("thumbnail") or {}).get("source") or (summary.get("originalimage") or {}).get("source")
            page_url = summary.get("content_urls", {}).get("desktop", {}).get("page", f"https://en.wikipedia.org/wiki/{urllib.parse.quote(article_title.replace(' ', '_'))}")

            if not thumb:
                manifest[t["id"]] = {
                    "name": t["name"], "query": query, "article": article_title,
                    "page": page_url, "status": "no_image", "reason": "no thumbnail",
                }
                counts["no_image"] += 1
                print(f"[{i+1:3}/{len(techs)}] {t['id']:30} NO_IMAGE   {article_title}")
                time.sleep(0.1)
                continue

            status, sc, reason = score(t, summary, used_override=bool(override))
            img_bytes, ctype = http_bytes(thumb)
            ext = ".jpg" if "jpeg" in ctype or "jpg" in ctype else (".png" if "png" in ctype else ".jpg")
            img_path = IMG_DIR / f"{t['id']}{ext}"
            img_path.write_bytes(img_bytes)

            manifest[t["id"]] = {
                "name": t["name"], "query": query, "article": article_title,
                "page": page_url, "image_url": thumb, "image_path": str(img_path.relative_to(ROOT)),
                "extract": (summary.get("extract") or "")[:280],
                "status": status, "score": sc, "reason": reason,
            }
            counts[status] += 1
            print(f"[{i+1:3}/{len(techs)}] {t['id']:30} {status.upper():8} {sc:.2f} {article_title}")
        except urllib.error.HTTPError as e:
            manifest[t["id"]] = {"name": t["name"], "query": query, "status": "no_match",
                                 "reason": f"HTTP {e.code}"}
            counts["no_match"] += 1
            print(f"[{i+1:3}/{len(techs)}] {t['id']:30} NO_MATCH   HTTP {e.code} ({query})")
        except Exception as e:
            manifest[t["id"]] = {"name": t["name"], "query": query, "status": "no_match",
                                 "reason": str(e)[:200]}
            counts["no_match"] += 1
            print(f"[{i+1:3}/{len(techs)}] {t['id']:30} ERR        {e}")

        # Be courteous to Wikipedia (REST API rate-limits aggressively).
        time.sleep(0.6)

        # Periodic flush
        if (i + 1) % 10 == 0:
            MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print()
    print("Summary:", counts)


if __name__ == "__main__":
    main()
