// Extended notes shown in the detail-extra side panel (toggled with the ‹ handle).
// Each value is HTML rendered into #detail-extra.innerHTML when the user opens
// the detail panel for that tech and clicks the expand button.
//
// If a tech has no entry here, the expand button is hidden for that tech.

window.TECH_DETAIL_EXTRA = {

  "trans-computable-mathematics": `
    <h3 class="extra-title">Trans-Computable Mathematics</h3>
    <p class="extra-lede">Mathematics that takes provably uncomputable objects as concrete working material rather than abstract existence claims.</p>

    <h4>The pre-history of the uncomputable</h4>
    <p>Hilbert's 1928 <em>Entscheidungsproblem</em> asked whether there is a single mechanical procedure that, given any first-order statement, decides if it is provable. Church (1936, λ-calculus) and Turing (1936, the universal machine) independently answered no — and in doing so identified an entire ladder of problems that no algorithm can solve. Turing's halting problem occupies the bottom rung. Above it, Post and Kleene built the <em>arithmetical hierarchy</em> Σⁿ / Πⁿ, in which each level is harder than the one below in a precise quantifier-alternation sense; above that, the analytical hierarchy Σ¹ₙ / Π¹ₙ measured by quantification over functions; above that, the projective hierarchy and beyond. Classical 20th-century computability theory mapped this terrain in extraordinary detail, but its objects remained referential: mathematicians proved that an uncomputable real <em>exists</em>, but no one had a way to write down its bits.</p>

    <h4>What hypercomputation changes</h4>
    <p>The key prerequisite is engineered <em>hypercomputation</em> — physical machinery that can evaluate halting-problem instances in finite proper time, whether through Malament–Hogarth spacetimes near rotating black holes (Hogarth 1992), Zeno-style infinite-acceleration computers, exotic quantum-gravity constructions, or some not-yet-named successor. The mechanism does not matter for the mathematical consequences. Once the hardware exists, every Δ⁰₂ predicate becomes effectively decidable, every Σ⁰₁ set explicitly enumerable, and the arithmetical hierarchy <em>collapses</em> below the new computational horizon: questions that were uncomputable for any Turing machine become routine queries.</p>

    <h4>Working objects, not theorems</h4>
    <p>Three families of objects move from the abstract into daily research practice:</p>
    <ul>
      <li><strong>Busy-Beaver values</strong>. The function BB(n) — the maximum number of steps a halting n-state Turing machine can make before stopping — grows faster than any computable function; BB(7) is already independent of ZFC. Trans-computable mathematics computes BB(n) for arbitrary <em>n</em> on demand and uses these values directly in proofs about complexity, randomness, and the structure of independence.</li>
      <li><strong>Chaitin's Ω</strong>. Ω, the halting probability of a universal prefix-free machine, is a specific real number whose digits are algorithmically random and whose first few thousand bits encode the answers to every well-formed mathematical question of bounded length. Earlier work proved Ω was incompressible; trans-computable engineering produces it to specified precision, turning Ω into a queryable oracle for open conjectures.</li>
      <li><strong>Π¹ₙ-complete sets</strong>. The complete sets of the analytical hierarchy can be exhibited explicitly and reasoned about by direct inspection, not by reduction arguments alone.</li>
    </ul>

    <h4>What stays hard</h4>
    <p>Hypercomputation does not abolish difficulty — it relocates it. A Malament–Hogarth machine can decide any Σ⁰₁ predicate but is silenced by Σ¹₁ questions about higher-order quantification; the arithmetical hierarchy collapses, but the analytical and projective hierarchies stand undisturbed above it. New "uncomputable" objects emerge: Δ¹ⱼ-complete sets relative to the new oracle, the structure of the constructible universe L at uncountable ordinals, the behavior of indescribable and ineffable large cardinals, the ω₁-Turing degrees. Each new tier of physical computation exposes a higher tier of mathematical limitation. The <em>shape</em> of mathematical difficulty turns out to be invariant under any specific advance in physics.</p>

    <h4>Consequences</h4>
    <p>The Riemann hypothesis, P vs NP, and similar bounded-arithmetic conjectures are settled within the first decade of trans-computable practice — most affirmatively, a few negatively, none surprisingly. The Goldbach conjecture and the twin-prime conjecture fall to direct verification of their respective Π⁰₂ statements. Independence results take on a new flavor: rather than proving "X is unprovable in ZFC," mathematicians can directly compute whether X is true in V and then quantify the gap between provability and truth. Algorithmic randomness theory, previously a relatively small subfield, becomes a central organizing framework because Ω (now concrete) is its central object.</p>

    <h4>Philosophical fallout</h4>
    <p>Three pre-existing positions become operationally testable. <em>Mathematical realism</em> (Platonism) is vindicated to the extent that hypercomputational queries return determinate answers — there is, in some sense, a "fact of the matter" about Ω's bits that a physical device can probe. <em>Mathematical empiricism</em> (Lakatos, Kitcher) gains a new case study: large parts of mathematical knowledge now have an experimental rather than purely deductive epistemology. <em>Constructivism</em> (Brouwer's intuitionism, Bishop's analysis) is partially absorbed: many objects previously rejected as non-constructive are now constructed, just by physical rather than syntactic means. The boundary between mathematics and physics, never as crisp as either side claimed, becomes a working interface.</p>

    <h4>Open as of the late 26th century</h4>
    <ul>
      <li>Whether trans-computable mathematics admits a self-referential foundational theory analogous to the role of ZFC for classical mathematics — a "ZFC + Ω" that captures its own oracle calls.</li>
      <li>Whether the analytical-hierarchy questions exposed at the new horizon admit a second tier of physical access (e.g., via deeper quantum-gravity machines) or are permanently transcendent.</li>
      <li>The status of the continuum hypothesis once direct computation in V is available: does CH have a determinate truth value, and if so, which?</li>
      <li>The right ethics of using hypercomputational oracles in proofs intended to be checkable by ordinary mathematicians who lack the hardware.</li>
    </ul>
  `,

};
