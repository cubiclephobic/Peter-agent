Source: AI Builder Course + interview 2026-06-02

# AI Terminology Reference

A quick-reference glossary for terms that come up in Corinna's AI work — courses, tool-building, prompt engineering, and working with Claude.

---

## Temperature

A setting (typically 0–2) that controls how random or creative an AI model's output is.

- **Low (0–0.3):** Consistent, predictable, focused. Use for structured outputs: SOPs, summaries, data extraction.
- **Medium (0.5–0.8):** Balanced. Good for most content drafts.
- **High (1–2):** More creative, varied, sometimes surprising. Use for brainstorming, headlines, first-draft hooks.

**In practice:** When content feels too mechanical, raise temperature. When it goes off the rails, lower it.

---

## Prompt

The instruction or input you give an AI model. Quality of output is directly tied to quality of prompt.

**In practice:** A prompt is not just a question — it includes context, role, format instructions, constraints, and examples. The more specific, the better.

---

## System Prompt

A behind-the-scenes instruction given to a model before the conversation starts. Sets the persona, rules, tone, and scope for all subsequent responses.

**In practice:** Corinna's CLAUDE.md files function as system prompts — they tell Claude who she is, what she's working on, and how to behave before any task starts.

---

## Context Window

The amount of text a model can "see" at one time — including the conversation history, system prompt, and any files loaded. Once exceeded, the model loses access to earlier content.

**In practice:** Long sessions drift. The wiki solves this by externalizing memory — Claude reads the wiki rather than relying on context window history.

---

## Eval (Evaluation)

A test or benchmark used to measure how well a model or prompt performs on a specific task. Evals can be automated (code checks output) or manual (human rates quality).

**In practice:** When building automations, an eval answers "is this output actually good?" before shipping it. E.g., does the post-session summary capture the key insight, or is it generic?

---

## RAG (Retrieval-Augmented Generation)

A technique where relevant documents or data are retrieved and injected into the prompt before the model generates a response. Lets the model answer from your specific knowledge base rather than just training data.

**In practice:** This wiki is the foundation of a RAG system. When Claude reads specific wiki articles before responding, that's RAG in action — without the infrastructure overhead.

---

## Agent / Agentic AI

An AI system that can take sequences of actions — using tools, making decisions, calling APIs — to complete a multi-step task autonomously, not just generate a single response.

**In practice:** Claude Code runs in agent mode. The /wrap skill, note alias, and n8n workflows are all forms of agentic behavior — Claude or a system acting on Corinna's behalf without step-by-step instruction.

---

## Hook (Claude Code)

A script that fires automatically at specific points in a Claude Code session — before/after tool use, on session start, or on session stop. Used to automate actions like wiki updates without requiring a manual trigger.

**In practice:** A Stop hook would fire when a Claude Code session ends and automatically run the wiki update process.

---

## MCP (Model Context Protocol)

A standard that lets Claude connect to external tools and services — HubSpot, Gmail, Google Drive, Slack, etc. — so it can read and write data in those systems during a session.

**In practice:** All of Corinna's integrations (HubSpot, Drive, Gmail, Calendar, Krisp, Canva, etc.) are connected via MCP. This is what makes cross-system automation possible without custom API code.

---

## n8n

An open-source workflow automation tool (self-hostable). Connects apps and services via visual workflows triggered by schedules, webhooks, or events.

**In practice:** Corinna's VPS runs n8n. The planned daily wiki update workflow will run here — pulling from Krisp, HubSpot, Drive, and raw/ to update wiki articles overnight.

---

## Compounding Artifact

A document or system that gets more valuable over time as it accumulates context — because each addition builds on what's already there rather than starting fresh.

**In practice:** This wiki is a compounding artifact. Each session that updates it makes future sessions faster and more accurate. Coined/popularized by Andrej Karpathy in the context of LLM wikis.

---

## CSS (Current State Summary)

Corinna's term for a structured context document maintained per project or client — used to resume AI sessions without re-explaining background. The wiki replaces and consolidates these.

**In practice:** All CSS documents from `/AI CONTEXT` in Google Drive have been migrated into this wiki as of 2026-06-02.

---

## Related

- [[hubspot]] — connected via MCP
- [[zaradigm]] — AI tools used in all Zaradigm content production
- [[coachilly-mag]] — AI tools used in all CMAG content production
- [[ai-practice-labs]] — an AI-powered product Zaradigm delivers to clients
