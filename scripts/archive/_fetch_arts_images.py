#!/usr/bin/env python3
"""Fetch Wikipedia thumbnails for the 6 arts/entertainment techs."""

import json, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "images"
MANIFEST = ROOT / "_image_manifest.json"
UA = "TechTreeImageFetcher/1.0 (personal project; contact: pittisl112@gmail.com)"

# Each is an artwork/object/movement article — never a person's portrait.
TARGETS = [
    ("abstract-expressionism", "No. 5, 1948"),
]


def http(url, accept_json=True, retries=5):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
                ctype = r.headers.get("Content-Type", "")
                return (json.loads(data.decode("utf-8")), ctype) if accept_json else (data, ctype)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt); continue
            raise


def fetch_one(tid, article):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(article.replace(" ", "_"))
    summary, _ = http(url, accept_json=True)
    article_title = summary.get("title", article)
    page_url = summary.get("content_urls", {}).get("desktop", {}).get("page",
        f"https://en.wikipedia.org/wiki/{urllib.parse.quote(article_title.replace(' ', '_'))}")
    thumb = (summary.get("thumbnail") or {}).get("source") or (summary.get("originalimage") or {}).get("source")
    if not thumb:
        return None, article_title, page_url, "no thumbnail", summary
    img_bytes, ctype = http(thumb, accept_json=False)
    ext = ".jpg" if ("jpeg" in ctype or "jpg" in ctype) else (".png" if "png" in ctype else ".jpg")
    img_path = IMG_DIR / f"{tid}{ext}"
    img_path.write_bytes(img_bytes)
    return img_path, article_title, page_url, None, summary


def main():
    IMG_DIR.mkdir(exist_ok=True)
    manifest = json.loads(MANIFEST.read_text())
    failed = []
    for tid, article in TARGETS:
        if manifest.get(tid, {}).get("status") == "ok" and any((IMG_DIR / f"{tid}{e}").exists() for e in (".jpg",".png")):
            print(f"  [cached] {tid}"); continue
        try:
            img_path, art, page, err, summary = fetch_one(tid, article)
            if err:
                print(f"  [no-image] {tid:30} ({art})")
                failed.append((tid, article, err))
                manifest[tid] = {"name": tid, "query": article, "article": art, "page": page,
                                 "status": "no_image", "reason": err}
                time.sleep(0.5); continue
            manifest[tid] = {
                "name": tid, "query": article, "article": art, "page": page,
                "image_url": (summary.get("thumbnail") or {}).get("source"),
                "image_path": str(img_path.relative_to(ROOT)),
                "extract": (summary.get("extract") or "")[:280],
                "status": "ok", "score": 0.9, "reason": "arts addition",
            }
            print(f"  [ok]       {tid:30} -> {art}")
        except Exception as e:
            print(f"  [err]      {tid}: {e}")
            failed.append((tid, article, str(e)))
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
        print(f"\n{len(failed)} failed:")
        for tid, art, err in failed:
            print(f"  {tid}: {art} ({err})")


if __name__ == "__main__":
    main()
