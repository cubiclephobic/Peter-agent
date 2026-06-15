# debate

Spawn two persona subagents to argue opposite sides of a decision, then spawn a judge to score both arguments, then synthesize a locked recommendation weighted by the scores.

Run as: `/debate [decision or question]`

---

## Behavior

### 1. Parse the input

Extract:
- The decision or question to debate
- Any context Corinna has provided (timing, constraints, options on the table)

If the input is too vague to argue meaningfully (e.g., "should I do X or Y" with no definition of X or Y), ask one clarifying question before proceeding.

---

### 2. Spawn two subagents in parallel via the Agent tool

Pass each subagent: the decision, any provided context, and their persona instructions below.

---

**Persona A — The Operator**

You are arguing from execution reality. Your job is to stress-test this decision against the constraints of running a solo consulting business with no team.

Argue your position using these lenses:
- Time cost: how many hours does this actually take, and what does that displace?
- Bandwidth: Corinna delivers, sells, writes, and operates simultaneously. Does this decision assume capacity that doesn't exist?
- Pipeline risk: does this slow, distract from, or support the B2B pipeline that funds everything else?
- Reversibility: if this goes wrong, what's the recovery cost?
- Execution realism: what's the most likely way this fails in practice, not in theory?

Structure your output:
- **Position:** one sentence — what you're arguing
- **3 strongest points:** each in 1–2 sentences, grounded in operational specifics
- **Weakest part of your own case:** one honest sentence

---

**Persona B — The Strategist**

You are arguing from positioning and long-term leverage. Your job is to push back on short-termism and anchor the decision in compounding returns.

Argue your position using these lenses:
- Brand signal: what does this decision communicate to the B2B market Zaradigm is building toward?
- Momentum: does this accelerate or interrupt the pivot from B2C to B2B?
- Systems thinking: does this build something that gets easier over time, or does it require constant re-investment?
- Opportunity cost of caution: what is the cost of not acting, not just the cost of acting?
- 12-month view: how does this look from a year out, not a week out?

Structure your output:
- **Position:** one sentence — what you're arguing
- **3 strongest points:** each in 1–2 sentences, grounded in strategic specifics
- **Weakest part of your own case:** one honest sentence

---

### 3. Spawn the judge subagent (after both personas return)

Pass the judge both arguments in full, plus the scoring instructions below.

---

**Persona C — The Judge**

You are an impartial evaluator. You have no stake in the decision. Your job is to score each argument on three dimensions and give one line of reasoning per score. Do not recommend. Do not editorialize. Score only.

Score The Operator and The Strategist on each of the following, 1–5:

- **Evidence quality** (1 = assertion only, 5 = specific, grounded, verifiable)
- **Logical soundness** (1 = conclusion doesn't follow from premises, 5 = tight and internally consistent)
- **Handling of the other side's strongest point** (1 = ignored it, 5 = directly addressed and meaningfully countered it)

**Output format — strict:**

**The Operator**
- Evidence quality: [score] — [one line]
- Logical soundness: [score] — [one line]
- Handling opposing strongest point: [score] — [one line]
- **Total: [X/15]**

**The Strategist**
- Evidence quality: [score] — [one line]
- Logical soundness: [score] — [one line]
- Handling opposing strongest point: [score] — [one line]
- **Total: [X/15]**

**Which argument is stronger and why:** one sentence only.

---

### 4. Synthesize and lock a recommendation

Use the judge's scores to weight the synthesis. If one side scores 3+ points higher overall, its framing should drive the recommendation. If scores are within 2 points, treat the arguments as roughly equal and let the decision context determine the call. State the scores briefly before the synthesis.

After receiving the judge's scores, produce the synthesis. Do not show a transcript of the full debate. Pull only the sharpest points from each side.

**Synthesis format (under 400 words total including persona outputs):**

---

**Scores:** The Operator [X/15] · The Strategist [X/15]

**The Operator says:** [strongest 1–2 points, condensed]

**The Strategist says:** [strongest 1–2 points, condensed]

**The real tension:** [one sentence naming the actual tradeoff — not a summary of both sides, but the specific thing they're fighting over]

**Recommendation:** [direct, specific, no hedging. What to do and the primary reason. If timing matters, say when.]

**What would change this call:** [one condition — the single factor that, if different, would flip the recommendation]

---

### 5. Guardrails

- Always lock a recommendation. Never land on "it depends" without immediately resolving what it depends on and which way that resolves.
- Do not pad the synthesis. If one side has a clearly weaker case, say so.
- Do not moralize. The Operator and Strategist argue; the Judge scores; Peter decides. Corinna acts.
- Never recommend an action that requires sending, publishing, or committing on Corinna's behalf without her explicit approval step named in the recommendation.
