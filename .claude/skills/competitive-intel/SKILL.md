# competitive-intel

Benchmark competitors and uncover their strengths, positioning, and likely next moves. Second skill in the Map stage. Chains naturally from `market-mapping` — if a map was just run, don't redo the player list, go straight to depth.

Run as: `/competitive-intel [subject or specific competitor set]`

---

## Behavior

### 1. Establish the competitive frame

Define whose competition is being analyzed: Zaradigm's, a specific client's, or a named competitor's position relative to the field. If a `market-mapping` was just run this session, use its ecosystem-players output as the starting list rather than reconstructing it.

Check `wiki/index.md` first — pull `zaradigm-positioning.md`, `marketing-plan.md` (which includes a competitor list), and any client-specific articles before forming a view.

### 2. Route external research

For any competitor-specific data not in the wiki (pricing, positioning copy, recent moves, customer reviews, hiring signals, product changes): route to the researcher subagent via the Agent tool. Do not answer from training data on specific competitor details — they go stale fast, and a wrong read here can misdirect strategy.

### 3. Build the competitive picture

Assess each material competitor across:
- **Positioning:** what do they claim to be, and who are they clearly selling to?
- **Differentiation:** what is actually distinct vs. what is marketing language?
- **Pricing architecture:** publicly known price points, packaging, anchors.
- **Go-to-market motion:** how do they acquire customers — channel, content, referral, enterprise sales?
- **Recent moves:** anything material in the last 12 months — pivots, new offers, partnerships, pricing changes.
- **Likely next move:** based on trajectory and market forces, what's the most probable play?

### 4. Identify implications

After the competitor-by-competitor pass:
- Where is the field crowded (many players saying similar things)?
- Where is there daylight — genuine whitespace that's uncontested or underserved?
- Which competitor is most dangerous to the subject, and why?

### 5. Output

**Format (scannable in under five minutes):**

- **Competitive field summary:** 2–3 sentences on the overall competitive dynamic (fragmented, concentrated, commoditizing, premiumizing, etc.).
- **Top 3–4 competitors profiled:** one short block per competitor — positioning, key differentiator, go-to-market, most recent notable move.
- **Whitespace / uncontested ground:** what no one (or almost no one) is credibly occupying.
- **Biggest threat:** one competitor, one reason.
- **So what:** handoff to `strategic-options` or `customer-segmentation` — what the competitive picture implies for where to play.

### 6. Guardrails

- This skill benchmarks. It doesn't recommend what Zaradigm or a client should do — that's `strategic-options`.
- Any specific claim about a competitor's pricing, offer, or move that isn't in the wiki must come from the researcher subagent, not recalled from training data.
- Avoid false precision: "their pricing is approximately X" is better than a confident wrong number.
