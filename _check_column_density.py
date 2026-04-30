#!/usr/bin/env python3
"""Mirror the layout logic in app.js (including compact + sparse-merge pass).
Reports per-era column counts and any column with > MAX_PER_COLUMN nodes."""

import re
from collections import defaultdict
from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")
MAX_PER_COLUMN = 12
SPARSE_THRESHOLD = 2

ERA_MIN_LEVELS = {
    "bronze": 8, "classical": 9, "medieval": 4, "renaissance": 4,
    "enlightenment": 5, "industrial": 5, "modern": 3, "atomic": 5, "information": 5,
    "future": 13, "far-future": 8,
}


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
        techs.append({"id": m.group(1), "era": m.group(2), "year": m.group(3), "prereqs": pids,
                      "landmark": False})
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


def compact_era(in_era_level, era_techs, N):
    """Mirror app.js compaction: drop empty cols + merge sparse cols.
    Returns (new_n_cols, updated_in_era_level_dict)."""
    if not era_techs:
        return 1, in_era_level
    root = list(range(N))
    count = [0] * N
    for t in era_techs:
        count[in_era_level[t["id"]]] += 1

    def active_roots():
        return [i for i in range(N) if root[i] == i and count[i] > 0]

    def merge_into(target, source):
        for i in range(N):
            if root[i] == source: root[i] = target
        count[target] += count[source]
        count[source] = 0

    def has_landmark(r):
        return any(t.get("landmark") and root[in_era_level[t["id"]]] == r for t in era_techs)

    progress = True
    while progress:
        progress = False
        groups = active_roots()
        if len(groups) <= 1: break
        for gi, r in enumerate(groups):
            if count[r] > SPARSE_THRESHOLD: continue
            if has_landmark(r): continue
            left = groups[gi-1] if gi > 0 else None
            right = groups[gi+1] if gi < len(groups)-1 else None
            l_ok = left is not None and count[left] + count[r] <= MAX_PER_COLUMN
            r_ok = right is not None and count[right] + count[r] <= MAX_PER_COLUMN
            target = None
            if l_ok and r_ok: target = left if count[left] <= count[right] else right
            elif l_ok: target = left
            elif r_ok: target = right
            if target is not None:
                merge_into(target, r)
                progress = True
                break

    final_groups = active_roots()
    idx_map = {g: i for i, g in enumerate(final_groups)}
    for t in era_techs:
        in_era_level[t["id"]] = idx_map[root[in_era_level[t["id"]]]]
    return len(final_groups), in_era_level


def main():
    techs, eras = parse_techs()
    topo = topo_levels(techs)
    by_era = defaultdict(list)
    for t in techs:
        by_era[t["era"]].append(t)

    # era_levels = max topo + 1, but bounded below by ERA_MIN_LEVELS
    era_levels = {}
    for t in techs:
        era_levels[t["era"]] = max(era_levels.get(t["era"], 0), topo[t["id"]])
    for e in eras:
        era_levels[e] = max(era_levels.get(e, 0), 1)
    for eid, n in ERA_MIN_LEVELS.items():
        era_levels[eid] = max(era_levels.get(eid, 0), n)

    # Year range per era
    y_min, y_max = {}, {}
    for t in techs:
        y = parse_year(t["year"])
        if y is None: continue
        y_min[t["era"]] = min(y_min.get(t["era"], float("inf")), y)
        y_max[t["era"]] = max(y_max.get(t["era"], float("-inf")), y)

    in_era_level = {}
    for t in techs:
        N = era_levels[t["era"]] + 1
        y = parse_year(t["year"])
        ymin = y_min.get(t["era"]); ymax = y_max.get(t["era"])
        if y is None or ymin is None or ymax is None or ymax == ymin or N <= 1:
            in_era_level[t["id"]] = 0
        else:
            frac = (y - ymin) / (ymax - ymin)
            in_era_level[t["id"]] = max(0, min(N - 1, round(frac * (N - 1))))

    # Compact each era
    print(f"Pre-compaction column counts per era:")
    for e in eras:
        print(f"  {e:14}: {era_levels[e]+1}")

    print(f"\nPost-compaction column counts (drop empty + merge sparse ≤ {SPARSE_THRESHOLD}):")
    new_levels = {}
    for e in eras:
        n_cols, in_era_level = compact_era(in_era_level, by_era[e], era_levels[e] + 1)
        new_levels[e] = n_cols - 1
        print(f"  {e:14}: {n_cols}")

    # Final bucket density
    buckets = defaultdict(list)
    for t in techs:
        buckets[(t["era"], in_era_level[t["id"]])].append(t)

    print(f"\nColumns with > {MAX_PER_COLUMN} nodes:")
    overfilled = [(e, s, len(g)) for (e, s), g in buckets.items() if len(g) > MAX_PER_COLUMN]
    if not overfilled:
        print("  (none — all columns within limit)")
    else:
        for e, s, c in overfilled:
            print(f"  {e} col {s}: {c}")

    print(f"\nColumns with ≤ {SPARSE_THRESHOLD} nodes (sparse, would normally be merged):")
    sparse = [(e, s, len(g)) for (e, s), g in buckets.items() if len(g) <= SPARSE_THRESHOLD]
    if not sparse:
        print("  (none)")
    else:
        for e, s, c in sparse:
            print(f"  {e} col {s}: {c}")


if __name__ == "__main__":
    main()
