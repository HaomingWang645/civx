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

// ───────────── Layout: assign each tech an (eraIdx, rowIdx) ─────────────
function layoutTechs() {
  const eraIdx = Object.fromEntries(ERAS.map((e, i) => [e.id, i]));
  const techById = Object.fromEntries(TECHS.map(t => [t.id, t]));

  // Group techs by era
  const byEra = ERAS.map(() => []);
  for (const t of TECHS) byEra[eraIdx[t.era]].push(t);

  // Within an era, sort by category then by name for deterministic layout,
  // but reorder iteratively to minimize crossings with the previous era.
  const catOrder = Object.keys(CATEGORIES);
  for (const list of byEra) {
    list.sort((a, b) => {
      const c = catOrder.indexOf(a.category) - catOrder.indexOf(b.category);
      return c !== 0 ? c : a.name.localeCompare(b.name);
    });
  }

  // Crossing-reduction: barycenter heuristic over a few sweeps.
  const positions = {}; // id -> rowIdx
  byEra.forEach((list, ei) => list.forEach((t, ri) => positions[t.id] = ri));

  for (let sweep = 0; sweep < 4; sweep++) {
    for (let ei = 1; ei < byEra.length; ei++) {
      const list = byEra[ei];
      list.sort((a, b) => {
        const aBary = barycenter(a, positions, techById);
        const bBary = barycenter(b, positions, techById);
        if (aBary !== bBary) return aBary - bBary;
        return catOrder.indexOf(a.category) - catOrder.indexOf(b.category);
      });
      list.forEach((t, ri) => positions[t.id] = ri);
    }
  }

  // Compute pixel positions
  const placed = {};
  byEra.forEach((list, ei) => {
    list.forEach((t, ri) => {
      placed[t.id] = {
        ...t,
        col: ei,
        row: ri,
        x: PADDING_X + ei * COL_WIDTH,
        y: PADDING_Y + ri * ROW_HEIGHT,
      };
    });
  });

  const maxRow = Math.max(...byEra.map(l => l.length));
  const totalW = PADDING_X * 2 + ERAS.length * COL_WIDTH;
  const totalH = PADDING_Y + maxRow * ROW_HEIGHT + 80;

  return { placed, byEra, totalW, totalH };
}

function barycenter(tech, positions, techById) {
  const prereqRows = tech.prereqs
    .map(id => positions[id])
    .filter(r => r !== undefined);
  if (prereqRows.length === 0) return positions[tech.id] ?? 0;
  return prereqRows.reduce((a, b) => a + b, 0) / prereqRows.length;
}

const layout = layoutTechs();

// ───────────── State ─────────────
const state = {
  selectedId: null,
  hoveredId: null,
  mutedCategories: new Set(),
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
    const x = PADDING_X + i * COL_WIDTH - 20;
    const w = COL_WIDTH;

    const band = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    band.setAttribute("class", "era-band");
    band.setAttribute("x", x);
    band.setAttribute("y", 30);
    band.setAttribute("width", w);
    band.setAttribute("height", layout.totalH - 30);
    eraGroup.appendChild(band);

    const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
    label.setAttribute("class", "era-label");
    label.setAttribute("x", x + w / 2);
    label.setAttribute("y", 56);
    label.setAttribute("text-anchor", "middle");
    label.textContent = era.name;
    eraGroup.appendChild(label);

    const range = document.createElementNS("http://www.w3.org/2000/svg", "text");
    range.setAttribute("class", "era-range-label");
    range.setAttribute("x", x + w / 2);
    range.setAttribute("y", 72);
    range.setAttribute("text-anchor", "middle");
    range.textContent = era.range;
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
    g.setAttribute("class", "node");
    g.setAttribute("transform", `translate(${p.x}, ${p.y})`);
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

  // Set viewBox to fit content with margin
  svg.setAttribute("viewBox", `0 0 ${layout.totalW} ${layout.totalH}`);
  fitToView();
  applyHighlights();
}

function edgePath(a, b) {
  const x1 = a.x + NODE_W;
  const y1 = a.y + NODE_H / 2;
  const x2 = b.x;
  const y2 = b.y + NODE_H / 2;
  const mx = (x1 + x2) / 2;
  return `M ${x1},${y1} C ${mx},${y1} ${mx},${y2} ${x2},${y2}`;
}

// ───────────── Highlights ─────────────
function applyHighlights() {
  const focusId = state.selectedId || state.hoveredId;
  const muted = state.mutedCategories;
  const search = state.search.trim().toLowerCase();

  const ancestors = new Set();
  const descendants = new Set();
  if (focusId) {
    collect(focusId, ancestors, "up");
    collect(focusId, descendants, "down");
  }

  // Nodes
  document.querySelectorAll(".node").forEach(n => {
    const id = n.dataset.id;
    const tech = techById[id];
    const isMuted = muted.has(tech.category);
    const matchesSearch = !search || tech.name.toLowerCase().includes(search);
    const inFocus = !focusId || id === focusId || ancestors.has(id) || descendants.has(id);
    n.classList.toggle("selected", id === state.selectedId);
    n.classList.toggle("dimmed", isMuted || !inFocus || !matchesSearch);
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
    const isMuted = muted.has(fromTech.category) || muted.has(toTech.category);
    e.classList.toggle("highlighted", !!focusId && inFocus);
    e.classList.toggle("dimmed", isMuted || (!!focusId && !inFocus));
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
    <div class="detail-title">${t.name}</div>
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
  detailEl.querySelector(".detail-close").onclick = clearSelection;
  detailEl.querySelectorAll(".detail-link").forEach(el => {
    el.onclick = () => selectNode(el.dataset.id);
  });
}

// ───────────── Pan / Zoom ─────────────
function applyTransform() {
  viewport.setAttribute("transform", `translate(${state.tx}, ${state.ty}) scale(${state.scale})`);
  zoomLevelEl.textContent = `${Math.round(state.scale * 100)}%`;
}

function fitToView() {
  const rect = svg.getBoundingClientRect();
  const scaleX = rect.width / layout.totalW;
  const scaleY = rect.height / layout.totalH;
  state.scale = Math.min(scaleX, scaleY, 1) * 0.95;
  state.tx = (rect.width - layout.totalW * state.scale) / 2;
  state.ty = (rect.height - layout.totalH * state.scale) / 2;
  applyTransform();
}

let isPanning = false;
let panStart = null;
svg.addEventListener("mousedown", (e) => {
  if (e.target.closest(".node")) return;
  isPanning = true;
  panStart = { x: e.clientX - state.tx, y: e.clientY - state.ty };
  svg.classList.add("dragging");
});
window.addEventListener("mousemove", (e) => {
  if (!isPanning) return;
  state.tx = e.clientX - panStart.x;
  state.ty = e.clientY - panStart.y;
  applyTransform();
});
window.addEventListener("mouseup", () => {
  isPanning = false;
  svg.classList.remove("dragging");
});

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
function renderSidebar() {
  const catList = document.getElementById("category-list");
  catList.innerHTML = "";
  Object.entries(CATEGORIES).forEach(([id, cat]) => {
    const el = document.createElement("div");
    el.className = "legend-item";
    el.innerHTML = `
      <span class="legend-swatch" style="color: ${cat.color}; background: ${cat.color}"></span>
      <span>${cat.name}</span>
    `;
    el.onclick = () => {
      if (state.mutedCategories.has(id)) state.mutedCategories.delete(id);
      else state.mutedCategories.add(id);
      el.classList.toggle("muted", state.mutedCategories.has(id));
      applyHighlights();
    };
    catList.appendChild(el);
  });

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
  const rect = svg.getBoundingClientRect();
  const targetX = PADDING_X + i * COL_WIDTH + COL_WIDTH / 2;
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
});

window.addEventListener("resize", () => fitToView());

// ───────────── Boot ─────────────
renderSidebar();
render();
})();
