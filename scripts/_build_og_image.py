#!/usr/bin/env python3
"""Generate images/og.png — the 1200x630 social-share card.
Renaissance parchment palette matched to styles.css. Re-runnable."""
import math, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images" / "og.png"

W, H = 1200, 630

# Palette pulled from body.theme-renaissance in styles.css.
BG       = (239, 226, 188)   # #efe2bc
BG_WARM  = (231, 214, 164)   # gold-leaning highlight
TEXT_0   = (59, 38, 20)      # #3b2614
TEXT_1   = (107, 74, 38)     # #6b4a26
TEXT_2   = (138, 106, 62)    # #8a6a3e
ACCENT   = (140, 26, 26)     # Florentine red
GOLD     = (184, 134, 43)

# Build base parchment with two soft illumination spots and faint horizontal lines.
img = Image.new("RGB", (W, H), BG)

# illumination top-left (gold) and bottom-right (red)
glow_tl = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(glow_tl)
for r in range(900, 0, -30):
    a = int(40 * (r / 900))
    d.ellipse([150 - r, 20 - r, 150 + r, 20 + r], fill=(BG[0] + a // 3, BG[1] + a // 4, BG[2] + a // 6))
glow_tl = glow_tl.filter(ImageFilter.GaussianBlur(80))

glow_br = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(glow_br)
for r in range(800, 0, -30):
    a = int(28 * (r / 800))
    d.ellipse([1050 - r, 600 - r, 1050 + r, 600 + r], fill=(BG[0] + a // 4, BG[1], BG[2] - a // 8 if BG[2] - a // 8 > 0 else 0))
glow_br = glow_br.filter(ImageFilter.GaussianBlur(80))

img = Image.blend(img, glow_tl, 0.55)
img = Image.blend(img, glow_br, 0.35)

draw = ImageDraw.Draw(img, "RGBA")

# faint horizontal scribe lines for paper feel
for y in range(0, H, 3):
    draw.line([(0, y), (W, y)], fill=(80, 50, 20, 8))

# double-line gold border
for off, w in [(28, 2), (38, 1)]:
    draw.rectangle([off, off, W - off, H - off], outline=GOLD, width=w)

# Font picker: prefer Georgia (serif, ships with macOS), fall back to default.
def load_font(candidates, size):
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

GEORGIA_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
GEORGIA      = "/System/Library/Fonts/Supplemental/Georgia.ttf"
GEORGIA_IT   = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"

f_title = load_font([GEORGIA_BOLD], 62)
f_sub   = load_font([GEORGIA_IT], 30)
f_stat  = load_font([GEORGIA_BOLD], 26)
f_url   = load_font([GEORGIA], 22)
f_era   = load_font([GEORGIA, GEORGIA_IT], 15)

# centered helpers
def text_w(s, f):
    return draw.textlength(s, font=f)

# Title — uppercase letterspaced, like Cinzel.
TITLE = "HUMAN HISTORY TECH TREE"
# Pillow doesn't do letter-spacing; emulate by drawing chars individually.
def draw_spaced(text, x, y, font, color, spacing=6):
    cur = x
    for ch in text:
        draw.text((cur, y), ch, font=font, fill=color)
        cur += text_w(ch, font) + spacing
    return cur - x

def spaced_w(text, font, spacing=6):
    return sum(text_w(c, font) for c in text) + spacing * (len(text) - 1)

tw = spaced_w(TITLE, f_title, spacing=4)
draw_spaced(TITLE, (W - tw) // 2, 130, f_title, TEXT_0, spacing=4)

# Decorative rule under title
cy = 230
draw.line([(W // 2 - 220, cy), (W // 2 - 30, cy)], fill=GOLD, width=2)
draw.line([(W // 2 + 30, cy), (W // 2 + 220, cy)], fill=GOLD, width=2)
# diamond ornament in the middle
ox, oy = W // 2, cy
draw.polygon([(ox, oy - 6), (ox + 8, oy), (ox, oy + 6), (ox - 8, oy)], fill=ACCENT)

# Subtitle (italic)
SUB = "Pleistocene  to  Information Age"
sw = text_w(SUB, f_sub)
draw.text(((W - sw) // 2, 250), SUB, font=f_sub, fill=TEXT_1)

# Stats line
STAT = "393 TECHNOLOGIES  ·  15 ERAS  ·  3.3 MILLION YEARS"
sw = spaced_w(STAT, f_stat, spacing=3)
draw_spaced(STAT, (W - sw) // 2, 320, f_stat, TEXT_0, spacing=3)

# Era timeline — 15 dots, major eras labeled (alternating above/below to avoid collision).
ERAS = [
    ("Paleolithic",   True,  "below"),
    ("",              False, None),
    ("",              False, None),
    ("",              False, None),
    ("Neolithic",     True,  "below"),
    ("Bronze",        True,  "above"),
    ("Classical",     True,  "below"),
    ("Medieval",      True,  "above"),
    ("Renaissance",   True,  "below"),
    ("",              False, None),
    ("Industrial",    True,  "above"),
    ("",              False, None),
    ("",              False, None),
    ("Information",   True,  "below"),
    ("Future",        False, None),
]
n = len(ERAS)
left, right = 140, W - 140
ty = 460
draw.line([(left, ty), (right, ty)], fill=TEXT_2, width=1)
for i, (label, major, side) in enumerate(ERAS):
    x = left + (right - left) * i / (n - 1)
    r = 8 if major else 4
    color = ACCENT if major else GOLD
    draw.ellipse([x - r, ty - r, x + r, ty + r], fill=color, outline=TEXT_0, width=1)
    if label:
        lw = text_w(label, f_era)
        ly = ty + 14 if side == "below" else ty - 14 - 16
        draw.text((x - lw / 2, ly), label, font=f_era, fill=TEXT_1)

# URL footer
URL = "haomingwang645.github.io/civx"
uw = text_w(URL, f_url)
draw.text(((W - uw) // 2, H - 70), URL, font=f_url, fill=TEXT_2)

# Vignette: darken corners gently
vignette = Image.new("L", (W, H), 0)
vd = ImageDraw.Draw(vignette)
vd.rectangle([0, 0, W, H], fill=255)
vd.ellipse([-200, -200, W + 200, H + 200], fill=255)
vignette = vignette.filter(ImageFilter.GaussianBlur(60))
dark = Image.new("RGB", (W, H), (90, 60, 30))
img = Image.composite(img, dark, vignette)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
