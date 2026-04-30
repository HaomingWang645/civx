#!/usr/bin/env python3
"""Generate techs.html from data.js — a crawler-friendly static index of every
tech, used so search engines can read all 346 entries without running JavaScript.
Re-runnable; safe to run after every data.js edit."""
import json, re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data.js"
TRANS = ROOT / "translations.js"
OUT = ROOT / "techs.html"
SITE = "https://haomingwang645.github.io/civx/"

src = DATA.read_text()

def grab_block(name):
    m = re.search(rf"const {name} = (\[[\s\S]*?\n\]);", src)
    if not m:
        raise SystemExit(f"could not find {name} in data.js")
    return m.group(1)

# data.js is JS, not JSON: keys are unquoted, strings use double quotes, trailing
# commas are allowed. Normalize to JSON.
def js_to_json(s):
    # strip line comments
    s = re.sub(r"//[^\n]*", "", s)
    # quote keys: { id: "..." } -> { "id": "..." }
    s = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', s)
    # remove trailing commas before } or ]
    s = re.sub(r",(\s*[}\]])", r"\1", s)
    return s

eras = json.loads(js_to_json(grab_block("ERAS")))
techs = json.loads(js_to_json(grab_block("TECHS")))

# Categories block uses `{ name: ..., color: ... }` values — easier to parse manually.
cats = {}
for m in re.finditer(r'(\w+):\s*\{\s*name:\s*"([^"]+)"', src):
    cats[m.group(1)] = m.group(2)

# Chinese names
zh_src = TRANS.read_text() if TRANS.exists() else ""
zh = {}
for m in re.finditer(r'"([\w\-]+)":\s*"([^"]+)"', zh_src):
    zh[m.group(1)] = m.group(2)

era_order = {e["id"]: i for i, e in enumerate(eras)}
era_name = {e["id"]: e["name"] for e in eras}
era_range = {e["id"]: e["range"] for e in eras}
tech_by_id = {t["id"]: t for t in techs}

techs_sorted = sorted(techs, key=lambda t: (era_order.get(t["era"], 99), t["name"].lower()))

def esc(s): return html.escape(s or "", quote=True)

out = []
out.append("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>All Technologies — Human History Tech Tree</title>
<meta name="description" content="Plain-text index of every technology in the Human History Tech Tree, from the Paleolithic to the Information Age, with era, year, prerequisites, and historical description." />
<link rel="canonical" href="%stechs.html" />
<link rel="stylesheet" href="styles.css" />
<style>
  body { max-width: 880px; margin: 0 auto; padding: 32px 20px 80px; font-family: 'EB Garamond', Georgia, serif; line-height: 1.55; color: #1a1a1a; background: #fbfaf6; }
  h1 { font-family: 'Cinzel', serif; font-size: 32px; margin: 0 0 4px; }
  h2 { font-family: 'Cinzel', serif; font-size: 22px; margin: 36px 0 6px; padding-top: 12px; border-top: 1px solid #d8d2bf; }
  h2 small { font-weight: normal; font-size: 14px; color: #6a6452; }
  article { margin: 18px 0; padding-left: 14px; border-left: 2px solid #e3dcc4; }
  article h3 { font-size: 18px; margin: 0 0 4px; }
  article h3 .zh { font-weight: normal; font-size: 15px; color: #4a4a4a; margin-left: 6px; }
  .meta { font-size: 13px; color: #6a6452; margin: 0 0 6px; }
  .prereqs { font-size: 13px; color: #6a6452; margin: 4px 0 0; }
  .prereqs a { color: #5a4a1a; }
  .home { display: inline-block; margin-bottom: 16px; }
</style>
</head>
<body>
<a class="home" href="./">&larr; Interactive tech tree</a>
<h1>All Technologies</h1>
<p>A flat, searchable index of every technology in the <a href="./">Human History Tech Tree</a> &mdash; %d entries across %d eras, from the Lower Paleolithic to the Information Age.</p>
""" % (SITE, len(techs), len(eras)))

current_era = None
for t in techs_sorted:
    if t["era"] != current_era:
        current_era = t["era"]
        out.append(f'<h2 id="era-{esc(current_era)}">{esc(era_name.get(current_era, current_era))} <small>{esc(era_range.get(current_era, ""))}</small></h2>')
    zh_name = zh.get(t["id"])
    zh_html = f'<span class="zh">({esc(zh_name)})</span>' if zh_name else ""
    cat = cats.get(t["category"], t["category"])
    prereqs = t.get("prereqs") or []
    prereq_html = ""
    if prereqs:
        links = []
        for p in prereqs:
            pname = tech_by_id.get(p, {}).get("name", p)
            links.append(f'<a href="#tech-{esc(p)}">{esc(pname)}</a>')
        prereq_html = f'<p class="prereqs"><strong>Builds on:</strong> {", ".join(links)}</p>'
    out.append(f"""<article id="tech-{esc(t['id'])}">
<h3>{esc(t['name'])} {zh_html}</h3>
<p class="meta">{esc(cat)} &middot; {esc(t.get('year',''))} &middot; {esc(era_name.get(t['era'], t['era']))}</p>
<p>{esc(t.get('desc',''))}</p>
{prereq_html}
</article>""")

out.append("</body></html>")
OUT.write_text("\n".join(out))
print(f"wrote {OUT} — {len(techs)} techs, {len(eras)} eras")
