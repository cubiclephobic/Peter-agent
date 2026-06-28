# market-mapping

Map the market landscape and ecosystem for a business, category, or client — who the players are, where value flows, how the market is growing, and where structural shifts are underway. First skill in the Map stage of the consulting OS (Diagnose → Map → Choose → Execute → Govern → Communicate).

Run as: `/market-mapping [market or subject]`

---

## Behavior

### 1. Scope the market

Clarify what market is being mapped: is this Zaradigm's own market (B2B leadership development, executive coaching, AI-assisted coaching), a specific segment of it, or a client's market? If ambiguous, name the assumption and proceed — don't ask unless the ambiguity would produce materially different output.

### 2. Check what's already known

Before calling on external knowledge:
- Check `wiki/index.md` and pull relevant articles (start with `zaradigm.md`, `zaradigm-positioning.md`, `marketing-plan.md`, or client-specific files if this is a client's market).
- Use any `situation-assessment` or `growth-barriers` output from this session as context.

For any market dynamics, competitor moves, industry trends, or sizing data not in the wiki: route to the researcher subagent via the Agent tool. Do not answer from training data on external market facts — route first.

### 3. Map the landscape

Produce the market map across four layers:

- **Market size and trajectory:** TAM / SAM / addressable niche — numbers where available, order-of-magnitude estimates where not. Growth direction and primary drivers (expanding, contracting, fragmenting, consolidating).
- **Value chain:** Who does what — creators, distributors, platforms, buyers, enablers. Where does money enter and where does it accumulate?
- **Ecosystem players:** Categorize by role — direct competitors, adjacent players, substitutes, potential disruptors, complementary services. Name real companies, not generic buckets.
- **Structural forces:** What's changing and why — technology shifts, buyer behavior changes, regulatory moves, platform dynamics. Flag what's directional (slow-moving) vs. what's a current event (fast-moving).

### 4. Output

**Format (scannable in under five minutes):**

- **Market size and trajectory:** 2–3 bullets with numbers and direction.
- **Value chain snapshot:** one short paragraph — where value is created and where it accrues.
- **Key players by role:** a short table or grouped list — don't pad; only name players material to the subject.
- **Structural forces to watch:** 2–3 bullets on what's actually changing.
- **So what:** one or two sentences — what the market map implies for the subject's positioning or strategic choices. Handoff to `competitive-intel` or `customer-segmentation`.

### 5. Guardrails

- This skill maps. It does not recommend positioning or strategy — that's `strategic-options`.
- Do not answer market-sizing or competitive-dynamics questions from training-data recall. External knowledge goes through the researcher subagent.
- If hard numbers aren't available, say so and use directional language. Never invent a figure.
