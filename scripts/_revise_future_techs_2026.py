#!/usr/bin/env python3
"""Apply the 2026 evidence and editorial revision of the future-tech tree.

The script is deliberately data-driven and idempotent. It keeps stable tech IDs
for old links while revising user-facing names, claims, dependencies, forecast
metadata, and the linked translations/unlocks/extended notes.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
DETAILS = ROOT / "details_extra.js"
TRANSLATIONS = ROOT / "translations.js"
UNLOCKS = ROOT / "unlocks.js"


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


REVISIONS = {
    "humanoid-robot": {
        "name": "General-Purpose Robotic Labor",
        "year": "2035",
        "desc": "Robotic systems that can perform a broad range of useful physical work in human-built environments without a task-specific machine for every job. Humanoid form is one option, not the milestone itself. Current robots can walk, manipulate selected objects, and follow demonstrations, but reliability, dexterity, safe operation around people, maintenance cost, and learning from limited data remain major barriers. This node is reached when robots can change tasks across warehouses, construction sites, farms, and care settings with independently measured productivity and acceptable incident rates—not when a staged prototype completes a short demonstration.",
    },
    "agi": {
        "year": "2040",
        "desc": "An AI system able to learn and perform a wide range of economically and scientifically useful cognitive tasks with human-level flexibility, including unfamiliar tasks for which it was not explicitly trained. Fluent conversation or benchmark performance alone does not establish general intelligence. A defensible milestone would require robust transfer, long-horizon planning, calibrated uncertainty, independent learning, and reliable operation outside curated evaluations. Scaling may be sufficient, or new architectures and training methods may be needed; no accepted test or credible completion date exists. The node is therefore an uncertain scientific and engineering scenario rather than a scheduled 2040 invention.",
    },
    "brain-computer-interface": {
        "name": "High-Bandwidth Bidirectional Neuroprosthesis",
        "year": "2045",
        "desc": "A clinically useful interface that both reads from and writes to the nervous system at sufficient bandwidth to restore complex movement, speech, touch, vision, or hearing. Brain-computer interfaces already exist, so the future milestone is durable, high-channel-count communication outside tightly supervised laboratories. The hard problems are long-term biocompatibility, stable decoding as neural signals change, safe stimulation, surgical risk, power and telemetry, and evidence that benefits exceed harms. Restorative applications for paralysis and sensory loss should be evaluated separately from elective cognitive augmentation, which carries different medical and political risks.",
    },
    "lab-grown-meat": {
        "name": "Cultivated Meat at Cost and Scale Parity",
        "year": "2035",
        "desc": "Cultivated meat is already produced and approved in limited markets; the future milestone is competitive production at food-industry scale. Cells must grow in inexpensive food-grade media, mature in large bioreactors without contamination, develop convincing fat and texture, and meet energy, land, water, and lifecycle-emissions targets. Ground products are likely to scale before structured steaks. Success means repeated commercial production at prices and environmental performance comparable with conventional meat, supported by transparent safety regulation—not merely another restaurant tasting or small approval.",
    },
    "synthetic-biology": {
        "name": "Predictable Genome-Scale Bioengineering",
        "year": "2040",
        "desc": "Synthetic biology already engineers organisms; the future milestone is reliable design at genome and ecosystem scale. Engineers would specify a function, predict how it interacts with cellular regulation and evolution, and obtain the intended behavior across manufacturing conditions without years of trial and error. Better biological models, automated laboratories, standardized genetic components, containment, and monitoring are all required. Applications include medicines, low-carbon chemicals, food proteins, materials, and environmental sensing, but predictable behavior and biosafety—not the mere ability to edit DNA—define this node.",
    },
    "quantum-applications": {
        "name": "Fault-Tolerant Quantum Advantage",
        "year": "2050",
        "desc": "Fault-tolerant quantum advantage means completing a valuable computation on logical qubits with lower verified cost or better accuracy than the best classical alternative. It is not defined by a raw physical-qubit count. Error-correction overhead depends on hardware error rates, code choice, connectivity, algorithm depth, and the target workload; a fixed claim of millions of physical qubits per logical qubit is therefore misleading. The central barriers are logical error rates, control and cryogenic infrastructure, scalable fabrication, and finding applications whose quantum speedup survives data-loading and verification costs. The likely timing remains uncertain.",
    },
    "carbon-capture-scale": {
        "name": "Direct Air Carbon Removal",
        "year": "2045",
        "prereqs": ["renewable-grid", "climate-science"],
        "desc": "Removing carbon dioxide directly from ambient air and storing it durably at climate-relevant scale. This is distinct from capturing concentrated emissions at a factory stack. Because air contains only about 0.04% CO₂, sorbent regeneration, heat, electricity, water, transport, storage integrity, and honest lifecycle accounting dominate the cost. The milestone is independently verified removal of hundreds of millions of tonnes per year with low-carbon energy and century-scale storage—not announced project capacity or CO₂ used for short-lived products. Direct air capture is one carbon-removal pathway and should not be conflated with BECCS, enhanced weathering, or ocean alkalinity enhancement.",
    },
    "universal-basic-income": {"name": "Sustained Universal Basic Income System"},
    "liquid-democracy": {"name": "Large-Scale Liquid Democracy"},
    "network-state": {"name": "Legally Recognized Network Polity"},
    "ai-governance": {"name": "Auditable Algorithmic Public Administration"},
    "transhumanism": {"name": "Clinical Human Augmentation", "year": "2050"},
    "longtermism": {"name": "Long-Term Governance Institutions"},
    "generative-art": {"name": "AI-Native Co-Creation"},
    "metaverse": {"name": "Persistent Interoperable Virtual Worlds"},
    "decentralized-autonomous-org": {"name": "Legally Integrated DAO"},
    "neuromorphic-chip": {"name": "Commercial Neuromorphic Computing"},
    "cancer-cure": {
        "name": "Broad Cancer Control",
        "year": "2060",
        "desc": "A broad reduction in cancer mortality through prevention, early detection, molecular classification, surgery, radiotherapy, targeted drugs, immune therapies, and adaptive combinations. Cancer is hundreds of evolving diseases, so no single immune mechanism or vaccine is a universal cure. The milestone is population-level control: most common cancers detected early or managed for long periods, with substantially lower age-adjusted mortality and treatment toxicity. Personalized neoantigen vaccines, CAR-T cells, checkpoint inhibitors, radioligands, and AI-assisted drug design are promising components, but resistance, metastasis, unequal access, and tumors lacking safe targets remain central limitations.",
    },
    "ai-judge": {
        "name": "AI-Assisted Judicial Administration",
        "year": "2035",
        "prereqs": ["large-language-model", "code-of-law"],
        "desc": "AI tools that help courts retrieve authority, translate records, organize evidence, draft routine text, identify inconsistent filings, and manage schedules while accountable humans retain coercive legal authority. The key requirement is not ingesting every statute; it is producing traceable sources, calibrated uncertainty, contestable reasons, audit logs, privacy protection, and equal performance across populations and case types. Estonia's frequently repeated autonomous 'AI judge' story mischaracterized procedural automation. Bail, sentencing, findings of fact, and final judgments require especially strong due-process safeguards, meaningful appeal, and clearly assigned human responsibility.",
    },
    "metamaterials": {"name": "Mass-Manufactured Active Metasurfaces", "year": "2045"},
    "pulsar-navigation": {"name": "Operational Autonomous X-Ray Pulsar Navigation", "year": "2040"},
    "formal-mathematics": {"name": "Routine Machine-Verified Mathematics"},
    "gravitational-wave-spectroscopy": {"name": "Precision Gravitational-Wave Astronomy", "year": "2045"},
    "fusion-power": {
        "name": "Utility-Scale Fusion Electricity",
        "year": "2060",
        "desc": "A fusion plant that delivers dependable net electricity to a public grid over sustained campaigns, including the electricity used by magnets, heating, fuel processing, cooling, and maintenance. Scientific breakeven in a target or plasma is not the same milestone. Commercial systems must survive neutron damage, breed and account for tritium where required, exhaust heat, replace activated components remotely, achieve useful availability, and compete with other low-carbon power. Tokamaks, stellarators, inertial systems, and alternative concepts remain active approaches. The date is contingent: even ITER's revised baseline places deuterium-tritium operation well after its initial plasma program.",
    },
    "inertial-confinement-fusion": {
        "name": "High-Repetition Inertial Fusion Energy",
        "year": "2065",
        "prereqs": ["plasma-physics", "advanced-chip-manufacturing", "fusion-materials"],
        "desc": "An inertial-fusion power system that repeats high-gain target shots many times per second and converts the released energy into reliable grid electricity. NIF achieved target ignition in 2022, but a power plant needs inexpensive precision targets, efficient drivers, rapid chamber clearing, blanket and optical materials that survive repeated bursts, tritium breeding, remote maintenance, and a favorable wall-plug energy balance. This node therefore marks an integrated power station rather than the already achieved scientific demonstration of inertial-confinement fusion.",
    },
    "personalized-medicine": {
        "name": "Real-Time Multi-Omic Medicine",
        "year": "2055",
        "prereqs": ["gene-sequencing", "deep-learning"],
        "desc": "Clinical decisions continuously informed by a patient's genome, transcriptome, proteins, metabolites, microbiome, imaging, exposures, and longitudinal physiology. Personalized medicine already exists in oncology and pharmacogenomics; the future milestone is routine, prospective evidence that integrated measurements improve outcomes across common disease. Models must distinguish causation from correlation, work across ancestries and care settings, protect unusually revealing data, and recommend actions that clinicians can understand and test. The value lies in better prevention and treatment selection, not in collecting every possible biomarker.",
    },
    "genetic-disease-eradication": {
        "name": "Routine Prevention and Treatment of Monogenic Disease",
        "year": "2070",
        "desc": "Routine prevention or somatic treatment of many severe single-gene disorders through carrier screening, reproductive choice, gene replacement, base or prime editing, RNA therapy, and durable cell therapy. Literal eradication is neither technically plausible nor ethically appropriate: new mutations continually arise, many conditions are polygenic, penetrance varies, and disability policy must not reduce people to genotypes. The milestone is broad voluntary access to safe treatment and prevention for well-understood monogenic disease, with consent, disability rights, and protection against coercive reproductive policy.",
    },
    "space-habitat": {
        "name": "Large Rotating Space Settlement",
        "year": "2100",
        "prereqs": ["closed-loop-life-support", "asteroid-mining", "orbital-servicing-refueling"],
        "desc": "A permanently inhabited rotating settlement that supplies partial or Earth-like artificial gravity, radiation shielding, closed-loop water and air processing, food production, and maintainable civic infrastructure. It is distinct from a small station or a Mars base and need not depend on Mars settlement. The milestone requires safe rotation geometry, shielding made largely from off-Earth material, ecological stability, fire and toxic-leak control, repairable life support, and an economy that can support residents for years without emergency evacuation to Earth.",
    },
    "terraforming-mars": {
        "name": "Mars Paraterraforming",
        "year": "2150",
        "prereqs": ["mars-colony", "closed-loop-life-support", "synthetic-biology"],
        "desc": "Creating large enclosed Martian environments with managed pressure, temperature, water cycles, radiation shielding, and engineered ecosystems. This is paraterraforming: roofs, membranes, caves, or linked pressure vessels make regional habitable landscapes without claiming that the entire planet has acquired a breathable atmosphere. Mars does not appear to contain enough readily accessible carbon dioxide for conventional near-term global terraforming, while imported volatiles and planetary-scale warming would require extreme energy and material flows. Full terraforming remains an open-ended planetary project, not a completed 2100 technology.",
    },
    "seti-first-contact": {
        "name": "Detection of Extraterrestrial Technology",
        "year": "2090",
        "prereqs": ["telescope", "radio-wireless", "large-language-model"],
        "desc": "A independently confirmed observation best explained by extraterrestrial technology: a structured radio or optical signal, an artificial atmospheric pollutant, anomalous waste heat, or another technosignature that survives instrumental and natural explanations. Detection could occur at any time and does not require an interstellar probe. Confirmation would require repeated observations, independent instruments, transparent data, and careful separation of detection from communication or physical contact. The node should therefore have an unknown horizon rather than a scheduled 2090 date.",
    },
    "universal-disease-eradication": {
        "name": "Global Disease Suppression Infrastructure",
        "year": "2090",
        "desc": "A durable global system that prevents, detects, and rapidly suppresses a large share of infectious disease while expanding access to treatment for genetic and chronic illness. Literal universal eradication is impossible to promise: animal reservoirs, pathogen evolution, new spillovers, new mutations, conflict, and failures of health delivery persist. The milestone is resilient surveillance, vaccination, ventilation, sanitation, rapid diagnostics, adaptable countermeasures, primary care, and logistics capable of containing outbreaks early and driving selected diseases toward regional elimination. Success is measured by sustained reductions in mortality and transmission, not declarations that disease has ended.",
    },
    "room-temp-superconductor": {
        "name": "Ambient-Condition Superconductor",
        "year": "2070",
        "desc": "A material that carries useful current without resistance at or near ordinary temperature and pressure, with adequate critical current, magnetic-field tolerance, mechanical toughness, manufacturability, and stability for real devices. High transition temperature alone is insufficient, particularly when it requires megabar pressure or produces fragile microscopic samples. No physical principle guarantees that a practical ambient-condition superconductor exists, so this remains a contingent materials-discovery node with an unknown horizon. If found, it could transform magnets, motors, power equipment, scientific instruments, and some transport systems, but it is not a prerequisite for a space elevator.",
    },
    "space-elevator": {
        "prereqs": ["nanotechnology", "reusable-rocket", "orbital-servicing-refueling"],
        "desc": "An Earth-anchored tether extending beyond geostationary orbit, along which electrically powered climbers carry cargo. The decisive barrier is a tether material with sufficient specific tensile strength, defect tolerance, manufacturable length, and resistance to weather, atomic oxygen, radiation, debris, and oscillation—not room-temperature superconductivity. Carbon nanotubes, graphene, and related fibers have exceptional microscopic properties but have not retained them in defect-tolerant bulk cables thousands of kilometres long. Even with a material breakthrough, deployment, collision avoidance, equatorial governance, repair, and controlled failure modes would be civilization-scale engineering problems.",
    },
    "nuclear-pulse-propulsion": {
        "name": "Nuclear-Pulse Spacecraft Demonstration",
        "year": "2060",
        "prereqs": ["nuclear-weapon", "reusable-rocket", "closed-loop-life-support"],
        "desc": "A spacecraft accelerated by a sequence of external nuclear explosions, following the Project Orion studies begun in 1958. Each pulse transfers momentum through a pusher plate and shock-absorber system, producing high thrust and much higher effective exhaust velocity than chemical rockets. The concept is not a newly invented 2060 technology; the future milestone would be a legal, remotely operated demonstration with validated plate survival and fallout containment. Nuclear-test treaties, launch safety, proliferation, electromagnetic pulse, public legitimacy, and catastrophic launch failure are at least as important as the propulsion engineering.",
    },
    "bussard-ramjet": {
        "name": "Ram-Augmented Interstellar Propulsion",
        "year": "2300",
        "desc": "Interstellar propulsion that uses a large electromagnetic field to collect or deflect sparse interstellar plasma, reducing carried reaction mass or providing magnetic braking. The original Bussard ramjet assumed collected protons could efficiently sustain fusion, but low density, fusion cross-sections, radiation losses, and drag make the classic self-fuelling design unlikely to produce net thrust. More credible descendants use a carried fuel supply, a pre-deployed particle stream, or the magnetic scoop primarily as a sail and brake. This node represents those conditional ram-augmented concepts, not the classic ramjet as an inevitable achieved machine.",
    },
    "antimatter-weapon": {
        "desc": "A weapon using controlled matter-antimatter annihilation. One milligram of antimatter annihilating with one milligram of ordinary matter releases about 1.8×10¹¹ joules—roughly 43 tonnes of TNT, not 43 kilotons. One gram of antimatter would yield about 43 kilotons. Production inefficiency, storage losses, neutral antimatter handling, accidental release, and the inability to manufacture macroscopic quantities dominate feasibility. Antimatter is extraordinarily energy-dense, but the energy must first be supplied during production; it is an energy carrier rather than a primary source. Any weaponization pathway would also present extreme proliferation and fail-safe problems.",
    },
    "relativistic-kinetic-weapon": {
        "desc": "A projectile accelerated to a substantial fraction of light speed. A one-tonne mass at 0.1c carries about 4.5×10¹⁷ joules, equivalent to roughly 108 megatons of TNT—catastrophic, but more than a million times below estimates for the Chicxulub impact. Chicxulub-scale energy at 0.1c would require a projectile of millions of tonnes. The principal challenges are the propulsion energy, beam or guidance accuracy over astronomical distance, collisions with interstellar dust, and detection long before arrival. A near miss would continue through space; it would not automatically generate a gamma-ray burst. This is best treated as a strategic implication of relativistic transport, not a likely weapon program.",
    },
    "kardashev-type-ii": {
        "year": "2700",
        "desc": "A civilization using power on the scale of a star, approximately 10²⁶ watts, through a mature Dyson swarm or equivalent stellar infrastructure. Compared with present global primary-energy use of roughly 2×10¹³ watts, this is about five trillion times larger—not ten billion. Reaching the scale requires enormous off-world mining, manufacturing, orbital control, heat rejection, and governance; it does not require enclosing the star in a rigid shell. The date is only a distant scenario anchor, and full Type II capability may take far longer than the centuries represented by this tree.",
    },
    "black-hole-engineering": {"year": "2750"},
    "antimatter-propulsion": {"year": "2600"},
    "kugelblitz-drive": {
        "year": "2800",
        "prereqs": ["black-hole-engineering", "antimatter-propulsion"],
        "desc": "A proposed starship powered by Hawking radiation from a manufactured microscopic black hole. Published feasibility estimates discuss black holes around 10⁹ kilograms—about a million tonnes—not 10⁶ kilograms, balancing useful power against a lifetime long enough for a voyage. Creation would require focusing an extraordinary gamma-ray energy pulse; feeding the hole and converting highly penetrating gamma radiation into directed thrust are unresolved. A simple reflective parabolic mirror is not known to work for the relevant gamma rays. The concept is compatible with semiclassical relativity in outline, but its manufacture, containment, and propulsion system remain speculative engineering far beyond demonstrated capability.",
    },
    "vacuum-energy-extraction": {
        "name": "Quantum Vacuum Energy Limits",
        "category": "knowledge",
        "year": "2780",
        "prereqs": ["quantum-gravity", "dark-sector-physics"],
        "desc": "Experimental and theoretical determination of whether quantum-vacuum phenomena can ever provide net usable work. Casimir forces and the dynamical Casimir effect are real, but they do not demonstrate a cyclic source of free energy: restoring a system to its initial state requires accounting for the work used to move boundaries or drive fields. No accepted mechanism extracts unlimited zero-point energy without violating ordinary thermodynamics. This node is therefore a scientific constraint with an unknown horizon, not an energy technology. Any positive result would require genuinely new physics and reproducible energy accounting.",
    },
    "dark-energy-engineering": {
        "name": "Controllable Dark-Energy Hypothesis",
        "category": "knowledge",
        "year": "2790",
        "prereqs": ["quantum-gravity", "dark-sector-physics"],
        "desc": "A hypothetical discovery that the phenomenon driving cosmic acceleration can be created, modified, or coupled to locally. Present observations constrain dark energy through cosmology; they do not identify a laboratory material with controllable negative pressure, nor show that the cosmological constant can be engineered. Equating dark energy with convenient negative-energy matter is unsupported. This node records a possible new-physics branch only. It has no forecast date and should not be read as a normal successor to Casimir experiments.",
    },
    "warp-drive": {
        "name": "Warp-Spacetime Feasibility Tests",
        "category": "knowledge",
        "year": "2800",
        "prereqs": ["quantum-gravity", "relativity"],
        "desc": "Tests of whether any physically realizable spacetime can reproduce useful warp-drive behavior. Alcubierre's metric is a mathematical geometry, not an engine design. Superluminal versions require violations of standard energy conditions, introduce severe causal and horizon problems, and provide no demonstrated way to create, steer, or stop the required stress-energy distribution. Some positive-energy constructions describe subluminal shells, but these are not faster-than-light propulsion and still require an independent means of motion. The node belongs to speculative gravitational physics with an unknown horizon; current evidence does not justify forecasting an operational drive.",
    },
    "cosmic-string-ftl": {
        "name": "Cosmic-String Chronology Models",
        "category": "knowledge",
        "year": "2800",
        "desc": "Theoretical study of causality around hypothetical cosmic strings. Gott's idealized construction uses two effectively infinite strings moving at relativistic speed to produce closed timelike curves under special global conditions; it is not a practical shortcut or a design for faster-than-light travel. Cosmic strings have not been observed, manipulating them would be beyond any known engineering, and follow-up analyses found major realizability and chronology-protection problems. This node documents an unresolved spacetime pathology, not an expected transportation technology, and therefore has no forecast date.",
    },
    "p-vs-np-resolved": {
        "name": "Resolution of P versus NP",
        "desc": "A proof establishing whether every problem whose solution can be verified efficiently can also be solved efficiently. P versus NP remains an open mathematical problem, and neither AI nor quantum computing provides a date by which it must be settled. A proof that P≠NP would not automatically establish the practical hardness of every cryptographic problem; a proof that P=NP might be nonconstructive or hide unusable constants. This is an undated scientific milestone, not a technology forecast, though its resolution could reshape algorithms, optimization, cryptography, and the theory of proof.",
    },
    "continuum-hypothesis-resolution": {
        "name": "Post-ZFC Foundational Consensus",
        "desc": "A broad mathematical consensus about which additional axioms are most useful beyond ZFC, with explicit translation between alternative foundations. Gödel and Cohen showed that the continuum hypothesis is independent of ZFC, so selecting an axiom that implies or refutes it is not a definitive proof within ZFC. Future mathematicians may favor forcing axioms, large-cardinal principles, multiverse views, or plural foundations for different purposes. The milestone is a transparent methodological consensus—not discovery of a uniquely compelled answer that current mathematics has somehow overlooked.",
    },
    "hypercomputation": {
        "name": "Physical Hypercomputation Hypotheses",
        "prereqs": ["quantum-gravity", "formal-mathematics"],
        "desc": "Investigation of whether any physically possible process can compute functions that a Turing machine cannot. Zeno machines assume infinitely many operations in finite time; Malament-Hogarth proposals rely on special spacetime structures; oracle models define extra capability rather than constructing it. All require idealizations involving infinite precision, unbounded resources, exotic causal structure, or unknown quantum gravity. Resolving P versus NP would not enable hypercomputation. This is an undated new-physics hypothesis, not forecast hardware. If physical law forbids it, the negative result is itself the scientifically meaningful milestone.",
    },
    "trans-computable-mathematics": {
        "name": "Conditional Trans-Turing Mathematics",
        "desc": "Mathematics that would become experimentally accessible only if a reproducible physical hypercomputer existed. Without such a device, uncomputable objects such as general busy-beaver values or arbitrary digits of Chaitin's Ω remain definable but not mechanically evaluable. The branch is explicitly conditional and does not follow from faster conventional, quantum, or superintelligent computation. It should be read as an exploration of the consequences of hypothetical physics, with an unknown horizon and no claim that the arithmetical hierarchy will collapse in practice.",
    },
    "knowledge-closure": {
        "name": "Domain-Specific Automated Science",
        "desc": "Automated systems that can generate hypotheses, design experiments, interpret results, reproduce findings, and maintain comprehensive models within well-bounded scientific domains. No civilization can certify that every empirically determinable fact is known: new systems, initial conditions, measurement precision, and questions continually appear, while formal limits prevent universal proof of completeness. A defensible milestone is domain-specific closure—for example, exhaustive reaction prediction within a defined chemical space—paired with explicit uncertainty and reproducibility. Science changes form; it does not reach a final universal endpoint.",
    },
    "theory-of-consciousness": {
        "name": "Predictive Science of Conscious States",
        "year": "2090",
        "desc": "A theory that makes reliable, discriminating predictions about reports and behavioral or physiological markers of conscious state across humans, animals, organoids, and artificial systems. Integrated-information, global-workspace, recurrent-processing, and higher-order theories currently disagree, and resolving neural correlates or access consciousness would not necessarily settle the metaphysical 'hard problem.' The milestone is a reproducible predictive science useful for anaesthesia, disorders of consciousness, animal welfare, and cautious AI assessment—not a guaranteed explanation of why subjective experience exists.",
    },
    "galactic-civilization": {
        "name": "Local Multi-Stellar Civilization",
        "desc": "A durable civilization distributed among the Solar System and a growing group of nearby stars, connected by sub-light travel and communications. This scale is compatible with settlement over centuries or millennia; a galaxywide civilization is not. The Milky Way is roughly 100,000 light-years across, so even light cannot coordinate it on a 2500 timetable. The central problems are settlement reliability, demographic continuity, political divergence, interstellar transport, and governance under years or decades of message delay. Expansion beyond the local stellar neighborhood belongs on a much deeper timeline.",
    },
    "galactic-ecology": {"name": "Interstellar Ecology"},
    "galactic-communication-network": {
        "name": "Interstellar Relay Network",
        "desc": "A delay-tolerant optical and radio network linking inhabited systems through high-power laser terminals, autonomous relays, precise clocks, and protocols designed for years of latency. It cannot provide real-time galaxywide conversation or evade light speed. Messages are cached, authenticated, error-corrected, and forwarded when geometry and power permit; local copies of scientific, cultural, and legal archives keep each system functional during long interruptions. The first network would connect the Solar System to nearby stars, with expansion measured in centuries.",
    },
    "pre-warp-interstellar-trade": {"name": "Local Interstellar Trade"},
    "pan-galactic-coordination-ai": {"name": "Distributed Interstellar Coordination AI"},
    "pan-galactic-festival": {"name": "Asynchronous Interstellar Cultural Exchange"},
    "galactic-citizenship": {"name": "Interstellar Civic Framework"},
    "lingua-galactica": {"name": "Interstellar Contact Protocol"},
    "r-process-astromining": {
        "name": "Stellar-Remnant Resource Mapping",
        "year": "2400",
        "desc": "Mapping where heavy elements produced by supernovae and neutron-star mergers ultimately concentrate into accessible bodies. Fresh merger ejecta expands at roughly a tenth of light speed and becomes an enormous diffuse cloud; harvesting it centuries later with dust collectors is not credible. Practical resource extraction would target differentiated asteroids, planetary crusts, compact debris disks, or material already incorporated into later star systems. The milestone is therefore remote compositional surveying and selection of concentrated deposits, not recovery of gold from a rapidly expanding kilonova shell.",
    },
    "bose-einstein-engineering": {
        "name": "Industrial Ultracold-Matter Engineering",
        "year": "2300",
        "prereqs": ["quantum-applications", "quantum-sensing", "optical-atomic-clock"],
        "desc": "Reliable engineering with ultracold atoms, atom lasers, superfluids, and Bose-Einstein condensates for precision sensing, clocks, navigation, materials measurement, and quantum simulation. Atomic condensates require careful isolation and very low effective temperatures; topological protection or quantum error correction does not make a room-temperature atomic BEC thermodynamically stable. The plausible advance is compact, continuous, maintainable ultracold apparatus—possibly operating in space or cryogenic facilities—rather than room-scale condensates persisting under ordinary ambient conditions.",
    },
    "memory-editing": {"prereqs": ["brain-computer-interface", "neuroscience", "deep-learning"]},
    "stellar-engineering": {"year": "2480", "prereqs": ["dyson-swarm", "fusion-power"]},
    "stellar-scale-spectacle": {"year": "2750"},
    "antimatter-production": {
        "desc": "Producing and storing antimatter at quantities useful outside particle physics. Accelerators create antiprotons very inefficiently; charged particles require electromagnetic traps, while neutral antihydrogen is difficult to confine and has not been demonstrated as bulk cryogenic 'ice.' One gram of antimatter annihilating with one gram of ordinary matter would release about 1.8×10¹⁴ joules, or 43 kilotons of TNT, but at least that energy—and in practice vastly more—must first be supplied. Industrial feasibility depends on production efficiency, heat rejection, loss rates, containment mass, and fail-safe handling, not on a claim that gram quantities require a Type II civilization.",
    },
    "moon-base": {
        "name": "Sustained Lunar Surface Base",
        "desc": "A continuously occupied lunar outpost that survives long nights, radiation, abrasive dust, vacuum, thermal cycling, and delayed resupply. The milestone is not a landing or short campaign: crews repeatedly operate habitats, power, communications, medical support, maintenance, and surface transport while using at least some local water, oxygen, shielding, or construction material. Polar ice and favorable illumination may help, but resource quantity, accessibility, and extraction cost must be measured on site. Artemis and other national programs are precursors; none establishes a guaranteed completion date for a permanent base.",
    },
    "mars-colony": {
        "name": "Self-Reliant Mars Settlement",
        "desc": "A Mars settlement able to survive long interruptions in Earth supply while producing food, water, oxygen, energy, structures, and a widening range of replacement parts locally. Full economic self-sufficiency is much harder than keeping a habitat alive: semiconductor tools, medicines, specialty chemicals, knowledge, reproductive health, and institutional continuity create long supply tails. The milestone should be expressed through measured closure of critical loops and maximum tolerable isolation, not a promised population in a particular decade. Self-reliance reduces risk but does not make the settlement immune to correlated failures or Earth politics.",
    },
    "lab-grown-organs": {
        "name": "Vascularized Lab-Grown Organs",
        "desc": "Whole transplantable organs produced from cultured cells and biological or synthetic scaffolds, with perfusable blood vessels, appropriate architecture, innervation where required, and reproducible function after implantation. Organoids, engineered skin, bladders, and tissue patches are important precursors, but a thick heart, kidney, liver, or lung presents much harder vascularization, maturation, manufacturing, and quality-control problems. A qualifying milestone is repeated long-term clinical function with acceptable tumor, thrombosis, immune, and batch-variation risk—not a company target date or a small tissue construct described as a complete organ.",
    },
    "space-based-solar": {
        "desc": "Orbital solar arrays that transmit power to Earth or space users by microwave or laser. Continuous illumination can raise capacity factor, but the advantage per unit panel area is not a universal seven-to-eight-fold multiplier: orbit, eclipse, radiation damage, conversion efficiency, transmission loss, rectenna area, latitude, weather, and maintenance all matter. The milestone is an end-to-end demonstration followed by a system whose delivered electricity, safety, spectrum use, launch and assembly impacts, and lifecycle cost compete with terrestrial alternatives. Launch cost is important but not the only gate.",
    },
    "direct-ai-democracy": {
        "name": "AI-Supported Participatory Democracy",
        "desc": "Civic systems that help large populations understand proposals, submit views, find areas of agreement, model trade-offs, and audit how public input affects decisions. AI can translate, summarize, retrieve evidence, and detect coordinated manipulation, but it can also shape agendas, hide minority positions, or concentrate power in model operators. The milestone is a constitutional and technical arrangement with transparent models, plural channels, privacy, accessibility, independent oversight, and a non-AI route to challenge outcomes. National adoption is a social scenario, not a technologically determined result.",
    },
    "cyber-kinetic-warfare": {
        "name": "Autonomous Cyber-Physical Warfare",
        "desc": "Operations in which software compromises or manipulates physical systems such as grids, factories, vehicles, satellites, logistics, or weapons. Cyber-physical attacks already exist, so the future milestone is autonomous, adaptive operation across heterogeneous systems—and correspondingly resilient defense. Claims must distinguish demonstrated access from physical effect and avoid treating escalation as inevitable. Authentication, segmented control, safe degraded modes, manual recovery, software supply-chain security, attribution, proportional response, and protection of civilian infrastructure are the central technical and legal problems.",
    },
    "directed-energy-weapons": {
        "name": "Operational High-Power Directed-Energy Defense",
        "desc": "Lasers and high-power microwave systems delivering repeatable effects against selected drones, sensors, rockets, mortars, or boats under operational conditions. Existing demonstrations make directed energy a present technology; the future milestone is dependable field performance with adequate beam quality, tracking, power, cooling, dwell time, atmospheric tolerance, magazine depth, and rules for eye and aviation safety. These systems complement rather than replace kinetic interceptors, and attackers can exploit weather, hardening, maneuver, geometry, and saturation.",
    },
    "drone-swarms": {
        "name": "Large-Scale Resilient Drone Swarms",
        "desc": "Many inexpensive uncrewed vehicles coordinating reconnaissance, deception, communications, electronic warfare, logistics, or attack despite jamming and losses. Groups of drones and loitering munitions already operate in war; the future milestone is robust distributed coordination rather than sheer quantity. Testing must cover identification errors, communications denial, adversarial spoofing, civilian environments, abort behavior, cybersecurity, fratricide, and human control. Cost asymmetry can favor attackers, but electronic warfare, passive protection, interceptors, and logistics make battlefield dominance contingent rather than predetermined.",
    },
    "anti-satellite-warfare": {
        "name": "Non-Debris Counterspace Operations",
        "desc": "Reversible or low-debris methods for disrupting hostile space services, including jamming, cyber operations, dazzling, maneuver, inspection, and temporary denial. Destructive anti-satellite tests already exist and have created long-lived debris, so the future milestone should not be their invention. The critical problems are attribution, dual-use servicing spacecraft, escalation, protection of civilian services, safe separation, and norms that discourage debris-generating attacks. Even non-kinetic interference can have strategic effects and must not be described as clean or automatically controllable.",
    },
    "engineered-pathogen-defense": {
        "name": "Rapid Biological Countermeasure Platform",
        "desc": "A defensive pipeline that detects unusual pathogens, characterizes them, and develops diagnostics, vaccines, antibodies, or antivirals quickly enough to change an outbreak. Sequencing and platform vaccines are present precursors; the future milestone is validated response across diverse pathogen families with distributed manufacturing, clinical trials, equitable delivery, ventilation and infection-control support, and secure data sharing. Surveillance alone is not defense, and speed cannot eliminate safety evaluation. The same tools are dual use, so access controls, screening, incident reporting, and international trust are part of the system.",
    },
    "synthetic-performers": {
        "name": "Autonomous Synthetic Performers",
        "desc": "Virtual performers that can generate and present new music, dialogue, movement, and audience interaction while maintaining a coherent disclosed identity. Vocaloid characters, VTubers, digital influencers, and generated media already establish the form; the future milestone is sustained autonomous creative direction and accountable operation. Consent for training data and likeness, provenance, labor displacement, ownership, deceptive parasocial design, moderation, and the rights of human collaborators matter more than a prediction that synthetic acts will outdraw people in a particular decade.",
    },
    "procedural-infinite-worlds": {
        "name": "AI-Responsive Procedural Worlds",
        "desc": "Interactive worlds that generate environments, characters, stories, and rules in response to player behavior while preserving coherence over long sessions. Procedural generation is already mature; the future milestone is controllable open-ended generation with persistent state, authorial constraints, safety, reproducibility, and acceptable computing cost. The system should disclose generated content and protect artists' and players' data. Infinite quantity is not the quality criterion: meaningful causality, memorable design, shared experiences, and the ability of human creators to shape the world remain essential.",
    },
    "bio-art": {
        "name": "Engineered Living-Media Art",
        "desc": "Art whose medium includes cultured cells, organisms, tissues, or designed ecosystems with explicit care, containment, and end-of-life plans. Bio-art already exists, so the future milestone is sophisticated engineered living media whose behavior can be composed without hiding welfare or biosafety costs. Galleries and artists need sterile practice, environmental monitoring, public explanation, consent for human-derived material, and rules for release or disposal. Technical novelty does not by itself justify creating suffering organisms or environmentally persistent modifications.",
    },
    "magnetic-confinement-fusion": {
        "name": "Sustained Burning-Plasma Magnetic Fusion",
        "year": "2050",
        "desc": "A magnetic-confinement experiment that sustains a burning deuterium-tritium plasma long enough to validate integrated control, exhaust, fueling, stability, and plasma-facing components. Tokamaks and stellarators already confine fusion plasmas; the future milestone is not the invention of magnetic confinement or a momentary Q value. ITER, SPARC, stellarators, and other machines explore different parts of the problem. Net grid electricity belongs to the separate Utility-Scale Fusion Electricity node, because plant recirculating power, tritium, materials, maintenance, and availability lie outside plasma gain alone.",
    },
    "reversible-computing": {
        "name": "Practical Reversible Computing",
        "desc": "Computing hardware that performs useful workloads with reversible or near-adiabatic logic and demonstrates an end-to-end energy advantage after control, memory, interconnect, clocking, and cooling are counted. Reversible logic is an established theoretical and experimental field, so the future milestone is practical system benefit rather than invention. Avoiding logical erasure can approach lower dissipation, but real devices still suffer leakage, noise, finite-speed loss, error correction, and input/output costs. Landauer's bound does not by itself imply that reversible chips become mandatory in a particular decade.",
    },
    "univalent-foundations": {
        "name": "Machine-Native Univalent Foundations",
        "desc": "Proof assistants and mathematical libraries in which univalence, higher inductive types, and structural equivalence are practical foundations for substantial new research. Homotopy type theory and univalent foundations already exist; the future milestone is mature tooling, automation, interoperability, and a body of results for which these foundations offer clear advantages. Adoption need not displace ZFC or other type theories. Multiple foundations can coexist, with translations and verified interfaces more valuable than a forecast that all mathematics migrates by a stated decade.",
    },
    "langlands-program-completion": {
        "name": "AI-Assisted Langlands Program",
        "desc": "Machine-assisted progress on the network of conjectures linking automorphic forms, Galois representations, geometry, and number theory. Major cases are already proved, but the Langlands program is not a single finite checklist with a defensible completion date. The milestone is proof assistants and AI systems contributing verifiable new theorems, organizing dependencies, testing examples, and translating across subfields while expert mathematicians retain responsibility for definitions and significance. Completion of every major conjecture should remain an open possibility, not narrated future history.",
    },
    "layered-air-missile-defense": {
        "name": "AI-Coordinated Layered Air Defense",
        "desc": "An integrated defensive network that assigns sensors and interceptors across drones, rockets, cruise missiles, aircraft, and selected ballistic threats. Layered systems already exist; the future milestone is interoperable, cyber-resilient coordination under saturation, decoys, jamming, uncertain identification, and limited magazines. Reported interception percentages are conflict- and denominator-specific and should not become universal performance claims. Automation can recommend engagements, but escalation control, civilian airspace, positive identification, and accountable rules of engagement remain human responsibilities.",
    },
    "ai-decision-loop-compression": {
        "name": "AI-Compressed Military Decision Loops",
        "desc": "Use of AI to fuse sensor data, estimate threats, generate options, and shorten military decision cycles. The central issue is not human reaction time alone: uncertainty, adversarial deception, communications loss, legal review, escalation, and the irreversible cost of false identification set necessary limits. A qualifying system must preserve abort paths, record provenance, expose confidence, resist spoofing, and keep meaningful human authority over lethal and strategic decisions. Competitive pressure may encourage adoption, but fully autonomous engagement is a contested policy choice rather than an inevitable 2045 fact.",
    },
    "engineered-microbiome": {
        "name": "Engineered Microbiome Therapeutics",
        "desc": "Defined microbial communities or engineered strains used to alter a host or environmental microbiome for a specific, measured outcome. Fecal microbiota transplantation for recurrent C. difficile establishes that microbiome intervention can work, but it does not validate routine treatment of depression, metabolic disease, or many other proposed indications. The milestone is reproducible composition, manufacturing, colonization, mechanism, safety, and clinical benefit in randomized trials. Agricultural applications likewise require field evidence, ecological monitoring, and control of persistence and gene transfer.",
    },
    "senolytic-longevity-therapy": {
        "name": "Validated Senolytic Therapy",
        "desc": "A treatment that selectively removes or modifies senescent cells and produces a clinically meaningful benefit with acceptable toxicity in people. Mouse studies and early human investigations motivate the field, but no current result establishes that senolytics compress most age-related illness or substantially extend human healthspan. Senescent cells also contribute to wound healing and tumor suppression, so timing and tissue specificity matter. The milestone is replicated human evidence for defined diseases or functional outcomes, followed by long-term surveillance—not a calendar promise of generalized rejuvenation.",
    },
    "brain-brain-communication": {
        "name": "Neurally Mediated Person-to-Person Signaling",
        "desc": "Transmission of limited intentional information from one nervous system through computers to stimulation of another. Existing demonstrations communicate very low-bandwidth choices or motor signals; they do not transfer thoughts, memories, emotions, or a shared visual field. The future milestone is a reproducible clinically or operationally useful channel with quantified bandwidth, error rate, training burden, privacy, consent, and reversibility. Higher-order percept transfer remains speculative and should not be narrated as an inevitable group-mind subculture in a particular decade.",
    },
    "formal-mathematics": {
        "name": "Routine Machine-Verified Mathematics",
        "desc": "A research environment in which important new proofs are routinely checked by proof assistants and substantial portions are generated or translated with machine help. Formal verification already exists, so the future milestone is practical coverage: mature libraries, interoperable foundations, usable interfaces, transparent automation, and independent checking of machine-generated steps. Formalization can expose hidden assumptions and improve reliability, but it does not determine which definitions or problems matter, and it should not be forecast as a universal migration completed in one decade.",
    },
    "pleistocene-restored": {
        "name": "Pleistocene Rewilding at Ecosystem Scale",
        "desc": "Long-term restoration experiments using living large herbivores and predators—and, only where safe and justified, engineered proxies—to test whether lost ecological functions can be recovered. Cloning announcements or a single edited animal do not restore an ecosystem. The milestone requires healthy multi-generation populations, habitat, animal welfare, disease control, community consent, genetic diversity, and measured effects on vegetation, fire, carbon, and existing species. De-extinction company schedules are goals, not evidence, and proxy organisms must not be described as exact returns of extinct species.",
    },
    "closed-cycle-cities": {
        "name": "Circular Resource Cities",
        "desc": "Urban systems designed to reduce virgin material, water, energy, and nutrient inputs through repair, reuse, industrial symbiosis, water recycling, composting, material passports, and recoverable construction. No city is literally closed: food, energy, people, information, and wastes cross its boundary. The milestone is a measured reduction in lifecycle extraction and pollution while maintaining health, affordability, and resilience. Recycling cannot overcome all thermodynamic loss, and dense monitoring must not become a pretext for surveillance. Progress should be reported as material and emissions accounts, not a calendar declaration of complete closure.",
    },
    "ai-coordination-treaty": {
        "name": "International AI Compute and Safety Accord",
        "desc": "A negotiated framework for transparency, incident reporting, evaluation, compute governance, proliferation controls, and crisis communication around highly capable AI. Verification might combine registered large training runs, hardware supply-chain records, audited safety cases, and protected inspections, but secrecy, open research, national security, and changing algorithmic efficiency complicate every mechanism. The milestone is a durable agreement with participation, compliance evidence, dispute resolution, and emergency channels. It is a political scenario, not an inevitable treaty concluded when models cross a stated capability threshold.",
    },
    "geothermal-drilling": {
        "name": "Superhot-Rock Geothermal Systems",
        "desc": "Geothermal systems that reach hotter, deeper rock in a wider range of locations using improved rotary drilling, stimulation, closed loops, or experimental millimetre-wave methods. Claims of drilling 10–20 kilometres anywhere on Earth remain unproven; rock mechanics, casing, cement, tool survival, induced seismicity, water loss, corrosion, and heat extraction over decades are major constraints. The milestone is a replicated commercial field with audited drilling cost, sustained thermal output, manageable seismic and water impacts, and full lifecycle performance—not a laboratory drilling rate extrapolated directly to a global baseload resource.",
    },
    "asteroid-capture": {
        "desc": "Controlled redirection of a small near-Earth object or extracted material into a deliberately chosen stable orbit for science or industry. The first milestone should involve a mass small enough for bounded risk, independently verified navigation, redundant abort options, and international review. Ion thrust, gravity tractors, mass drivers, or surface ablation may provide gradual momentum change. Claims that an arbitrary hundred-metre asteroid contains more accessible platinum than humanity has mined ignore composition, concentration, processing, market response, and return cost. Water and bulk shielding material may be more useful in space than precious-metal export to Earth.",
    },
    "anti-senescence-cellular-substrate": {
        "name": "Gradual Bio-Synthetic Tissue Replacement",
        "desc": "A speculative program for replacing selected tissue functions with durable bio-synthetic components while preserving physiology and personal continuity. Present medicine can replace joints, valves, skin, blood components, and some organ functions; replacing cells throughout a living body with molecular machines is not an established extension of those successes. Immune integration, metabolism, repair, cancer, neural function, infection, manufacturing, and failure containment would all have to be solved. The node must not promise effective biological immortality and should remain a distant speculative-engineering scenario.",
    },
    "cryogenic-hibernation": {
        "name": "Reversible Therapeutic Torpor",
        "desc": "Controlled reduction of human metabolism for hours, days, or potentially weeks, followed by complete recovery. This is distinct from cryonics, which preserves legally dead people without demonstrated revival. A defensible milestone begins with shorter clinical torpor for trauma, surgery, critical care, or transport and measures neurological outcome, clotting, infection, muscle loss, organ injury, rewarming, and repeated use. Natural hibernators provide biological clues but do not establish that healthy humans can be frozen or placed in century-long suspension. Interstellar hibernation remains a much more distant extrapolation.",
    },
    "whole-brain-emulation": {
        "desc": "A computational model of a particular brain detailed enough to reproduce specified functions and behavior. Mapping a connectome is not sufficient: synaptic state, cell types, neuromodulation, plasticity, glia, body interaction, and the required level of molecular detail remain uncertain. No existing worm, fly, rodent, or cortical simulation demonstrates transfer of a person's memories or identity. The milestone should proceed through organisms and bounded neural functions with predictions tested against biology. Human whole-brain emulation has no defensible completion date, and functional similarity would not by itself settle consciousness, legal personhood, or continuity of identity.",
    },
}


ADDITIONS = [
    dict(id="long-duration-energy-storage", name="Long-Duration Energy Storage", era="future", category="energy", year="2035", prereqs=["renewable-grid", "lithium-battery"], desc="Grid storage designed to deliver power for roughly ten hours to multiple days, complementing short-duration lithium-ion batteries. Flow batteries, iron-air cells, thermal stores, pumped storage, compressed air, and gravity systems trade energy density for long life, low material cost, or easy scaling. The milestone is bankable deployment across different climates with measured round-trip efficiency, degradation, fire safety, supply-chain impacts, and full system cost. Long-duration storage helps bridge nights, weather systems, and transmission constraints, but seasonal balancing may still require fuels, demand response, overbuilding, or continental grids."),
    dict(id="advanced-fission-systems", name="Advanced Fission Systems", era="future", category="energy", year="2040", prereqs=["nuclear-fission", "advanced-chip-manufacturing"], desc="Commercial fission reactors that improve construction repeatability, passive safety, fuel use, waste management, or high-temperature heat supply. The family includes small modular light-water reactors and advanced sodium, gas, molten-salt, and fast-spectrum designs; their benefits and risks differ and should not be collapsed into one promise. The milestone is a replicated fleet with audited cost, schedule, capacity factor, safeguards, decommissioning, and waste performance. Licensing, financing, supply chains, and public institutions may be harder constraints than reactor physics."),
    dict(id="green-hydrogen-electrofuels", name="Green Hydrogen and Electrofuels", era="future", category="energy", year="2040", prereqs=["renewable-grid", "synthetic-fertilizer"], desc="Hydrogen made by low-emission electrolysis and used directly or combined with captured carbon or nitrogen to make ammonia, methanol, aviation fuel, and other molecules. The strongest applications are likely sectors that cannot be electrified easily, including fertilizer, selected steelmaking, shipping, and long-duration chemical storage—not routine heating or passenger cars. Success requires cheap clean electricity, durable electrolysers, leak control, new transport and storage infrastructure, rigorous lifecycle accounting, and rules that prevent scarce hydrogen from being diverted to inefficient uses."),
    dict(id="point-source-carbon-capture", name="Industrial Point-Source Carbon Capture", era="future", category="energy", year="2035", prereqs=["climate-science", "portland-cement"], desc="Capturing concentrated carbon dioxide from cement, lime, chemicals, refining, or selected power plants before it reaches the atmosphere, then transporting and storing it geologically. This is easier than direct-air capture but does not remove historical emissions, and capture rates must be measured across the whole facility rather than at one stream. The milestone is durable storage with low methane and energy penalties, monitored wells, assigned long-term liability, and deployment focused on genuinely hard-to-abate processes rather than extending avoidable fossil use."),
    dict(id="enhanced-weathering", name="Verified Enhanced Weathering", era="future", category="energy", year="2045", prereqs=["climate-science", "mining-metallurgy"], desc="Accelerating natural mineral reactions that convert atmospheric carbon dioxide into dissolved bicarbonate or stable carbonate by spreading carefully selected crushed rock on land or coastlines. The chemistry is established, but climate value depends on mining and grinding energy, reaction rates, soil and water effects, trace metals, transport distance, and measurement of carbon that would not otherwise have been removed. The milestone is large, independently monitored deployment with credible lifecycle accounting and ecological limits, not simply counting tonnes of rock distributed."),
    dict(id="ocean-carbon-removal", name="Monitored Ocean Carbon Removal", era="future", category="energy", year="2050", prereqs=["climate-science", "public-sanitation"], desc="Methods that increase durable ocean uptake or storage of carbon while measuring ecological effects and preventing double counting. Candidate approaches include alkalinity enhancement, electrochemical separation, and biomass pathways, each with different risks. The ocean is not an empty disposal reservoir: local pH, nutrients, oxygen, trace contaminants, food webs, and international law constrain intervention. The milestone is verified net removal with long-duration monitoring, transparent governance, and ecological performance demonstrated beyond a small experiment."),
    dict(id="climate-adaptation-infrastructure", name="Climate-Adaptation Infrastructure", era="future", category="shelter", year="2035", prereqs=["climate-science", "public-sanitation"], desc="Infrastructure and public systems redesigned for unavoidable heat, flood, drought, fire, smoke, disease, and coastal risk. Measures include passive cooling and heat refuges, floodable landscapes, coastal retreat or protection, wildfire-resistant construction, water banking, resilient grids, crop changes, insurance reform, and early warning. Adaptation does not substitute for emissions cuts; risks grow with every increment of warming. The milestone is routine use of forward-looking climate conditions in building codes, capital planning, health systems, and land use, with protection for populations least able to relocate or self-finance."),
    dict(id="advanced-water-reuse", name="Advanced Desalination and Water Reuse", era="future", category="subsistence", year="2035", prereqs=["public-sanitation", "renewable-grid"], desc="Reliable production of potable water from seawater, brackish sources, and treated wastewater with lower energy, membrane fouling, concentrate, and ecosystem impacts. Reverse osmosis is already mature; the future milestone is integrated water systems that combine reuse, leak reduction, aquifer recharge, desalination, and renewable power while controlling persistent contaminants. Brine disposal, intake harm, public trust, affordability, and drought governance are as important as membrane efficiency. Water scarcity is usually a systems and distribution problem as well as a treatment problem."),
    dict(id="autonomous-laboratories", name="Autonomous Scientific Laboratories", era="future", category="knowledge", year="2035", prereqs=["deep-learning", "robotics", "formal-mathematics"], desc="Laboratories in which software proposes experiments, robotic instruments execute them, results update a model, and the cycle repeats with limited human intervention. Early self-driving labs already optimize selected materials and chemical processes; the milestone is reproducible operation across multiple instrument types with calibrated uncertainty, negative-result retention, contamination detection, and human-auditable reasoning. These systems can search large design spaces for catalysts, drugs, batteries, and materials, but they do not replace scientific judgment about valuable questions, causal interpretation, safety, or social consequences."),
    dict(id="precision-fermentation-agriculture", name="Precision Fermentation and Gene-Edited Crops", era="future", category="subsistence", year="2035", prereqs=["genetic-engineering", "crispr", "synthetic-fertilizer"], desc="Large-scale production of proteins, fats, chemicals, and crop traits using engineered microbes and precise plant breeding. The milestone combines cost-competitive fermentation with crops designed for heat, drought, disease resistance, nutrition, or reduced fertilizer demand. Biological performance must survive real farms and industrial bioreactors, while regulation addresses gene flow, resistance evolution, biodiversity, farmer dependence, and equitable access. This branch is distinct from cultivated animal tissue even though both may reshape food supply chains."),
    dict(id="xenotransplantation-organ-preservation", name="Xenotransplantation and Organ Preservation", era="future", category="medicine", year="2040", prereqs=["organ-transplant", "crispr", "tissue-engineering"], desc="A combined clinical system that expands the organ supply through gene-edited animal organs, longer ex-vivo perfusion, improved matching, and reliable preservation. The milestone is not a single dramatic transplant but reproducible multi-year survival, controlled rejection and coagulation, low zoonotic risk, ethical animal husbandry, and equitable allocation. Better preservation also allows organs to be evaluated, treated, transported farther, and scheduled rather than rushed. Xenotransplantation complements lab-grown organs and prevention of organ failure rather than guaranteeing that every donor shortage disappears."),
    dict(id="pandemic-surveillance-platform", name="Genomic and Wastewater Pandemic Surveillance", era="future", category="medicine", year="2035", prereqs=["gene-sequencing", "mrna-vaccine", "public-sanitation"], desc="A privacy-preserving network that detects unusual disease patterns through clinical sampling, metagenomic sequencing, wastewater, air monitoring, animal surveillance, and interoperable reporting. The milestone is early warning linked to confirmatory testing and rapid countermeasure development—not indiscriminate collection of personal data. Systems must distinguish signal from background microbes, represent underserved regions, share benefits with sample-origin communities, resist political suppression, and maintain capacity between crises. Surveillance only helps when public-health institutions can act on it."),
    dict(id="orbital-servicing-refueling", name="Orbital Servicing, Refueling, and Debris Removal", era="future", category="transport", year="2035", prereqs=["satellite", "robotics", "reusable-rocket"], desc="Spacecraft that inspect, repair, refuel, reposition, assemble, or safely dispose of other spacecraft. Rendezvous and docking already exist; the future milestone is interoperable commercial service using standardized interfaces and transparent traffic coordination. Robotic manipulation, fluid transfer, autonomous navigation, liability, cybersecurity, and avoidance of dual-use anti-satellite behavior are core constraints. Servicing extends spacecraft life and enables larger structures, while debris removal focuses on a small number of high-risk objects whose removal measurably reduces collision cascades."),
    dict(id="lunar-isru-logistics", name="Lunar ISRU and Cislunar Logistics", era="future", category="transport", year="2045", prereqs=["moon-base", "orbital-servicing-refueling", "closed-loop-life-support"], desc="Prospecting, extracting, processing, and using lunar materials as part of a repeatable transport network between Earth orbit, the Moon, and nearby space. Initial products are likely water, oxygen, shielding, and bulk construction material rather than profitable export of rare metals to Earth. The milestone is sustained production with measured energy and maintenance costs, storage and transfer of propellant, reliable landing infrastructure, and governance of shared polar resources. ISRU must reduce total mission risk and mass compared with supplies launched from Earth."),
    dict(id="nuclear-space-propulsion", name="Nuclear Thermal and Electric Space Propulsion", era="future", category="transport", year="2045", prereqs=["nuclear-fission", "reusable-rocket"], desc="Space propulsion using a fission reactor either to heat propellant directly for high thrust or to generate electricity for efficient ion or plasma thrusters. Nuclear thermal propulsion can shorten high-energy crewed journeys; nuclear electric propulsion offers lower thrust but excellent propellant efficiency for cargo and outer-system missions. The milestone is a flight-qualified reactor with safe ground handling, launch-accident containment, heat rejection, reliable control, and a mission whose benefits justify cost and political risk. It is a more grounded precursor to fusion propulsion."),
    dict(id="integrated-space-networks", name="Integrated Terrestrial-Satellite Networks", era="future", category="communication", year="2035", prereqs=["satellite", "mobile-phone", "fiber-optic"], desc="Communication systems in which ordinary devices move securely among terrestrial cells, low-orbit constellations, high-altitude platforms, and local emergency networks. Direct-to-device satellite links already exist in limited forms; the milestone is interoperable broadband and messaging with efficient spectrum sharing, manageable orbital congestion, resilient routing, and affordable service. Latency, indoor coverage, handset power, debris, astronomy interference, market concentration, censorship, and cross-border regulation remain constraints. The goal is graceful coverage and disaster resilience, not a claim that satellites replace fiber and dense terrestrial networks."),
    dict(id="post-cmos-integration", name="Post-CMOS Integration and Optical Interconnects", era="future", category="tools", year="2035", prereqs=["advanced-chip-manufacturing", "fiber-optic"], desc="Computing systems that improve performance by combining chiplets, three-dimensional stacking, advanced packaging, specialized accelerators, new memories, and optical links rather than relying only on smaller transistors. The milestone is economical high-volume integration with acceptable yield, heat removal, repairability, software portability, and energy per operation. Some logic may remain CMOS for decades while communication and memory change first. This branch provides a grounded path between current semiconductor scaling and more speculative neuromorphic, photonic, quantum, or reversible machines."),
    dict(id="autonomous-built-environment", name="Autonomous Construction and Agriculture", era="future", category="tools", year="2040", prereqs=["robotics", "humanoid-robot", "gps"], desc="Robotic systems that perform substantial construction and farm work in changing outdoor environments: surveying, earthmoving, planting, weeding, harvesting, material placement, inspection, and repair. The milestone is dependable multi-season productivity with safe human collaboration and adaptation to weather, soil, damaged structures, and irregular objects. Automation can reduce dangerous labor and inputs, but ownership, rural employment, cybersecurity, right-to-repair, and failure during emergencies shape its social value. General-purpose robots and specialized machines will likely work together."),
    dict(id="solar-gravitational-lens-observatory", name="Solar Gravitational-Lens Observatory", era="far-future", category="knowledge", year="2150", prereqs=["interstellar-probe", "autonomous-laboratories"], desc="A telescope mission operating beyond roughly 550 astronomical units, where the Sun's gravity focuses light from a distant target into an Einstein ring. A spacecraft moving along the focal line could reconstruct high-resolution information about an exoplanet, but the measurement is not a conventional snapshot: the solar corona, target motion, navigation, deconvolution, and scanning across the image plane must all be controlled. The milestone is a decades-long autonomous mission that reconstructs independently validated planetary features, providing a known-physics route to detailed exoplanet observation."),
    dict(id="beamed-interstellar-probe", name="Beamed Relativistic Probe", era="far-future", category="transport", year="2125", prereqs=["laser", "interstellar-probe", "space-based-solar"], desc="A very small spacecraft accelerated to a significant fraction of light speed by a distant laser or particle beam, avoiding the need to carry most of its propulsion energy. The milestone requires a phased array with extreme pointing accuracy, an ultralight sail, survival through the interplanetary and interstellar medium, autonomous navigation, and a communication link from a tiny fast-moving probe. Braking at the destination is harder than launch and may require magnetic, electric, photonic, or pre-positioned infrastructure. This is a grounded precursor to crewed interstellar travel."),
    dict(id="stellar-material-extraction", name="Star Lifting and Stellar Propulsion", era="far-future", category="energy", year="2500", prereqs=["dyson-swarm", "stellar-engineering"], desc="Controlled use of magnetic fields, radiation, or orbital structures to remove material from a star or alter its motion over very long periods. Star lifting could supply hydrogen and heavier elements, manage stellar evolution, or feed fusion and manufacturing; stellar engines could slowly move a planetary system. Both are compatible with known conservation laws in broad outline but require power, material, stability, and control on a scale far beyond planetary industry. The milestone is a measurable, sustained change to stellar mass flow or velocity—not a complete redesign of a star in a few decades."),
    dict(id="interstellar-shielding-deceleration", name="Interstellar Shielding and Deceleration", era="far-future", category="transport", year="2120", prereqs=["interstellar-probe", "metamaterials"], desc="Systems that let fast spacecraft survive dust and gas impacts and shed velocity on arrival without carrying an impractical amount of propellant. Candidate methods include layered sacrificial shields, forward dust clouds, magnetic or electric sails, photon sails, and interaction with a stellar wind or destination laser. At relativistic speed, even tiny grains are hazardous and uncertain dust distributions become mission-critical. The milestone is a probe-scale demonstration that combines shielding, sensing, trajectory correction, and independently measured deceleration in a target stellar system."),
    dict(id="deep-time-archives", name="Deep-Time Civilizational Archives", era="far-future", category="communication", year="2150", prereqs=["dna-data-storage", "space-habitat"], desc="Archives engineered to remain interpretable through centuries or millennia of institutional, linguistic, and technological change. Redundant copies use different media and locations, with human-readable primers, error correction, provenance, repair schedules, and governance for controlled but durable access. The milestone is not simply a long-lived material; it is an actively tested preservation system that can recover knowledge after software loss, political fragmentation, migration, or planetary disaster. Archives may be distributed across Earth, the Moon, habitats, and eventually nearby stars."),
    dict(id="heat-limited-computing", name="Heat-Limited Computing Infrastructure", era="far-future", category="tools", year="2180", prereqs=["reversible-computing", "photonic-computing", "space-based-solar"], desc="Computing infrastructure designed around thermodynamic cost and waste-heat rejection rather than transistor count alone. Reversible logic, optical links, cryogenic stages, workload scheduling, large radiators, and location in cold or well-shaded environments may reduce energy per useful operation. Cooling is not free: refrigeration consumes work and every computation ultimately interacts with a heat sink. The milestone is an audited end-to-end gain, including cooling and communication, at scales where thermal engineering dominates architecture. It is a grounded precursor to stellar-scale computation."),
]


ZH = {
    "humanoid-robot": "通用机器人劳动",
    "brain-computer-interface": "高带宽双向神经假体",
    "lab-grown-meat": "达到成本与规模平价的培养肉",
    "synthetic-biology": "可预测的全基因组生物工程",
    "quantum-applications": "容错量子优势",
    "carbon-capture-scale": "直接空气碳移除",
    "ai-judge": "人工智能辅助司法行政",
    "cancer-cure": "广谱癌症控制",
    "metamaterials": "规模化主动超表面",
    "personalized-medicine": "实时多组学医学",
    "inertial-confinement-fusion": "高重复率惯性聚变能源",
    "genetic-disease-eradication": "单基因疾病的常规预防与治疗",
    "universal-disease-eradication": "全球疾病抑制基础设施",
    "space-habitat": "大型旋转太空聚居地",
    "terraforming-mars": "火星局部环境地球化",
    "theory-of-consciousness": "意识状态预测科学",
    "knowledge-closure": "特定领域自动化科学",
    "galactic-civilization": "近邻多恒星文明",
    "galactic-communication-network": "星际中继网络",
    "vacuum-energy-extraction": "量子真空能量边界",
    "dark-energy-engineering": "可控暗能量假说",
    "warp-drive": "曲率时空可行性检验",
    "cosmic-string-ftl": "宇宙弦年代学模型",
    "r-process-astromining": "恒星遗迹资源测绘",
    "bose-einstein-engineering": "工业超冷物质工程",
    "long-duration-energy-storage": "长时储能",
    "advanced-fission-systems": "先进裂变系统",
    "green-hydrogen-electrofuels": "绿氢与电合成燃料",
    "point-source-carbon-capture": "工业点源碳捕集",
    "enhanced-weathering": "可核证增强风化",
    "ocean-carbon-removal": "受监测海洋碳移除",
    "climate-adaptation-infrastructure": "气候适应基础设施",
    "advanced-water-reuse": "先进海水淡化与水回用",
    "autonomous-laboratories": "自主科学实验室",
    "precision-fermentation-agriculture": "精准发酵与基因编辑作物",
    "xenotransplantation-organ-preservation": "异种移植与器官保存",
    "pandemic-surveillance-platform": "基因组与污水疫情监测",
    "orbital-servicing-refueling": "在轨服务、加注与碎片清除",
    "lunar-isru-logistics": "月球原位资源利用与地月物流",
    "nuclear-space-propulsion": "核热与核电推进",
    "integrated-space-networks": "天地融合通信网络",
    "post-cmos-integration": "后CMOS集成与光互连",
    "autonomous-built-environment": "自主建造与农业",
    "solar-gravitational-lens-observatory": "太阳引力透镜观测站",
    "beamed-interstellar-probe": "束能相对论探测器",
    "stellar-material-extraction": "恒星物质提取与恒星推进",
    "interstellar-shielding-deceleration": "星际防护与减速",
    "deep-time-archives": "深时文明档案",
    "heat-limited-computing": "热极限计算基础设施",
}


NEW_UNLOCKS = {
    t["id"]: [
        {"type": "resource", "name": t["name"], "name_zh": ZH.get(t["id"], t["name"]), "wiki": False},
        {"type": "resource", "name": "Verification standard", "name_zh": "核证标准", "wiki": False},
        {"type": "org", "name": "Public-interest test program", "name_zh": "公共利益测试计划", "wiki": False},
    ]
    for t in ADDITIONS
}


EXTRA_REWRITES = {
    "terraforming-mars": (
        "Mars Paraterraforming",
        "Building large enclosed Martian environments without implying that the whole planet becomes Earth-like.",
        "A qualifying system maintains pressure, temperature, water, radiation protection, and a managed ecology across a region large enough for settlement and agriculture. Caves, tensioned membranes, buried structures, and linked pressure zones are more credible than a breathable open atmosphere on a one-century timetable.",
        "Available Martian carbon dioxide is insufficient for familiar rapid-terraforming scenarios, and imported volatiles would demand extraordinary transport. Low gravity, dust, perchlorates, ecological instability, maintenance, and planetary protection remain unresolved. Full planetary terraforming should remain an undated scenario separate from this milestone.",
    ),
    "ai-judge": (
        "AI-Assisted Judicial Administration",
        "Reducing delay and clerical burden while keeping legal authority, explanation, and appeal accountable to people.",
        "Useful systems retrieve controlling authority, translate and organize records, check filings, draft routine language, and flag inconsistencies. Every material claim should link to evidence, expose uncertainty, preserve an audit trail, and allow parties to challenge both inputs and reasoning.",
        "Historical data reflects unequal policing and access to counsel; model opacity can turn those inequalities into apparently neutral scores. Final findings of fact, detention, sentencing, and coercive orders need responsible human decision-makers. Estonia's reported autonomous AI judge was a misconception, not evidence that autonomous judging is already established.",
    ),
    "cancer-cure": (
        "Broad Cancer Control",
        "Replacing the misleading promise of one cure with measurable control across many evolving diseases.",
        "Progress comes from layered prevention, screening, molecular diagnostics, surgery, radiation, targeted therapy, immunotherapy, and adaptive combinations. A defensible milestone is a large sustained fall in age-adjusted mortality and treatment burden across common cancers, including difficult metastatic disease.",
        "Tumor evolution, resistance, heterogeneous targets, immune suppression, toxicity, and unequal delivery prevent a universal guarantee. Personalized vaccines and CAR-T cells are important platforms, but the evidence must be stated by cancer type and trial phase rather than extrapolated to all cancer.",
    ),
    "universal-disease-eradication": (
        "Global Disease Suppression Infrastructure",
        "A permanent prevention and response system, not a declaration that disease has disappeared.",
        "The stack combines sanitation, ventilation, vaccination, primary care, genomic and wastewater surveillance, rapid diagnostics, adaptable medicines, manufacturing reserves, and logistics. It can eliminate selected human-only pathogens regionally or globally and suppress many others before they spread widely.",
        "Animal reservoirs, evolution, novel spillovers, conflict, mistrust, new mutations, and unequal health systems persist. Maintenance continues even when cases are rare. Success should be measured through mortality, transmission, access, response time, and resilience rather than the absolute phrase 'universal eradication.'",
    ),
    "quantum-applications": (
        "Fault-Tolerant Quantum Advantage",
        "A useful verified logical-qubit computation—not a milestone defined by physical-qubit marketing.",
        "Logical error rates, code distance, physical fidelity, connectivity, algorithm depth, data movement, and classical comparison together determine the necessary machine. Chemistry and materials simulation are plausible targets, while cryptanalytic machines would require much larger reliable systems.",
        "There is no universal physical-qubits-per-logical-qubit number and no accepted delivery date. Claims should state the workload, accuracy, total energy and runtime, error-correction overhead, and best classical baseline. Independent reproduction matters as much as raw hardware scale.",
    ),
    "carbon-capture-scale": (
        "Direct Air Carbon Removal",
        "Removing legacy carbon from dilute ambient air and storing it durably.",
        "A complete system includes air contact, sorbent regeneration, clean heat and electricity, compression, transport, injection or mineralization, leakage monitoring, and lifecycle accounting. Capacity announcements are not removals; the credited quantity must be net of construction, energy, and material emissions.",
        "Direct-air capture is different from stack capture, BECCS, enhanced weathering, and ocean methods. It is likely most valuable for residual emissions rather than as permission to delay cheaper emissions cuts. Land, water, energy, community consent, storage liability, and measurement determine whether it is genuinely climate-beneficial.",
    ),
    "vacuum-energy-extraction": (
        "Quantum Vacuum Energy Limits",
        "Testing the limits of vacuum phenomena without presenting the Casimir effect as a free-energy source.",
        "Casimir forces arise from boundary-dependent quantum fields, and driven systems can produce photons through the dynamical Casimir effect. In every demonstrated cycle, the apparatus or driving field supplies energy. A valid extraction claim must restore the complete system to its starting state and include every input.",
        "No accepted cycle obtains unlimited net work from the vacuum. This branch remains scientific investigation with an unknown horizon. If future experiments reveal a reproducible exception, the result would be new physics; until then, zero-point cells and Casimir generators should not appear as unlocked devices.",
    ),
    "dark-energy-engineering": (
        "Controllable Dark-Energy Hypothesis",
        "A placeholder for a possible discovery, clearly separated from established cosmology.",
        "Cosmological observations show accelerated expansion and constrain equations of state. They do not provide a sample of dark energy, a local control mechanism, or evidence that vacuum-energy terminology translates into an engineering material.",
        "Any future claim must demonstrate a locally produced, repeatable stress-energy effect; rule out electromagnetic, mechanical, thermal, and gravitational artifacts; and connect the laboratory result to cosmology. Without that evidence, this is an unknown-horizon hypothesis and cannot serve as a normal prerequisite for transport technology.",
    ),
    "warp-drive": (
        "Warp-Spacetime Feasibility Tests",
        "Separating exact solutions of Einstein's equations from machines that could create those solutions.",
        "Research can calculate required stress-energy, horizons, tidal fields, causal structure, stability, and quantum inequalities for proposed metrics. Subluminal positive-energy shells and superluminal warp bubbles are different claims and must not be presented as interchangeable.",
        "Known superluminal constructions require exotic stress-energy and provide no build, steering, or shutdown method. The scientifically honest milestone is a decisive feasibility or impossibility result. An operational drive should not be forecast unless experiments first reveal suitable new physics.",
    ),
    "cosmic-string-ftl": (
        "Cosmic-String Chronology Models",
        "A theoretical causality problem, not a transport roadmap.",
        "The Gott construction considers idealized moving strings and global spacetime conditions that permit closed timelike curves. Later analyses challenged whether physically acceptable sources can form the required configuration and whether quantum effects destabilize it.",
        "Cosmic strings remain unobserved and cannot be treated as manipulable infrastructure. This entry belongs beside quantum gravity and chronology protection, carries a Requires New Physics label, and should unlock no FTL vehicle. Observational bounds, finite-string formation, backreaction, stability, and quantum effects all have to be addressed before the geometry can be connected even to a physical thought experiment.",
    ),
    "kugelblitz-drive": (
        "Kugelblitz Drive",
        "A black-hole-starship proposal whose central numbers and engineering uncertainties must remain visible.",
        "The useful mass window discussed in feasibility literature is around a million tonnes, with an attometre-scale radius and an intense Hawking output. Creating it requires an immense converging gamma-ray pulse; a ship would also have to accelerate the hole, feed it, and survive its radiation.",
        "Gamma rays are not conveniently reflected by an ordinary mirror. Absorbing and reradiating them adds mass and heat, while speculative plasma reflectors are unproven. The corrected chronology places this node after black-hole engineering and antimatter propulsion rather than before both prerequisites.",
    ),
    "r-process-astromining": (
        "Stellar-Remnant Resource Mapping",
        "Finding concentrated deposits produced by stellar nucleosynthesis instead of trying to sweep up a diffuse kilonova cloud.",
        "Neutron-star mergers synthesize heavy nuclei, but their ejecta expands at a substantial fraction of light speed and rapidly mixes into an enormous volume. Useful prospecting targets are differentiated asteroids and planets, compact debris structures, or later systems whose formation concentrated the material.",
        "Interstellar transport costs will usually dominate the value of ordinary elements. The milestone should identify unusual concentration, isotope, or strategic-location advantages and compare them with recycling and local substitution before claiming that remote mining is economic.",
    ),
    "bose-einstein-engineering": (
        "Industrial Ultracold-Matter Engineering",
        "Making ultracold quantum systems reliable and useful without claiming that error correction defeats thermodynamics.",
        "Compact vacuum systems, laser cooling, magnetic or optical traps, continuous atom sources, autonomous calibration, and low-vibration platforms could bring atom interferometers and quantum simulators into routine scientific and navigation use.",
        "Atomic condensates still require ultralow effective temperatures and isolation. Topological phases may be more robust against selected perturbations, but they do not turn a thermal atomic gas into an ambient BEC. Applications and environmental requirements must be stated together.",
    ),
    "knowledge-closure": (
        "Domain-Specific Automated Science",
        "Automating discovery within explicit boundaries rather than announcing the end of knowledge.",
        "A mature system links literature, causal models, experiment planning, robotic execution, statistics, proof assistants, and replication. Within a defined chemical, biological, or engineering space it may enumerate possibilities and certify coverage under declared assumptions.",
        "Universal closure is impossible to establish because new systems and questions can be created, empirical precision is open-ended, and formal systems have limits. Every closure claim must state its domain, observables, assumptions, uncertainty, and conditions under which it would be reopened.",
    ),
    "hypercomputation": (
        "Physical Hypercomputation Hypotheses",
        "Asking whether nature permits more than Turing computation, with no assumption that the answer is yes.",
        "Zeno machines, relativistic spacetimes, analog infinite precision, and oracle models each import an idealization that may be physically unavailable. A serious program identifies the finite observer, measurement, noise, energy, and causal requirements rather than labeling an abstract oracle as hardware.",
        "P versus NP concerns efficient algorithms inside ordinary computability and is not a prerequisite. This branch should remain undated and conditional on experimental new physics; a no-go theorem would be a valid completion.",
    ),
    "theory-of-consciousness": (
        "Predictive Science of Conscious States",
        "Building discriminating empirical models without promising to dissolve every philosophical question.",
        "Competing theories must make different predictions in preregistered experiments across waking, sleep, anaesthesia, brain injury, animal nervous systems, organoids, and artificial systems. Measurements need independent replication and protection against circular definitions based only on human report.",
        "A successful science can improve clinical assessment and inform ethics while leaving the metaphysical hard problem unresolved. Legal status should not be derived from one contested metric, and uncertainty should increase caution rather than create a false binary test for sentience.",
    ),
    "galactic-civilization": (
        "Local Multi-Stellar Civilization",
        "A civilization among nearby stars, scaled to the distances that sub-light travel can actually cross in the represented centuries.",
        "Settlements require closed ecologies, repairable industry, demographic continuity, radiation protection, propulsion, destination braking, and the ability to function without rapid assistance from Earth. Communication delay makes every system politically and economically semi-autonomous.",
        "The Milky Way is roughly 100,000 light-years across. Galaxywide settlement and coordination belong on a timeline of hundreds of thousands to millions of years, not 2500. Descendant nodes are therefore rewritten as local interstellar networks and institutions.",
    ),
    "fusion-power": (
        "Utility-Scale Fusion Electricity",
        "Grid electricity from an integrated plant, not scientific gain inside a target or plasma.",
        "The accounting boundary includes magnets or drivers, heating, cryogenics, fuel processing, cooling, tritium systems, component replacement, and plant availability. A qualifying facility supplies net electricity over sustained campaigns and publishes the complete balance.",
        "Materials damage, exhaust, breeding and inventory of tritium, remote maintenance, reliability, licensing, and cost remain open across different concepts. The horizon is contingent and should follow demonstrated subsystem and pilot-plant progress rather than a fixed promise.",
    ),
    "inertial-confinement-fusion": (
        "High-Repetition Inertial Fusion Energy",
        "Turning target ignition into a complete, maintainable power station.",
        "A plant needs high-gain shots at useful repetition, efficient drivers, mass-produced precision targets, rapid chamber clearing, durable optics and blankets, heat conversion, fuel recovery, and remote maintenance. The full facility—not the capsule alone—must return net electricity.",
        "NIF's 2022 ignition result is the scientific precursor, so ignition itself cannot be dated as a future invention. Target cost, wall-plug efficiency, materials lifetime, and availability should define progress toward this separate engineering milestone.",
    ),
    "room-temp-superconductor": (
        "Ambient-Condition Superconductor",
        "A useful material under ordinary temperature and pressure, not a transient high-pressure laboratory signal.",
        "The qualifying material carries engineering current in relevant magnetic fields, survives manufacturing and cycling, forms wires or films, and can be produced reproducibly at useful scale. Transition temperature alone is not enough.",
        "No theorem guarantees such a material exists, so the horizon is unknown. Downstream systems should list it only where superconductivity is truly indispensable; a space elevator is primarily constrained by tether specific strength. Negative results, reproducibility failures, pressure dependence, and current-density limits belong in the story because they determine whether a reported transition is a material or merely an experimental signal.",
    ),
    "space-elevator": (
        "Space Elevator",
        "An orbital tether whose central problem is strength-to-weight ratio and defect-tolerant manufacture.",
        "A complete design must model taper, climber traffic, power, oscillations, atmosphere, lightning, atomic oxygen, radiation, debris, repair, equatorial anchoring, counterweight deployment, and controlled failure. The cable has to retain exceptional microscopic strength across tens of thousands of kilometres.",
        "Ambient superconductivity is not the gating prerequisite. Carbon nanotube and graphene results at small scale do not establish a manufacturable tether, and governance of the risk footprint is inseparable from the materials problem.",
    ),
    "nuclear-pulse-propulsion": (
        "Nuclear-Pulse Spacecraft Demonstration",
        "A future validation of Project Orion engineering, which originated in the 1950s.",
        "Pulse units detonate behind a pusher plate, with shock absorbers spreading the impulse into survivable acceleration. A demonstration would measure plate erosion, ablation, structural fatigue, pulse timing, navigation, and containment with no crew and a tightly bounded environment.",
        "Treaties, fallout, proliferation, launch accidents, electromagnetic effects, and public legitimacy are central constraints. Project Daedalus was a fusion design and is not an appropriate figure for this technology; the replacement diagram shows the pulse-unit and pusher-plate architecture.",
    ),
    "bussard-ramjet": (
        "Ram-Augmented Interstellar Propulsion",
        "Preserving useful magnetic-scoop ideas without claiming the classic self-fuelling ramjet works.",
        "A magnetic field may collect or deflect plasma for braking, interact with a pre-deployed particle stream, or supplement carried fuel. Each mission must account for collection efficiency, ionization, drag, fusion losses, field mass, radiation, and the changing interstellar medium.",
        "For the original proton-fusion ramjet, drag and poor reaction conditions can exceed thrust. It should not be described as the routine 23rd-century workhorse; it is a family of conditional propulsion and braking studies.",
    ),
    "antimatter-production": (
        "Antimatter Production and Storage",
        "An energy-intensive carrier whose feasibility depends on efficiency and containment, not stellar-civilization rhetoric.",
        "One gram of antimatter annihilating with one gram of matter releases about 1.8×10¹⁴ joules, or 43 kilotons of TNT. Producing it requires at least the stored energy and currently vastly more. Charged antiprotons can be trapped; bulk neutral antihydrogen storage remains hypothetical.",
        "Useful milestones should state particles captured per input joule, storage duration, loss rate, trap and shielding mass, and fail-safe behavior. Gram scale does not inherently require a Type II budget, but present efficiency makes it extraordinarily expensive.",
    ),
    "antimatter-weapon": (
        "Antimatter Weapon",
        "Correcting the thousand-fold milligram-to-kiloton error and keeping production and containment visible.",
        "One milligram of antimatter plus one milligram of matter releases about 1.8×10¹¹ joules, roughly 43 tonnes of TNT. One gram of antimatter plus one gram of matter produces roughly 43 kilotons. Yield scales with the annihilated mass, but coupling radiation into a target is a separate engineering question.",
        "Storage failure, accidental release, detection of production, security, and proliferation dominate the strategic problem. Fictional future treaties and invented incident histories should not be written as facts.",
    ),
    "relativistic-kinetic-weapon": (
        "Relativistic Kinetic Weapon",
        "A strategic consequence of relativistic propulsion with corrected impact-energy arithmetic.",
        "A one-tonne mass at 0.1c carries about 4.5×10¹⁷ joules, or 108 megatons of TNT. Chicxulub estimates are more than a million times greater and would require millions of tonnes at the same speed.",
        "Acceleration energy, dust impacts, guidance, target motion, early detection, and terminal interception matter as much as nominal yield. A near miss continues on its trajectory; it does not create a gamma-ray burst simply by passing a planet.",
    ),
    "kardashev-type-ii": (
        "Kardashev Type II Civilization",
        "Stellar-scale power with the human-energy comparison corrected by roughly three orders of magnitude.",
        "A Type II scale is around 10²⁶ watts, approximately five trillion times current global primary-energy use. A Dyson swarm is a distributed collection of orbiting collectors and habitats, not a rigid shell, and only gradual construction can keep orbits, resources, and heat rejection manageable.",
        "The internal date is a distant layout anchor rather than a prediction. Material throughput, autonomous industry, orbital stability, and governance could make full stellar-scale use take much longer than this tree depicts.",
    ),
    "seti-first-contact": (
        "Detection of Extraterrestrial Technology",
        "An unknown-horizon observation that does not require sending an interstellar probe first.",
        "Candidate technosignatures include structured radio or optical signals, artificial atmospheric chemistry, waste heat, or engineered transits. Confirmation requires repeat observations, independent instruments, open analysis, and serious natural alternatives. Search coverage, instrument sensitivity, observing time, and the prior probability assigned to rare natural phenomena should be reported so a non-detection or ambiguous candidate remains scientifically informative.",
        "Detection, communication, and physical contact are different milestones. A single anomaly or machine-learning score is insufficient, and the tree should not assert that a confirmed detection arrives in a particular decade.",
    ),
    "p-vs-np-resolved": (
        "Resolution of P versus NP",
        "An undated mathematical result rather than a scheduled technology.",
        "A valid proof must survive expert scrutiny and formal checking. Its practical consequences depend on the direction of the result, constructiveness, constants, average-case behavior, and the specific assumptions used by cryptographic systems.",
        "Quantum speedups do not settle the classical P-versus-NP question, and AI capability does not create a completion date. The node should remain a scientific milestone with an unknown horizon. Explanations should separate worst-case from average-case complexity and mathematical existence from an algorithm that is practical at real input sizes.",
    ),
    "continuum-hypothesis-resolution": (
        "Post-ZFC Foundational Consensus",
        "A choice and comparison of foundations, not a proof of an independent statement inside ZFC.",
        "Mathematicians may evaluate forcing axioms, large-cardinal principles, multiverse approaches, constructive systems, and type-theoretic foundations by fruitfulness, explanatory reach, and formal interoperability. Different fields may rationally retain different foundations.",
        "Any conclusion about the continuum hypothesis is conditional on added axioms. Calling that a definitive resolution hides the foundational choice; the revised node makes the choice explicit. A genuine consensus would be judged by durable mathematical fruitfulness, interoperability with formal tools, and clarity about which statements depend on which assumptions—not by a fictional final vote that ends foundational pluralism.",
    ),
    "galactic-communication-network": (
        "Interstellar Relay Network",
        "Delay-tolerant links among nearby inhabited systems, not real-time galaxywide communication.",
        "High-power optical terminals, autonomous relays, precise clocks, authentication, forward error correction, caching, and store-and-forward protocols keep messages moving despite years of latency and intermittent geometry. Local archives preserve essential knowledge when links fail.",
        "No protocol removes light-speed delay. The first network is local and asynchronous; a Milky-Way-scale exchange would take tens of thousands of years for a one-way message. Governance therefore resembles archival correspondence among autonomous societies, with versioned law, delayed revocation, local trust roots, and conflict resolution designed for messages whose senders may be dead before a reply arrives.",
    ),
}


for tech_id, changes in REVISIONS.items():
    if "desc" not in changes or tech_id in EXTRA_REWRITES:
        continue
    title = changes.get("name") or tech_id.replace("-", " ").title()
    description = changes["desc"]
    EXTRA_REWRITES[tech_id] = (
        title,
        description.split(". ", 1)[0] + ".",
        description,
        "This entry is a milestone definition, not a dated certainty. Evaluation should publish the baseline, full system boundary, failure modes, independent evidence, and the conditions that would delay, narrow, or falsify the forecast.",
    )


for tech in ADDITIONS:
    EXTRA_REWRITES[tech["id"]] = (
        tech["name"],
        tech["desc"].split(". ", 1)[0] + ".",
        tech["desc"],
        "The forecast is a milestone definition rather than a promise. Progress should be measured with independently reported cost, reliability, lifecycle, safety, and distributional outcomes, and the date should move when those observations change.",
    )


TYPE_OVERRIDES = {
    "universal-basic-income": "Institutional or cultural scenario",
    "liquid-democracy": "Institutional or cultural scenario",
    "network-state": "Institutional or cultural scenario",
    "ai-governance": "Institutional or cultural scenario",
    "ai-judge": "Institutional or cultural scenario",
    "longtermism": "Institutional or cultural scenario",
    "degrowth-economics": "Institutional or cultural scenario",
    "solarpunk": "Institutional or cultural scenario",
}

NEW_PHYSICS = {
    "vacuum-energy-extraction", "dark-energy-engineering", "warp-drive",
    "cosmic-string-ftl", "hypercomputation", "trans-computable-mathematics",
}

UNKNOWN_HORIZON = NEW_PHYSICS | {
    "agi", "room-temp-superconductor", "seti-first-contact",
    "p-vs-np-resolved", "continuum-hypothesis-resolution",
}


TECH_PATTERN = re.compile(
    r'  \{ id: "(?P<id>[^"]+)"[\s\S]*?\n    desc: "(?:\\.|[^"\\])*" \},'
)


def revise_tech(src: str, tech_id: str, changes: dict) -> str:
    match = next((m for m in TECH_PATTERN.finditer(src) if m.group("id") == tech_id), None)
    if not match:
        raise RuntimeError(f"missing tech {tech_id}")
    block = match.group(0)
    if "name" in changes:
        block = re.sub(r'(name: )"(?:\\.|[^"\\])*"', r'\1' + q(changes["name"]), block, count=1)
    if "category" in changes:
        block = re.sub(r'(category: )"[^"]+"', r'\1' + q(changes["category"]), block, count=1)
    if "year" in changes:
        block = re.sub(r'(year: )"[^"]+"', r'\1' + q(changes["year"]), block, count=1)
    if "prereqs" in changes:
        plist = "[" + ", ".join(q(p) for p in changes["prereqs"]) + "]"
        block = re.sub(r'prereqs: \[[^\]]*\]', "prereqs: " + plist, block, count=1)
    if "desc" in changes:
        block = re.sub(r'desc: "(?:\\.|[^"\\])*"', "desc: " + q(changes["desc"]), block, count=1)
    return src[: match.start()] + block + src[match.end() :]


def make_tech(tech: dict) -> str:
    return (
        f'  {{ id: {q(tech["id"])}, name: {q(tech["name"])}, era: {q(tech["era"])}, category: {q(tech["category"])},\n'
        f'    year: {q(tech["year"])}, prereqs: [{", ".join(q(p) for p in tech["prereqs"])}],\n'
        f'    desc: {q(tech["desc"])} }},'
    )


def forecast_values(block: str) -> tuple[str, str, str]:
    tech_id = re.search(r'id: "([^"]+)"', block).group(1)
    era = re.search(r'era: "([^"]+)"', block).group(1)
    category = re.search(r'category: "([^"]+)"', block).group(1)
    year_text = re.search(r'year: "([^"]+)"', block).group(1)
    try:
        year = int(re.match(r'\d+', year_text).group())
    except (AttributeError, ValueError):
        year = 2800

    if tech_id in UNKNOWN_HORIZON:
        horizon = "Unknown"
    elif era == "future":
        horizon = "Around 2100" if year >= 2100 else f"{year // 10 * 10}s"
    else:
        century = (year - 1) // 100 + 1
        horizon = f"{century}th century" if 10 <= century <= 20 else f"{century}st century" if century % 10 == 1 else f"{century}nd century" if century % 10 == 2 else f"{century}rd century" if century % 10 == 3 else f"{century}th century"

    if tech_id in NEW_PHYSICS:
        confidence = "Requires new physics"
    elif category in {"social", "economy"}:
        confidence = "Social scenario"
    elif era == "far-future":
        confidence = "Speculative engineering"
    elif year <= 2040:
        confidence = "Established trajectory"
    else:
        confidence = "Plausible extrapolation"

    if tech_id in TYPE_OVERRIDES:
        forecast_type = TYPE_OVERRIDES[tech_id]
    elif category == "knowledge" or tech_id in {"seti-first-contact", "p-vs-np-resolved"}:
        forecast_type = "Scientific milestone"
    elif category in {"social", "economy"}:
        forecast_type = "Institutional or cultural scenario"
    else:
        forecast_type = "Engineering milestone"
    return horizon, forecast_type, confidence


def add_forecast_metadata(src: str) -> str:
    def repl(match: re.Match) -> str:
        block = match.group(0)
        if 'era: "future"' not in block and 'era: "far-future"' not in block:
            return block
        # Metadata is intentionally stored on one line. Remove that complete
        # line before reinserting it so rerunning this script cannot duplicate
        # forecastType/confidence properties.
        block = re.sub(r'\n    horizon: "[^"]+"[^\n]*', "", block)
        block = re.sub(r'\n    (?:forecastType|confidence): "[^"]+",?', "", block)
        horizon, forecast_type, confidence = forecast_values(block)
        return re.sub(
            r'(\n    year: "[^"]+",)',
            r'\1\n    horizon: ' + q(horizon) + ', forecastType: ' + q(forecast_type) + ', confidence: ' + q(confidence) + ',',
            block,
            count=1,
        )
    return TECH_PATTERN.sub(repl, src)


def normalize_description_quotes(src: str) -> str:
    """Escape accidental raw double quotes inside one-line JS descriptions.

    Several legacy descriptions contain prose such as Second, "capacity": while
    the enclosing JavaScript string also uses double quotes. Browsers and the
    static-index builder cannot parse those lines. Existing escaped quotes are
    preserved, so the pass is safe to rerun.
    """
    line_pattern = re.compile(r'(?P<prefix>\bdesc: ")(?P<body>.*)(?P<suffix>" \},)')

    def fix_line(match: re.Match) -> str:
        body = match.group("body")
        out: list[str] = []
        for index, char in enumerate(body):
            if char == '"':
                slash_count = 0
                cursor = index - 1
                while cursor >= 0 and body[cursor] == "\\":
                    slash_count += 1
                    cursor -= 1
                if slash_count % 2 == 0:
                    out.append("\\")
            out.append(char)
        return match.group("prefix") + "".join(out) + match.group("suffix")

    return "\n".join(line_pattern.sub(fix_line, line) for line in src.split("\n"))


def update_data() -> None:
    src = DATA.read_text()
    src = src.replace(
        "// Each tech: { id, name, era, category, year (approx earliest evidence), prereqs[], desc }",
        "// Historical year = approximate earliest evidence. Future year = layout anchor; horizon is the user-facing forecast range.\n// Future entries also declare forecastType and confidence so scenarios are not presented as established fact.",
    )
    src = src.replace(
        '{ id: "far-future",    name: "Far Future",         name_zh: "远未来", range: "2100 – 2800",',
        '{ id: "far-future",    name: "Far Future",         name_zh: "远未来", range: "2100 onward",',
    )
    for tech_id, changes in REVISIONS.items():
        src = revise_tech(src, tech_id, changes)
    existing = {m.group("id") for m in TECH_PATTERN.finditer(src)}
    for tech in ADDITIONS:
        if tech["id"] in existing:
            src = revise_tech(src, tech["id"], tech)
    missing = [t for t in ADDITIONS if t["id"] not in existing]
    if missing:
        marker = "\n];\n\nwindow.TECH_TREE = { ERAS, CATEGORIES, TECHS };"
        block = "\n\n  // ─── Evidence-based future additions (2026 revision) ───\n" + "\n".join(make_tech(t) for t in missing)
        src = src.replace(marker, block + marker)
    src = add_forecast_metadata(src)
    src = normalize_description_quotes(src)
    DATA.write_text(src)


def set_extra(src: str, tech_id: str, values: tuple[str, str, str, str]) -> str:
    title, lede, milestone, constraints = values
    body = (
        f'  {q(tech_id)}: `\n'
        f'    <h3 class="extra-title">{title}</h3>\n'
        f'    <p class="extra-lede">{lede}</p>\n'
        f'    <h4>Milestone definition</h4>\n'
        f'    <p>{milestone}</p>\n'
        f'    <h4>Evidence, constraints, and uncertainty</h4>\n'
        f'    <p>{constraints}</p>\n'
        f'  `,'
    )
    pattern = re.compile(r'  ' + re.escape(q(tech_id)) + r': `[\s\S]*?\n  `,')
    match = pattern.search(src)
    if match:
        return src[: match.start()] + body + src[match.end() :]
    return src.rstrip()[:-2] + "\n\n" + body + "\n};\n"


def update_details() -> None:
    src = DETAILS.read_text()
    for tech_id, values in EXTRA_REWRITES.items():
        src = set_extra(src, tech_id, values)
    # Keep the extended-panel heading synchronized with every renamed node,
    # including entries whose longer legacy essay remains otherwise useful.
    names = {}
    for match in TECH_PATTERN.finditer(DATA.read_text()):
        name_match = re.search(r'name: ("(?:\\.|[^"\\])*")', match.group(0))
        if name_match:
            names[match.group("id")] = json.loads(name_match.group(1))
    for tech_id, name in names.items():
        pattern = re.compile(
            r'(' + re.escape(q(tech_id)) + r': `[\s\S]*?<h3 class="extra-title">)[^<]*(</h3>)'
        )
        src = pattern.sub(lambda match: match.group(1) + name + match.group(2), src, count=1)
    # Extended notes should read as scenarios, not as a fictional chronicle of
    # events that definitely occur in a named future decade.
    src = re.sub(r'\bBy (?:the )?20\d\ds?,', "In this scenario,", src)
    src = re.sub(r'\bby (?:the )?20\d\ds?\b', "in this scenario", src)
    DETAILS.write_text(src)


def update_translations() -> None:
    src = TRANSLATIONS.read_text()
    for tech_id, value in ZH.items():
        pattern = re.compile(r'  ' + re.escape(q(tech_id)) + r': "(?:\\.|[^"\\])*",')
        line = f'  {q(tech_id)}: {q(value)},'
        if pattern.search(src):
            src = pattern.sub(line, src, count=1)
        else:
            src = src.rstrip()[:-2] + "\n" + line + "\n};\n"
    TRANSLATIONS.write_text(src)


def unlock_block(tech_id: str, items: list[dict]) -> str:
    lines = [f'  {q(tech_id)}: [']
    for item in items:
        parts = [f'type: {q(item["type"])}', f'name: {q(item["name"])}', f'name_zh: {q(item["name_zh"])}']
        if item.get("wiki") is False:
            parts.append("wiki: false")
        elif item.get("wiki"):
            parts.append(f'wiki: {q(item["wiki"])}')
        lines.append("    { " + ", ".join(parts) + " },")
    lines.append("  ],")
    return "\n".join(lines)


def update_unlocks() -> None:
    src = UNLOCKS.read_text()
    for tech_id, items in NEW_UNLOCKS.items():
        body = unlock_block(tech_id, items)
        pattern = re.compile(r'  ' + re.escape(q(tech_id)) + r': \[[\s\S]*?\n  \],')
        match = pattern.search(src)
        if match:
            src = src[: match.start()] + body + src[match.end() :]
        else:
            src = src.rstrip()[:-2] + "\n" + body + "\n};\n"
    UNLOCKS.write_text(src)


def main() -> None:
    update_data()
    update_details()
    update_translations()
    update_unlocks()
    print(f"revised {len(REVISIONS)} future entries and ensured {len(ADDITIONS)} additions")


if __name__ == "__main__":
    main()
