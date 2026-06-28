# profit-pool-analysis

Find where profit actually concentrates in a value chain — who is capturing it, who is being squeezed, and where structural advantage is available. Fourth skill in the Map stage. Often most useful after `market-mapping` has established the value chain.

Run as: `/profit-pool-analysis [market or subject]`

---

## Behavior

### 1. Establish the value chain

If a `market-mapping` was run this session, use its value chain output directly. Otherwise, sketch the chain quickly: who are the key actors from raw input to end customer, and what role does each play?

### 2. Locate the profit pools

For each actor or layer in the value chain, assess:
- **Revenue concentration:** who commands the most revenue at their layer?
- **Margin concentration:** revenue isn't the same as profit — where are margins high, and where are they thin despite high volume?
- **Bargaining power:** who can raise prices without losing customers? Who gets squeezed when costs rise?
- **Switching cost:** who benefits from lock-in, and who is one commodity swap away from being displaced?

For any market-level margin data not in the wiki: route to the researcher subagent. Do not estimate margins from training data.

### 3. Identify capture opportunities

Where is profit available but not yet captured by the subject? Look for:
- **Under-monetized steps:** parts of the value chain where the subject already operates but captures less margin than the structural position would support.
- **Adjacencies:** neighboring steps in the chain where entry would be low-friction and margin is higher.
- **Extraction risks:** where is current margin at risk from structural shifts (platformization, commoditization, new entrants)?

For Zaradigm specifically: check `wiki/articles/services/` to understand current offer positioning across the value chain before identifying gaps.

### 4. Output

**Format (scannable in under five minutes):**

- **Where profit pools:** 2–3 bullets on which actors/layers in the value chain hold the margin and why.
- **Where margin is thin or under structural pressure:** 2–3 bullets on the squeeze points.
- **Capture opportunities for the subject:** the 1–2 most credible places where the subject could shift to higher-margin positioning.
- **Extraction risks:** what's threatening current margin, and how fast is that threat moving?
- **So what:** handoff to `strategic-options` — what the profit pool picture implies for where to compete and at what price.

### 5. Guardrails

- This skill surfaces where value accrues structurally. It doesn't design the move to capture it — that's `strategic-options`.
- Margin and revenue estimates must come from real sources (wiki, HubSpot, researcher subagent). Never synthesize a margin figure from inference when the actual number is checkable.
- For Zaradigm, distinguish between Zaradigm revenue (B2B) and Coachilly (B2C winding down) — they are different positions in their respective value chains and should never be blended in the analysis.
