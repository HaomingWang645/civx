#!/usr/bin/env python3
"""Find techs where ALL prerequisites are at least 2 eras earlier than the
tech itself — meaning every connecting edge to this tech jumps over at least
one whole era.

Excludes techs with zero prereqs (vacuous true)."""

import re
from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")


def parse_techs():
    src = DATA.read_text()
    pat = re.compile(
        r'\{\s*id:\s*"([^"]+)"\s*,\s*name:\s*"([^"]*)"\s*,'
        r'\s*era:\s*"([^"]+)"\s*,\s*category:\s*"[^"]+"\s*,'
        r'\s*year:\s*"[^"]+"\s*,'
        r'\s*prereqs:\s*\[([^\]]*)\]', re.S)
    techs = []
    for m in pat.finditer(src):
        prereqs = re.findall(r'"([^"]+)"', m.group(4))
        techs.append({"id": m.group(1), "name": m.group(2), "era": m.group(3), "prereqs": prereqs})
    eras_pat = re.compile(r'const\s+ERAS\s*=\s*\[(.*?)\];', re.S)
    em = eras_pat.search(src)
    eras = re.findall(r'id:\s*"([^"]+)"', em.group(1)) if em else []
    return techs, eras


def main():
    techs, eras = parse_techs()
    era_idx = {e: i for i, e in enumerate(eras)}
    by_id = {t["id"]: t for t in techs}

    matches = []
    for t in techs:
        if not t["prereqs"]:
            continue
        gaps = []
        ok = True
        for p in t["prereqs"]:
            if p not in by_id:
                ok = False; break
            g = era_idx[t["era"]] - era_idx[by_id[p]["era"]]
            if g < 2:
                ok = False; break
            gaps.append((p, g))
        if ok:
            min_gap = min(g for _, g in gaps)
            matches.append((min_gap, len(gaps), t, gaps))

    # Sort: largest min-gap first, then most prereqs, then era, then name
    matches.sort(key=lambda x: (-x[0], -x[1], era_idx.get(x[2]["era"], 99), x[2]["name"]))

    print(f"Total techs: {len(techs)}")
    print(f"Techs whose every prereq is ≥2 eras back: {len(matches)}\n")
    print(f"{'min':>3} {'#pq':>4}  {'tech (era)':45}  prereqs (era, gap)")
    print("-" * 120)
    for min_gap, _n, t, gaps in matches:
        prereq_strs = []
        for p, g in gaps:
            prereq_strs.append(f"{by_id[p]['name']} [{by_id[p]['era']}, +{g}]")
        print(f"{min_gap:>3} {len(gaps):>4}  {t['name']+' ('+t['era']+')':45}  {' | '.join(prereq_strs)}")


if __name__ == "__main__":
    main()
