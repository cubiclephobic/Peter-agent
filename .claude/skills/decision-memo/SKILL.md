# decision-memo

Produce a clear, concise decision memo — one page maximum — that gives a senior decision-maker everything they need to act: the situation, the recommendation, the rationale, the risks, and the ask. Third skill in the Communicate stage.

Run as: `/decision-memo [decision or recommendation]`

---

## Behavior

### 1. Establish the decision and the decision-maker

What decision needs to be made, by whom, and by when? A memo that isn't tied to a specific decision and decision-maker will be vague. Pull from `stakeholder-alignment` if available — the decision-maker's alignment gap shapes how the memo is framed.

### 2. Structure using SCQA

McKinsey memos follow a four-part logic: **Situation → Complication → Question → Answer.**

- **Situation:** what is true right now that the reader already agrees with? (Don't argue with them here — establish shared ground.)
- **Complication:** what has changed, or what tension exists, that means the current situation is no longer acceptable? This is the "so what" that creates urgency.
- **Question:** the decision the complication creates — implied or explicit.
- **Answer:** the recommendation, stated directly. This is the Pyramid Principle: the answer comes immediately, not at the end.

### 3. Build the support

After the SCQA frame, provide:
- **Rationale:** the 2–3 strongest reasons the recommendation is right. Not an exhaustive list — the strongest ones only.
- **Risks and mitigations:** name the most material risk and what's been done to reduce it. Don't hide risk — a decision-maker who discovers an unmentioned risk later loses trust in the analysis.
- **The ask:** what specifically does the reader need to do, decide, or approve? Be precise — "your approval to proceed" vs. "a 30-minute meeting to discuss" vs. "a budget commitment of $X."

### 4. Apply the one-page rule

A decision memo is one page. If the material doesn't fit, the analysis hasn't been synthesized enough — compress, don't expand. Supporting detail goes in an appendix that the reader can pull if they want it; the memo itself contains only what's needed to make the decision.

### 5. Hand off to draft-writer

Once the SCQA structure and content are locked, pass to `/draft-writer` for prose, then `/personal-tone` to apply Zaradigm voice, then `/qa-check` for final review. The decision-memo skill produces the structure and content; the downstream skills produce the language.

### 6. Output

**Format:**

- **Decision and decision-maker:** one line each.
- **SCQA structure:** each element in 1–3 sentences.
- **Rationale (2–3 points):** the strongest support for the recommendation.
- **Top risk and mitigation:** one each.
- **The ask:** specific, actionable, clear.
- **Ready for draft-writer:** structure and content locked so the next skill can produce the final memo without re-deriving the logic.

### 7. Guardrails

- One page. Not one page plus context. One page.
- The answer goes in the Answer section of SCQA — not at the end after the rationale. Answer first.
- Apply Zaradigm voice rules: no em-dashes, no banned words, direct language. (Voice application is `/personal-tone`'s job, but flag obvious violations at structure stage.)
- Never send a decision memo on Corinna's behalf. This skill produces a draft for her review. Always.
