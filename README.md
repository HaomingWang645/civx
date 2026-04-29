# Human History Tech Tree

An interactive visualization of human technological development, from the Lower Paleolithic (~3.3 Mya) through the Information Age. Techs are laid out as a directed graph by era and prerequisite, with categories, descriptions, generated sigils, and what each tech historically unlocked (resources, organisms, wonders, units, works, organizations, people).

## Run

It's a static site — open [index.html](index.html) in a browser, or serve the directory:

```sh
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Features

- **Layered graph layout** — techs grouped in columns by era, rows assigned via topological sort to minimize edge crossings ([app.js](app.js)).
- **Pan / zoom / fit-to-view** controls with a horizontal scrollbar.
- **Search** across tech names (English and Chinese).
- **Categories & eras** sidebar — click to filter/highlight.
- **Theme toggle** — Modern ↔ Renaissance ([styles.css](styles.css)).
- **Bilingual** — English + Chinese names and translations ([translations.js](translations.js)).
- **Unlocks panel** — each tech lists historical resources, organisms, wonders, devices, works, organizations, and people it enabled ([unlocks.js](unlocks.js)).
- **Generative sigils** — deterministic per-tech SVG glyphs as visual identifiers.

## Structure

| File | Purpose |
| --- | --- |
| [index.html](index.html) | Page shell, SVG canvas, script load order |
| [styles.css](styles.css) | Layout, themes, typography |
| [app.js](app.js) | Layout algorithm, rendering, interactions |
| [data.js](data.js) | `ERAS`, `CATEGORIES`, `TECHS` (~346 entries) |
| [translations.js](translations.js) | Chinese tech names |
| [unlocks.js](unlocks.js) | Per-tech unlocked entities |
| [images.js](images.js) / [images/](images/) | Image references and assets |

## Data model

Each tech in [data.js](data.js):

```js
{
  id: "acheulean",
  name: "Acheulean Hand Axes",
  era: "lower-paleo",
  category: "tools",
  year: "~1.76 Mya",
  prereqs: ["oldowan"],
  desc: "Bifacially worked teardrop-shaped hand axes…"
}
```

## Maintenance scripts

Python helpers used to build and refine the dataset (re-runnable, not needed at runtime):

- [_expand_descs.py](_expand_descs.py) — rewrite each tech's `desc` with longer historical context.
- [_apply_fixes.py](_apply_fixes.py) — bulk corrections to [data.js](data.js).
- [_fetch_images.py](_fetch_images.py) — populate [images/](images/) and the image manifest.
