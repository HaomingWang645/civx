#!/usr/bin/env python3
"""Fetch Wikipedia thumbnails for the 12 newly added Modern era techs and
regenerate images.js from the full manifest."""

import json, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# Hand-picked Wikipedia article titles for each of the 12 new techs.
# Chose articles whose lead image is iconic and unmistakable for the topic.
TARGETS = [
    ("insulin-therapy",     "Insulin (medication)"),
    ("continental-drift",   "Alfred Wegener"),
    ("radio-broadcasting",  "Radio broadcasting"),
    ("sound-film",          "The Jazz Singer"),
    ("big-bang-cosmology",  "Edwin Hubble"),
    ("federal-reserve",     "Federal Reserve"),
    ("russian-revolution",  "October Revolution"),
    ("fascism",             "Benito Mussolini"),
    ("womens-suffrage",     "Women's suffrage"),
    ("keynesian-economics", "John Maynard Keynes"),
    ("cryptanalysis-bombe", "Bombe"),
    ("strategic-bombing",   "Boeing B-29 Superfortress"),
]


def http(url, accept_json=True, retries=5):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
                ctype = r.headers.get("Content-Type", "")
                if accept_json:
                    return json.loads(data.decode("utf-8")), ctype
                return data, ctype
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise


def main():
    IMG_DIR.mkdir(exist_ok=True)
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}

    for tid, article in TARGETS:
        if manifest.get(tid, {}).get("status") == "ok" and (IMG_DIR / f"{tid}.jpg").exists():
            print(f"  [cached] {tid}")
            continue
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(article.replace(" ", "_"))
        try:
            summary, _ = http(url, accept_json=True)
            article_title = summary.get("title", article)
            page_url = summary.get("content_urls", {}).get("desktop", {}).get("page",
                f"https://en.wikipedia.org/wiki/{urllib.parse.quote(article_title.replace(' ', '_'))}")
            thumb = (summary.get("thumbnail") or {}).get("source") or (summary.get("originalimage") or {}).get("source")
            if not thumb:
                print(f"  [no-image] {tid} ({article_title})")
                manifest[tid] = {"name": tid, "article": article_title, "page": page_url,
                                 "status": "no_image", "reason": "no thumbnail"}
                continue
            img_bytes, ctype = http(thumb, accept_json=False)
            ext = ".jpg" if ("jpeg" in ctype or "jpg" in ctype) else (".png" if "png" in ctype else ".jpg")
            img_path = IMG_DIR / f"{tid}{ext}"
            img_path.write_bytes(img_bytes)
            manifest[tid] = {
                "name": tid, "query": article, "article": article_title,
                "page": page_url, "image_url": thumb,
                "image_path": str(img_path.relative_to(ROOT)),
                "extract": (summary.get("extract") or "")[:280],
                "status": "ok", "score": 0.9, "reason": "manual override",
            }
            print(f"  [ok]     {tid:25} -> {article_title}")
        except Exception as e:
            print(f"  [err]    {tid}: {e}")
            manifest[tid] = {"name": tid, "query": article, "status": "no_match", "reason": str(e)[:200]}
        time.sleep(0.6)

    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    # Regenerate images.js from the full manifest.
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
    print(f"\nimages.js: {len(entries)} entries with images, {len(attribution)} credits")


if __name__ == "__main__":
    main()
