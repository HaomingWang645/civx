#!/usr/bin/env python3
"""Fix the 5 year-inversions introduced by my prereq additions:
  - Replace village → semi-sedentism in megaliths
  - Replace printing-press → paper-mill in vernacular-literature
  - Replace factory-system → coke-iron in 3 enlightenment-era techs
"""

import re
from pathlib import Path

DATA = Path("/Users/haomingwang/Desktop/Python/tech-tree/data.js")

# (tech-id, old-prereq-id-to-replace, new-prereq-id)
REPLACEMENTS = [
    ("megaliths",                   "village",          "semi-sedentism"),
    ("vernacular-literature",       "printing-press",   "paper-mill"),
    ("canal-system",                "factory-system",   "coke-iron"),
    ("spinning-jenny",              "factory-system",   "coke-iron"),
    ("standardized-field-artillery","factory-system",   "coke-iron"),
]


def main():
    src = DATA.read_text()
    pat = re.compile(
        r'(\{\s*id:\s*"(?P<tid>[^"]+)"\s*,[^{}]*?prereqs:\s*\[)(?P<plist>[^\]]*)\]', re.S)

    by_tech = {tid: (old, new) for tid, old, new in REPLACEMENTS}
    fixed = 0

    def replace_in(m):
        nonlocal fixed
        tid = m.group("tid")
        if tid not in by_tech:
            return m.group(0)
        old, new = by_tech[tid]
        plist = m.group("plist")
        if f'"{new}"' in plist:
            # Already replaced — drop the old one
            new_plist = re.sub(r',?\s*"' + re.escape(old) + r'"', '', plist).strip().lstrip(",").strip()
        else:
            new_plist = plist.replace(f'"{old}"', f'"{new}"')
        if new_plist != plist:
            fixed += 1
        return m.group(1) + new_plist + "]"

    new_src = pat.sub(replace_in, src)
    DATA.write_text(new_src)
    print(f"Fixed {fixed} prereq replacements.")


if __name__ == "__main__":
    main()
