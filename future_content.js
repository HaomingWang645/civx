// Evidence layer for the Near Future and Far Future eras.
//
// data.js keeps the compact card copy and details_extra.js keeps the longer
// scenario essays.  This file adds a dated research baseline, references, and
// targeted editorial corrections without mixing forecast prose with historical
// facts.  app.js renders the material as distinct sections in the expanded tab.

(() => {
  const SOURCES = {
    "ai-index-2026": {
      label: "Stanford HAI — AI Index Report 2026",
      url: "https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf"
    },
    "metr-horizons": {
      label: "METR — Measuring AI task-completion time horizons",
      url: "https://metr.org/time-horizons/"
    },
    "gemini-robotics": {
      label: "Google DeepMind — Gemini Robotics",
      url: "https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/"
    },
    "a-lab": {
      label: "Berkeley Lab — A-Lab autonomous materials laboratory",
      url: "https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/"
    },
    "imo-ai": {
      label: "Google DeepMind — AI at the 2025 International Mathematical Olympiad",
      url: "https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/"
    },
    "voice-bci": {
      label: "Nature (2025) — instantaneous voice synthesis from neural activity",
      url: "https://www.nature.com/articles/s41586-025-09127-3"
    },
    "casgevy": {
      label: "U.S. FDA — Casgevy gene-editing therapy",
      url: "https://www.fda.gov/vaccines-blood-biologics/casgevy"
    },
    "pig-kidney": {
      label: "NEJM (2025) — gene-edited pig kidney transplantation",
      url: "https://www.nejm.org/doi/full/10.1056/NEJMoa2412747"
    },
    "partial-reprogramming": {
      label: "Ageing Research Reviews (2025) — partial reprogramming review",
      url: "https://pubmed.ncbi.nlm.nih.gov/40096911/"
    },
    "organoid-bioprinting": {
      label: "Nature Reviews Bioengineering (2025) — organoid bioprinting",
      url: "https://www.nature.com/articles/s44222-024-00268-0"
    },
    "cancer-vaccine": {
      label: "Nature (2025) — personalized neoantigen vaccine trial",
      url: "https://www.nature.com/articles/s41586-024-08507-5"
    },
    "cultivated-food": {
      label: "FAO/WHO — Food safety aspects of cell-based food",
      url: "https://www.who.int/publications/i/item/9789240070943"
    },
    "fda-cultivated": {
      label: "U.S. FDA — cultured-animal-cell food consultation",
      url: "https://www.fda.gov/food/hfp-constituent-updates/fda-completes-second-pre-market-consultation-human-food-made-using-animal-cell-culture-technology"
    },
    "nif-2025": {
      label: "Lawrence Livermore — National Ignition Facility 2025 results",
      url: "https://annual.llnl.gov/fy-2025/national-ignition-facility-2025"
    },
    "iea-batteries": {
      label: "IEA — Battery storage in Global Energy Review 2026",
      url: "https://www.iea.org/reports/global-energy-review-2026/technology-battery-storage"
    },
    "iea-hydrogen": {
      label: "IEA — Global Hydrogen Review 2025",
      url: "https://www.iea.org/reports/global-hydrogen-review-2025"
    },
    "doe-ldes": {
      label: "U.S. DOE — Long-Duration Energy Storage Liftoff",
      url: "https://www.energy.gov/sites/default/files/2025-07/LIFTOFF_DOE_Long-Duration-Energy-Storage.pdf"
    },
    "doe-geothermal": {
      label: "U.S. DOE — Next-Generation Geothermal Liftoff",
      url: "https://www.energy.gov/sites/default/files/2025-07/LIFTOFF_DOE_Next-Generation-Geothermal%20Power.pdf"
    },
    "ocean-cdr": {
      label: "U.S. National Academies — Ocean-based carbon dioxide removal",
      url: "https://www.nationalacademies.org/read/26278"
    },
    "nist-pqc": {
      label: "NIST — Post-quantum cryptography standards",
      url: "https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards"
    },
    "superconductivity": {
      label: "Nature Communications (2025) — ambient-pressure superconducting limits",
      url: "https://www.nature.com/articles/s41467-025-63702-w"
    },
    "desi-2025": {
      label: "DESI Collaboration — 2025 dark-energy results",
      url: "https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/"
    },
    "ligo-o4": {
      label: "LIGO Scientific Collaboration — fourth observing run",
      url: "https://ligo.org/ligo-virgo-kagra-to-resume-and-extend-the-o4-run/"
    },
    "artemis": {
      label: "NASA — Artemis program",
      url: "https://www.nasa.gov/humans-in-space/artemis/"
    },
    "moon-base": {
      label: "NASA — Moon Base systems roadmap",
      url: "https://www.nasa.gov/moonbase-systems/"
    },
    "moxie": {
      label: "NASA — MOXIE oxygen-production experiment",
      url: "https://www.nasa.gov/solar-system/nasas-oxygen-generating-experiment-moxie-completes-mars-mission/"
    },
    "nasa-water": {
      label: "NASA — 98% water-recovery demonstration on the ISS",
      url: "https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/"
    },
    "dart": {
      label: "NASA — DART planetary-defense result",
      url: "https://science.nasa.gov/missions/dart/close-up-views-of-nasas-dart-impact-to-inform-planetary-defense/"
    },
    "neo-surveyor": {
      label: "NASA — NEO Surveyor mission",
      url: "https://science.nasa.gov/mission/neo-surveyor/"
    },
    "nasa-isam": {
      label: "NASA — In-space servicing, assembly, and manufacturing",
      url: "https://www.nasa.gov/isam/"
    },
    "solar-lens": {
      label: "NASA NIAC — solar gravitational-lens mission study",
      url: "https://www.nasa.gov/general/direct-multipixel-imaging-and-spectroscopy-of-an-exoplanet-with-a-solar-gravitational-lens-mission/"
    },
    "starshot": {
      label: "Breakthrough Initiatives — Starshot photon-engine specification",
      url: "https://breakthroughinitiatives.org/i/docs/rfp_photon_engine_final.pdf"
    },
    "space-solar": {
      label: "Caltech — MAPLE space solar-power demonstration",
      url: "https://www.caltech.edu/about/news/in-a-first-caltechs-space-solar-power-demonstrator-wirelessly-transmits-power-in-space"
    },
    "outer-space-treaty": {
      label: "UN Office for Outer Space Affairs — Outer Space Treaty",
      url: "https://www.unoosa.org/oosa/SpaceLaw/outerspt.html"
    },
    "antarctic-treaty": {
      label: "Antarctic Treaty Secretariat — peaceful-use provisions",
      url: "https://www.ats.aq/e/peaceful.html"
    },
    "eu-ai-act": {
      label: "European Commission — AI Act implementation timeline",
      url: "https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline"
    },
    "finland-ubi": {
      label: "Kela — Finnish basic-income experiment findings",
      url: "https://www.kela.fi/ajankohtaista/perustulokokeilu-opetti-mita-yhteiskunnallisen-kenttakokeen-toteuttaminen-vaatii"
    }
  };

  const DEFAULTS = {
    weapons: {
      frontier: "Current systems increasingly combine networked sensors, autonomy, electronic warfare, and precision effects, but performance is highly context-dependent. Future claims must account for spoofing, communications loss, civilian protection, escalation risk, and meaningful human control rather than treating faster automation as automatic superiority.",
      pathway: "A credible future system would be judged by resilient command, bounded autonomy, auditable decisions, and performance under adversarial testing—not by a prototype operating in a permissive demonstration.",
      refs: ["ai-index-2026"]
    },
    energy: {
      frontier: "The energy transition is already scaling batteries, renewables, nuclear systems, hydrogen projects, and carbon management, but each solves a different constraint. Whole-system accounting must include conversion losses, storage duration, transmission, materials, maintenance, and lifecycle emissions.",
      pathway: "The future milestone is an integrated service that is reliable and economical at useful scale; a record-setting component or isolated pilot is evidence, not completion.",
      refs: ["iea-batteries", "iea-hydrogen"]
    },
    tools: {
      frontier: "Advanced materials, robotics, and post-CMOS computing are progressing through narrow demonstrations. The central gap is usually not a single laboratory effect but manufacturability, error rates, energy use, durability, supply chains, and safe operation outside controlled settings.",
      pathway: "The scenario becomes credible when a complete system repeats the result at scale and reports the full energy, material, reliability, and maintenance boundary.",
      refs: ["a-lab", "gemini-robotics"]
    },
    knowledge: {
      frontier: "AI-assisted research and larger scientific instruments are expanding what can be searched, measured, and proved. They do not remove the need for reproducible evidence: benchmark success, suggestive correlations, and internally consistent theories remain distinct from discoveries that survive independent tests.",
      pathway: "A future breakthrough should specify a discriminating prediction, a reproducible observation or proof, and what result would count against it.",
      refs: ["a-lab", "imo-ai"]
    },
    medicine: {
      frontier: "Gene editing, cell therapy, neural interfaces, organ preservation, and precision medicine have produced real clinical results, but most futuristic extensions remain early trials or laboratory models. Safety, durability, access, and comparison with standard care matter as much as technical novelty.",
      pathway: "The milestone requires replicated clinical benefit with long follow-up, manageable harms, scalable production, and equitable delivery—not a single patient or preclinical result.",
      refs: ["casgevy", "pig-kidney"]
    },
    shelter: {
      frontier: "Long-duration settlement research currently centers on radiation protection, closed-loop life support, maintainability, local resources, and reliable logistics. The ISS has demonstrated high water recovery, while planetary habitats still depend on systems not yet proven together beyond low Earth orbit.",
      pathway: "A settlement becomes real when people can survive repeated failures and delayed resupply while maintaining health, power, food, air, water, and governance over years.",
      refs: ["nasa-water", "moon-base"]
    },
    transport: {
      frontier: "Reusable launch, electric propulsion, navigation, and autonomous spacecraft are improving, but interplanetary and interstellar concepts span very different readiness levels. Vehicle performance must include power source, heat rejection, shielding, braking, payload, and mission reliability.",
      pathway: "The milestone is an end-to-end mission demonstration with measured payload and energy accounting, not an idealized exhaust velocity or cruise speed by itself.",
      refs: ["nasa-isam", "starshot"]
    },
    subsistence: {
      frontier: "Food, water, and ecosystem technologies are moving from laboratory control toward regulated production and field deployment. Their value depends on energy and nutrient inputs, contamination control, land and water use, affordability, and ecological effects across the whole supply chain.",
      pathway: "A future food or resource system must sustain diverse populations through disruptions while showing audited environmental and nutritional performance at scale.",
      refs: ["cultivated-food", "fda-cultivated"]
    },
    communication: {
      frontier: "Secure networks, brain interfaces, distributed storage, and optical links are advancing at very different rates. Demonstrations often have low bandwidth, short distance, trusted nodes, or carefully controlled conditions that disappear in a civilizational-scale network.",
      pathway: "A credible network specifies latency, bandwidth, trust assumptions, error correction, repair, and governance—and continues to work when institutions and hardware change.",
      refs: ["nist-pqc", "voice-bci"]
    },
    economy: {
      frontier: "Digital institutions and social-policy experiments show that rules can be encoded, simulated, and evaluated, but legitimacy cannot be reduced to software. Distribution, accountability, exit rights, public goods, enforcement, and unequal bargaining power remain central design constraints.",
      pathway: "The future scenario succeeds only if it delivers measurable welfare and durable consent across ordinary cases, crises, and transfers of power.",
      refs: ["eu-ai-act", "finland-ubi"]
    },
    social: {
      frontier: "Generative media, virtual communities, biotechnology, and machine agency already challenge ideas about authorship, identity, consent, and moral status. Technical possibility does not settle which practices deserve recognition or which institutions can govern them fairly.",
      pathway: "The imaginative branch asks how norms and culture might adapt; it should remain plural and contested rather than presenting one social outcome as inevitable.",
      refs: ["ai-index-2026", "voice-bci"]
    }
  };

  const CONTEXT = {};
  const assign = (ids, frontier, pathway, refs) => ids.forEach(id => {
    CONTEXT[id] = { frontier, pathway, refs };
  });

  assign(
    ["agi", "superintelligence", "pan-galactic-coordination-ai", "ai-coordination-treaty", "direct-ai-democracy", "ai-governance", "ai-judge", "ai-decision-loop-compression"],
    "Frontier models now solve a wider range of coding, reasoning, and research tasks, yet capability remains jagged and long autonomous work is much less reliable than short benchmark tasks. Governance has also moved from principles to enforceable rules, including phased obligations for general-purpose and high-risk AI in the EU.",
    "The scenario becomes credible through robust transfer to unfamiliar work, calibrated uncertainty, adversarial evaluation, incident reporting, and institutions able to audit and restrain systems without assuming that fluent output equals general intelligence.",
    ["ai-index-2026", "metr-horizons", "eu-ai-act"]
  );

  assign(
    ["humanoid-robot", "autonomous-built-environment", "self-replicating-machines", "self-replicating-combat-drones", "drone-swarms", "autonomous-laboratories"],
    "Robots can now follow language instructions and generalize across selected manipulation tasks, while autonomous laboratories can plan and execute constrained materials workflows. Household success rates and operation in messy, changing environments still lag far behind polished demonstrations.",
    "Future autonomy requires graceful failure, recovery without expert intervention, safe collaboration, secure supply chains, and measured productivity over months—not a short scripted task or a machine that merely fabricates some of its own parts.",
    ["gemini-robotics", "a-lab", "ai-index-2026"]
  );

  assign(
    ["formal-mathematics", "p-vs-np-resolved", "univalent-foundations", "langlands-program-completion", "beyond-zfc-foundations", "continuum-hypothesis-resolution", "hypercomputation", "trans-computable-mathematics", "knowledge-closure"],
    "AI systems have reached competition-level mathematical performance and proof assistants can mechanically check large formal developments. That is substantial progress in search and verification, but it neither guarantees solutions to famous open problems nor changes computability limits without new physical assumptions.",
    "The grounded path joins machine conjecture, human interpretation, and formal checking. Farther branches remain conditional: a theorem is not established until its proof and assumptions can be independently inspected.",
    ["imo-ai"]
  );

  assign(
    ["brain-computer-interface", "brain-brain-communication", "memory-editing", "theory-of-consciousness", "whole-brain-emulation", "digital-immortality", "subjective-time-compression", "substrate-independent-humanity"],
    "Implanted interfaces have restored limited communication, including real-time expressive speech synthesis for a person with paralysis. They do not read unrestricted thoughts, transfer memories, or establish a theory of consciousness; bandwidth, invasiveness, stability, and interpretation remain major limits.",
    "The future branch should advance through reversible clinical functions and explicit consent before considering identity copying, shared experience, or subjective-time engineering. Those later nodes also require philosophical and legal criteria that neuroscience alone cannot settle.",
    ["voice-bci"]
  );

  assign(
    ["genetic-disease-eradication", "personalized-medicine", "cancer-cure", "universal-disease-eradication", "pandemic-surveillance-platform", "synthetic-biology"],
    "CRISPR-based therapy is now approved for specific blood disorders, personalized cancer vaccines and cell therapies are in early trials, and genomic surveillance can detect emerging variants. These are disease-specific advances, not evidence for one universal cure or risk-free population editing.",
    "A plausible future combines prevention, rapid diagnostics, adaptable platforms, targeted therapies, and public-health delivery. Success is measured disease by disease, with durable outcomes and access, rather than by declaring all illness eliminated.",
    ["casgevy", "cancer-vaccine"]
  );

  assign(
    ["lab-grown-organs", "printable-organs-on-demand", "xenotransplantation-organ-preservation", "artificial-womb"],
    "Gene-edited pig organs have reached living human recipients, and organoid bioprinting can arrange living building blocks for research. Full-size vascularized organs, long-term xenograft survival, and complete ectogenesis remain unsolved; current placental and organoid models reproduce only selected functions.",
    "The pathway runs through better preservation, perfusion, immune control, vascularization, and staged clinical indications. A future replacement organ must survive and function for years, not merely resemble tissue or remain viable briefly.",
    ["pig-kidney", "organoid-bioprinting"]
  );

  assign(
    ["anti-aging", "senolytic-longevity-therapy", "anti-senescence-cellular-substrate", "cryogenic-hibernation"],
    "Senolytics, metabolic interventions, and partial cellular reprogramming can alter aging markers in cells and animals, but no intervention has demonstrated broad, durable age reversal in humans. Reprogramming also raises loss-of-identity and cancer risks.",
    "A credible longevity milestone requires randomized human evidence showing longer healthy life across multiple organ systems, with cancer and functional outcomes followed for years. Hibernation adds separate challenges in metabolism, clotting, muscle, bone, and safe rewarming.",
    ["partial-reprogramming"]
  );

  assign(
    ["fusion-power", "inertial-confinement-fusion", "magnetic-confinement-fusion", "tritium-breeding", "aneutronic-fusion", "fusion-materials", "fusion-rocket"],
    "Inertial fusion has repeatedly exceeded target-level scientific breakeven; NIF reported an 8.6 MJ yield from 2.08 MJ delivered to the target in April 2025. That ratio excludes the much larger facility energy, and no fusion system yet supplies net electricity to a grid.",
    "The future milestone integrates fuel supply, breeding where required, heat conversion, radiation-resistant materials, remote maintenance, availability, and cost. Propulsion additionally needs a flight-mass power system and heat rejection, not just a high-temperature plasma.",
    ["nif-2025"]
  );

  assign(
    ["long-duration-energy-storage", "green-hydrogen-electrofuels", "geothermal-drilling", "advanced-fission-systems", "artificial-photosynthesis"],
    "Battery deployment is scaling quickly, while long-duration storage, advanced geothermal, low-emission hydrogen, and new fission designs are at mixed stages from commercial operation to demonstration. Cost, permitting, supply chains, utilization, and connection to real demand remain decisive.",
    "The future grid uses complementary technologies rather than a single winner. Each node should qualify through reliable delivered energy, complete lifecycle accounting, and repeatable construction and operation.",
    ["iea-batteries", "doe-ldes", "doe-geothermal", "iea-hydrogen"]
  );

  assign(
    ["carbon-capture-scale", "point-source-carbon-capture", "enhanced-weathering", "ocean-carbon-removal", "climate-adaptation-infrastructure"],
    "Carbon removal methods differ sharply in maturity, measurement, permanence, energy demand, and ecological risk. National Academies reviews treat ocean methods as a research agenda with unresolved environmental and governance questions, not as ready permission for planetary-scale deployment.",
    "Credible scale requires verified net removal, long monitoring, transparent baselines, liability for reversal, community consent, and emissions reduction alongside removal. Adaptation must be evaluated through avoided harm, especially for vulnerable populations.",
    ["ocean-cdr"]
  );

  assign(
    ["space-based-solar", "dyson-swarm", "kardashev-type-ii", "stellar-material-extraction", "stellar-engineering", "matrioshka-brain", "heat-limited-computing", "civilizational-entropy-management"],
    "Caltech's MAPLE experiment transmitted small amounts of power wirelessly in orbit and produced a detectable signal on Earth, a useful component demonstration far short of utility-scale space power. Stellar-scale collection and computation have no experimental analogue and are constrained by construction, control, and waste heat.",
    "The imaginative path scales only through modular hardware that can be manufactured, repaired, safely coordinated, and economically justified in space. Even an enormous collector cannot evade thermodynamics or eliminate heat rejection.",
    ["space-solar", "nasa-isam"]
  );

  assign(
    ["room-temp-superconductor", "metamaterials", "nanotechnology", "programmable-matter", "femto-engineering", "strange-quark-matter", "bose-einstein-engineering"],
    "Materials research can engineer unusual electromagnetic, quantum, and mechanical behavior, but dramatic effects often require small samples, cryogenic temperatures, high pressure, narrow bandwidth, or short lifetimes. Recent analysis finds ambient-pressure room-temperature conventional superconductivity extremely unlikely, though not forbidden by a general theorem.",
    "The future milestone is a stable, manufacturable material with useful current, force, lifetime, and safety under ordinary operating conditions. Nuclear-scale and programmable-matter branches remain speculative until a controllable building block exists.",
    ["superconductivity", "a-lab"]
  );

  assign(
    ["neuromorphic-chip", "photonic-computing", "reversible-computing", "post-cmos-integration", "quantum-applications", "quantum-internet", "dna-data-storage", "deep-time-archives"],
    "Post-CMOS devices, photonic accelerators, quantum processors, and molecular storage each excel on selected workloads, but end-to-end systems still pay for memory, conversion, control, cooling, error correction, and manufacturing. NIST has already standardized post-quantum cryptography; this is distinct from distributing quantum states over a quantum network.",
    "A future computing platform must beat strong conventional baselines on useful workloads after every overhead is counted. Long-lived networks and archives also need migration, repair, provenance, and human-readable recovery paths.",
    ["nist-pqc", "a-lab"]
  );

  assign(
    ["gravitational-wave-spectroscopy", "dark-sector-physics", "quantum-gravity", "higgs-factory", "dark-energy-engineering", "vacuum-energy-extraction", "warp-drive", "cosmic-string-ftl"],
    "LIGO–Virgo–KAGRA now observe many compact-object candidates, while DESI's three-year analysis strengthened—but did not settle—hints that dark energy may evolve. No experiment has demonstrated controllable dark matter, quantum gravity, negative energy suitable for propulsion, or extraction of vacuum energy.",
    "The near branch advances with better detectors and falsifiable models. Engineering branches remain conditional on discovering a manipulable physical effect; mathematical solutions alone do not show that the required matter, energy, stability, or causal structure exists.",
    ["ligo-o4", "desi-2025"]
  );

  assign(
    ["moon-base", "mars-landing", "mars-habitat", "mars-colony", "terraforming-mars", "space-habitat", "closed-cycle-cities", "lunar-industrial-base", "lunar-isru-logistics", "existential-risk-hedge"],
    "Lunar programs are moving from sorties toward mobility and habitation demonstrations, while Mars oxygen production has been demonstrated only at small scale by MOXIE. The ISS has reached 98% water recovery, but no habitat has closed the food, air, water, maintenance, and health loops for years without terrestrial support.",
    "The future settlement path is incremental: repeated safe missions, maintainable habitats, measured local-resource use, dependable logistics, then growing autonomy. A settlement is not self-sufficient merely because people remain there continuously.",
    ["artemis", "moon-base", "moxie", "nasa-water"]
  );

  assign(
    ["asteroid-mining", "asteroid-capture", "orbital-servicing-refueling", "asteroid-belt-settlement", "r-process-astromining"],
    "Sample-return missions prove that asteroid material can be reached and handled, while in-space servicing is developing through robotic inspection, refueling, repair, and assembly. No commercial operation has yet mined and sold extraterrestrial bulk material, and uncertain composition and microgravity mechanics dominate risk.",
    "The credible pathway starts with reconnaissance and resources consumed in space—especially water or structural material—before assuming profitable return of metals to Earth. Capture and settlement require planetary-defense review and long-duration logistics.",
    ["nasa-isam", "dart"]
  );

  assign(
    ["pulsar-navigation", "interstellar-probe", "beamed-sail-propulsion", "beamed-interstellar-probe", "interstellar-shielding-deceleration", "nuclear-space-propulsion", "nuclear-pulse-propulsion", "bussard-ramjet", "antimatter-propulsion", "von-neumann-probe", "generation-ship-colony"],
    "Pulsar navigation has been demonstrated experimentally, and laser-driven gram-scale sails are under serious study, but no hardware has approached interstellar cruise speed. Starshot's roughly 20%-of-light-speed target remains a concept requiring unprecedented lasers, pointing, sail materials, shielding, communication, and arrival strategy.",
    "The future path moves from instrumented sail and propulsion tests to complete probe missions with survivable payloads and braking. Crew, replication, or century-long habitats add biological and institutional problems far beyond propulsion.",
    ["starshot", "solar-lens"]
  );

  assign(
    ["space-elevator", "orbital-ring", "kugelblitz-drive", "antimatter-production", "antimatter-weapon", "relativistic-kinetic-weapon", "black-hole-engineering"],
    "These concepts are consistent with selected equations or laboratory phenomena but lack the materials, energy scale, confinement, or construction method needed for a system. Antimatter is produced only in tiny quantities, and no known material meets an Earth space elevator's full strength-to-weight and defect-tolerance requirements.",
    "They should remain conditional branches. Progress means demonstrating the missing physical or engineering primitive and a safe full-system architecture—not assigning a date based on extrapolated energy alone.",
    ["a-lab", "superconductivity"]
  );

  assign(
    ["lab-grown-meat", "precision-fermentation-agriculture", "advanced-water-reuse", "pleistocene-restored", "engineered-planetary-biosphere", "galactic-ecology"],
    "Cultivated animal cells have passed pre-market safety consultations for specific products, and water-recovery systems have achieved high reuse in space. Scaling food and ecosystem interventions still faces media and feedstock inputs, contamination, cost, energy, biodiversity, and governance.",
    "The future branch should prioritize resilient nutrition and water before ecological spectacle. Restored or engineered ecosystems need long monitoring, reversible trials, and rules for unintended spread and animal welfare.",
    ["cultivated-food", "fda-cultivated", "nasa-water"]
  );

  assign(
    ["planetary-defense-system", "directed-energy-weapons", "anti-satellite-warfare", "layered-air-missile-defense"],
    "DART changed Dimorphos's orbital period by 33 minutes, demonstrating kinetic deflection, while NEO Surveyor is intended to improve hazardous-object detection. This does not amount to a standing planetary shield: warning time, orbit determination, launch readiness, fragmentation, attribution, and international authority remain essential.",
    "A responsible future system begins with shared detection and rehearsed civil decision-making, then adds multiple deflection options. Military interception should not be conflated with asteroid defense or narrated as perfectly protective.",
    ["dart", "neo-surveyor", "outer-space-treaty"]
  );

  assign(
    ["cyber-kinetic-warfare", "strategic-memetic-warfare", "engineered-pathogen-defense", "sixth-gen-fighter"],
    "Cyber-physical attacks, generated persuasion, biosecurity screening, and highly networked aircraft are active fields, but effects are constrained by access, attribution, human behavior, countermeasures, and escalation. Claims based on a vendor roadmap or a controlled exercise should not be treated as operational fact.",
    "The future milestone emphasizes resilient defense: authenticated systems, safe degraded modes, recovery, provenance, public communication, and legal accountability. Offensive capability alone does not produce stable security.",
    ["ai-index-2026", "eu-ai-act"]
  );

  assign(
    ["universal-basic-income", "post-scarcity", "degrowth-economics", "network-state", "decentralized-autonomous-org", "liquid-democracy", "pre-warp-interstellar-trade"],
    "Finland's randomized basic-income experiment found limited employment effects but better reported wellbeing and less bureaucracy. Online organizations and experimental voting tools show new coordination mechanisms, yet taxes, public goods, legal jurisdiction, security, and unequal ownership remain outside the code.",
    "The future economy should be evaluated through distribution, resilience, ecological throughput, freedom, and administrative burden. Automation can relax scarcity in some goods without eliminating land, energy, attention, care, or political conflict.",
    ["finland-ubi", "eu-ai-act"]
  );

  assign(
    ["interstellar-treaty", "galactic-civilization", "galactic-citizenship", "universal-sentient-rights", "speciation-ethics", "substrate-pluralism", "sentientism"],
    "Existing space law supplies principles of peaceful use, state responsibility, and non-appropriation, while the Antarctic system shows how parties can cooperate without resolving every sovereignty claim. Neither framework settles interstellar resource rights, digital personhood, or enforcement across light-speed delays.",
    "The imaginative pathway uses local autonomy, authenticated records, slow ratification, mutual restraint, and revisable rights frameworks. It should accommodate political divergence rather than assuming a single centralized galactic state.",
    ["outer-space-treaty", "antarctic-treaty"]
  );

  assign(
    ["generative-art", "metaverse", "synthetic-performers", "procedural-infinite-worlds", "bio-art", "mind-linked-collective-art", "engineered-sensory-modalities", "ai-native-art-forms", "post-human-aesthetics", "stellar-scale-spectacle", "pan-galactic-festival", "constructed-religions"],
    "Generative systems, virtual performers, immersive worlds, and bio-art already expand the space of cultural production. Current disputes over training consent, provenance, labor, environmental cost, deceptive identity, and platform power are part of the technology—not external details.",
    "Future culture is best presented as a set of possible practices shaped by creators and audiences. Greater scale or novelty does not imply a single aesthetic, autonomous authorship, or the disappearance of human performance.",
    ["ai-index-2026", "voice-bci"]
  );

  assign(
    ["transhumanism", "speciation", "time-dilation-cultures", "end-time-philosophy", "solarpunk", "longtermism"],
    "Enhancement, climate response, demographic change, and spaceflight already generate competing ethical frameworks, but none follows mechanically from technical capability. Evidence can inform consequences; it cannot by itself decide identity, obligation to future people, acceptable inequality, or the value of remaining biologically human.",
    "These nodes are lenses for exploring choices and trade-offs. The future should preserve disagreement, reversible experimentation, and protections for people who decline enhancement or reject a dominant worldview.",
    ["voice-bci", "finland-ubi"]
  );

  assign(
    ["integrated-space-networks", "galactic-communication-network", "lingua-galactica", "solar-gravitational-lens-observatory"],
    "Space communication already combines radio, optical links, delay-tolerant networking, and autonomous scheduling. A solar gravitational-lens observatory remains a mission concept beyond roughly 548 AU, not a telescope under construction; interstellar networks inherit years of latency and very low received power.",
    "Future networks should be designed around delay rather than pretending it disappears. Durable protocols, local caches, authenticated scientific records, and graceful partial failure matter more than real-time metaphors borrowed from today's internet.",
    ["solar-lens", "nasa-isam"]
  );

  // Apply category baselines first, then retain the more specific contexts above.
  const tree = window.TECH_TREE;
  const futureTechs = tree.TECHS.filter(t => t.era === "future" || t.era === "far-future");
  for (const tech of futureTechs) {
    if (!CONTEXT[tech.id]) CONTEXT[tech.id] = { ...DEFAULTS[tech.category] };
  }

  // Intros that were too long, too certain, or mixed a milestone with an essay.
  // All stay close to the existing card footprint while preserving the useful idea.
  const INTRO_OVERRIDES = {
    "pulsar-navigation": "Spacecraft navigation using the stable pulses of rotating neutron stars as natural beacons. X-ray instruments can compare pulse arrival times with predicted ephemerides to estimate position without constant contact with Earth. NASA's SEXTANT experiment demonstrated the principle, but present accuracy, detector size, clock errors, and long integration times limit use. The milestone is a compact system that provides reliable autonomous navigation on deep-space missions and complements, rather than replaces, optical navigation and radio tracking.",
    "quantum-gravity": "A tested framework that consistently describes gravity and quantum phenomena in the same regimes. String theory, loop approaches, causal sets, and effective field theories offer mathematical programs, but none has decisive experimental confirmation. The milestone is not elegance alone: it is a distinctive prediction—perhaps in cosmology, black-hole physics, precision clocks, or high-energy observations—that survives independent measurement and distinguishes the framework from general relativity plus known quantum fields.",
    "digital-immortality": "A social and clinical scenario in which a sufficiently faithful brain emulation is treated as a continuation, copy, or descendant of a person. No technology can currently record the structure and state needed for a human emulation, and neuroscience cannot decide whether copying preserves personal identity. Beyond engineering, the milestone requires consent, legal status, continuity rules, security, and protections against involuntary duplication or deletion. The term describes a contested aspiration, not demonstrated immortality.",
    "mars-landing": "The first crewed expedition to land on Mars, operate safely on the surface, and return—or enter a deliberately provisioned longer stay. It requires heavy cargo delivery, radiation and microgravity countermeasures, reliable life support, surface power, ascent fuel, communications, and abort strategies across launch windows separated by years. Robotic missions and lunar operations are precursors, but no current schedule makes a crewed date dependable. The milestone is a completed mission with independently documented crew health and system performance.",
    "dna-data-storage": "Encoding digital information in synthesized DNA, then recovering it by sequencing. DNA offers exceptional density and can remain readable for long periods under controlled storage, but writing is slow and expensive, random access is difficult, and sequencing and error correction add overhead. The milestone is a practical archival service with standardized formats, reliable retrieval, migration plans, and lifecycle costs competitive for rarely accessed data. It complements conventional storage rather than replacing fast memory or everyday databases.",
    "self-replicating-machines": "Machines that can reproduce a large fraction of their hardware from local feedstocks with limited outside inputs. Factories already manufacture components for other factories, but no autonomous system mines raw material, refines it, fabricates every critical part, assembles a copy, and verifies it without extensive infrastructure. A credible milestone must publish its dependency boundary, replication time, energy and material balance, error control, and shutdown mechanisms. Partial self-expansion may be valuable long before unrestricted replication is possible.",
    "generative-art": "Creative practice in which models generate or transform images, music, text, video, performance, or interactive worlds in response to human direction or other inputs. The technology expands iteration and hybrid forms, but authorship still involves choices about data, prompts, editing, presentation, and context. Its future depends as much on consent, attribution, provenance, labor, and audience trust as on model capability. The milestone is not art without people, but durable creative forms and institutions built around human–machine collaboration.",
    "matrioshka-brain": "A hypothetical computing system using nested structures around a star to capture energy at successively lower temperatures. The concept extends a Dyson swarm by turning much of its energy into computation while radiating unavoidable waste heat outward. No precursor exists beyond ordinary data centers and small space-power demonstrations; construction, communication delay, fault management, and thermodynamic efficiency dominate the design. It is a far-future upper-bound scenario, not a forecast that stellar-scale intelligence must take this form.",
    "longtermism": "An ethical view that gives substantial weight to how present choices affect people and other beings in the distant future. It motivates work on extinction risks, institutional durability, and preserving valuable options, but estimates of far-future populations and probabilities are deeply uncertain. Critics warn that speculative benefits can overshadow present injustice or concentrate authority. A careful version therefore connects near-term evidence and accountable policy to long-term resilience instead of treating enormous hypothetical numbers as decisive by themselves.",
    "superintelligence": "A hypothetical AI whose general reasoning, learning, and strategic capability greatly exceeds the best humans across most cognitive domains. Rapid self-improvement is one proposed route, not an established law; progress could also be slow, bottlenecked, or uneven. Because capabilities and control may develop at different rates, the practical research agenda concerns evaluation, corrigibility, security, oversight, and limiting irreversible deployment. This node marks a high-impact scenario whose timing and even feasibility remain unknown.",
    "decentralized-autonomous-org": "An organization whose membership, treasury, voting, and selected operations are coordinated through smart contracts and public digital records. Existing DAOs demonstrate transparent proposals and programmable funds, but they still rely on legal systems, software maintainers, interfaces, oracles, and concentrated token ownership. The future milestone is not governance without humans; it is a durable institution with secure code, accountable delegation, dispute resolution, privacy, and a workable relationship to real-world law and public goods.",
    "substrate-independent-humanity": "A scenario in which persons can live on biological, synthetic, or computational substrates while retaining recognized identity and rights. Present prosthetics and neural interfaces replace or augment limited functions; no whole human mind has been transferred or emulated. The concept therefore depends on advances in neuroscience and computing as well as unresolved standards for continuity, consent, copying, embodiment, and legal personhood. Its central question is whether humanity becomes defined more by social and psychological continuity than by a particular material body.",
    "dark-sector-physics": "Experimental identification of the matter or fields responsible for phenomena currently attributed to dark matter, and possibly their interactions beyond gravity. Astronomical evidence for unseen mass is strong, but direct searches have not established a particle candidate, and modified-gravity alternatives remain under study. A qualifying discovery needs reproducible signals across detectors or observations, a consistent model, and tests that exclude backgrounds. It would open new physics; it would not automatically make dark matter an engineerable material.",
    "liquid-democracy": "A voting system in which people can vote directly on an issue or temporarily delegate their vote to a trusted person, with delegation changing by topic and remaining revocable. Digital platforms make the mechanism feasible, but small experiments reveal challenges in participation, privacy, expertise, unequal influence, and resistance to coercion or account capture. The milestone is a binding public institution that remains legitimate, accessible, secure, and understandable at scale—not merely software that can tally delegated votes.",
    "orbital-ring": "A proposed launch and transport structure in which a fast-moving mass stream or cable circles Earth and supports stationary platforms through controlled electromagnetic forces. Unlike a space elevator, it does not require one tether to reach geostationary orbit, but it demands enormous construction, precise active control, protection from debris, and safe behavior during power or component failure. No experimental structure validates the full concept. The node is a conditional megaproject unlocked by mature orbital manufacturing and materials, not a scheduled successor to rockets.",
    "asteroid-mining": "Robotic extraction and processing of water, metals, or minerals from asteroids for use in space or return to Earth. Sample-return missions prove access to small quantities, not commercial mining. Economics depend on target composition, prospecting uncertainty, microgravity excavation, processing, transport, demand, and planetary-defense constraints. Water used as propellant or life-support feedstock in space may be a more plausible early market than precious metals returned to Earth. The milestone is sustained sale or operational use of verified extraterrestrial material.",
    "sixth-gen-fighter": "A future combat-air system combining crewed aircraft, uncrewed collaborators, distributed sensors, electronic warfare, secure networking, and adaptable software. Individual national programs use different requirements, so the label does not describe one settled design or guaranteed generation. The milestone is an operational system that demonstrates survivability, mission effectiveness, maintainability, and disciplined human control under realistic electronic and cyber attack. Cost, escalation risk, interoperability, and autonomous-weapons policy remain as important as speed or stealth.",
    "gravitational-wave-spectroscopy": "Using gravitational-wave signals to infer detailed properties of compact objects and test gravity under extreme conditions. Today's detector network already measures mergers and population statistics; higher sensitivity and additional observatories could resolve multiple ringdown modes, continuous sources, and broader frequency bands. The milestone is repeated, high-signal observations that distinguish competing models of black holes, neutron-star matter, or gravity—not simply another detection. Results must be consistent across instruments and analysis methods.",
    "quantum-internet": "A network that distributes quantum states or entanglement between distant nodes for tasks such as quantum key distribution, networked sensing, or distributed quantum computing. Photons cannot be copied and amplified like ordinary data, so long distances require low-loss links, quantum memories, and repeaters. Existing demonstrations remain small or specialized. The quantum internet would complement classical networks, which still carry control and most information; its milestone is reliable multi-node service with quantified rate, fidelity, security assumptions, and interoperability.",
    "post-scarcity": "An economic scenario in which automation, abundant energy, and advanced production make many essential goods inexpensive enough that access is no longer governed mainly by wages or prices. It does not abolish scarcity: land, energy, time, care, attention, rare materials, and political power remain limited. The milestone is sustained universal access to housing, food, healthcare, education, and basic infrastructure with low ecological cost. Distribution and ownership determine whether productive abundance becomes shared security or deeper concentration.",
    "metaverse": "Persistent, interoperable digital spaces where people work, learn, play, trade, and create through avatars and mixed-reality interfaces. Today's games, social worlds, and spatial-computing platforms supply pieces, but identity, assets, moderation, accessibility, privacy, and standards remain fragmented. A meaningful milestone is not one company's headset ecosystem; it is a durable network of worlds with user agency, portable identity where desired, accountable governance, and clear boundaries between immersive participation and manipulation.",
    "programmable-matter": "Materials or assemblies that can alter shape, optical properties, stiffness, or function under digital control. Current precursors include modular robots, active metamaterials, soft actuators, and shape-memory systems, each with narrow capabilities. Science-fiction-like matter that becomes arbitrary objects would require extraordinary resolution, power, bonding, sensing, and error control. The milestone is a manufacturable material that performs several useful transformations repeatedly and safely while reporting its energy, load, speed, and durability limits.",
    "mars-habitat": "A Mars surface habitat that protects crews through long missions with delayed rescue and infrequent resupply. It must integrate radiation shielding, reliable power, air and water recovery, dust control, food, medical care, maintenance, and psychologically workable living space. MOXIE demonstrated small-scale oxygen production from the atmosphere, but no complete habitat has operated on Mars. The milestone is multi-year occupied performance with safe degraded modes and measured use of local resources, not an inflatable module alone.",
    "dyson-swarm": "A hypothetical population of independent solar collectors, habitats, and industries orbiting a star and capturing a significant share of its energy. A swarm avoids the impossible stresses of a rigid shell, but still requires space manufacturing, collision control, communication, maintenance, and vast material flows. Space solar-power experiments are extremely small precursors. The milestone would be sustained, modular growth with measurable energy delivery and manageable orbital and thermal effects; it is a scale of infrastructure, not evidence of a single enclosing object.",
    "photonic-computing": "Computing that uses light for selected operations or communication, potentially reducing data-movement energy and accelerating matrix calculations. Photonic chips already perform specialized inference and high-speed interconnect functions, but memory, control, nonlinear operations, conversion, precision, and manufacturing remain bottlenecks. The milestone is an end-to-end system that beats strong electronic alternatives on useful workloads after lasers, converters, error correction, and cooling are counted. It will likely complement electronics rather than replace every transistor.",
    "interstellar-probe": "A scientific spacecraft sent into interstellar space or toward another star with instruments capable of returning useful data. Voyager crossed the heliopause but is not targeted at a nearby system; proposed laser sails could travel much faster with gram-scale payloads. The milestone requires propulsion, precision navigation, dust protection, power, extreme-lifetime electronics, communication, and ideally arrival braking. A credible mission is defined by its complete payload and link budget, not cruise speed alone.",
    "generation-ship-colony": "A hypothetical interstellar habitat whose population lives and reproduces during a voyage lasting multiple generations. It trades extreme propulsion demands for equally difficult life-support, genetic, medical, cultural, and governance requirements. No closed ecosystem or isolated community has demonstrated the necessary centuries of resilience, and faster probes should precede any crewed attempt. The milestone would require informed consent across generations, repairable industry, viable population planning, destination braking, and the ability to survive loss of contact with Earth.",
    "memory-editing": "Clinical techniques that deliberately weaken, strengthen, or reconsolidate specific memories to treat trauma, addiction, or neurological disease. Current therapies and experiments can influence emotional associations or reconsolidation under limited conditions; they cannot select and rewrite a complex autobiographical memory like a file. The milestone is a precise, durable, and reversible intervention with strong safeguards for consent, identity, legal evidence, and misuse. Therapeutic value should be established before enhancement or commercial manipulation is considered.",
    "hyperloop": "High-speed ground transport using vehicles in low-pressure tubes to reduce aerodynamic drag. Short test tracks have demonstrated components, but no system has shown safe, economical passenger service at the proposed speed and throughput. Vacuum maintenance, switching, emergency evacuation, thermal expansion, ride quality, land acquisition, and station capacity affect the whole design. The milestone is certified intercity operation with lifecycle cost and energy use competitive with rail and aviation—not a capsule speed record in a short tube.",
    "universal-basic-income": "A recurring cash payment provided individually and without a work requirement or means test. Trials can test behavior and wellbeing, but they do not by themselves settle national financing, inflation, housing constraints, migration, or interaction with public services. Finland's experiment found limited employment effects alongside improved reported wellbeing and reduced bureaucracy. The future milestone is a durable, adequately funded policy evaluated against poverty, health, freedom, work, distribution, and the benefits it replaces or preserves.",
    "asteroid-belt-settlement": "Permanent communities in the main asteroid belt supported by habitats, reliable transport, power, closed-loop life support, and local material processing. The belt's resources are dispersed across enormous distances, so it is not one compact mining district. Radiation, low gravity, medical care, communication delay, economics, and emergency logistics dominate viability. A credible settlement would grow from robotic prospecting and industrial outposts and demonstrate years of survival with limited Earth resupply before claiming political or economic independence.",
    "artificial-womb": "An extracorporeal system that supports part of fetal development outside a human body. Experimental platforms have sustained extremely premature animal fetuses in fluid environments, but complete human gestation has not been achieved and would raise distinct developmental, medical, legal, and ethical questions. A realistic early milestone is improved survival and health for extremely premature infants under carefully regulated clinical trials. Full ectogenesis is a separate, much more speculative scenario involving consent, parenthood, inequality, and long-term follow-up.",
    "speciation": "A future in which long-isolated, deliberately modified, or differently embodied human populations diverge enough to become distinct biological or reproductive lineages. Cultural separation can occur quickly; biological speciation ordinarily takes much longer and is not guaranteed by space settlement or enhancement. The milestone would require sustained heritable divergence and careful scientific definition, while the more immediate issue is ethical: preventing discrimination, coercive breeding, or unequal rights as human variation grows.",
    "lunar-industrial-base": "A network of lunar facilities that extracts local material and produces useful propellant, shielding, structures, or components at sustained scale. Polar resources and regolith are promising but must be mapped, excavated, processed, and maintained in vacuum, dust, radiation, and extreme temperatures. The economic case depends on what is cheaper to make locally than launch from Earth. The milestone is reliable delivery of certified products to lunar or orbital customers, not the mere presence of a pilot reactor or excavator.",
    "network-state": "A digitally organized community that develops durable governance, shared assets, and a physical presence across one or more jurisdictions. Online coordination and portable membership are real; sovereignty, public services, taxation, policing, and territorial recognition still depend on states and local residents. The milestone is not a large follower count or temporary gathering, but a legitimate institution with accountable leadership, dispute resolution, rights for minorities and non-members, financial transparency, and negotiated legal status.",
    "printable-organs-on-demand": "Biofabrication of patient-compatible tissues or organs with controlled cell placement, architecture, and function. Organoid printing already creates useful research models, but full organs require dense vascular and nerve networks, multiple cell types, mechanical strength, maturation, sterility, and reliable integration after transplantation. The milestone is reproducible manufacture and long-term clinical function under regulated quality control. Smaller grafts and tissue patches are plausible steps; a printed shape that briefly contains living cells is not an organ replacement.",
    "nanotechnology": "Engineering structures and devices at nanometre scales to obtain useful chemical, optical, electronic, or mechanical behavior. Nanoparticles, semiconductor fabrication, catalysts, and molecular machines already make nanotechnology a broad present-day field. The future milestone is more programmable and general molecular manufacturing, but atomically precise production must still solve error correction, feedstocks, energy, throughput, and containment. It should not be equated with unrestricted self-replicating assemblers or assumed to make material goods nearly free.",
    "fusion-rocket": "Space propulsion that uses fusion reactions to heat propellant or produce directed exhaust. Fusion could offer high exhaust velocity, but a useful vehicle also needs ignition, confinement, shielding, power conversion, radiators, fuel handling, and a mass low enough to accelerate. No fusion reactor has yet produced net grid electricity, much less flown. The milestone is a ground-tested integrated engine with measured thrust, specific impulse, lifetime, and total mass, followed by an uncrewed mission demonstration.",
    "existential-risk-hedge": "Infrastructure and institutions designed to keep civilization recoverable after global catastrophe. Examples include redundant food and energy systems, seed and data archives, protected refuges, pandemic readiness, resilient communications, and eventually settlements beyond Earth. Off-world populations are not automatically independent or safe; they may share supply chains, software, pathogens, or political failures. The milestone is demonstrated recovery capacity across several plausible disasters, with transparent governance and support for prevention rather than a privileged escape plan.",
    "anti-aging": "Interventions intended to slow multiple mechanisms of biological aging and extend healthy function, rather than treat one age-related disease at a time. Animal studies and early human trials investigate senescent cells, metabolism, immune aging, and epigenetic state, but no therapy has shown broad age reversal or large lifespan extension in humans. The milestone is replicated clinical evidence across organ systems with long follow-up, acceptable cancer and other risks, functional benefits, and access beyond a small wealthy population.",
    "stellar-engineering": "Deliberate alteration of a star's environment, output, motion, or lifetime using very large-scale infrastructure. Proposed methods include controlled mass extraction, asymmetric radiation pressure, or long-lived collector swarms, but none has an experimental precursor beyond ordinary solar observation and tiny space-power systems. The milestone would begin with measurable manipulation of stellar material using autonomous, repairable hardware. Energy availability alone does not solve stability, heat, materials, coordination, or the consequences for inhabited systems.",
    "ai-governance": "Use of AI in public administration together with rules for governing AI itself. Systems can summarize evidence, detect patterns, or assist casework, but binding decisions require explainability appropriate to the stakes, appeal, privacy, bias testing, security, and a clearly responsible human institution. The EU AI Act is an early risk-based framework; claims of autonomous 'AI judges' often overstate limited pilots. The milestone is accountable public value under independent audit, not replacing democratic legitimacy with model output.",
    "neuromorphic-chip": "Computing hardware inspired by features of nervous systems, such as event-driven signals, local memory, spiking neurons, and massive parallelism. Existing chips can be efficient for selected sensing and inference tasks, but programming tools, training, precision, benchmarking, and integration limit general use. The milestone is a reliable platform that delivers reproducible energy or latency advantages on important workloads after data conversion and training costs are included. Biological inspiration does not imply consciousness or human-like intelligence.",
    "artificial-photosynthesis": "Engineered systems that use sunlight to produce fuels or chemical feedstocks from water, carbon dioxide, or nitrogen-containing inputs. Laboratory devices can demonstrate individual reactions, but efficiency, catalyst lifetime, product separation, scarce materials, safety, and cost determine practical value. The milestone is continuous outdoor operation at useful scale with verified lifecycle emissions and competitive delivered product. It complements renewable electricity and electrolysis rather than automatically outperforming them.",
    "engineered-planetary-biosphere": "Deliberate management or construction of ecosystems at planetary scale, from climate-resilient restoration on Earth to closed or partially open ecologies elsewhere. Current restoration, gene drives, synthetic biology, and controlled ecosystems offer limited tools, not command of ecological complexity. The milestone requires staged, reversible interventions with long monitoring, evolutionary stability, biodiversity protection, and legitimate governance. A biosphere is a network of changing organisms and environments, not a machine whose outputs remain fixed after design.",
    "transhumanism": "A family of views supporting the use of technology to expand human health, ability, lifespan, or forms of embodiment. Prosthetics, reproductive technologies, gene editing, and neural interfaces make parts of the debate current, while radical enhancement and mind transfer remain speculative. The central issues are consent, safety, unequal access, pressure to conform, disability justice, and rights for modified or unmodified people. Transhumanism is an ethical and political project, not an inevitable stage after biotechnology.",
    "cybernetic-enhancement": "Integrated prosthetic, neural, sensory, or computational systems that restore or extend bodily functions. Cochlear implants, deep-brain stimulation, robotic limbs, and brain interfaces demonstrate narrow forms, but seamless multi-system enhancement faces surgery, infection, power, calibration, repair, security, and neural adaptation. The milestone is long-term everyday benefit that users can control and safely remove or upgrade. Medical restoration is the clearest path; elective performance enhancement adds fairness, coercion, and access questions.",
    "von-neumann-probe": "A hypothetical autonomous spacecraft that uses local resources to manufacture descendants, allowing exploration to expand without launching every probe from Earth. No system can presently reproduce its mining, refining, electronics, propulsion, and quality-control chain. Partial replication and self-repair are more plausible precursors. The milestone requires a bounded dependency audit, error containment, reliable communication, destination protection, and shutdown authority; exponential growth is a mathematical possibility, not proof of safe or feasible engineering.",
    "metamaterials": "Engineered structures whose geometry produces electromagnetic, acoustic, thermal, or mechanical responses uncommon in bulk materials. Demonstrations include negative refraction, compact antennas, cloaking over narrow conditions, and unusual vibration control. Performance is often limited by bandwidth, loss, angle, fabrication scale, or active power. The milestone is a durable, mass-manufactured material that retains a valuable response across realistic environments. Metamaterials can improve sensors and shielding without implying perfect invisibility or violation of ordinary physical limits."
  };

  for (const [id, desc] of Object.entries(INTRO_OVERRIDES)) {
    const tech = futureTechs.find(t => t.id === id);
    if (tech) tech.desc = desc;
  }

  // Replace a few extended entries that presented illustrative future history as fact.
  const DETAIL_OVERRIDES = {
    "interstellar-treaty": `
      <h3 class="extra-title">Interstellar Treaty</h3>
      <p class="extra-lede">A durable governance framework between politically independent settlements in different star systems.</p>
      <h4>The coordination problem</h4>
      <p>Years of communication delay make real-time central government impractical. Participating systems would need substantial local autonomy while coordinating through authenticated records, slow ratification, transparent verification, and rules that remain usable when no party has current information about the others.</p>
      <h4>Likely scope</h4>
      <p>A workable treaty could cover jurisdiction, resource access, military restraint, environmental protection, autonomous systems, scientific exchange, migration, and contact with unfamiliar intelligence. Existing space and commons law supply precedents, but neither the Outer Space Treaty nor the Antarctic Treaty already resolves these questions.</p>
      <h4>What would count</h4>
      <p>The milestone is not a ceremonial declaration. The framework must retain participation, legitimate amendment, dispute resolution, and compliance across at least two inhabited star systems despite delay, political divergence, and changing technology.</p>
    `,
    "asteroid-mining": `
      <h3 class="extra-title">Asteroid Resource Industry</h3>
      <p class="extra-lede">Commercially useful extraterrestrial material, with prospecting and transport included in the accounting.</p>
      <h4>Nearer pathway</h4>
      <p>Water, oxygen, and structural feedstock used in orbit may avoid more launch mass than precious metals returned to Earth. That advantage is conditional on finding a suitable body, anchoring in microgravity, processing uncertain material, and delivering a certified product to a real customer.</p>
      <h4>Milestone definition</h4>
      <p>A qualifying operation repeatedly extracts and sells or consumes a measured quantity of asteroid material. Its balance sheet includes failed prospecting, energy, equipment replacement, transport time, planetary-defense review, and competition from terrestrial launch and recycling.</p>
      <h4>Failure modes</h4>
      <p>Sample return proves access, not profitability. Commodity prices can fall, composition can differ from remote sensing, fine material can foul machinery, and moving an object can create unacceptable collision risk. Those uncertainties make staged robotic use more credible than claims of instant abundance.</p>
    `,
    "ai-governance": `
      <h3 class="extra-title">Accountable AI Governance</h3>
      <p class="extra-lede">Public institutions using AI under rules that preserve responsibility, review, and democratic authority.</p>
      <h4>Present boundary</h4>
      <p>AI can assist research, translation, fraud detection, and case triage. It can also reproduce bias, fabricate reasons, leak sensitive data, and become difficult to contest when agencies treat an output as objective. Widely repeated stories of an autonomous Estonian “AI judge” overstate what was proposed.</p>
      <h4>Milestone definition</h4>
      <p>A qualifying deployment publishes its legal basis, data limits, error rates, impact assessment, audit process, security model, and routes for explanation and appeal. Officials remain identifiable and responsible for binding decisions.</p>
      <h4>Future pathway</h4>
      <p>As systems become more capable, governance may include licensed high-risk uses, incident reporting, independent evaluations, compute or deployment controls, and international coordination. Legitimacy comes from institutions and affected people, not from model scale.</p>
    `,
    "digital-immortality": `
      <h3 class="extra-title">Digital Continuation</h3>
      <p class="extra-lede">A speculative identity practice built on whole-brain emulation, not a demonstrated route around death.</p>
      <h4>Technical dependency</h4>
      <p>A system would need to capture the biological organization and dynamic state required for a person's memories, dispositions, and cognition, then reproduce them on another substrate. No human brain has been recorded or emulated at anything close to that level.</p>
      <h4>Identity is not a benchmark</h4>
      <p>Behavioral similarity cannot establish that subjective continuity survived. Societies could instead regard an emulation as a copy, descendant, estate representative, or new person. Each choice produces different rules for consent, inheritance, marriage, duplication, liability, and deletion.</p>
      <h4>Milestone definition</h4>
      <p>Technical fidelity, voluntary informed consent, secure operation, legal status, and long public deliberation would all be required. The tree keeps the node conditional because neither neuroscience nor philosophy currently supplies an accepted continuity test.</p>
    `,
    "strategic-memetic-warfare": `
      <h3 class="extra-title">Strategic Memetic Warfare</h3>
      <p class="extra-lede">AI-assisted influence operations aimed at changing behavior, trust, and collective decision-making.</p>
      <h4>Present evidence</h4>
      <p>Generated text, images, voices, and synthetic personas can reduce the cost of producing persuasive or deceptive material. Their actual effect is not automatic: audiences adapt, distribution matters, attribution is difficult, and repeated exposure can provoke resistance as well as belief.</p>
      <h4>Future pathway</h4>
      <p>More capable systems could personalize narratives, test messages continuously, and coordinate across platforms. Defensive infrastructure would combine provenance, independent media, rapid investigation, platform accountability, privacy-preserving research, and public resilience.</p>
      <h4>Milestone definition</h4>
      <p>The node is reached when adaptive campaigns show reproducible strategic effects under real countermeasures. It should never imply that an AI can deterministically control a population.</p>
    `,
    "planetary-defense-system": `
      <h3 class="extra-title">Planetary Defense System</h3>
      <p class="extra-lede">A continuously maintained chain from hazardous-object discovery to a legitimate, rehearsed response.</p>
      <h4>What exists</h4>
      <p>DART demonstrated that a kinetic impact can change a small body's orbit, and NEO Surveyor is designed to improve discovery of hazardous asteroids and comets. One successful experiment does not provide complete sky coverage or a ready response to every orbit, size, composition, and warning time.</p>
      <h4>System architecture</h4>
      <p>The system joins surveys, orbit refinement, characterization, civil planning, launch capacity, several deflection methods, international decision rules, and follow-up measurement. Long warning time is often more valuable than a powerful last-minute interceptor.</p>
      <h4>Milestone definition</h4>
      <p>Readiness must be demonstrated through repeated exercises and deployable hardware, with authority and liability agreed before a crisis. Natural-hazard defense should remain distinguishable from military control of space.</p>
    `,
    "femto-engineering": `
      <h3 class="extra-title">Femto-Engineering</h3>
      <p class="extra-lede">A conditional branch for controlled engineering at nuclear length scales.</p>
      <h4>Present boundary</h4>
      <p>Nuclear physics can create isotopes, excite selected nuclear states, and synthesize short-lived nuclei. That is not a general manufacturing toolkit: nuclei are governed by quantum interactions, many products decay, and useful control often requires large accelerators or reactors.</p>
      <h4>What would change</h4>
      <p>A true engineering discipline would need repeatable methods to design, create, arrange, and stabilize nuclear-scale structures with useful input-output behavior. Energy density alone is not enough; controllability, lifetime, radiation, waste, and containment set the practical boundary.</p>
      <h4>Tree role</h4>
      <p>This speculative node links advanced materials to exotic-matter branches. It remains undated until an experimentally controllable nuclear building block appears.</p>
    `,
    "pan-galactic-festival": `
      <h3 class="extra-title">Pan-Galactic Festival</h3>
      <p class="extra-lede">A shared cultural form across settlements that cannot experience the same event in real time.</p>
      <h4>Asynchronous culture</h4>
      <p>Across interstellar distances, “together” would mean following a common score, calendar convention, archive, or evolving theme rather than exchanging live performances. Every system would interpret the event locally, and later transmissions could become material for celebrations generations elsewhere have not yet begun.</p>
      <h4>Why it matters</h4>
      <p>The festival tests whether a dispersed civilization can sustain belonging without pretending away light-speed delay. Translation, access, cultural appropriation, archival integrity, and the right not to participate matter as much as spectacle.</p>
      <h4>Tree role</h4>
      <p>It grows from interstellar communication and plural citizenship and leads toward shared institutions only in a cultural—not centralized—sense.</p>
    `
  };

  Object.assign(window.TECH_DETAIL_EXTRA, DETAIL_OVERRIDES);
  window.FUTURE_RESEARCH_SOURCES = SOURCES;
  window.FUTURE_RESEARCH_CONTEXT = CONTEXT;
})();
