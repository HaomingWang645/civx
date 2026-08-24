#!/usr/bin/env python3
"""Build fallbacks and manifest entries for abstract future concepts.

Speculative milestones use AI-generated editorial PNGs when a reviewed asset is
available. Purpose-built SVGs remain as deterministic fallbacks so rebuilding
the manifest never leaves a technology without a figure.
"""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images" / "concepts"
GENERATED = ROOT / "images" / "generated"
MANIFEST = ROOT / "_image_manifest.json"
IMAGES_JS = ROOT / "images.js"


TARGETS = {
    "long-duration-energy-storage": ("LONG-DURATION STORAGE", "hours to days · full-system cost · grid resilience", "material"),
    "advanced-fission-systems": ("ADVANCED FISSION SYSTEMS", "passive safety · repeatable construction · safeguards", "nuclear"),
    "green-hydrogen-electrofuels": ("GREEN HYDROGEN + ELECTROFUELS", "clean power → molecules for hard-to-electrify uses", "chemistry"),
    "point-source-carbon-capture": ("INDUSTRIAL CARBON CAPTURE", "concentrated source · transport · durable storage", "chemistry"),
    "enhanced-weathering": ("ENHANCED WEATHERING", "mineral reaction · lifecycle accounting · monitoring", "matter"),
    "ocean-carbon-removal": ("OCEAN CARBON REMOVAL", "chemistry · ecology · verification", "ecology"),
    "climate-adaptation-infrastructure": ("CLIMATE-ADAPTATION INFRASTRUCTURE", "heat · flood · fire · drought resilience", "biosphere"),
    "advanced-water-reuse": ("ADVANCED WATER REUSE", "treatment · desalination · aquifer recharge", "chemistry"),
    "autonomous-laboratories": ("AUTONOMOUS LABORATORIES", "hypothesis → experiment → evidence → update", "network"),
    "precision-fermentation-agriculture": ("PRECISION BIOPRODUCTION", "fermentation · edited crops · field evidence", "biosphere"),
    "xenotransplantation-organ-preservation": ("ORGAN SUPPLY PLATFORM", "preservation · perfusion · xenotransplantation", "capsule"),
    "pandemic-surveillance-platform": ("PANDEMIC EARLY WARNING", "genomics · wastewater · confirmatory response", "network"),
    "orbital-servicing-refueling": ("ORBITAL SERVICING", "inspect · repair · refuel · remove debris", "propulsion"),
    "lunar-isru-logistics": ("LUNAR ISRU + LOGISTICS", "water · oxygen · shielding · propellant transfer", "matter"),
    "nuclear-space-propulsion": ("NUCLEAR SPACE PROPULSION", "thermal thrust · electric efficiency · heat rejection", "propulsion"),
    "integrated-space-networks": ("INTEGRATED SPACE NETWORKS", "terrestrial · orbital · resilient routing", "network"),
    "post-cmos-integration": ("POST-CMOS INTEGRATION", "chiplets · 3D stacking · optical interconnects", "reversible"),
    "autonomous-built-environment": ("AUTONOMOUS CONSTRUCTION + AGRICULTURE", "outdoor robotics · safety · repairability", "abundance"),
    "solar-gravitational-lens-observatory": ("SOLAR GRAVITATIONAL LENS", "550+ AU · Einstein ring · reconstruction", "navigation"),
    "beamed-interstellar-probe": ("BEAMED INTERSTELLAR PROBE", "remote energy · light sail · deep-space link", "projectile"),
    "stellar-material-extraction": ("STAR LIFTING + STELLAR PROPULSION", "mass flow · momentum · deep-time control", "shells"),
    "interstellar-shielding-deceleration": ("INTERSTELLAR SHIELDING + BRAKING", "dust defense · magnetic sail · arrival", "defense"),
    "deep-time-archives": ("DEEP-TIME ARCHIVES", "redundancy · primers · repair · provenance", "protocol"),
    "heat-limited-computing": ("HEAT-LIMITED COMPUTING", "reversible logic · cryogenics · radiators", "shells"),
    "agi": ("GENERAL INTELLIGENCE", "transfer · planning · uncertainty", "network"),
    "nuclear-pulse-propulsion": ("NUCLEAR-PULSE SPACECRAFT", "pusher plate · shock absorbers · pulse units", "propulsion"),
    "cryogenic-hibernation": ("REVERSIBLE TORPOR", "cooling · perfusion · controlled rewarming", "capsule"),
    "post-scarcity": ("ABUNDANCE SCENARIO", "automation · energy · distribution", "abundance"),
    "langlands-program-completion": ("LANGLANDS PROGRAM", "number theory ↔ representation theory", "bridge"),
    "reversible-computing": ("REVERSIBLE COMPUTING", "preserve information · uncompute intermediates", "reversible"),
    "artificial-photosynthesis": ("ARTIFICIAL PHOTOSYNTHESIS", "sunlight + CO₂ + H₂O → fuel", "chemistry"),
    "engineered-sensory-modalities": ("ENGINEERED SENSES", "new sensors mapped into neural codes", "sensory"),
    "relativistic-kinetic-weapon": ("RELATIVISTIC PROJECTILE", "0.1c example · interstellar scale", "projectile"),
    "matrioshka-brain": ("MATRIOSHKA BRAIN", "nested computing shells · outward heat flow", "shells"),
    "galactic-ecology": ("INTERSTELLAR ECOLOGY", "biospheres · exchange · containment", "ecology"),
    "speciation-ethics": ("SPECIATION ETHICS", "divergence · consent · shared rights", "ethics"),
    "cosmic-string-ftl": ("COSMIC-STRING CHRONOLOGY", "idealized strings · closed timelike curves", "strings"),
    "ai-judge": ("AI-ASSISTED COURTS", "sources · audit · appeal · human authority", "justice"),
    "degrowth-economics": ("POST-GROWTH POLICY", "well-being within material and ecological limits", "policy"),
    "synthetic-performers": ("SYNTHETIC PERFORMERS", "generated voice · motion · accountable identity", "performer"),
    "pulsar-navigation": ("AUTONOMOUS XNAV", "X-ray pulsars · timing · position estimate", "navigation"),
    "layered-air-missile-defense": ("LAYERED AIR DEFENSE", "sensors · interceptors · command network", "defense"),
    "fusion-materials": ("FUSION MATERIALS", "neutrons · heat · transmutation · maintenance", "material"),
    "theory-of-consciousness": ("CONSCIOUS-STATE SCIENCE", "competing models · discriminating tests", "consciousness"),
    "superintelligence": ("SUPERINTELLIGENCE SCENARIO", "capability · control · governance", "supernetwork"),
    "programmable-matter": ("PROGRAMMABLE MATTER", "reconfigure shape · stiffness · function", "matter"),
    "continuum-hypothesis-resolution": ("POST-ZFC CONSENSUS", "independence · added axioms · plural foundations", "foundations"),
    "engineered-planetary-biosphere": ("ENGINEERED BIOSPHERE", "closed cycles · monitoring · adaptive control", "biosphere"),
    "lingua-galactica": ("INTERSTELLAR CONTACT PROTOCOL", "translation · delay · error correction", "protocol"),
    "galactic-citizenship": ("INTERSTELLAR CIVIC FRAMEWORK", "rights across autonomous star systems", "civic"),
    "pan-galactic-festival": ("ASYNCHRONOUS CULTURAL EXCHANGE", "art and ritual across light-year delays", "cultural"),
    "femto-engineering": ("NUCLEAR-SCALE ENGINEERING", "isomers · nuclei · controlled transitions", "nuclear"),
    "strange-quark-matter": ("DENSE QCD MATTER", "quark phases under extreme pressure", "quark"),
    # Replace adjacent-topic, duplicated, or visually misleading stock figures.
    "moon-base": ("SUSTAINED LUNAR BASE", "continuous occupancy · local resources · maintainable life support", "settlement"),
    "mars-landing": ("FIRST CREWED MARS LANDING", "interplanetary transit · entry and descent · safe return", "landing"),
    "mars-habitat": ("MARS SURFACE HABITAT", "radiation shielding · ISRU · long-duration habitation", "settlement"),
    "mars-colony": ("SELF-RELIANT MARS SETTLEMENT", "critical-loop closure · local industry · institutional continuity", "settlement"),
    "asteroid-mining": ("ASTEROID MINING", "prospect · extract · process · deliver useful material", "mining"),
    "anti-aging": ("LONGEVITY MEDICINE", "human evidence · healthspan · long-term safety", "longevity"),
    "lab-grown-meat": ("CULTIVATED MEAT AT SCALE", "food-grade cells · bioreactors · cost and lifecycle parity", "chemistry"),
    "quantum-applications": ("FAULT-TOLERANT QUANTUM ADVANTAGE", "logical qubits · error correction · verified useful workload", "quantum"),
    "space-elevator": ("SPACE ELEVATOR", "high-specific-strength tether · climbers · orbital dynamics", "elevator"),
    "network-state": ("NETWORK POLITY", "digital membership · territorial law · external recognition", "civic"),
    "transhumanism": ("CLINICAL HUMAN AUGMENTATION", "restoration and enhancement · consent · reversibility", "sensory"),
    "generative-art": ("AI-NATIVE CO-CREATION", "human direction · generative models · provenance", "cultural"),
    "decentralized-autonomous-org": ("LEGALLY INTEGRATED DAO", "on-chain coordination · legal wrapper · accountable governance", "civic"),
    "sentientism": ("SENTIENTISM", "moral consideration by capacity for experience", "ethics"),
    "photonic-computing": ("PHOTONIC COMPUTING", "optical interconnects · computation · electro-optic integration", "reversible"),
    "terraforming-mars": ("MARS PARATERRAFORMING", "enclosed pressure · managed climate · engineered ecology", "biosphere"),
    "dark-sector-physics": ("DARK-SECTOR PHYSICS", "gravitational evidence · laboratory tests · cosmological constraints", "foundations"),
    "p-vs-np-resolved": ("P VERSUS NP", "formal proof · complexity classes · practical consequences", "foundations"),
    "kardashev-type-ii": ("TYPE II CIVILIZATION", "stellar-scale power · distributed collectors · waste heat", "shells"),
    "universal-sentient-rights": ("SENTIENT RIGHTS", "capacity · legal standing · enforceable protections", "ethics"),
    "post-human-aesthetics": ("POST-HUMAN AESTHETICS", "new bodies · senses · media · authorship", "cultural"),
    "interstellar-treaty": ("INTERSTELLAR TREATY", "autonomous systems · delayed consent · durable protocol", "civic"),
    "time-dilation-cultures": ("TIME-DILATION CULTURES", "divergent subjective rates · synchronization · consent", "time"),
    "end-time-philosophy": ("END-TIME PHILOSOPHY", "finite resources · deep time · value under cosmic limits", "time"),
    "closed-cycle-cities": ("CIRCULAR RESOURCE CITIES", "water · materials · energy loops · equitable access", "abundance"),
    "ai-coordination-treaty": ("INTERNATIONAL AI ACCORD", "compute monitoring · safety standards · verification", "civic"),
    "direct-ai-democracy": ("AI-SUPPORTED PARTICIPATION", "translation · deliberation · plural channels · audit", "civic"),
    "asteroid-belt-settlement": ("ASTEROID-BELT SETTLEMENT", "distributed habitats · local material · long-delay autonomy", "settlement"),
    "cybernetic-enhancement": ("CYBERNETIC ENHANCEMENT", "integrated prostheses · feedback · consent · maintenance", "sensory"),
    "orbital-ring": ("ORBITAL RING", "fast orbital cable · stationary tethers · active stabilization", "ring"),
    "cyber-kinetic-warfare": ("CYBER-PHYSICAL WARFARE", "sensors · autonomous systems · cyber effects · human control", "defense"),
    "drone-swarms": ("RESILIENT DRONE SWARMS", "distributed sensing · coordination · graceful degradation", "swarm"),
    "anti-satellite-warfare": ("NON-DEBRIS COUNTERSPACE", "reversible effects · attribution · debris avoidance", "defense"),
    "strategic-memetic-warfare": ("STRATEGIC MEMETIC WARFARE", "narrative targeting · network propagation · attribution", "network"),
    "self-replicating-combat-drones": ("SELF-REPLICATING COMBAT DRONES", "resource capture · reproduction · containment failure", "matter"),
    "antimatter-weapon": ("ANTIMATTER WEAPON", "energy accounting · containment · catastrophic release", "antimatter"),
    "galactic-communication-network": ("INTERSTELLAR RELAY NETWORK", "laser links · store-and-forward · years of latency", "relay"),
    "pre-warp-interstellar-trade": ("LOCAL INTERSTELLAR TRADE", "high-value exchange · long transit · autonomous contracts", "protocol"),
    "dark-energy-engineering": ("DARK-ENERGY HYPOTHESIS", "cosmological observation · no demonstrated local control", "foundations"),
    "mind-linked-collective-art": ("MIND-LINKED COLLECTIVE ART", "consenting neural channels · shared timing · authorship", "brainlink"),
    "ai-native-art-forms": ("AI-NATIVE ART FORMS", "adaptive media · model agency · human curation", "cultural"),
    "stellar-scale-spectacle": ("STELLAR-SCALE SPECTACLE", "astronomical energy · deliberate signal · deep-time audience", "cultural"),
    "substrate-pluralism": ("SUBSTRATE PLURALISM", "biological · synthetic · hybrid persons", "bridge"),
    "inertial-confinement-fusion": ("INERTIAL FUSION ENERGY", "high-gain targets · repetition rate · wall-plug balance", "nuclear"),
    "beamed-sail-propulsion": ("BEAMED-SAIL PROPULSION", "remote laser array · light sail · precise beam control", "sail"),
    "antimatter-propulsion": ("ANTIMATTER PROPULSION", "production · containment · controlled annihilation · thrust", "antimatter"),
    "civilizational-entropy-management": ("CIVILIZATIONAL ENTROPY MANAGEMENT", "useful work · waste heat · long-term efficiency", "shells"),
    "beyond-zfc-foundations": ("BEYOND-ZFC FOUNDATIONS", "alternative axioms · translation · explicit assumptions", "foundations"),
    "hypercomputation": ("PHYSICAL HYPERCOMPUTATION", "idealized spacetime · infinite precision · falsifiable limits", "supernetwork"),
    "knowledge-closure": ("AUTOMATED DOMAIN SCIENCE", "hypothesis · experiment · model update · bounded scope", "network"),
    "subjective-time-compression": ("SUBJECTIVE TIME COMPRESSION", "accelerated cognition · synchronization · psychological continuity", "time"),
    "brain-brain-communication": ("NEURAL PERSON-TO-PERSON SIGNALING", "encoded intent · measured bandwidth · consent", "brainlink"),
    "anti-senescence-cellular-substrate": ("BIO-SYNTHETIC TISSUE REPLACEMENT", "integration · repair · failure containment", "capsule"),
    "ai-governance": ("AUDITABLE PUBLIC ADMINISTRATION", "traceable authority · appeal · human accountability", "civic"),
    "longtermism": ("LONG-TERM GOVERNANCE", "future generations · institutional continuity · uncertainty", "policy"),
    "cancer-cure": ("BROAD CANCER CONTROL", "prevention · early detection · multimodal treatment · access", "network"),
    "speciation": ("POST-HUMAN SPECIATION", "divergent bodies · reproductive isolation · shared rights", "ethics"),
    "existential-risk-hedge": ("EXISTENTIAL-RISK HEDGE", "redundancy · prevention · recovery · distributed resilience", "network"),
    "universal-disease-eradication": ("GLOBAL DISEASE SUPPRESSION", "surveillance · countermeasures · delivery · durable institutions", "network"),
    "engineered-pathogen-defense": ("RAPID BIOLOGICAL COUNTERMEASURES", "detect · characterize · design · manufacture · distribute", "network"),
    "procedural-infinite-worlds": ("AI-RESPONSIVE PROCEDURAL WORLDS", "persistent state · authorial control · player agency", "cultural"),
    "kugelblitz-drive": ("KUGELBLITZ DRIVE", "manufactured micro black hole · radiation · thrust", "propulsion"),
    "substrate-independent-humanity": ("SUBSTRATE-INDEPENDENT HUMANITY", "biological continuity · emulation · synthetic embodiment", "bridge"),
}


def motif(kind: str) -> str:
    common = 'stroke="#79dcff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    accent = 'stroke="#d7a6ff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    shapes = {
        "network": f'<g {common}><circle cx="310" cy="160" r="38"/><circle cx="205" cy="105" r="20"/><circle cx="420" cy="95" r="20"/><circle cx="210" cy="230" r="20"/><circle cx="425" cy="225" r="20"/><path d="M275 143L225 115M344 140L400 105M276 180L230 220M343 181L405 216"/></g><path d="M284 160h52M310 134v52" {accent}/>',
        "propulsion": f'<g {common}><path d="M245 115L395 160 245 205 275 160Z"/><path d="M245 135h-42M245 185h-42"/><circle cx="180" cy="160" r="13"/><circle cx="142" cy="160" r="8"/><circle cx="112" cy="160" r="5"/></g><path d="M275 120v80M292 126v68" {accent}/>',
        "capsule": f'<g {common}><rect x="210" y="85" width="200" height="150" rx="70"/><path d="M250 190q60-90 120 0M265 200h90"/></g><g {accent}><path d="M170 110v100M150 130l40 60M190 130l-40 60"/><circle cx="170" cy="160" r="12"/></g>',
        "abundance": f'<g {common}><path d="M165 215V120l65 35 55-50 70 40 70-30v100Z"/><rect x="215" y="178" width="58" height="37"/><rect x="300" y="165" width="70" height="50"/></g><g {accent}><path d="M185 105c20-35 55-35 75 0M370 95c18-28 45-28 63 0"/><circle cx="222" cy="86" r="10"/><circle cx="401" cy="78" r="9"/></g>',
        "bridge": f'<g {common}><circle cx="205" cy="160" r="67"/><circle cx="415" cy="160" r="67"/><path d="M265 135q45-55 90 0M265 185q45 55 90 0"/></g><g {accent}><path d="M180 135l50 50M180 185l50-50M390 125h50M390 160h50M390 195h50"/></g>',
        "reversible": f'<g {common}><rect x="210" y="118" width="75" height="84" rx="10"/><rect x="345" y="118" width="75" height="84" rx="10"/><path d="M160 145h50M285 145h60M420 145h50M470 175h-50M345 175h-60M210 175h-50"/></g><path d="M235 160l25-18v36zM395 160l-25-18v36z" {accent}/>',
        "chemistry": f'<g {common}><circle cx="165" cy="105" r="32"/><path d="M165 52v22M165 136v22M112 105h22M196 105h22"/><rect x="235" y="90" width="150" height="105" rx="8"/><path d="M235 125h150M275 90v105M330 90v105"/></g><g {accent}><circle cx="435" cy="115" r="18"/><circle cx="470" cy="145" r="14"/><circle cx="430" cy="178" r="12"/><path d="M450 126l12 10M457 156l-17 14"/></g>',
        "sensory": f'<g {common}><path d="M280 220q-55-45-25-110 22-48 80-35 55 12 55 75 0 45-40 65"/><circle cx="315" cy="135" r="20"/><path d="M335 135h72M255 125h-70M255 160h-88"/></g><g {accent}><path d="M405 115q40 20 0 40M425 100q65 35 0 70M185 105l-20 20 20 20M170 150l-24 18 24 18"/></g>',
        "projectile": f'<g {common}><path d="M125 160h300"/><path d="M385 135l45 25-45 25z"/><circle cx="160" cy="95" r="4"/><circle cx="230" cy="225" r="3"/><circle cx="365" cy="82" r="5"/></g><g {accent}><path d="M160 140h140M190 160h110M220 180h80"/><text x="305" y="115" fill="#d7a6ff" stroke="none" font-size="24">0.1c</text></g>',
        "shells": f'<g {common}><circle cx="310" cy="160" r="28"/><circle cx="310" cy="160" r="68"/><circle cx="310" cy="160" r="112"/><path d="M310 48v224M198 160h224"/></g><g {accent}><path d="M330 76q55 20 72 67M225 195q25 55 80 72"/><circle cx="310" cy="160" r="9" fill="#d7a6ff"/></g>',
        "ecology": f'<g {common}><path d="M180 190q65-130 180-60 70 43 10 105-60 61-145 8-65-40-10-100 50-54 115-18"/><circle cx="205" cy="113" r="18"/><circle cx="418" cy="185" r="18"/><circle cx="275" cy="240" r="18"/></g><g {accent}><path d="M220 120q90-60 180 50M400 200q-50 60-108 45M260 225q-65-40-45-94"/></g>',
        "ethics": f'<g {common}><path d="M310 80v150M310 130l-100 85M310 130l100 85"/><circle cx="310" cy="72" r="18"/><circle cx="205" cy="220" r="22"/><circle cx="415" cy="220" r="22"/></g><g {accent}><path d="M270 165h80M280 165l-20 38h40zM340 165l-20 38h40z"/></g>',
        "strings": f'<g {common}><path d="M230 60v200M390 60v200"/><path d="M245 90q145 65 0 140M375 90q-145 65 0 140"/></g><g {accent}><path d="M310 90c65 0 65 140 0 140s-65-140 0-140z"/><path d="M310 90l-12 18M310 90l15 15"/></g>',
        "justice": f'<g {common}><path d="M310 80v145M240 110h140M255 110l-38 75h76zM365 110l-38 75h76zM260 225h100"/></g><g {accent}><circle cx="310" cy="105" r="14"/><path d="M292 105h-28M328 105h28M310 91V65"/></g>',
        "policy": f'<g {common}><circle cx="310" cy="160" r="96"/><circle cx="310" cy="160" r="48"/><path d="M214 160h48M358 160h48M310 64v48M310 208v48"/></g><g {accent}><path d="M250 105q60-45 120 0M370 215q-60 45-120 0"/><path d="M360 94l14 13-19 5M260 226l-14-13 19-5"/></g>',
        "performer": f'<g {common}><circle cx="260" cy="130" r="42"/><path d="M200 225q15-65 60-65t60 65M350 100v120"/></g><g {accent}><path d="M350 125q20-45 40 0t40 0t40 0M350 170q20-30 40 0t40 0t40 0"/></g>',
        "navigation": f'<g {common}><circle cx="310" cy="160" r="18"/><circle cx="155" cy="95" r="12"/><circle cx="445" cy="85" r="12"/><circle cx="470" cy="225" r="12"/><path d="M165 102l130 50M433 94l-108 55M458 219l-133-52"/></g><g {accent}><path d="M125 95h60M415 85h60M440 225h60"/><circle cx="310" cy="160" r="45"/></g>',
        "defense": f'<g {common}><path d="M150 220q160-190 320 0M205 220q105-120 210 0M260 220q50-55 100 0"/><circle cx="310" cy="220" r="13"/></g><g {accent}><path d="M180 90l55 65M430 110l-55 55M310 65v85"/><circle cx="180" cy="90" r="7"/><circle cx="430" cy="110" r="7"/></g>',
        "material": f'<g {common}><path d="M215 95h190v130H215zM250 95v130M290 95v130M330 95v130M370 95v130M215 130h190M215 165h190M215 200h190"/></g><g {accent}><path d="M165 105q30 20 0 40t0 40M455 105q-30 20 0 40t0 40"/><circle cx="310" cy="165" r="23"/></g>',
        "consciousness": f'<g {common}><path d="M245 215q-55-85 5-145 70-55 140 0 55 55 0 145"/><circle cx="275" cy="125" r="12"/><circle cx="345" cy="110" r="12"/><circle cx="365" cy="175" r="12"/><circle cx="285" cy="185" r="12"/><path d="M285 125l48-12M353 120l10 43M353 179l-56 4M282 173l-5-36"/></g><g {accent}><path d="M205 90l-45-25M215 160h-60M410 90l45-25M405 165h55"/></g>',
        "supernetwork": f'<g {common}><circle cx="310" cy="160" r="88"/><circle cx="310" cy="160" r="35"/><circle cx="220" cy="90" r="16"/><circle cx="415" cy="90" r="16"/><circle cx="215" cy="230" r="16"/><circle cx="420" cy="225" r="16"/><path d="M235 102l45 32M399 102l-58 35M232 221l54-38M403 216l-62-39"/></g><circle cx="310" cy="160" r="10" fill="#d7a6ff"/>',
        "matter": f'<g {common}><rect x="175" y="105" width="42" height="42"/><rect x="220" y="150" width="42" height="42"/><rect x="175" y="195" width="42" height="42"/><path d="M300 170h70M350 145l25 25-25 25"/><circle cx="430" cy="170" r="66"/><path d="M385 170q45-80 90 0q-45 80-90 0z"/></g>',
        "foundations": f'<g {common}><circle cx="245" cy="160" r="78"/><circle cx="375" cy="160" r="78"/><path d="M310 82v156"/></g><g {accent}><path d="M210 145h70M340 145h70M225 178h40M355 178h40"/><circle cx="310" cy="160" r="18"/></g>',
        "biosphere": f'<g {common}><path d="M165 220h290M190 220q15-145 120-145t120 145"/><path d="M250 200q20-65 60-80 40 15 60 80"/><path d="M310 120v95M310 150l-35 30M310 165l35 25"/></g><g {accent}><path d="M225 110q85-65 170 0M395 190q-85 65-170 0"/></g>',
        "protocol": f'<g {common}><circle cx="180" cy="160" r="25"/><circle cx="440" cy="160" r="25"/><path d="M205 145h210M415 175H205"/></g><g {accent}><rect x="270" y="115" width="80" height="90" rx="12"/><path d="M285 140h50M285 160h50M285 180h32"/></g>',
        "civic": f'<g {common}><circle cx="185" cy="105" r="18"/><circle cx="435" cy="105" r="18"/><circle cx="310" cy="235" r="18"/><path d="M200 115l95 108M420 115l-95 108M210 105h200"/></g><g {accent}><rect x="265" y="115" width="90" height="72" rx="8"/><path d="M282 138h56M282 158h56"/></g>',
        "cultural": f'<g {common}><circle cx="175" cy="160" r="30"/><circle cx="445" cy="160" r="30"/><path d="M205 140q105-70 210 0M415 180q-105 70-210 0"/></g><g {accent}><path d="M275 125h70l25 35-25 35h-70l-25-35z"/><circle cx="290" cy="160" r="8"/><circle cx="330" cy="160" r="8"/></g>',
        "nuclear": f'<g {common}><circle cx="310" cy="160" r="82"/><circle cx="285" cy="145" r="24"/><circle cx="335" cy="145" r="24"/><circle cx="310" cy="185" r="24"/></g><g {accent}><path d="M310 55v35M310 230v35M205 160h35M380 160h35"/><path d="M420 95l-25 25M225 200l-25 25"/></g>',
        "quark": f'<g {common}><circle cx="310" cy="160" r="105"/><circle cx="310" cy="160" r="65"/><circle cx="310" cy="160" r="26"/></g><g {accent}><circle cx="290" cy="148" r="8" fill="#d7a6ff"/><circle cx="330" cy="148" r="8" fill="#d7a6ff"/><circle cx="310" cy="182" r="8" fill="#d7a6ff"/><path d="M290 148l40 0M300 157l10 25M320 157l-10 25"/></g>',
        "settlement": f'<g {common}><path d="M115 235h410"/><path d="M185 235q15-130 125-130t125 130"/><rect x="235" y="178" width="70" height="57" rx="5"/><rect x="335" y="165" width="65" height="70" rx="5"/><path d="M270 178v-30M367 165v-38"/><circle cx="475" cy="83" r="25"/></g><g {accent}><path d="M205 128q105-70 210 0M160 235q45-35 90 0M390 235q45-35 90 0"/><path d="M262 205h16M355 195h25"/></g>',
        "landing": f'<g {common}><path d="M110 235q200-55 420 0"/><path d="M265 90h90l25 95H240z"/><path d="M250 180l-45 45M370 180l45 45M280 185v38M340 185v38"/><circle cx="310" cy="130" r="18"/></g><g {accent}><path d="M275 220l-18 40M310 220v48M345 220l18 40"/><path d="M190 125q-45 35-55 90M430 112q55 25 75 85"/></g>',
        "mining": f'<g {common}><path d="M170 105l95-35 95 30 48 78-55 72-120 4-78-67z"/><circle cx="235" cy="135" r="18"/><circle cx="320" cy="190" r="25"/><circle cx="350" cy="120" r="12"/><path d="M410 145h62v72h-62M472 165h45M472 198h45"/></g><g {accent}><path d="M390 180l-65-5M390 195l-55 22"/><circle cx="525" cy="165" r="7"/><circle cx="535" cy="200" r="5"/><circle cx="500" cy="225" r="6"/></g>',
        "longevity": f'<g {common}><circle cx="275" cy="160" r="95"/><circle cx="275" cy="160" r="26"/><circle cx="225" cy="115" r="13"/><circle cx="330" cy="105" r="12"/><circle cx="220" cy="210" r="11"/><circle cx="345" cy="205" r="14"/><path d="M242 130l20 19M303 140l20-25M252 181l-25 20M300 180l35 18"/></g><g {accent}><circle cx="430" cy="160" r="62"/><path d="M430 160v-35M430 160l28 18M400 95l30-25 30 25"/></g>',
        "quantum": f'<g {common}><path d="M185 90h250v145H185zM235 90v145M285 90v145M335 90v145M385 90v145M185 138h250M185 186h250"/><circle cx="235" cy="138" r="12"/><circle cx="335" cy="186" r="12"/><circle cx="385" cy="138" r="12"/></g><g {accent}><circle cx="310" cy="160" r="70"/><path d="M205 65h210M205 260h210M205 65l-25 20M415 65l25 20M205 260l-25-20M415 260l25-20"/></g>',
        "elevator": f'<g {common}><path d="M120 245q190-115 380 0"/><path d="M310 235V65"/><circle cx="310" cy="50" r="18"/><rect x="287" y="130" width="46" height="55" rx="7"/><path d="M333 155h60M393 140v30M393 140l22 15-22 15"/></g><g {accent}><path d="M230 195q80-50 160 0M270 212q40-25 80 0"/><circle cx="310" cy="245" r="12"/><path d="M300 105h20M300 93h20"/></g>',
        "time": f'<g {common}><circle cx="235" cy="160" r="82"/><circle cx="395" cy="160" r="60"/><path d="M235 160v-45M235 160l35 25M395 160v-30M395 160l-22 18"/></g><g {accent}><path d="M185 78q50-38 100 0M285 242q-50 38-100 0M360 105q35-28 70 0M430 215q-35 28-70 0"/><path d="M275 68l14 14-20 4M195 252l-14-14 20-4M420 96l14 12-18 5M370 224l-14-12 18-5"/></g>',
        "ring": f'<g {common}><circle cx="310" cy="160" r="88"/><ellipse cx="310" cy="160" rx="165" ry="52"/><path d="M222 160q88 50 176 0M310 72v176"/></g><g {accent}><ellipse cx="310" cy="160" rx="150" ry="38"/><rect x="445" y="144" width="35" height="32" rx="5"/><rect x="140" y="148" width="30" height="25" rx="4"/></g>',
        "swarm": f'<g {common}><path d="M185 100l28 48h-56zM310 72l28 48h-56zM435 105l28 48h-56zM235 195l28 48h-56zM385 195l28 48h-56z"/><path d="M205 140l80-50M335 92l80 35M210 147l15 50M410 150l-18 47M263 218h94"/></g><g {accent}><circle cx="310" cy="160" r="24"/><path d="M286 160h-62M334 160h62M310 136v-35M310 184v35"/></g>',
        "antimatter": f'<g {common}><circle cx="250" cy="160" r="55"/><circle cx="370" cy="160" r="55"/><path d="M195 160q115-120 230 0M195 160q115 120 230 0M170 115q140-85 280 0M170 205q140 85 280 0"/></g><g {accent}><path d="M230 160h40M250 140v40M350 160h40"/><circle cx="310" cy="160" r="13" fill="#d7a6ff"/></g>',
        "relay": f'<g {common}><circle cx="155" cy="160" r="36"/><circle cx="310" cy="110" r="23"/><circle cx="455" cy="170" r="42"/><path d="M190 150l96-32M332 120l84 35"/><path d="M210 190l70 35 80-20 55 20"/></g><g {accent}><circle cx="235" cy="135" r="7"/><circle cx="375" cy="140" r="7"/><path d="M225 125l20 20M365 130l20 20"/></g>',
        "brainlink": f'<g {common}><path d="M155 220q-45-60-12-125 35-60 100-25 45 28 25 92-8 30-35 48M465 220q45-60 12-125-35-60-100-25-45 28-25 92 8 30 35 48"/><circle cx="220" cy="125" r="13"/><circle cx="400" cy="125" r="13"/></g><g {accent}><path d="M240 115q70-65 140 0M240 138q70 65 140 0"/><circle cx="310" cy="95" r="7"/><circle cx="310" cy="158" r="7"/></g>',
        "sail": f'<g {common}><rect x="135" y="105" width="65" height="110" rx="6"/><path d="M150 105v110M170 105v110M185 105v110"/><path d="M200 125l185 25M200 160h185M200 195l185-25"/><path d="M390 90l90 70-90 70z"/></g><g {accent}><path d="M480 160h45M500 145l25 15-25 15"/><circle cx="420" cy="160" r="8"/></g>',
    }
    return shapes[kind]


def build_svg(title: str, subtitle: str, kind: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-labelledby="title desc">
  <title id="title">{html.escape(title.title())}</title>
  <desc id="desc">Conceptual diagram: {html.escape(subtitle)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#081522"/><stop offset="1" stop-color="#211334"/></linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#b9dfff" stroke-opacity=".055"/></pattern>
  </defs>
  <rect width="640" height="360" rx="18" fill="url(#bg)"/>
  <rect width="640" height="360" rx="18" fill="url(#grid)"/>
  <g transform="translate(0 8)">{motif(kind)}</g>
  <rect x="34" y="292" width="572" height="1" fill="#79dcff" opacity=".28"/>
  <text x="34" y="321" fill="#f1f8ff" font-family="system-ui, sans-serif" font-size="19" font-weight="650" letter-spacing="1.5">{html.escape(title)}</text>
  <text x="34" y="343" fill="#a7bdd0" font-family="system-ui, sans-serif" font-size="12" letter-spacing=".55">{html.escape(subtitle)}</text>
</svg>
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(MANIFEST.read_text())
    for tech_id, (title, subtitle, kind) in TARGETS.items():
        fallback_path = OUT / f"{tech_id}.svg"
        fallback_path.write_text(build_svg(title, subtitle, kind))
        generated_path = GENERATED / f"{tech_id}.png"
        has_generated_figure = generated_path.is_file()
        selected_path = generated_path if has_generated_figure else fallback_path
        manifest[tech_id] = {
            "name": title.title(),
            "query": "",
            "article": "",
            "page": "",
            "image_url": "",
            "image_path": str(selected_path.relative_to(ROOT)),
            "extract": subtitle,
            "status": "ok",
            "score": 1.0,
            "reason": (
                "Reviewed CIVX AI-generated editorial illustration for a speculative milestone."
                if has_generated_figure
                else "Purpose-built CIVX conceptual diagram fallback."
            ),
            "credit_label": (
                "CIVX · AI-generated editorial illustration"
                if has_generated_figure
                else "CIVX · conceptual illustration"
            ),
        }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    entries = {}
    credits = {}
    for tech_id, item in manifest.items():
        if not item.get("image_path"):
            continue
        entries[tech_id] = item["image_path"]
        if item.get("credit_label"):
            credits[tech_id] = {"label": item["credit_label"], "url": item.get("page") or ""}
        else:
            credits[tech_id] = {"article": item.get("article"), "url": item.get("page")}
    IMAGES_JS.write_text(
        "// Auto-generated from _image_manifest.json. Do not edit by hand.\n"
        "// Maps tech id -> image path + attribution.\n"
        "window.TECH_IMAGES = " + json.dumps(entries, indent=2, ensure_ascii=False) + ";\n"
        "window.TECH_IMAGE_CREDITS = " + json.dumps(credits, indent=2, ensure_ascii=False) + ";\n"
    )
    generated_count = sum((GENERATED / f"{tech_id}.png").is_file() for tech_id in TARGETS)
    print(
        f"wrote {len(TARGETS)} SVG fallbacks; selected {generated_count} generated PNGs; "
        f"images.js now has {len(entries)} entries"
    )


if __name__ == "__main__":
    main()
