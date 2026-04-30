#!/usr/bin/env python3
"""Add one intermediate / nearer prereq to each tech that currently has all
its prereqs ≥2 eras back. This compresses long-span single-edge connections
into denser stepping-stone chains, without adding new tech nodes."""

import re
from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")

# tech-id -> additional prereq id to inject. Each fix uses an existing tech
# in the era right before (or equal to) the target tech, semantically related.
ADDITIONS = {
    # Mesolithic / Neolithic
    "semi-sedentism":          "trade-networks",       # +1 era (upper-paleo → mesolithic)
    "megaliths":               "village",              # same era (neolithic)

    # Bronze
    "composite-bow":           "bronze-metallurgy",    # same era

    # Classical / Medieval / Renaissance
    "vernacular-literature":   "printing-press",       # same era
    "spinning-jenny":          "factory-system",       # same era
    "canal-system":            "factory-system",       # same era
    "steam-pump":              "coke-iron",            # same era
    "separation-of-powers":    "nation-state",         # same era

    # Industrial / Modern (atomic targets)
    "synthetic-fertilizer":    "electrification",      # +1 era → industrial
    # Modern era
    "womens-suffrage":         "labor-union",          # +1 era → industrial
    # Atomic era
    "decolonization":          "russian-revolution",   # +1 era → modern
    "united-nations":          "federal-reserve",      # +1 era → modern
    "abstract-expressionism":  "bauhaus",              # +1 era → modern
    "credit-card":             "federal-reserve",      # +1 era → modern
    "digital-computer":        "cryptanalysis-bombe",  # +1 era → modern
    "vaccines-modern":         "antibiotics",          # +1 era → modern
    "suburban-tract-housing":  "radio-broadcasting",   # +1 era → modern

    # Information era
    "neoliberalism":           "arpanet-internet",     # same era
    "wind-turbine":            "solar-photovoltaic",   # same era (parallel renewable)
    "closed-loop-life-support":"green-revolution",     # +1 era → atomic

    # Future / Far Future
    "dark-sector-physics":     "standard-model",       # +1 era → information
    "nanotechnology":          "metamaterials",        # +1 era → future

    # Second pass — additional fixes
    "food-preservation":       "hafting",              # +1 era → middle-paleo
    "dna-structure":           "quantum-mechanics",    # +1 era → modern
    "neuroscience":            "quantum-mechanics",    # +1 era → modern
    "welfare-state":           "russian-revolution",   # +1 era → modern
    "quantum-gravity":         "dark-sector-physics",  # +1 era → future

    # Final pass — last 2 fixable
    "highway-system":          "tank",                 # +1 era → modern (Eisenhower's autobahn)
    "glass-lens":              "paper-making",         # +1 era → classical (reading culture)
}


def main():
    src = DATA.read_text()
    by_id_pat = re.compile(
        r'(\{\s*id:\s*"([^"]+)"\s*,[^{}]*?prereqs:\s*\[)([^\]]*)\]', re.S)

    modified = 0
    for m in by_id_pat.finditer(src):
        tid = m.group(2)
        if tid not in ADDITIONS:
            continue
        new_prereq = ADDITIONS[tid]
        old_list = m.group(3).strip()
        # Skip if already present (idempotent)
        if f'"{new_prereq}"' in old_list:
            continue
        # Append new prereq to the existing list
        if old_list and not old_list.endswith(","):
            new_list = f'{old_list}, "{new_prereq}"'
        else:
            new_list = f'{old_list}"{new_prereq}"'
        old_full = m.group(1) + m.group(3) + "]"
        new_full = m.group(1) + new_list + "]"
        src = src.replace(old_full, new_full, 1)
        modified += 1

    DATA.write_text(src)
    print(f"Patched {modified} techs with intermediate prereqs.")


if __name__ == "__main__":
    main()
