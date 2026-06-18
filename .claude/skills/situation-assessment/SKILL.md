# situation-assessment

Diagnose the real current state of a business, client account, or initiative: performance against goals, what's actually moving versus stuck, and the market/competitive backdrop driving it. First step in the Diagnose stage of the consulting OS (Diagnose → Map → Choose → Execute → Govern → Communicate).

Run as: `/situation-assessment [subject]` — subject can be Zaradigm itself, a named client/account, or a specific initiative.

---

## Behavior

### 1. Scope the subject

If the subject is ambiguous (no name, no time window), ask one clarifying question: what's being assessed, and over what period. Don't ask anything else — infer reasonable defaults (e.g., trailing 90 days) and state the assumption.

### 2. Pull real signal, not stated belief

Before writing anything, gather what's actually available:
- If it's a HubSpot-tracked account: pull deal stage, `notes_last_contacted`, recent activity — not `hs_lastmodifieddate` or open rates.
- If it's Zaradigm overall: pull pipeline state, revenue against the $5K–$15K/month target, content cadence.
- If relevant wiki pages exist (check `wiki/index.md` first), read them before forming a view. Never start from a blank slate if context already exists.
- Do not fabricate data. If a number isn't available, say "not available" rather than estimating it silently.

### 3. Separate performance from narrative

Write down what's measurably true (numbers, dates, stages) separately from what's *believed* to be true (assumptions, stated reasons, plans). The two get reconciled in step 4 — don't blend them while gathering.

### 4. Produce the assessment

**Output format (scannable in under five minutes):**

- **Current state:** 2–4 bullets, numbers where available, dated.
- **What's moving / what's stuck:** the actual delta versus the prior period or stated goal — not a status report, the *change*.
- **Context that explains it:** market, competitive, seasonal, or operational factors actually driving the numbers — not generic commentary.
- **So what:** one or two sentences naming the real issue this assessment points to. This is the handoff to `growth-barriers` or `assumption-audit` — not a recommendation yet.

### 5. Guardrails

- This skill diagnoses. It does not recommend a strategy — that's `strategic-options`. Stop at "so what."
- Never reduce a client relationship to a pipeline stage in the writeup — keep relationship context (per CLAUDE.md) even when citing CRM data.
- If the data needed lives in HubSpot/Calendar/Gmail and isn't available in this session, say so explicitly rather than guessing.
