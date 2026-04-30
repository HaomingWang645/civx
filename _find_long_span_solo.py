#!/usr/bin/env python3
"""Find techs that:
  (1) have exactly ONE prerequisite, AND
  (2) the prerequisite's era is at least 2 eras earlier than the tech's era
      (so the connecting edge spans 3 or more consecutive eras inclusive,
       with at least one era completely skipped in between).

Example: tech in 'classical' with sole prereq in 'neolithic' qualifies
(skips 'bronze')."""

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
        if len(t["prereqs"]) != 1:
            continue
        p = t["prereqs"][0]
        if p not in by_id:
            continue
        gap = era_idx[t["era"]] - era_idx[by_id[p]["era"]]
        if gap >= 2:
            matches.append((gap, t, by_id[p]))

    matches.sort(key=lambda x: (-x[0], x[1]["era"], x[1]["name"]))

    print(f"Total techs: {len(techs)}")
    print(f"Techs satisfying the criterion: {len(matches)}\n")
    print(f"{'gap':>4}  {'tech (era)':40}  ←  {'prereq (era)'}")
    print("-" * 100)
    for gap, t, p in matches:
        print(f"{gap:>4}  {t['name']+' ('+t['era']+')':40}  ←  {p['name']+' ('+p['era']+')'}")


if __name__ == "__main__":
    main()
