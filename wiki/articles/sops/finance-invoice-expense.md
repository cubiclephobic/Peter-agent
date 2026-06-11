Source: Google Drive — "CSS_Finance" (migrated 2026-06-02) + session 2026-06-05

# Invoice & Expense Processing

**Category:** SOPs
**Last Updated:** June 5, 2026
**Status:** Semi-automated (Phase 1/Phase 2 split recommended — not yet built)

---

## What This Is

Weekly expense reconciliation workflow. Runs every Friday. Claude searches Gmail for receipts, cross-references the expense folder, and updates the Financial Performance Dashboard spreadsheet.

---

## Current Process

**To start a new automation run:** prompt `reconcile receipts`

**Scheduled task:** `receipt-email-finder` — currently manual-triggered; scheduled task exists but requires Corinna present throughout due to mid-workflow PDF-saving step.

### Step 1 — Gmail Search
- Claude searches Gmail for `receipt OR invoice OR payment OR subscription OR order OR charge newer_than:7d`
- Cross-references against expense folder (`/01_Z/02_FINANCE/❇️ 2026_Taxes/1_Expense & Refund Receipts/`)
- Presents copy-ready filenames for missing PDFs

### Step 2 — PDF Saving (Manual — Corinna required)
- **Type A (has attachment):** Vendors like Anthropic, Google Workspace send PDF invoices as email attachments. Currently saved via Cmd+P. *Could be auto-downloaded via Gmail MCP — not yet built.*
- **Type B (no attachment):** Print-to-PDF via Cmd+P in Gmail. Cannot be automated — requires native OS dialog.
- Naming convention: `YY-MM-DD Vendor Name.pdf`

### Step 3 — Validation + Reconciliation
- Claude validates all filenames against convention
- Reads Financial Performance Dashboard (Google Sheets ID: `1h-U7kF5TCyRaxA9kUmLvJookFtR_DY_nm6W6MejACXA`, gid: `291086194`)
- Writes missing expense entries using ClipboardEvent paste method
- ⚠️ Known issue: gviz range API has inconsistent row-number offsets when fetching sub-ranges. Always verify with same range after writing.

---

## Expense Folder
- Path: `/Users/corinnas/Library/Mobile Documents/com~apple~CloudDocs/01_Z/02_FINANCE/❇️ 2026_Taxes/1_Expense & Refund Receipts/`
- Healthcare receipts (BSW, BCBS) tracked separately under `3/✚ Health` Gmail label — never flag as missing business expenses

---

## Spreadsheet Structure (Financial Performance Dashboard)
- Sheet: `291086194` (main transactions tab)
- Months are stacked vertically; each has: header row, income rows (cols A–E), expense rows (cols G–K)
- June 2026 section: starts at ~row 157; expenses in col G (description), H (amount), I (day of month)
- **Note:** Use `range=G156:I185` style fetches starting from section header row for reliable row numbers

---

## Bank Sources (Not Yet Reconciled — Parked)
- Amex Checking — income + some expenses; limited detail
- Amex CC — nearly all business expenses
- PayPal — some income + contractor payments; has detail Amex lacks
- Stripe — most income; monthly CSV reports downloaded manually
- QBO — some invoicing income
- HubSpot — connected to Stripe; deal + contact context
- **Ultimate goal:** Reconcile spreadsheet + QBO against actual bank activity. Not active — park until Phase 1/2 split is running.

---

## Recommended Next Build: Phase 1/2 Split
- **Phase 1 (auto, 11:30am Friday):** Gmail search → write report to expense folder → stop
- **Phase 2 (Corinna-triggered):** Filename validation + spreadsheet reconciliation
- Reduces Corinna's required time from ~45 min (present throughout) to ~10 min (focused PDF-saving only)
- **Medium-term:** Add Gmail attachment auto-download for Type A receipts (Anthropic, Google Workspace) — eliminates most Cmd+P work

---

## USVA Project — Key Decisions & Options

*Note: This document also contains the USVA project scoping summary, captured below.*

### Who's Involved

| Person | Role |
|--------|------|
| Corinna | Lead — strategic content, brand voice, enrollment messaging |
| Erik | Referral partner; quoted USVA at $2,500 |
| Suhan | Web developer (full build, Phase 2) |
| DeeEtte | USVA internal stakeholder |
| USVA Partners (3) | Client — older, well-funded, August cohort deadline |

---

### Current Status

- Initial scoping call scheduled: **February 20, 2026**
- MVP and brand work pending call outcomes
- Retainer scope and pricing TBD post-call
- August cohort = hard deadline

---

### Decisions Made (Locked In)

| Decision | What | Why |
|----------|------|-----|
| Engagement model | DFY Retainer (not AI system setup) | USVA is older, well-funded, wants minimal friction |
| Website Phase 1 | Fast MVP on Hostinger Horizon, then hand off to Suhan | Meets April deadline; avoids bottleneck |
| Design direction | Modern/clean similar to Sora Schools | Contemporary, trustworthy, parent-focused |
| Logo | Propose simpler alternative to current (too busy/outdated) | Better scalability across state pages and marketing |
| Multi-state architecture | Systematic, templated approach | Scalable without rebuilding from scratch per state |

---

### Options Proposed (Awaiting Confirmation)

**Brand Kit Development**
- Price: $1,000–$1,500
- Includes: Color, typography, logo system, voice guidelines, messaging frameworks, living document
- Timeline: Parallel to MVP build
- Status: Proposed; pending USVA confirmation

**Content + SEO Retainer**
- Option A (Full Service): $2,500–$3,500/month — content calendar, SEO, email sequences, ad copy, ongoing consultation
- Option B (Lighter Touch): Fewer pieces/month, quarterly updates, lower fee (TBD)
- Status: Scope and pricing TBD Thursday

---

### Pricing Structure

| Phase | Item | Price | Status |
|-------|------|-------|--------|
| 1 | MVP Landing Page | $1,800–$2,000 | Approved |
| 1b | Brand Kit | $1,000–$1,500 | Pending USVA |
| 2 | Content + SEO Retainer | $2,500–$3,500/mo | Pending USVA |
| — | AI System Setup | $2,500–$4,500 | Rejected |
| — | Multi-page build | $25,000+ | TBD |

**Total Potential Revenue (through June):** $10,300–$14,000

---

### Timeline

| When | What | Who |
|------|------|-----|
| Feb 20 | Initial scoping call | Corinna, Erik, USVA partners |
| Feb 20 – March | MVP build, brand kit, content strategy framework | Corinna |
| April 1 | MVP live + brand kit finalized | Corinna + Suhan |
| April | Suhan's full build live | Suhan |
| May – June | Retainer content work + state-specific scaling | Corinna |
| August | First cohort begins | USVA |

---

### Open Questions (Thursday Call)

- How many states are they targeting and in what priority order?
- Suhan timeline: Can he commit to April? Full build or main page only?
- Who handles payment processor integration and testing?
- Total budget through June and how it splits (web/brand/content)?
- Retainer scope: # of pieces/month, email cadence, blog schedule, social frequency?
- Will DeeEtte stay on retainer or transition in-house once trained?
- Who is the final decision-maker?
- Contract signature and project kickoff timeline?
- Success metrics for April launch and June enrollment?

---

### Next Actions

**Before Thursday:**
- [ ] Prepare design direction (Sora Schools reference + rationale)
- [ ] Draft 2–3 logo alternatives with rationale
- [ ] Outline brand kit section headings and scope ([Canva Template](https://www.canva.com/design/DAHBoYxZYpw/LJVLOzFAkXPu27ih8o2iXw/edit))
- [ ] Prepare retainer service menu (full, mid-tier, light options)
- [ ] List 3–5 key enrollment messaging themes (parent pain points, student desires)

**During Thursday Call:**
- [ ] Clarify state priorities and launch order
- [ ] Confirm Suhan timeline
- [ ] Lock retainer scope and pricing
- [ ] Identify decision-maker and approval timeline
- [ ] Get agreement on Phase 1b (brand kit) as essential

**After Thursday Call:**
- [ ] Send written proposal recap within 24 hours
- [ ] Create detailed content strategy outline
- [ ] Schedule brand kit kickoff or confirm designer
- [ ] Begin MVP wireframes on Hostinger

---

### Risks & Opportunities

| Type | Item |
|------|------|
| Risk | Suhan's capacity could delay full build — Plan B: MVP + state pages via Hostinger |
| Risk | 3-partner decision-making slows approvals — mitigate by aligning Erik + one lead partner first |
| Opportunity | Multi-state scaling = expanded scope and longer retainer |
| Opportunity | Early logo redesign proposal positions Corinna as strategic, not tactical |
