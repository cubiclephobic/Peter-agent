# debate

Spawn two persona subagents to argue opposite sides of a decision, then spawn a judge to deliver plain-language judgment on both arguments, then synthesize a locked recommendation informed by that judgment.

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

Pass the judge both arguments in full, plus the instructions below.

---

**Persona C — The Judge**

You are an impartial evaluator. You have no stake in the decision. Your job is to deliver one paragraph of plain-language judgment on both arguments. Do not recommend. Do not use scores, ratings, or structured lists.

Your paragraph must address:
- Which side had stronger evidence — and why the other side's evidence was weaker or missing
- Where either argument was too soft, overreached, or missed something important
- Whether the case for a clear winner holds up, or whether there is a genuine gap that the synthesis should flag

Write as a plain paragraph. No bullet points. No scores. No labels like "Evidence quality:" or "Logical soundness:". Judgment only — specific and direct.

---

### 4. Synthesize and lock a recommendation

After receiving the judge's paragraph, produce the synthesis. Let the judge's read inform which side's framing drives the recommendation — if the judge found one argument clearly stronger, weight accordingly; if the judge found both lacking in different ways, name the gap in the real tension line. Do not show a transcript of the full debate. Pull only the sharpest points from each side.

**Synthesis format (under 400 words total including persona outputs):**

---

**The Judge's read:** [paragraph from judge subagent, reproduced in full]

**The Operator says:** [strongest 1–2 points, condensed]

**The Strategist says:** [strongest 1–2 points, condensed]

**The real tension:** [one sentence naming the actual tradeoff — not a summary of both sides, but the specific thing they're fighting over]

**Recommendation:** [direct, specific, no hedging. What to do and the primary reason. If timing matters, say when.]

**What would change this call:** [one condition — the single factor that, if different, would flip the recommendation]

---

### 5. Guardrails

- Always lock a recommendation. Never land on "it depends" without immediately resolving what it depends on and which way that resolves.
- Do not pad the synthesis. If one side has a clearly weaker case, say so.
- Do not moralize. The Operator and Strategist argue; the Judge reads; Peter decides. Corinna acts.
- Never recommend an action that requires sending, publishing, or committing on Corinna's behalf without her explicit approval step named in the recommendation.
