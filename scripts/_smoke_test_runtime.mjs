#!/usr/bin/env node
// Browserless startup smoke test for the static application.
// Run with: node scripts/_smoke_test_runtime.mjs

import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const elements = new Map();

function makeElement(id = "") {
  return {
    id,
    children: [],
    dataset: {},
    style: { setProperty() {}, removeProperty() {} },
    attributes: {},
    innerHTML: "",
    textContent: "",
    hidden: false,
    className: "",
    parentElement: null,
    classList: {
      add() {},
      remove() {},
      contains() { return false; },
      toggle() { return false; },
    },
    setAttribute(key, value) { this.attributes[key] = String(value); },
    getAttribute(key) { return this.attributes[key] ?? null; },
    removeAttribute(key) { delete this.attributes[key]; },
    appendChild(child) {
      child.parentElement = this;
      this.children.push(child);
      return child;
    },
    remove() {},
    addEventListener() {},
    removeEventListener() {},
    querySelector(selector) { return makeElement(selector); },
    querySelectorAll() { return []; },
    getBoundingClientRect() {
      return { width: 1200, height: 800, left: 0, top: 0, right: 1200, bottom: 800 };
    },
  };
}

const document = {
  body: makeElement("body"),
  getElementById(id) {
    if (!elements.has(id)) elements.set(id, makeElement(id));
    return elements.get(id);
  },
  createElement() { return makeElement(); },
  createElementNS() { return makeElement(); },
  querySelector() { return makeElement(); },
  querySelectorAll() { return []; },
  addEventListener() {},
  removeEventListener() {},
};

const window = { addEventListener() {}, removeEventListener() {}, print() {} };
const context = vm.createContext({
  window,
  document,
  localStorage: { getItem() { return null; }, setItem() {}, removeItem() {} },
  requestAnimationFrame() {},
  setTimeout() {},
  clearTimeout() {},
  console,
});

for (const file of ["data.js", "images.js", "translations.js", "unlocks.js", "details_extra.js"]) {
  new vm.Script(fs.readFileSync(path.join(root, file), "utf8"), { filename: file }).runInContext(context);
}

const { ERAS, CATEGORIES, TECHS } = window.TECH_TREE;
const ids = new Set(TECHS.map(tech => tech.id));
for (const tech of TECHS) {
  if (!Array.isArray(tech.prereqs)) throw new Error(`${tech.id} is missing its prereqs array`);
  for (const prereq of tech.prereqs) {
    if (!ids.has(prereq)) throw new Error(`${tech.id} references unknown prerequisite ${prereq}`);
  }
}

new vm.Script(fs.readFileSync(path.join(root, "app.js"), "utf8"), { filename: "app.js" })
  .runInContext(context, { timeout: 10_000 });

if (elements.get("category-list").children.length !== Object.keys(CATEGORIES).length) {
  throw new Error("category sidebar did not render");
}
if (elements.get("era-list").children.length !== ERAS.length) {
  throw new Error("era sidebar did not render");
}
if (elements.get("nodes").children.length !== TECHS.length) {
  throw new Error("technology nodes did not render");
}

console.log(`runtime smoke test passed: ${TECHS.length} techs, ${ERAS.length} eras`);
