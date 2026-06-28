# operating-model-design

Design the operating model that makes a strategy executable — what capabilities are needed, who owns what, how decisions get made, and what the day-to-day engine actually looks like. First skill in the Execute stage.

Run as: `/operating-model-design [strategy or subject]`

---

## Behavior

### 1. Anchor to the strategy

An operating model is only meaningful relative to a strategy. Pull the chosen path from `strategic-options` if run this session. If not, establish the strategic intent in one sentence before proceeding — the model is designed to serve a specific direction, not to be generic.

### 2. Define required capabilities

What does this strategy require the business to be *distinctly good at* to win? List only the capabilities that are genuinely differentiating — not table stakes. For each, assess: does the capability currently exist, is it partially in place, or does it need to be built?

For Zaradigm specifically: capabilities map across Corinna's time (delivery, sales, content, operations), automation (HubSpot, LinkedIn sync, transcript pipeline, morning brief), and outsourced/tool-supported functions. Be specific about what's in each bucket — "automation handles X" is more useful than "streamline operations."

### 3. Map decision rights and accountability

For each key operating decision: who decides, who inputs, who executes, who is informed? For a solo operator, most of these collapse to Corinna — but the exercise still surfaces where decisions are implicit (and therefore inconsistent) vs. explicit. Flag any decisions that should be systematized or automated rather than made case-by-case.

### 4. Identify operating gaps

Where does the current operating model not support the strategy? Look for:
- **Capability gaps:** required but not yet built.
- **Decision bottlenecks:** things that only Corinna can unblock, that are creating delay or inconsistency.
- **Automation candidates:** repeated manual decisions or tasks that could be systematized — flag these explicitly per CLAUDE.md (if Corinna is doing the same manual task twice, name the automation opportunity).

### 5. Output

**Format (scannable in under five minutes):**

- **Strategy being served:** one line.
- **Required capabilities:** what this strategy needs to work — existing, partial, missing.
- **Operating model sketch:** who/what does what — Corinna's time, automation, tools, outsourced. Keep it concrete.
- **Decision rights:** 2–3 key decisions, made explicit — who owns them, any that should be systematized.
- **Operating gaps:** what needs to be built or fixed for the model to actually support the strategy.
- **So what:** handoff to `initiative-prioritizer` (sequence the gap-closing work) or `transformation-roadmap` (phase it over time).

### 6. Guardrails

- This skill designs the model. It doesn't build the automations or write the SOPs — those are downstream execution tasks.
- For Zaradigm, never design an operating model that assumes a team exists. Design for a solo operator plus tools and automation — no ghost headcount.
- Flag automation candidates clearly. Don't bury them in the operating model as assumed capability.
