#!/usr/bin/env python3
"""For each era, find the minimum sub-column count such that no single
year-bucket exceeds 12 techs. Output new ERA_MIN_LEVELS suitable for
pasting into app.js."""

import re
from collections import defaultdict
from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")

MAX_PER_COLUMN = 12


def parse_year(s):
    if not s: return None
    s = s.strip().lstrip("~")
    s = re.sub(r"\s*\(.*?\)\s*", "", s).strip()
    m = re.match(r"^([\-\d.]+)\s*[–\-]\s*([\-\d.]+)\s*([A-Za-z]*)$", s)
    if m: s = m.group(1) + " " + (m.group(3) or "")
    m = re.match(r"^(-?[\d.]+)\s*([A-Za-z]*)", s)
    if not m: return None
    n = float(m.group(1))
    u = (m.group(2) or "").upper()
    if u == "MYA": return -n * 1e6
    if u == "KYA": return -n * 1e3
    if u in ("BCE", "BC"): return -n
    return n


def parse_techs():
    src = DATA.read_text()
    pat = re.compile(
        r'\{\s*id:\s*"([^"]+)"\s*,'
        r'\s*name:\s*"[^"]*"\s*,'
        r'\s*era:\s*"([^"]+)"\s*,'
        r'\s*category:\s*"[^"]+"\s*,'
        r'\s*year:\s*"([^"]+)"\s*,'
        r'\s*prereqs:\s*\[([^\]]*)\]', re.S)
    techs = []
    for m in pat.finditer(src):
        pids = re.findall(r'"([^"]+)"', m.group(4))
        techs.append({"id": m.group(1), "era": m.group(2), "year": m.group(3), "prereqs": pids})
    eras_pat = re.compile(r'const\s+ERAS\s*=\s*\[(.*?)\];', re.S)
    em = eras_pat.search(src)
    eras = re.findall(r'id:\s*"([^"]+)"', em.group(1)) if em else []
    return techs, eras


def topo_levels(techs):
    by_id = {t["id"]: t for t in techs}
    topo = {t["id"]: -1 for t in techs}
    for _ in range(50):
        changed = False
        for t in techs:
            if topo[t["id"]] >= 0: continue
            in_era = [p for p in t["prereqs"] if p in by_id and by_id[p]["era"] == t["era"]]
            if not in_era:
                topo[t["id"]] = 0; changed = True
            elif all(topo[p] >= 0 for p in in_era):
                topo[t["id"]] = max(topo[p] for p in in_era) + 1; changed = True
        if not changed: break
    for t in techs:
        if topo[t["id"]] < 0: topo[t["id"]] = 0
    return topo


def max_bucket_for(era_techs, num_cols):
    """Given a list of techs from one era, return the max bucket size with
    `num_cols` sub-columns."""
    y_min = float("inf"); y_max = float("-inf")
    parsed = []
    for t in era_techs:
        y = parse_year(t["year"])
        parsed.append((t, y))
        if y is None: continue
        y_min = min(y_min, y); y_max = max(y_max, y)
    if y_min == y_max or y_min == float("inf"): return len(era_techs)
    counts = defaultdict(int)
    N = num_cols
    for t, y in parsed:
        if y is None:
            sub = 0
        else:
            frac = (y - y_min) / (y_max - y_min)
            sub = max(0, min(N - 1, round(frac * (N - 1))))
        counts[sub] += 1
    return max(counts.values()) if counts else 0


def main():
    techs, eras = parse_techs()
    topo = topo_levels(techs)
    by_era = defaultdict(list)
    for t in techs:
        by_era[t["era"]].append(t)

    # natural per-era max from topology
    natural_levels = {}
    for e, group in by_era.items():
        natural_levels[e] = max([topo[t["id"]] for t in group] + [1])  # +1 col baseline

    print(f"Tuning ERA_MIN_LEVELS so no column has > {MAX_PER_COLUMN} techs")
    print(f"{'era':14}  {'natural':>7}  {'tuned':>5}  {'max-bucket':>10}")

    new_overrides = {}
    for e in eras:
        group = by_era.get(e, [])
        if not group: continue
        natural = natural_levels[e]
        # Find min N (≥ natural+1) where max bucket ≤ MAX_PER_COLUMN.
        N = max(2, natural + 1)
        while max_bucket_for(group, N) > MAX_PER_COLUMN:
            N += 1
            if N > 50: break  # safety
        max_bucket = max_bucket_for(group, N)
        levels = N - 1
        # Only record override if levels exceeds natural depth
        if levels > natural:
            new_overrides[e] = levels
        print(f"  {e:14}  {natural:>7}  {levels:>5}  {max_bucket:>10}")

    print(f"\nProposed ERA_MIN_LEVELS:")
    parts = []
    for e in eras:
        if e in new_overrides:
            key = f'"{e}"' if "-" in e else e
            parts.append(f"{key}: {new_overrides[e]}")
    print("  const ERA_MIN_LEVELS = { " + ", ".join(parts) + " };")


if __name__ == "__main__":
    main()
