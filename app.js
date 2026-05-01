// Tech Tree renderer.
// Layout: techs are placed in columns by era, rows assigned by a layered topological sort
// that minimizes edge crossings and groups categories. Edges are drawn as smooth cubic Béziers.

// IIFE so our top-level `const` names don't collide with the same names already
// declared at top level in data.js (browsers share one script-scoped lexical env).
(() => {
const { ERAS, CATEGORIES, TECHS } = window.TECH_TREE;

const techById = Object.fromEntries(TECHS.map(t => [t.id, t]));
const childrenById = Object.fromEntries(TECHS.map(t => [t.id, []]));
for (const t of TECHS) for (const p of t.prereqs) if (childrenById[p]) childrenById[p].push(t.id);

// ───────────── Generative sigil ─────────────
// Deterministic abstract glyph keyed off tech.id. Same image across reloads,
// distinguishable across techs, unified style across categories.
function hash32(s) {
  let h = 2166136261 >>> 0;
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
  return h >>> 0;
}
function makeRng(seed) {
  let s = seed >>> 0 || 1;
  return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 100000) / 100000; };
}

// Build a tiny SVG <g> sigil sized to fit a `size`×`size` box. Returns a DOM <g>.
function buildSigilGroup(techId, color, size) {
  const r = makeRng(hash32(techId));
  const cx = size / 2, cy = size / 2;
  const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
  g.setAttribute("class", "sigil");

  // tinted backdrop disc
  const back = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  back.setAttribute("cx", cx); back.setAttribute("cy", cy);
  back.setAttribute("r", size * 0.46);
  back.setAttribute("fill", color);
  back.setAttribute("opacity", "0.14");
  g.appendChild(back);

  const ring = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  ring.setAttribute("cx", cx); ring.setAttribute("cy", cy);
  ring.setAttribute("r", size * 0.46);
  ring.setAttribute("fill", "none");
  ring.setAttribute("stroke", color); ring.setAttribute("stroke-opacity", "0.55");
  ring.setAttribute("stroke-width", "0.8");
  g.appendChild(ring);

  const motif = Math.floor(r() * 5);
  const rot = Math.floor(r() * 360);
  const inner = document.createElementNS("http://www.w3.org/2000/svg", "g");
  inner.setAttribute("transform", `rotate(${rot} ${cx} ${cy})`);
  g.appendChild(inner);

  const stroke = (el, w = 1.1) => {
    el.setAttribute("fill", "none");
    el.setAttribute("stroke", color);
    el.setAttribute("stroke-width", w);
    el.setAttribute("stroke-linecap", "round");
    el.setAttribute("stroke-linejoin", "round");
    el.setAttribute("opacity", "0.92");
    return el;
  };
  const ns = "http://www.w3.org/2000/svg";

  if (motif === 0) {
    // radial spokes
    const n = 5 + Math.floor(r() * 5);
    for (let i = 0; i < n; i++) {
      const a = (i / n) * Math.PI * 2;
      const r1 = size * 0.10, r2 = size * (0.28 + r() * 0.12);
      const ln = document.createElementNS(ns, "line");
      ln.setAttribute("x1", cx + Math.cos(a) * r1);
      ln.setAttribute("y1", cy + Math.sin(a) * r1);
      ln.setAttribute("x2", cx + Math.cos(a) * r2);
      ln.setAttribute("y2", cy + Math.sin(a) * r2);
      stroke(ln, 1.0);
      inner.appendChild(ln);
    }
    const dot = document.createElementNS(ns, "circle");
    dot.setAttribute("cx", cx); dot.setAttribute("cy", cy);
    dot.setAttribute("r", size * 0.06);
    dot.setAttribute("fill", color);
    inner.appendChild(dot);
  } else if (motif === 1) {
    // concentric arcs
    const arcs = 2 + Math.floor(r() * 2);
    for (let i = 0; i < arcs; i++) {
      const rad = size * (0.16 + i * 0.10);
      const start = r() * Math.PI * 2, sweep = Math.PI * (0.7 + r() * 0.9);
      const x1 = cx + Math.cos(start) * rad, y1 = cy + Math.sin(start) * rad;
      const x2 = cx + Math.cos(start + sweep) * rad, y2 = cy + Math.sin(start + sweep) * rad;
      const large = sweep > Math.PI ? 1 : 0;
      const path = document.createElementNS(ns, "path");
      path.setAttribute("d", `M ${x1.toFixed(2)} ${y1.toFixed(2)} A ${rad} ${rad} 0 ${large} 1 ${x2.toFixed(2)} ${y2.toFixed(2)}`);
      stroke(path, 1.1);
      inner.appendChild(path);
    }
  } else if (motif === 2) {
    // polygon
    const sides = 3 + Math.floor(r() * 4);
    let pts = "";
    for (let i = 0; i < sides; i++) {
      const a = (i / sides) * Math.PI * 2 + r() * 0.2;
      const rad = size * (0.26 + r() * 0.08);
      pts += `${(cx + Math.cos(a) * rad).toFixed(2)},${(cy + Math.sin(a) * rad).toFixed(2)} `;
    }
    const poly = document.createElementNS(ns, "polygon");
    poly.setAttribute("points", pts.trim());
    stroke(poly, 1.2);
    inner.appendChild(poly);
  } else if (motif === 3) {
    // crossed diagonals + dots
    const a = r() * Math.PI;
    for (let k = 0; k < 2; k++) {
      const ang = a + k * Math.PI / 2;
      const ln = document.createElementNS(ns, "line");
      const rad = size * 0.34;
      ln.setAttribute("x1", cx - Math.cos(ang) * rad); ln.setAttribute("y1", cy - Math.sin(ang) * rad);
      ln.setAttribute("x2", cx + Math.cos(ang) * rad); ln.setAttribute("y2", cy + Math.sin(ang) * rad);
      stroke(ln, 1.0); inner.appendChild(ln);
    }
    for (let i = 0; i < 3; i++) {
      const aa = r() * Math.PI * 2;
      const rr = size * (0.18 + r() * 0.18);
      const dot = document.createElementNS(ns, "circle");
      dot.setAttribute("cx", cx + Math.cos(aa) * rr);
      dot.setAttribute("cy", cy + Math.sin(aa) * rr);
      dot.setAttribute("r", size * 0.04);
      dot.setAttribute("fill", color);
      inner.appendChild(dot);
    }
  } else {
    // sine ribbon
    let d = "";
    const amp = size * (0.10 + r() * 0.06);
    const phase = r() * Math.PI * 2;
    for (let x = -size * 0.36; x <= size * 0.36; x += size * 0.06) {
      const y = Math.sin((x / size) * 7 + phase) * amp;
      d += (d ? " L " : "M ") + (cx + x).toFixed(2) + " " + (cy + y).toFixed(2);
    }
    const path = document.createElementNS(ns, "path");
    path.setAttribute("d", d);
    stroke(path, 1.2);
    inner.appendChild(path);
    // small fixed dot at center
    const dot = document.createElementNS(ns, "circle");
    dot.setAttribute("cx", cx); dot.setAttribute("cy", cy);
    dot.setAttribute("r", size * 0.045);
    dot.setAttribute("fill", color);
    inner.appendChild(dot);
  }
  return g;
}

// ───────────── Layout constants ─────────────
const COL_WIDTH = 300;
const ROW_HEIGHT = 90;
const NODE_W = 240;
const NODE_H = 64;
const ERA_HEADER_H = 60;
const PADDING_X = 60;
const PADDING_Y = 100;

// ───────────── Year parsing ─────────────
// Parses tech.year strings into a numeric calendar year so we can position
// techs chronologically. Handles "~3.3 Mya", "~400 kya", "~3300 BCE",
// "~500 CE", "1453", "1300–1500" (uses first), "12 kya (widespread)".
function parseYear(s) {
  if (!s) return null;
  s = String(s).trim().replace(/^~/, "").replace(/\s*\(.*?\)\s*/g, "").trim();
  // Range like "1300-1500" or "1300–1500": take first number
  let m = s.match(/^([\-\d.]+)\s*[–\-]\s*([\-\d.]+)\s*([A-Za-z]*)$/);
  if (m) s = m[1] + " " + (m[3] || "");
  m = s.match(/^(-?[\d.]+)\s*([A-Za-z]*)/);
  if (!m) return null;
  const num = parseFloat(m[1]);
  const unit = (m[2] || "").toUpperCase();
  if (unit === "MYA") return -num * 1_000_000;
  if (unit === "KYA") return -num * 1000;
  if (unit === "BCE" || unit === "BC") return -num;
  return num; // CE, AD, or no unit
}

// ───────────── Layout: assign each tech an (eraSubcol, rowIdx) ─────────────
// Sub-column = chronological bucket inside the era (so x-axis ≈ time).
// Bucket count per era is set to match the topological depth (so older
// "depth=N" widths still hold), but tech position within the era is by year:
//   subcol = round( (year - era_min_year) / (era_max_year - era_min_year) * (N-1) )
// Then within a bucket, vertical order is by category + barycenter sweep.
function layoutTechs() {
  const eraIdx = Object.fromEntries(ERAS.map((e, i) => [e.id, i]));
  const techById = Object.fromEntries(TECHS.map(t => [t.id, t]));

  // (a) Compute in-era topological depth — used only to set per-era width.
  const topoLevel = {};
  for (const t of TECHS) topoLevel[t.id] = -1;
  let changed = true, iter = 0;
  while (changed && iter < 50) {
    changed = false; iter++;
    for (const t of TECHS) {
      if (topoLevel[t.id] >= 0) continue;
      const inEraPrereqs = t.prereqs.filter(p => techById[p] && techById[p].era === t.era);
      if (inEraPrereqs.length === 0) {
        topoLevel[t.id] = 0; changed = true;
      } else if (inEraPrereqs.every(p => topoLevel[p] >= 0)) {
        topoLevel[t.id] = Math.max(...inEraPrereqs.map(p => topoLevel[p])) + 1;
        changed = true;
      }
    }
  }
  for (const t of TECHS) if (topoLevel[t.id] < 0) topoLevel[t.id] = 0;

  // (b) Year-based sub-column inside each era. nLevels per era = max(2, topo+1)
  // so a long-prereq-chain era keeps enough room.
  const eraLevels = {}; // era_id -> nLevels - 1
  for (const t of TECHS) eraLevels[t.era] = Math.max(eraLevels[t.era] ?? 0, topoLevel[t.id]);
  for (const era of ERAS) eraLevels[era.id] = Math.max(eraLevels[era.id] ?? 0, 1);

  // Per-era minimum sub-column count (overrides auto-derived). Used to spread
  // densely-clustered eras (e.g. Future) across more columns so a single year
  // bucket doesn't pile up into one tall stack.
  const ERA_MIN_LEVELS = {
    mesolithic: 1,
    neolithic: 5, bronze: 20, classical: 9, medieval: 4, renaissance: 7,
    enlightenment: 6, industrial: 9, modern: 6, atomic: 9, information: 8,
    future: 14, "far-future": 12,
  };
  for (const eraId in ERA_MIN_LEVELS) {
    eraLevels[eraId] = Math.max(eraLevels[eraId] ?? 0, ERA_MIN_LEVELS[eraId]);
  }

  // Year range per era
  const eraYearMin = {}, eraYearMax = {};
  for (const t of TECHS) {
    const y = parseYear(t.year);
    if (y == null) continue;
    eraYearMin[t.era] = Math.min(eraYearMin[t.era] ?? Infinity, y);
    eraYearMax[t.era] = Math.max(eraYearMax[t.era] ?? -Infinity, y);
  }

  const inEraLevel = {};
  for (const t of TECHS) {
    const N = eraLevels[t.era] + 1;
    const y = parseYear(t.year);
    const yMin = eraYearMin[t.era], yMax = eraYearMax[t.era];
    if (y == null || yMin == null || yMax == null || yMax === yMin || N <= 1) {
      inEraLevel[t.id] = 0;
    } else {
      const frac = (y - yMin) / (yMax - yMin);
      inEraLevel[t.id] = Math.max(0, Math.min(N - 1, Math.round(frac * (N - 1))));
    }
  }

  // Compact + balance pass per era:
  //   1. Drop empty sub-columns (collapse the horizontal space they take).
  //   2. Merge sparse sub-columns (≤ SPARSE_THRESHOLD techs) into the smaller
  //      of their two neighbors — but only if the merge keeps the target
  //      column at ≤ MAX_PER_COLUMN, so we don't trade sparseness for overflow.
  // A tech tagged `landmark: true` in data.js protects its column from being
  // merged — use this for century-defining techs that should anchor their slot.
  const SPARSE_THRESHOLD = 2;
  const MAX_PER_COLUMN = 12;
  for (const era of ERAS) {
    const eraTechs = TECHS.filter(t => t.era === era.id);
    if (eraTechs.length === 0) continue;
    const N = eraLevels[era.id] + 1;

    // Disjoint-set-ish: root[i] = root col index that col i has been merged into.
    const root = Array.from({ length: N }, (_, i) => i);
    const count = new Array(N).fill(0);
    for (const t of eraTechs) count[inEraLevel[t.id]]++;

    const activeRoots = () => {
      const out = [];
      for (let i = 0; i < N; i++) if (root[i] === i && count[i] > 0) out.push(i);
      return out;
    };
    const mergeInto = (target, source) => {
      for (let i = 0; i < N; i++) if (root[i] === source) root[i] = target;
      count[target] += count[source];
      count[source] = 0;
    };
    const groupHasLandmark = (rootIdx) =>
      eraTechs.some(t => t.landmark && root[inEraLevel[t.id]] === rootIdx);

    // Iteratively absorb sparse groups until none remain (or only one group).
    let progress = true;
    while (progress) {
      progress = false;
      const groups = activeRoots();
      if (groups.length <= 1) break;
      for (let gi = 0; gi < groups.length; gi++) {
        const r = groups[gi];
        if (count[r] > SPARSE_THRESHOLD) continue;
        if (groupHasLandmark(r)) continue;
        const left  = gi > 0                     ? groups[gi - 1] : null;
        const right = gi < groups.length - 1     ? groups[gi + 1] : null;
        // Only consider neighbors that won't overflow MAX_PER_COLUMN.
        const lOk = left  !== null && count[left]  + count[r] <= MAX_PER_COLUMN;
        const rOk = right !== null && count[right] + count[r] <= MAX_PER_COLUMN;
        let target = null;
        if (lOk && rOk) target = count[left] <= count[right] ? left : right;
        else if (lOk) target = left;
        else if (rOk) target = right;
        // If neither neighbor can absorb without overflow, leave the column
        // standalone — better a sparse column than a too-dense one.
        if (target !== null) {
          mergeInto(target, r);
          progress = true;
          break;
        }
      }
    }

    // Renumber surviving groups to 0..K-1 (also drops empty cols by construction).
    const finalGroups = activeRoots();
    const finalIdx = new Map(finalGroups.map((g, i) => [g, i]));
    for (const t of eraTechs) {
      inEraLevel[t.id] = finalIdx.get(root[inEraLevel[t.id]]);
    }
    eraLevels[era.id] = Math.max(0, finalGroups.length - 1);
  }

  // Group by (era, level) into buckets — eraLevels was already set above.
  const buckets = {}; // key "era|level" -> [techs]
  for (const t of TECHS) {
    const key = t.era + "|" + inEraLevel[t.id];
    (buckets[key] ||= []).push(t);
  }

  // Era pixel start (variable widths now)
  const eraXStart = {};
  let xCursor = PADDING_X;
  for (const era of ERAS) {
    eraXStart[era.id] = xCursor;
    xCursor += (eraLevels[era.id] + 1) * COL_WIDTH;
  }
  const totalW = xCursor + PADDING_X;

  // Process buckets left-to-right (era, then level) for barycenter sweeps
  const sortedKeys = Object.keys(buckets).sort((a, b) => {
    const [ae, al] = a.split("|"); const [be, bl] = b.split("|");
    return (eraIdx[ae] - eraIdx[be]) || (parseInt(al) - parseInt(bl));
  });

  // Initial in-bucket order: by category, then name
  const catOrder = Object.keys(CATEGORIES);
  for (const key of sortedKeys) {
    buckets[key].sort((a, b) => {
      const c = catOrder.indexOf(a.category) - catOrder.indexOf(b.category);
      return c !== 0 ? c : a.name.localeCompare(b.name);
    });
  }
  const positions = {};
  for (const key of sortedKeys) buckets[key].forEach((t, ri) => positions[t.id] = ri);

  // Barycenter sweeps to reduce crossings
  for (let sweep = 0; sweep < 4; sweep++) {
    for (const key of sortedKeys) {
      const list = buckets[key];
      if (list.length <= 1) continue;
      list.sort((a, b) => {
        const aBary = barycenter(a, positions, techById);
        const bBary = barycenter(b, positions, techById);
        if (aBary !== bBary) return aBary - bBary;
        return catOrder.indexOf(a.category) - catOrder.indexOf(b.category);
      });
      list.forEach((t, ri) => positions[t.id] = ri);
    }
  }

  // Pixel positions
  const placed = {};
  for (const t of TECHS) {
    placed[t.id] = {
      ...t,
      eraIdx: eraIdx[t.era],
      level: inEraLevel[t.id],
      row: positions[t.id],
      x: eraXStart[t.era] + inEraLevel[t.id] * COL_WIDTH,
      y: PADDING_Y + positions[t.id] * ROW_HEIGHT,
    };
  }

  let maxRow = 0;
  for (const key of sortedKeys) maxRow = Math.max(maxRow, buckets[key].length);
  const totalH = PADDING_Y + maxRow * ROW_HEIGHT + 80;

  return { placed, eraXStart, eraLevels, totalW, totalH };
}

function barycenter(tech, positions, techById) {
  const prereqRows = tech.prereqs
    .map(id => positions[id])
    .filter(r => r !== undefined);
  if (prereqRows.length === 0) return positions[tech.id] ?? 0;
  return prereqRows.reduce((a, b) => a + b, 0) / prereqRows.length;
}

const layout = layoutTechs();

// Vertical mode is implemented as a coordinate flip: every (x, y) becomes
// (y, x) at render time. The layout function is unchanged. Helper:
function flipPos(x, y) {
  return state.vertical ? [y, x] : [x, y];
}
function canvasW() { return state.vertical ? layout.totalH : layout.totalW; }
function canvasH() { return state.vertical ? layout.totalW : layout.totalH; }

// ───────────── State ─────────────
const state = {
  selectedId: null,
  hoveredId: null,
  // Time runs left-to-right when false, top-to-bottom when true.
  vertical: false,
  // Categories the user has clicked to filter on. Empty = show everything.
  // Non-empty = only techs whose category is in this set are highlighted.
  selectedCategories: new Set(),
  scale: 1,
  tx: 0,
  ty: 0,
  search: "",
};

// ───────────── DOM refs ─────────────
const svg = document.getElementById("canvas");
const viewport = document.getElementById("viewport");
const detailEl = document.getElementById("detail");
const zoomLevelEl = document.getElementById("zoom-level");

// ───────────── Render ─────────────
function render() {
  // Era bands + headers
  const eraGroup = document.getElementById("eras");
  eraGroup.innerHTML = "";
  ERAS.forEach((era, i) => {
    const xStart = layout.eraXStart[era.id];
    const nLevels = layout.eraLevels[era.id] + 1;
    const x = xStart - 20;
    const w = nLevels * COL_WIDTH;
    const eraCls = "era-" + era.id;

    // In vertical mode, era bands span horizontally and stack top-to-bottom;
    // in horizontal mode, they span vertically and stack left-to-right.
    const [bx, by] = flipPos(x, 30);
    const [bw, bh] = state.vertical ? [layout.totalH - 30, w] : [w, layout.totalH - 30];

    const band = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    band.setAttribute("class", "era-band " + (i % 2 === 0 ? "era-even" : "era-odd") + " " + eraCls);
    band.setAttribute("x", bx); band.setAttribute("y", by);
    band.setAttribute("width", bw); band.setAttribute("height", bh);
    eraGroup.appendChild(band);

    if (i > 0) {
      const divider = document.createElementNS("http://www.w3.org/2000/svg", "line");
      divider.setAttribute("class", "era-divider " + eraCls);
      const [d1x, d1y] = flipPos(x, 30);
      const [d2x, d2y] = flipPos(x, layout.totalH);
      divider.setAttribute("x1", d1x); divider.setAttribute("y1", d1y);
      divider.setAttribute("x2", d2x); divider.setAttribute("y2", d2y);
      eraGroup.appendChild(divider);
    }

    const labelW = Math.min(220, w - 40);
    const labelBg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    labelBg.setAttribute("class", "era-label-pill " + (i % 2 === 0 ? "era-even" : "era-odd") + " " + eraCls);
    const [lbx, lby] = flipPos(x + (w - labelW) / 2, 38);
    const [lbw, lbh] = state.vertical ? [38, labelW] : [labelW, 38];
    labelBg.setAttribute("x", lbx); labelBg.setAttribute("y", lby);
    labelBg.setAttribute("width", lbw); labelBg.setAttribute("height", lbh);
    labelBg.setAttribute("rx", 6);
    labelBg.style.cursor = "pointer";
    labelBg.addEventListener("click", (e) => { e.stopPropagation(); showEraDetail(era.id); });
    eraGroup.appendChild(labelBg);

    const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
    label.setAttribute("class", "era-label " + eraCls);
    const [lx, ly] = flipPos(x + w / 2, 56);
    label.setAttribute("x", lx); label.setAttribute("y", ly);
    label.setAttribute("text-anchor", "middle");
    label.textContent = era.name;
    label.style.cursor = "pointer";
    label.addEventListener("click", (e) => { e.stopPropagation(); showEraDetail(era.id); });
    eraGroup.appendChild(label);

    const range = document.createElementNS("http://www.w3.org/2000/svg", "text");
    range.setAttribute("class", "era-range-label " + eraCls);
    const [rx, ry] = flipPos(x + w / 2, 72);
    range.setAttribute("x", rx); range.setAttribute("y", ry);
    range.setAttribute("text-anchor", "middle");
    range.textContent = era.range;
    range.style.cursor = "pointer";
    range.addEventListener("click", (e) => { e.stopPropagation(); showEraDetail(era.id); });
    eraGroup.appendChild(range);
  });

  // Edges
  const edgeGroup = document.getElementById("edges");
  edgeGroup.innerHTML = "";
  for (const t of TECHS) {
    const child = layout.placed[t.id];
    for (const pid of t.prereqs) {
      const parent = layout.placed[pid];
      if (!parent) continue;
      const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
      path.setAttribute("class", "edge");
      path.setAttribute("d", edgePath(parent, child));
      path.dataset.from = pid;
      path.dataset.to = t.id;
      edgeGroup.appendChild(path);
    }
  }

  // Nodes
  const nodeGroup = document.getElementById("nodes");
  nodeGroup.innerHTML = "";
  for (const t of TECHS) {
    const p = layout.placed[t.id];
    const cat = CATEGORIES[t.category];

    const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
    g.setAttribute("class", "node era-" + t.era);
    const [nx, ny] = flipPos(p.x, p.y);
    g.setAttribute("transform", `translate(${nx}, ${ny})`);
    g.dataset.id = t.id;

    const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    rect.setAttribute("class", "node-rect");
    rect.setAttribute("width", NODE_W);
    rect.setAttribute("height", NODE_H);
    rect.setAttribute("rx", 10);
    g.appendChild(rect);

    const bar = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    bar.setAttribute("class", "node-cat-bar");
    bar.setAttribute("x", 0);
    bar.setAttribute("y", 0);
    bar.setAttribute("width", 4);
    bar.setAttribute("height", NODE_H);
    bar.setAttribute("fill", cat.color);
    bar.setAttribute("rx", 2);
    g.appendChild(bar);

    const SIGIL = 28;
    const sigil = buildSigilGroup(t.id, cat.color, SIGIL);
    sigil.setAttribute("transform", `translate(${10}, ${(NODE_H - SIGIL) / 2})`);
    g.appendChild(sigil);

    const TEXT_X = 10 + SIGIL + 8; // sigil + gap

    const meta = document.createElementNS("http://www.w3.org/2000/svg", "text");
    meta.setAttribute("class", "node-meta");
    meta.setAttribute("x", TEXT_X);
    meta.setAttribute("y", 22);
    meta.setAttribute("fill", cat.color);
    meta.textContent = cat.name;
    g.appendChild(meta);

    const title = document.createElementNS("http://www.w3.org/2000/svg", "text");
    title.setAttribute("class", "node-title");
    title.setAttribute("x", TEXT_X);
    title.setAttribute("y", 42);
    title.textContent = t.name;
    g.appendChild(title);

    const year = document.createElementNS("http://www.w3.org/2000/svg", "text");
    year.setAttribute("class", "node-year");
    year.setAttribute("x", NODE_W - 14);
    year.setAttribute("y", NODE_H - 12);
    year.textContent = t.year;
    g.appendChild(year);

    g.addEventListener("click", (e) => {
      e.stopPropagation();
      selectNode(t.id);
    });
    g.addEventListener("mouseenter", () => { state.hoveredId = t.id; applyHighlights(); });
    g.addEventListener("mouseleave", () => { state.hoveredId = null; applyHighlights(); });

    nodeGroup.appendChild(g);
  }

  // No viewBox: SVG user units = CSS pixels 1:1, so state.scale is the
  // only zoom factor in play. (With a fitting viewBox, max zoom was clamped
  // to ~0.4× because two scale layers were multiplying.)
  svg.removeAttribute("viewBox");
  buildEraTicks();
  initialView();
  applyHighlights();
}

function edgePath(a, b) {
  // Compute connection points in horizontal-mode coordinates first…
  let x1 = a.x + NODE_W, y1 = a.y + NODE_H / 2;
  let x2 = b.x,          y2 = b.y + NODE_H / 2;
  // …then flip both endpoints if vertical mode is on.
  if (state.vertical) {
    [x1, y1] = [y1, x1];
    [x2, y2] = [y2, x2];
  }
  const isVert = state.vertical;
  // Bezier handles run along the time axis (x in horizontal mode, y in vertical).
  const c1x = isVert ? x1               : (x1 + x2) / 2;
  const c1y = isVert ? (y1 + y2) / 2    : y1;
  const c2x = isVert ? x2               : (x1 + x2) / 2;
  const c2y = isVert ? (y1 + y2) / 2    : y2;
  return `M ${x1},${y1} C ${c1x},${c1y} ${c2x},${c2y} ${x2},${y2}`;
}

// ───────────── Highlights ─────────────
function applyHighlights() {
  const focusId = state.selectedId || state.hoveredId;
  const sel = state.selectedCategories;
  const filtering = sel.size > 0;
  const search = state.search.trim().toLowerCase();

  const ancestors = new Set();
  const descendants = new Set();
  if (focusId) {
    collect(focusId, ancestors, "up");
    collect(focusId, descendants, "down");
  }

  // Nodes — when category filter is active, dim techs outside the set.
  document.querySelectorAll(".node").forEach(n => {
    const id = n.dataset.id;
    const tech = techById[id];
    const outOfFilter = filtering && !sel.has(tech.category);
    const matchesSearch = !search || tech.name.toLowerCase().includes(search);
    const inFocus = !focusId || id === focusId || ancestors.has(id) || descendants.has(id);
    n.classList.toggle("selected", id === state.selectedId);
    n.classList.toggle("dimmed", outOfFilter || !inFocus || !matchesSearch);
  });

  // Edges
  document.querySelectorAll(".edge").forEach(e => {
    const from = e.dataset.from, to = e.dataset.to;
    const fromTech = techById[from];
    const toTech = techById[to];
    const inFocus = !focusId
      || (ancestors.has(from) && (ancestors.has(to) || to === focusId))
      || (descendants.has(to) && (descendants.has(from) || from === focusId))
      || from === focusId || to === focusId;
    const outOfFilter = filtering && (!sel.has(fromTech.category) || !sel.has(toTech.category));
    e.classList.toggle("highlighted", !!focusId && inFocus);
    e.classList.toggle("dimmed", outOfFilter || (!!focusId && !inFocus));
  });
}

function collect(id, set, direction) {
  const tech = techById[id];
  if (!tech) return;
  const next = direction === "up" ? tech.prereqs : childrenById[id];
  for (const nid of next) {
    if (set.has(nid)) continue;
    set.add(nid);
    collect(nid, set, direction);
  }
}

// ───────────── Selection / Detail panel ─────────────
function selectNode(id) {
  state.selectedId = id;
  showDetail(id);
  applyHighlights();
}

function clearSelection() {
  state.selectedId = null;
  detailEl.classList.remove("open");
  applyHighlights();
}

function showDetail(id) {
  const t = techById[id];
  const cat = CATEGORIES[t.category];
  const dependents = childrenById[id].map(cid => techById[cid]);
  const prereqs = t.prereqs.map(pid => techById[pid]).filter(Boolean);

  // Image slot. images.js maps tech id -> downloaded Wikipedia thumbnail path.
  // If missing or fails to load, the slot collapses to the larger generative sigil.
  const imgPath = (window.TECH_IMAGES && window.TECH_IMAGES[t.id]) || null;
  const imgCredit = (window.TECH_IMAGE_CREDITS && window.TECH_IMAGE_CREDITS[t.id]) || null;
  const credit = imgCredit
    ? `<a class="detail-img-credit" href="${imgCredit.url}" target="_blank" rel="noopener">Wikipedia · ${imgCredit.article}</a>`
    : "";

  detailEl.innerHTML = `
    <button class="detail-close" aria-label="Close">×</button>
    <div class="detail-img${imgPath ? "" : " no-img"}" style="--cat: ${cat.color}">
      ${imgPath ? `<img src="${imgPath}" alt="${t.name}" onerror="this.parentElement.classList.add('no-img');" />` : ""}
      <div class="detail-img-fallback" aria-hidden="true"></div>
      ${credit}
    </div>
    <div class="detail-cat" style="color: ${cat.color}">
      <span class="detail-cat-dot" style="background: ${cat.color}"></span>
      ${cat.name}
    </div>
    <a class="detail-title" href="${imgCredit?.url || `https://en.wikipedia.org/wiki/Special:Search?search=${encodeURIComponent(t.name)}&go=Go`}" target="_blank" rel="noopener" title="Open source on Wikipedia">${t.name}</a>
    ${(window.TECH_NAMES_ZH && window.TECH_NAMES_ZH[t.id]) ? `<div class="detail-title-zh">${window.TECH_NAMES_ZH[t.id]}</div>` : ""}
    <div class="detail-year">${t.year} · ${ERAS.find(e => e.id === t.era).name}</div>
    <div class="detail-desc">${t.desc}</div>
    ${prereqs.length ? `
      <div class="detail-section">
        <div class="detail-section-title">Requires</div>
        ${prereqs.map(p => `<div class="detail-link" data-id="${p.id}">${p.name}</div>`).join("")}
      </div>` : ""}
    ${dependents.length ? `
      <div class="detail-section">
        <div class="detail-section-title">Leads to</div>
        ${dependents.map(p => `<div class="detail-link" data-id="${p.id}">${p.name}</div>`).join("")}
      </div>` : ""}
    ${(() => {
      const unlocks = (window.TECH_UNLOCKS && window.TECH_UNLOCKS[t.id]) || [];
      const cats = window.TECH_UNLOCK_CATEGORIES || {};
      if (!unlocks.length) return "";
      return `
        <div class="detail-section">
          <div class="detail-section-title">Unlocks</div>
          <div class="detail-unlocks">
            ${unlocks.map(u => {
              const c = cats[u.type] || { icon: "•", label: u.type };
              const zh = u.name_zh ? ` <span class="unlock-zh">(${u.name_zh})</span>` : "";
              const inner = `<span class="unlock-icon">${c.icon}</span><span class="unlock-name">${u.name}${zh}</span>`;
              // Linking precedence:
              //   u.url = "https://..."  → link to that arbitrary URL (use when no good Wikipedia article exists)
              //   u.wiki = false         → render as a flat (non-link) chip
              //   u.wiki = "Article"     → link directly to that Wikipedia article
              //   absent / true          → link via Wikipedia search (legacy default)
              if (typeof u.url === "string" && u.url) {
                return `<a class="unlock-chip" href="${u.url}" target="_blank" rel="noopener" title="${c.label} · open source">${inner}</a>`;
              }
              if (u.wiki === false) {
                return `<span class="unlock-chip unlock-chip-flat" title="${c.label}">${inner}</span>`;
              }
              const article = (typeof u.wiki === "string" && u.wiki) ? u.wiki : u.name;
              const wikiUrl = (typeof u.wiki === "string" && u.wiki)
                ? `https://en.wikipedia.org/wiki/${encodeURIComponent(article.replace(/ /g, "_"))}`
                : `https://en.wikipedia.org/wiki/Special:Search?search=${encodeURIComponent(article)}&go=Go`;
              return `<a class="unlock-chip" href="${wikiUrl}" target="_blank" rel="noopener" title="${c.label} · open Wikipedia">${inner}</a>`;
            }).join("")}
          </div>
        </div>`;
    })()}
  `;

  // Render the fallback sigil into the .detail-img-fallback div (used when <img> errors).
  const fallback = detailEl.querySelector(".detail-img-fallback");
  const sig = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  sig.setAttribute("viewBox", "0 0 200 200");
  sig.setAttribute("preserveAspectRatio", "xMidYMid meet");
  sig.style.width = "100%";
  sig.style.height = "100%";
  sig.appendChild(buildSigilGroup(t.id, cat.color, 200));
  fallback.appendChild(sig);

  detailEl.classList.add("open");
  detailEl.scrollTop = 0; // reset scroll so new tech opens from the top
  detailEl.querySelector(".detail-close").onclick = clearSelection;
  detailEl.querySelectorAll(".detail-link").forEach(el => {
    el.onclick = () => selectNode(el.dataset.id);
  });
}

function showEraDetail(eraId) {
  const era = ERAS.find(e => e.id === eraId);
  if (!era) return;

  // Techs in this era, grouped by category, year-sorted within each group.
  const eraTechs = TECHS.filter(t => t.era === eraId);
  const yearKey = (y) => {
    const s = String(y || "").replace(/^~/, "").trim();
    const m = s.match(/(-?\d+(?:\.\d+)?)\s*(kya|Mya|BCE|BC|CE)?/i);
    if (!m) return 9e9;
    const n = parseFloat(m[1]); const u = (m[2] || "").toUpperCase();
    if (u === "MYA") return -n * 1e6;
    if (u === "KYA") return -n * 1e3;
    if (u === "BCE" || u === "BC") return -n;
    return n;
  };
  const byCat = {};
  for (const t of eraTechs) (byCat[t.category] ||= []).push(t);
  for (const k in byCat) byCat[k].sort((a, b) => yearKey(a.year) - yearKey(b.year));
  const catOrder = Object.keys(CATEGORIES).filter(c => byCat[c]);
  const nameZh = era.name_zh ? `<div class="detail-title-zh">${era.name_zh}</div>` : "";

  detailEl.innerHTML = `
    <button class="detail-close" aria-label="Close">×</button>
    <div class="detail-cat" style="color: #94a3b8">
      <span class="detail-cat-dot" style="background: #94a3b8"></span>
      Era
    </div>
    <div class="detail-title">${era.name}</div>
    ${nameZh}
    <div class="detail-year">${era.range} · ${eraTechs.length} techs</div>
    <div class="detail-desc">${era.desc || ""}</div>
    ${catOrder.map(cid => {
      const cat = CATEGORIES[cid];
      const list = byCat[cid];
      return `
        <div class="detail-section">
          <div class="detail-section-title" style="color: ${cat.color}">
            <span class="detail-cat-dot" style="background: ${cat.color}"></span>
            ${cat.name} <span style="opacity:.6;font-weight:400">· ${list.length}</span>
          </div>
          ${list.map(t => `<div class="detail-link" data-id="${t.id}">${t.name} <span style="opacity:.55;font-size:.85em">${t.year}</span></div>`).join("")}
        </div>`;
    }).join("")}
  `;

  detailEl.classList.add("open");
  detailEl.scrollTop = 0;
  detailEl.querySelector(".detail-close").onclick = clearSelection;
  detailEl.querySelectorAll(".detail-link").forEach(el => {
    el.onclick = () => selectNode(el.dataset.id);
  });
}

// ───────────── Pan / Zoom ─────────────
function applyTransform() {
  viewport.setAttribute("transform", `translate(${state.tx}, ${state.ty}) scale(${state.scale})`);
  zoomLevelEl.textContent = `${Math.round(state.scale * 100)}%`;
  if (typeof updateScrollbar === "function") updateScrollbar();
  if (typeof updateMinimapViewport === "function") updateMinimapViewport();
}

function fitToView() {
  const rect = svg.getBoundingClientRect();
  const W = state.vertical ? layout.totalH : layout.totalW;
  const H = state.vertical ? layout.totalW : layout.totalH;
  const scaleX = rect.width / W;
  const scaleY = rect.height / H;
  state.scale = Math.min(scaleX, scaleY, 1) * 0.95;
  state.tx = (rect.width - W * state.scale) / 2;
  state.ty = (rect.height - H * state.scale) / 2;
  applyTransform();
}

// Initial view on first load: native scale, anchored at the left/top of the canvas.
// Lets nodes render at full readable size; user can pan/scroll/zoom from there.
function initialView() {
  state.scale = 1.0;
  state.tx = 0;
  state.ty = 0;
  applyTransform();
}

let isPanning = false;
let panStart = null;
let panMoved = false;
const PAN_THRESHOLD = 5; // px before a press counts as a drag rather than a click
svg.addEventListener("mousedown", (e) => {
  isPanning = true;
  panMoved = false;
  panStart = { x: e.clientX - state.tx, y: e.clientY - state.ty, sx: e.clientX, sy: e.clientY };
  svg.classList.add("dragging");
});
window.addEventListener("mousemove", (e) => {
  if (!isPanning) return;
  if (!panMoved && Math.hypot(e.clientX - panStart.sx, e.clientY - panStart.sy) > PAN_THRESHOLD) {
    panMoved = true;
  }
  state.tx = e.clientX - panStart.x;
  state.ty = e.clientY - panStart.y;
  applyTransform();
});
window.addEventListener("mouseup", () => {
  isPanning = false;
  svg.classList.remove("dragging");
});

// Suppress the synthetic click that follows a drag, so pan-from-node doesn't also select.
svg.addEventListener("click", (e) => {
  if (panMoved) {
    e.stopPropagation();
    e.preventDefault();
    panMoved = false;
  }
}, true);

svg.addEventListener("wheel", (e) => {
  e.preventDefault();
  const rect = svg.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;
  const delta = -e.deltaY * 0.0015;
  const newScale = Math.max(0.2, Math.min(3, state.scale * (1 + delta)));
  // Zoom toward cursor
  const k = newScale / state.scale;
  state.tx = mx - (mx - state.tx) * k;
  state.ty = my - (my - state.ty) * k;
  state.scale = newScale;
  applyTransform();
}, { passive: false });

svg.addEventListener("click", (e) => {
  if (!e.target.closest(".node")) clearSelection();
});

// Controls
document.getElementById("zoom-in").onclick = () => zoomBy(1.2);
document.getElementById("zoom-out").onclick = () => zoomBy(1 / 1.2);
document.getElementById("zoom-fit").onclick = () => fitToView();

// Smooth horizontal pan helper (used by arrow keys)
function panBy(dx, ms = 280) {
  const t0 = performance.now();
  const startTx = state.tx;
  function step(t) {
    const e = Math.min(1, (t - t0) / ms);
    const eased = 1 - Math.pow(1 - e, 3);
    state.tx = startTx + dx * eased;
    applyTransform();
    if (e < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

// ───────────── Horizontal scrollbar ─────────────
const scrollbarEl = document.getElementById("scrollbar-h");
const scrollTrackEl = document.getElementById("scrollbar-track");
const scrollThumbEl = document.getElementById("scrollbar-thumb");

function updateScrollbar() {
  const vw = svg.getBoundingClientRect().width;
  const cw = layout.totalW * state.scale;
  if (cw <= vw + 1) { scrollbarEl.classList.add("hidden"); return; }
  scrollbarEl.classList.remove("hidden");

  const trackW = scrollTrackEl.getBoundingClientRect().width;
  const visibleFrac = vw / cw;
  const thumbW = Math.max(40, trackW * visibleFrac);
  // tx = 0  → content's x=0 at viewport's x=0
  // tx = -(cw - vw) → content's right edge at viewport's right edge
  const sf = Math.max(0, Math.min(1, -state.tx / (cw - vw)));
  const thumbX = sf * (trackW - thumbW);
  scrollThumbEl.style.width = thumbW + "px";
  scrollThumbEl.style.left = thumbX + "px";
}

// Build era tick marks on the scrollbar (positions are in canvas units, so
// scale-invariant — render once after layout).
function buildEraTicks() {
  scrollTrackEl.querySelectorAll(".scrollbar-era-tick").forEach(el => el.remove());
  for (let i = 0; i < ERAS.length; i++) {
    const era = ERAS[i];
    const tick = document.createElement("div");
    tick.className = "scrollbar-era-tick";
    tick.dataset.name = era.name;
    tick.style.left = ((layout.eraXStart[era.id] / layout.totalW) * 100) + "%";
    tick.title = era.name + " · " + era.range;
    tick.addEventListener("mousedown", (e) => e.stopPropagation()); // don't trigger track-click
    tick.addEventListener("click", (e) => { e.stopPropagation(); panToEra(i); });
    scrollTrackEl.appendChild(tick);
  }
}

let scrollDragging = false;
let scrollDragStart = { mx: 0, txAtStart: 0, factor: 1 };

scrollThumbEl.addEventListener("mousedown", (e) => {
  e.preventDefault(); e.stopPropagation();
  const vw = svg.getBoundingClientRect().width;
  const cw = layout.totalW * state.scale;
  if (cw <= vw) return;
  const trackW = scrollTrackEl.getBoundingClientRect().width;
  const visibleFrac = vw / cw;
  const thumbW = Math.max(40, trackW * visibleFrac);
  scrollDragging = true;
  scrollDragStart = {
    mx: e.clientX,
    txAtStart: state.tx,
    factor: (cw - vw) / Math.max(1, trackW - thumbW),
  };
  scrollThumbEl.classList.add("dragging");
});
window.addEventListener("mousemove", (e) => {
  if (!scrollDragging) return;
  const dx = e.clientX - scrollDragStart.mx;
  const cw = layout.totalW * state.scale;
  const vw = svg.getBoundingClientRect().width;
  state.tx = Math.max(-(cw - vw), Math.min(0, scrollDragStart.txAtStart - dx * scrollDragStart.factor));
  applyTransform();
});
window.addEventListener("mouseup", () => {
  if (scrollDragging) {
    scrollDragging = false;
    scrollThumbEl.classList.remove("dragging");
  }
});
// Click on track outside thumb: jump there
scrollTrackEl.addEventListener("mousedown", (e) => {
  if (e.target === scrollThumbEl) return;
  const vw = svg.getBoundingClientRect().width;
  const cw = layout.totalW * state.scale;
  if (cw <= vw) return;
  const rect = scrollTrackEl.getBoundingClientRect();
  const trackW = rect.width;
  const visibleFrac = vw / cw;
  const thumbW = Math.max(40, trackW * visibleFrac);
  const clickX = e.clientX - rect.left - thumbW / 2;
  const sf = Math.max(0, Math.min(1, clickX / Math.max(1, trackW - thumbW)));
  state.tx = -sf * (cw - vw);
  applyTransform();
});

function zoomBy(factor) {
  const rect = svg.getBoundingClientRect();
  const cx = rect.width / 2, cy = rect.height / 2;
  const newScale = Math.max(0.2, Math.min(3, state.scale * factor));
  const k = newScale / state.scale;
  state.tx = cx - (cx - state.tx) * k;
  state.ty = cy - (cy - state.ty) * k;
  state.scale = newScale;
  applyTransform();
}

// ───────────── Sidebar ─────────────
//
// Category list behavior: clicking a category adds it to a filter set.
// • Empty filter set → all techs visible (default).
// • Non-empty filter set → only techs in selected categories are highlighted;
//   the rest dim out, and so do edges that touch any non-selected category.
// Clicking a selected category again removes it from the filter (back toward
// "show all" once the set empties).
function renderSidebar() {
  const catList = document.getElementById("category-list");
  catList.innerHTML = "";

  const clearBtn = document.getElementById("category-clear");
  const updateRowStates = () => {
    const filtering = state.selectedCategories.size > 0;
    catList.querySelectorAll(".legend-item").forEach(item => {
      const id = item.dataset.id;
      item.classList.toggle("active", state.selectedCategories.has(id));
      item.classList.toggle("muted", filtering && !state.selectedCategories.has(id));
    });
    if (clearBtn) clearBtn.hidden = !filtering;
  };
  if (clearBtn) {
    clearBtn.onclick = () => {
      state.selectedCategories.clear();
      updateRowStates();
      applyHighlights();
    };
  }

  Object.entries(CATEGORIES).forEach(([id, cat]) => {
    const el = document.createElement("div");
    el.className = "legend-item";
    el.dataset.id = id;
    el.innerHTML = `
      <span class="legend-swatch" style="color: ${cat.color}; background: ${cat.color}"></span>
      <span>${cat.name}</span>
    `;
    el.onclick = () => {
      if (state.selectedCategories.has(id)) state.selectedCategories.delete(id);
      else state.selectedCategories.add(id);
      updateRowStates();
      applyHighlights();
    };
    catList.appendChild(el);
  });
  updateRowStates();

  const eraList = document.getElementById("era-list");
  eraList.innerHTML = "";
  ERAS.forEach((era, i) => {
    const el = document.createElement("div");
    el.className = "era-item";
    el.innerHTML = `
      <div>${era.name}</div>
      <div class="era-range">${era.range}</div>
    `;
    el.onclick = () => panToEra(i);
    eraList.appendChild(el);
  });
}

function panToEra(i) {
  const era = ERAS[i];
  const rect = svg.getBoundingClientRect();
  const xStart = layout.eraXStart[era.id];
  const nLevels = layout.eraLevels[era.id] + 1;
  const targetX = xStart + (nLevels * COL_WIDTH) / 2;
  state.tx = rect.width / 2 - targetX * state.scale;
  applyTransform();
}

// Search
document.getElementById("search-input").addEventListener("input", (e) => {
  state.search = e.target.value;
  applyHighlights();
});

// Keyboard
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") clearSelection();
  if (e.key === "0" && (e.metaKey || e.ctrlKey)) { e.preventDefault(); fitToView(); }
  if (e.target.tagName === "INPUT") return;
  if (e.key === "ArrowLeft")  { e.preventDefault(); panStep(+1); }
  if (e.key === "ArrowRight") { e.preventDefault(); panStep(-1); }
});

window.addEventListener("resize", () => updateScrollbar());

// ───────────── Theme switching ─────────────
// Two palettes: modern (the original cool pastels) and Renaissance (warm,
// saturated tones that read well on parchment). Snapshot the modern palette
// from data.js at load so we can switch back without losing it.
const CATEGORY_COLORS_MODERN = Object.fromEntries(
  Object.entries(CATEGORIES).map(([id, c]) => [id, c.color])
);
const CATEGORY_COLORS_RENAISSANCE = {
  tools:         "#3a6678",
  subsistence:   "#5a7a3a",
  shelter:       "#b8862b",
  social:        "#8c2c4b",
  weapons:       "#8b3a1f",
  knowledge:     "#3a4a7a",
  energy:        "#c25b1f",
  transport:     "#3f7a7a",
  medicine:      "#4a7a3a",
  communication: "#a87a1a",
  economy:       "#6a3a6a",
};

// 3-theme cycle: Modern → Renaissance → Era-Native → ...
const THEMES = ["modern", "renaissance", "eras"];
const THEME_LABELS = { modern: "Modern", renaissance: "Renaissance", eras: "Era-Native" };

function applyTheme(name) {
  if (!THEMES.includes(name)) name = "modern";
  document.body.className = "theme-" + name;
  // Modern palette is the default; Renaissance overrides; Eras keeps modern as base.
  const palette = name === "renaissance" ? CATEGORY_COLORS_RENAISSANCE : CATEGORY_COLORS_MODERN;
  for (const id in CATEGORIES) {
    if (palette[id]) CATEGORIES[id].color = palette[id];
  }
  try { localStorage.setItem("techtree-theme", name); } catch(e) {}
  const btn = document.getElementById("theme-toggle");
  if (btn) {
    const next = THEMES[(THEMES.indexOf(name) + 1) % THEMES.length];
    btn.textContent = THEME_LABELS[next];
  }
}

const themeBtn = document.getElementById("theme-toggle");
themeBtn.addEventListener("click", () => {
  let cur = "modern";
  for (const t of THEMES) if (document.body.classList.contains("theme-" + t)) cur = t;
  const next = THEMES[(THEMES.indexOf(cur) + 1) % THEMES.length];
  applyTheme(next);
  // Re-render so node sigils / category bars pick up the new palette,
  // preserving the user's current pan + zoom.
  const saved = { tx: state.tx, ty: state.ty, scale: state.scale };
  renderSidebar();
  render();
  state.tx = saved.tx; state.ty = saved.ty; state.scale = saved.scale;
  applyTransform();
});

// ───────────── Orientation toggle (horizontal / vertical timeline) ─────────────
const orientBtn = document.getElementById("orient-toggle");
if (orientBtn) {
  orientBtn.addEventListener("click", () => {
    state.vertical = !state.vertical;
    document.body.classList.toggle("orient-vertical", state.vertical);
    orientBtn.textContent = state.vertical ? "↔" : "↕";
    try { localStorage.setItem("techtree-orient", state.vertical ? "vertical" : "horizontal"); } catch(e){}
    render();
    if (typeof renderMinimap === "function") renderMinimap();
    fitToView();
  });
}

// ───────────── Minimap ─────────────
//
// A tiny scaled-down copy of the canvas in the bottom-right corner with a
// rectangle indicating the current visible viewport. Click the minimap to pan
// the main canvas to that location.
const minimapEl     = document.getElementById("minimap");
const minimapSvg    = document.getElementById("minimap-svg");
const minimapContent= document.getElementById("minimap-content");
const minimapVp     = document.getElementById("minimap-viewport");
const minimapToggle = document.getElementById("minimap-toggle");

function renderMinimap() {
  if (!minimapSvg) return;
  const W = state.vertical ? layout.totalH : layout.totalW;
  const H = state.vertical ? layout.totalW : layout.totalH;
  minimapSvg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  minimapContent.innerHTML = "";

  // Era band rectangles
  ERAS.forEach((era, i) => {
    const xStart = layout.eraXStart[era.id];
    const nLevels = layout.eraLevels[era.id] + 1;
    const x = xStart - 20;
    const w = nLevels * COL_WIDTH;
    const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    r.setAttribute("class", i % 2 === 0 ? "minimap-era-band-even" : "minimap-era-band-odd");
    if (state.vertical) {
      r.setAttribute("x", 0); r.setAttribute("y", x);
      r.setAttribute("width", H); r.setAttribute("height", w);
    } else {
      r.setAttribute("x", x); r.setAttribute("y", 0);
      r.setAttribute("width", w); r.setAttribute("height", H);
    }
    minimapContent.appendChild(r);
  });

  // One small dot per tech, colored by category
  for (const t of TECHS) {
    const p = layout.placed[t.id];
    const cat = CATEGORIES[t.category];
    const [x, y] = flipPos(p.x + NODE_W / 2, p.y + NODE_H / 2);
    const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    r.setAttribute("class", "minimap-node");
    r.setAttribute("x", x - 6); r.setAttribute("y", y - 4);
    r.setAttribute("width", 12); r.setAttribute("height", 8);
    r.setAttribute("fill", cat.color);
    minimapContent.appendChild(r);
  }
  updateMinimapViewport();
}

function updateMinimapViewport() {
  if (!minimapVp) return;
  const cw = svg.getBoundingClientRect();
  const W = state.vertical ? layout.totalH : layout.totalW;
  const H = state.vertical ? layout.totalW : layout.totalH;
  // Visible canvas region in canvas coords:
  //   tx + scale * cx_canvas = cx_viewport  →  cx_canvas = (cx_viewport - tx) / scale
  const visX = -state.tx / state.scale;
  const visY = -state.ty / state.scale;
  const visW = cw.width  / state.scale;
  const visH = cw.height / state.scale;
  minimapVp.setAttribute("x", Math.max(0, visX));
  minimapVp.setAttribute("y", Math.max(0, visY));
  minimapVp.setAttribute("width",  Math.min(W, visW));
  minimapVp.setAttribute("height", Math.min(H, visH));
}

function panToMinimapPoint(clientX, clientY) {
  const rect = minimapSvg.getBoundingClientRect();
  const W = state.vertical ? layout.totalH : layout.totalW;
  const H = state.vertical ? layout.totalW : layout.totalH;
  const px = (clientX - rect.left) / rect.width  * W;
  const py = (clientY - rect.top)  / rect.height * H;
  const cw = svg.getBoundingClientRect();
  // Center the canvas viewport on (px, py)
  state.tx = cw.width  / 2 - px * state.scale;
  state.ty = cw.height / 2 - py * state.scale;
  applyTransform();
}

if (minimapSvg) {
  let dragging = false;
  minimapSvg.addEventListener("mousedown", (e) => {
    dragging = true;
    panToMinimapPoint(e.clientX, e.clientY);
  });
  window.addEventListener("mousemove", (e) => {
    if (dragging) panToMinimapPoint(e.clientX, e.clientY);
  });
  window.addEventListener("mouseup", () => { dragging = false; });
}
if (minimapToggle) {
  minimapToggle.addEventListener("click", (e) => {
    e.stopPropagation();
    minimapEl.classList.toggle("collapsed");
    minimapToggle.title = minimapEl.classList.contains("collapsed") ? "Show minimap" : "Hide minimap";
  });
}

// (applyTransform is wired to call updateMinimapViewport directly inside its
// own body — see the function definition above.)

// ───────────── Touch handling (mobile pinch-zoom + pan) ─────────────
let touchPanStart = null;
let touchPinchStart = null;
function touchDist(t1, t2) {
  return Math.hypot(t2.clientX - t1.clientX, t2.clientY - t1.clientY);
}
function touchMid(t1, t2) {
  return { x: (t1.clientX + t2.clientX) / 2, y: (t1.clientY + t2.clientY) / 2 };
}
svg.addEventListener("touchstart", (e) => {
  if (e.touches.length === 1) {
    const t = e.touches[0];
    touchPanStart = { x: t.clientX - state.tx, y: t.clientY - state.ty, sx: t.clientX, sy: t.clientY };
    touchPinchStart = null;
  } else if (e.touches.length === 2) {
    const [t1, t2] = e.touches;
    const m = touchMid(t1, t2);
    touchPinchStart = {
      d0: touchDist(t1, t2),
      scale0: state.scale,
      mx: m.x, my: m.y,
      tx0: state.tx, ty0: state.ty,
    };
    touchPanStart = null;
  }
}, { passive: true });

svg.addEventListener("touchmove", (e) => {
  if (e.touches.length === 1 && touchPanStart) {
    const t = e.touches[0];
    state.tx = t.clientX - touchPanStart.x;
    state.ty = t.clientY - touchPanStart.y;
    applyTransform();
    e.preventDefault();
  } else if (e.touches.length === 2 && touchPinchStart) {
    const [t1, t2] = e.touches;
    const d = touchDist(t1, t2);
    const newScale = Math.max(0.2, Math.min(3, touchPinchStart.scale0 * (d / touchPinchStart.d0)));
    const k = newScale / touchPinchStart.scale0;
    // Anchor zoom around the pinch midpoint at gesture start.
    const rect = svg.getBoundingClientRect();
    const ax = touchPinchStart.mx - rect.left;
    const ay = touchPinchStart.my - rect.top;
    state.tx = ax - (ax - touchPinchStart.tx0) * k;
    state.ty = ay - (ay - touchPinchStart.ty0) * k;
    state.scale = newScale;
    applyTransform();
    e.preventDefault();
  }
}, { passive: false });

svg.addEventListener("touchend", () => {
  touchPanStart = null;
  touchPinchStart = null;
});

// ───────────── PDF export (via browser print → Save as PDF) ─────────────
//
// Strategy: temporarily set the SVG to viewBox the entire layout (so the
// browser scales it to fit the printable area), reset the pan/zoom state,
// hide UI chrome via @media print, and trigger window.print(). The user
// chooses "Save as PDF" in the print dialog. On afterprint we restore.
const pdfBtn = document.getElementById("export-pdf");
if (pdfBtn) {
  pdfBtn.addEventListener("click", () => {
    const W = state.vertical ? layout.totalH : layout.totalW;
    const H = state.vertical ? layout.totalW : layout.totalH;
    const saved = { tx: state.tx, ty: state.ty, scale: state.scale };
    // Show the entire tree at scale 1 inside the SVG viewBox.
    svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
    svg.setAttribute("preserveAspectRatio", "xMidYMid meet");
    state.tx = 0; state.ty = 0; state.scale = 1;
    applyTransform();

    function restore() {
      svg.removeAttribute("viewBox");
      svg.removeAttribute("preserveAspectRatio");
      state.tx = saved.tx; state.ty = saved.ty; state.scale = saved.scale;
      applyTransform();
      window.removeEventListener("afterprint", restore);
    }
    window.addEventListener("afterprint", restore);
    // Defer print() so the layout/render flush before opening the dialog.
    requestAnimationFrame(() => requestAnimationFrame(() => window.print()));
  });
}

// ───────────── Boot ─────────────
applyTheme((function(){ try { return localStorage.getItem("techtree-theme") || "renaissance"; } catch(e) { return "renaissance"; } })());
// Restore vertical preference
try {
  if (localStorage.getItem("techtree-orient") === "vertical") {
    state.vertical = true;
    document.body.classList.add("orient-vertical");
    if (orientBtn) orientBtn.textContent = "↔";
  }
} catch(e) {}
renderSidebar();
render();
renderMinimap();
})();
