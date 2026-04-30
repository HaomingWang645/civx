#!/usr/bin/env python3
"""Audit recent unlock additions in unlocks.js. For each unlock, check if a
Wikipedia article exists for that exact name. If not, either:
  - Tag wiki: false (speculative concept, no article)
  - Add wiki: "Real Article Title" (canonical article exists under different name)

Manual override map below decides each case. Then rewrite the matching lines."""

import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
UNLOCKS = ROOT / "unlocks.js"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# Override map for unlock names I added that DON'T resolve to a real Wikipedia
# article. Each value is either:
#   None              → tag wiki: false (speculative; no article exists)
#   "Article Title"   → link directly to that Wikipedia article
OVERRIDES = {
    # ─── Future/Far-Future weapons (recent additions) ───
    "Stuxnet":                                  "Stuxnet",
    "NotPetya":                                  "Petya and NotPetya",
    "U.S. Cyber Command":                        "United States Cyber Command",
    "Tallinn Manual":                            "Tallinn Manual",
    "HELIOS Laser":                              "AN/SEQ-3 Laser Weapon System",
    "DragonFire":                                "DragonFire (laser weapon)",
    "Iron Beam":                                 "Iron Beam",
    "U.S. Naval Research Laboratory":            "United States Naval Research Laboratory",
    "Bayraktar TB2":                             "Bayraktar TB2",
    "Switchblade 600":                           "AeroVironment Switchblade",
    "Pentagon Replicator Initiative":            None,
    "Anduril Industries":                        "Anduril Industries",
    "Fengyun-1C ASAT Test":                      "2007 Chinese anti-satellite missile test",
    "Mission Shakti":                            "Mission Shakti",
    "U.S. Space Force":                          "United States Space Force",
    "China PLA Strategic Support Force":         "People's Liberation Army Strategic Support Force",
    "BARDA":                                     "Biomedical Advanced Research and Development Authority",
    "DARPA Pandemic Prevention Platform":        None,
    "Metagenomic biosurveillance":               "Metagenomics",
    "Biological Weapons Convention":             "Biological Weapons Convention",
    "AI persuasion campaign":                    None,
    "Internet Research Agency":                  "Internet Research Agency",
    "Synthetic media saturation":                "Synthetic media",
    "Active Measures doctrine":                  "Active measures",
    "Von Neumann combat probe":                  "Von Neumann probe",
    "Autonomous weapons accord":                 None,
    "Convention on Self-Replicating Systems":    None,
    "DART Spacecraft":                           "Double Asteroid Redirection Test",
    "NEO Surveyor":                              "NEO Surveyor",
    "UN Office for Outer Space Affairs":         "United Nations Office for Outer Space Affairs",
    "Solar System Defense Grid":                 None,
    "Casaba-Howitzer":                           "Casaba-Howitzer",
    "Project Longshot":                          "Project Longshot",
    "Interstellar deterrence":                   None,
    "Positron annihilation device":              "Positron annihilation",
    "Antiproton arsenal":                        "Antiproton",
    "Air Force Research Laboratory":             "Air Force Research Laboratory",

    # ─── Far Future 2500-2700 fill (mostly speculative) ───
    "Penrose process":                           "Penrose process",
    "Hawking-radiation harvester":               "Hawking radiation",
    "Kerr power plant":                          "Kerr metric",
    "Black-hole bomb":                           "Black hole bomb",
    "Neutrino relay station":                    "Neutrino communication",
    "Long-baseline laser link":                  "Free-space optical communication",
    "Galactic Asynchronous Protocol":            None,
    "Sagittarius A* relay hub":                  "Sagittarius A*",
    "Slow-trade contract":                       None,
    "Light-lag arbitrage":                       None,
    "Interstellar Mercantile Consortium":        None,
    "Sub-light freighter":                       None,
    "Galactic Mind substrate":                   None,
    "Inter-instance value reconciliation":       None,
    "Pan-Galactic Coordination Treaty":          None,
    "Designer atomic nucleus":                   "Synthetic element",
    "Nuclear-isomer battery":                    "Nuclear isomer",
    "Femto-fabricator":                          "Femtotechnology",
    "Casimir-cavity generator":                  "Casimir effect",
    "Zero-point energy cell":                    "Zero-point energy",
    "Dynamical Casimir emitter":                 "Dynamical Casimir effect",
    "Strange-matter ingot":                      "Strange matter",
    "Color-flavor-locked phase":                 "Color–flavor locking",
    "Quark-matter hull":                         "Quark star",
    "Negative-energy field":                     "Negative energy",
    "Cosmological-constant modulator":           "Cosmological constant",
    "Alcubierre precursor coil":                 "Alcubierre drive",
}


def check_wikipedia(title):
    """Return True if a Wikipedia article exists at that exact title."""
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(title.replace(" ", "_"))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            j = json.loads(r.read().decode("utf-8"))
            return j.get("type") not in ("disambiguation",) and "extract" in j
    except urllib.error.HTTPError as e:
        return False
    except Exception:
        return False


def main():
    src = UNLOCKS.read_text()
    # Verify each "Article Title" override actually exists; downgrade to wiki:false if not.
    print("Verifying Wikipedia targets for redirects…")
    verified = {}
    for unlock_name, target in OVERRIDES.items():
        if target is None:
            verified[unlock_name] = None
            continue
        ok = check_wikipedia(target)
        verified[unlock_name] = target if ok else None
        print(f"  [{'ok ' if ok else 'NO '}] {unlock_name:50} -> {target}")
        time.sleep(0.3)

    # Now rewrite unlocks.js: for any unlock entry whose name is in OVERRIDES,
    # add wiki: false or wiki: "Article Title" before the closing brace.
    edits = 0
    for name, target in verified.items():
        # Existing line pattern: { type: "...", name: "...", name_zh: "..." },
        # We append wiki info before the closing brace.
        # Escape regex-meaningful chars in the name for the source match.
        esc = re.escape(name)
        # JavaScript stringifies special chars (e.g. - is normal, but * needs escape)
        # The line in the file uses double-quoted JSON-ish. Use a tolerant pattern.
        pat = re.compile(
            r'(\{\s*type:\s*"[^"]+"\s*,\s*name:\s*"' + esc + r'"\s*,\s*name_zh:\s*"[^"]+"\s*)\}',
            re.S,
        )
        if target is None:
            replacement = r'\1, wiki: false }'
        else:
            replacement = r'\1, wiki: ' + json.dumps(target, ensure_ascii=False) + r' }'
        new_src, n = pat.subn(replacement, src)
        if n > 0:
            src = new_src
            edits += n
            print(f"  patched {n}× {name}")
    UNLOCKS.write_text(src)
    print(f"\nunlocks.js: {edits} edits applied")


if __name__ == "__main__":
    main()
