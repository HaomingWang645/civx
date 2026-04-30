#!/usr/bin/env python3
"""One-shot reorganization: move all _*.py and helper _*.html into scripts/.
Patch scripts that use Path(__file__).resolve().parent so they still resolve
to project root after the move."""

import re, shutil
from pathlib import Path

ROOT = Path("/Users/haomingwang/Desktop/Python/tech-tree")
SCRIPTS = ROOT / "scripts"


def main():
    SCRIPTS.mkdir(exist_ok=True)
    moved = []
    for p in sorted(ROOT.iterdir()):
        if not p.is_file(): continue
        # Move all _*.py, plus the diagnostic/demo HTMLs.
        if (p.name.startswith("_") and p.suffix == ".py") or p.name in ("_diag.html", "_image_demo.html"):
            # Don't move this reorganizer itself.
            if p.name == "_reorganize.py": continue
            target = SCRIPTS / p.name
            shutil.move(str(p), str(target))
            moved.append(p.name)
    print(f"Moved {len(moved)} files into scripts/")

    # Now patch any script that uses Path(__file__).resolve().parent — that
    # used to resolve to project root (because scripts lived in root); after
    # the move it would resolve to scripts/. We replace with .parent.parent
    # so it again points to the project root.
    pat = re.compile(r'Path\(__file__\)\.resolve\(\)\.parent(?!\.parent)')
    patched = 0
    for p in SCRIPTS.glob("*.py"):
        src = p.read_text()
        new = pat.sub('Path(__file__).resolve().parent.parent', src)
        if new != src:
            p.write_text(new)
            patched += 1
    print(f"Patched {patched} scripts to use parent.parent")


if __name__ == "__main__":
    main()
