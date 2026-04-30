#!/usr/bin/env python3
"""Apply realism fixes:
  (1) Add 3 missing prereq connections.
  (2) Address timing issues:
      - senolytic 2040 → 2045 (after anti-aging) + add anti-aging prereq
      - layered-air-missile-defense 2038 → 2040 (natural year)
      - stellar-engineering 2500 → 2480 (earlier than galactic-civilization)
"""

import re
from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")

# Tuples: (target-tech-id, prereq-to-add)
PREREQ_ADDS = [
    ("mind-linked-collective-art", "brain-brain-communication"),
    ("whole-brain-emulation",       "theory-of-consciousness"),
    ("memory-editing",              "theory-of-consciousness"),
    ("senolytic-longevity-therapy", "anti-aging"),
]

# Tuples: (tech-id, old-year, new-year)
YEAR_SHIFTS = [
    ("senolytic-longevity-therapy",  "2040", "2045"),
    ("layered-air-missile-defense",  "2038", "2040"),
    ("stellar-engineering",          "2500", "2480"),
]


def main():
    src = DATA.read_text()

    # 1. Add prereqs
    for tid, new in PREREQ_ADDS:
        pat = re.compile(r'(\{\s*id:\s*"' + re.escape(tid) + r'"\s*,[^{}]*?prereqs:\s*\[)(?P<plist>[^\]]*)\]', re.S)
        m = pat.search(src)
        if not m:
            print(f"  WARN: {tid} not found"); continue
        plist = m.group("plist")
        if f'"{new}"' in plist:
            print(f"  {tid}: already has {new}"); continue
        new_plist = plist.rstrip().rstrip(",")
        new_plist = (new_plist + f', "{new}"') if new_plist else f'"{new}"'
        src = src[:m.start()] + m.group(1) + new_plist + "]" + src[m.end():]
        print(f"  + {tid}: +{new}")

    # 2. Year shifts (only the year field of the targeted tech)
    for tid, old_year, new_year in YEAR_SHIFTS:
        pat = re.compile(r'(\{\s*id:\s*"' + re.escape(tid) + r'"\s*,[^{}]*?year:\s*")' + re.escape(old_year) + r'(")', re.S)
        new_src, n = pat.subn(r'\g<1>' + new_year + r'\2', src)
        if n == 0:
            print(f"  WARN: {tid}: year {old_year} not found")
        else:
            src = new_src
            print(f"  shift {tid}: {old_year} → {new_year}")

    DATA.write_text(src)


if __name__ == "__main__":
    main()
