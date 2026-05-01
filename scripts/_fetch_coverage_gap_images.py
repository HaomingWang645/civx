#!/usr/bin/env python3
"""Fetch Wikipedia thumbnails for the 5 coverage-gap-fill techs added May 2026.

Target cells: mesolithic×weapons, neolithic×weapons, neolithic×economy,
enlightenment×communication, modern×shelter. Same fallback-chain logic as
_fetch_future_realign_images.py: try priority-ordered candidate articles,
reject portraits and math-render SVG, use media-list as a fallback.
"""

import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

TARGETS = [
    ("geometric-microlith-weapons", ["Microlith", "Maglemosian culture", "Mesolithic"]),
    ("neolithic-mace",              ["Mace (bludgeon)", "Mace-head", "Narmer Palette"]),
    ("chiefdom",                    ["Chiefdom", "Varna culture", "Cahokia"]),
    ("early-newspaper",             ["The Daily Courant", "The Spectator (1711)", "Newspaper", "History of newspaper publishing"]),
    ("international-style",         ["International Style (architecture)", "Villa Savoye", "Seagram Building", "Bauhaus building, Dessau"]),
]

PORTRAIT_DESC = re.compile(r"\bborn\s+\d{4}\b", re.I)
MATH_RENDER = "wikimedia.org/api/rest_v1/media/math/render/svg/"


def http(url, accept_json=True, retries=5):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read(); ctype = r.headers.get("Content-Type", "")
                return (json.loads(data.decode("utf-8")), ctype) if accept_json else (data, ctype)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt); continue
            raise


def looks_like_portrait(summary):
    desc = (summary.get("description") or "")
    return bool(PORTRAIT_DESC.search(desc))


def media_list_first_image(article):
    url = "https://en.wikipedia.org/api/rest_v1/page/media-list/" + urllib.parse.quote(article.replace(" ", "_"))
    try:
        data, _ = http(url, accept_json=True)
    except urllib.error.HTTPError:
        return None
    for item in data.get("items", []):
        if item.get("type") != "image":
            continue
        candidate = ""
        srcset = item.get("srcset") or []
        if srcset:
            candidate = srcset[0].get("src") or ""
        if not candidate:
            candidate = (item.get("original") or {}).get("source") or ""
        if not candidate:
            continue
        if candidate.startswith("//"):
            candidate = "https:" + candidate
        if MATH_RENDER in candidate:
            continue
        return candidate
    return None


def try_one_candidate(tid, article):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(article.replace(" ", "_"))
    try:
        summary, _ = http(url, accept_json=True)
    except urllib.error.HTTPError as e:
        return None, None, None, None, False, f"summary HTTP {e.code}"
    if looks_like_portrait(summary):
        return None, summary.get("title", article), None, summary, False, "portrait (description has 'born YYYY')"
    article_title = summary.get("title", article)
    page_url = summary.get("content_urls", {}).get("desktop", {}).get("page",
        f"https://en.wikipedia.org/wiki/{urllib.parse.quote(article_title.replace(' ', '_'))}")
    thumb = (summary.get("thumbnail") or {}).get("source") or (summary.get("originalimage") or {}).get("source")
    fallback_used = False
    if not thumb:
        thumb = media_list_first_image(article_title)
        fallback_used = bool(thumb)
    if not thumb:
        return None, article_title, page_url, summary, fallback_used, "no usable image"
    img_bytes, ctype = http(thumb, accept_json=False)
    ext = ".jpg" if ("jpeg" in ctype or "jpg" in ctype) else (".png" if "png" in ctype else (".svg" if "svg" in ctype else ".jpg"))
    for e in (".jpg", ".png", ".jpeg", ".svg"):
        p = IMG_DIR / f"{tid}{e}"
        if p.exists() and e != ext:
            p.unlink()
    img_path = IMG_DIR / f"{tid}{ext}"
    img_path.write_bytes(img_bytes)
    return img_path, article_title, page_url, summary, fallback_used, None


def main():
    IMG_DIR.mkdir(exist_ok=True)
    manifest = json.loads(MANIFEST.read_text())
    failed = []
    for tid, candidates in TARGETS:
        prior = manifest.get(tid, {})
        attempts = []
        success = None
        for article in candidates:
            try:
                img_path, art, page, summary, fb, err = try_one_candidate(tid, article)
            except Exception as e:
                attempts.append((article, f"err: {e}"))
                time.sleep(0.4); continue
            if err:
                attempts.append((article, err))
                time.sleep(0.4); continue
            success = (img_path, art, page, summary, fb)
            break

        if not success:
            print(f"  [no-image] {tid:32} tried: " + ", ".join(f'{a}({e})' for a, e in attempts))
            failed.append((tid, attempts))
            prior_with_note = dict(prior)
            prior_with_note["last_refetch_attempt"] = {"candidates": [a for a, _ in attempts], "errors": [e for _, e in attempts]}
            manifest[tid] = prior_with_note
            continue

        img_path, art, page, summary, fb = success
        tag = "[ok-fb]" if fb else "[ok]"
        print(f"  {tag:11} {tid:32} -> {art}" + ("  (fallback chain)" if attempts else ""))
        manifest[tid] = {
            "name": tid, "query": candidates[0], "article": art, "page": page,
            "image_url": (summary.get("thumbnail") or {}).get("source") or "(media-list fallback)",
            "image_path": str(img_path.relative_to(ROOT)),
            "extract": (summary.get("extract") or "")[:280],
            "status": "ok", "score": 0.9,
            "reason": "coverage gap fill (May 2026)" + (" [media-list]" if fb else "") + (f" [fallback after: {[a for a,_ in attempts]}]" if attempts else ""),
        }
        time.sleep(0.6)

    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    entries, attribution = {}, {}
    for k, v in manifest.items():
        if v.get("image_path"):
            entries[k] = v["image_path"]
            attribution[k] = {"article": v.get("article"), "url": v.get("page")}
    out = ROOT / "images.js"
    with open(out, "w") as f:
        f.write("// Auto-generated from _image_manifest.json. Do not edit by hand.\n")
        f.write("// Maps tech id -> Wikipedia image path + attribution.\n")
        f.write("window.TECH_IMAGES = " + json.dumps(entries, indent=2, ensure_ascii=False) + ";\n")
        f.write("window.TECH_IMAGE_CREDITS = " + json.dumps(attribution, indent=2, ensure_ascii=False) + ";\n")
    print(f"\nimages.js: {len(entries)} entries")
    if failed:
        print("\nStill failing (consider AI generation):")
        for tid, attempts in failed:
            print(f"  {tid}")
            for a, e in attempts:
                print(f"      {a} -> {e}")


if __name__ == "__main__":
    main()
