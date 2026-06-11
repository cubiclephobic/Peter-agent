Source: Built in Claude Code session, 2026-05-29 through 2026-06-04
Confidence: 0.95
Updated: 2026-06-04 — Initial article created
Updated: 2026-06-04 — Added course extraction files and my-ai-tools.md registry
Updated: 2026-06-05 — Migrated to Cloudflare Access; DNS moved from Hostinger to Cloudflare; SSL switched to Cloudflare Origin Certificate; local-only (no VPS public exposure)

# AI Builder Dashboard

## What It Is

A self-hosted Kanban board + project tracker + asset inventory deployed at **dashboard.zaradigm.com**. Corinna's daily operations hub — shows active projects, automation backlog, toolkit inventory, and session habits at a glance.

---

## Live URLs

| URL | What it is |
|-----|-----------|
| `https://dashboard.zaradigm.com` | Main dashboard (Kanban + In Motion + AI Toolkit) |
| `https://dashboard.zaradigm.com/time-audit.html` | Time audit (June 2026) |

**Auth:** Cloudflare Access (email OTP — corinna@zaradigm.com, 1-week session). The old HTTP Basic Auth has been superseded by Cloudflare Access at the edge.

---

## Infrastructure

- **VPS:** 167.88.43.189 (Hostinger, Ubuntu 24.04)
- **DNS:** Cloudflare (migrated 2026-06-05 from Hostinger — nameservers: doug + laura .ns.cloudflare.com)
- **SSL:** Cloudflare Origin Certificate (wildcard *.zaradigm.com, expires 2041) — Traefik uses file provider, not Let's Encrypt
- **Edge security:** Cloudflare Access (Zero Trust Free) — unauthenticated requests get email OTP login screen
- **Firewall:** VPS ports 80/443 restricted to Cloudflare IPs only (DOCKER-USER iptables chain, persisted via iptables-persistent)
- **Stack:** Python 3 `http.server` → Docker container → Traefik → Cloudflare
- **Docker Compose:** `/docker/dashboard/docker-compose.yml`
- **Files on VPS:** `/docker/dashboard/` — `index.html`, `server.py`, `time-audit.html`, `data/state.json`
- **Cert files on VPS:** `/docker/n8n/certs/origin.pem` + `origin.key`; dynamic config: `/docker/n8n/traefik-dynamic/tls.yml`
- **SSH key:** `~/.ssh/dashboard_deploy_key`
- **Network:** `n8n_default` (shared with n8n/Traefik stack)

---

## State Persistence

Board state (card positions, custom cards) stored in `/docker/dashboard/data/state.json` on the VPS. Synced on every card move/add/edit via `POST /api/state`. Falls back to `localStorage` if server unreachable.

---

## Deploying Updates

HTML files are **volume-mounted** — no container rebuild needed:

```bash
scp -i ~/.ssh/dashboard_deploy_key "/Users/corinnas/AI CODE/ai-builder-dashboard.html" root@167.88.43.189:/docker/dashboard/index.html
```

For `server.py` changes, also volume-mounted but requires container restart:
```bash
ssh -i ~/.ssh/dashboard_deploy_key root@167.88.43.189 "cd /docker/dashboard && docker compose restart"
```

---

## Dashboard Sections

| Section | What it shows |
|---------|--------------|
| **Header** | Top 3 time audit insights (updates each audit) |
| **Kanban** | Suggested / To Build / In Progress / Done — automation ideas backlog |
| **Session habits bar** | Wiki fetch prompt + /wrap + /wiki-update reminders (persistent reference) |
| **In Motion** | 15 active projects with accomplished/ahead — manually maintained |
| **AI Toolkit** | Full inventory from `my-ai-tools.md` — slash commands, scheduled skills, automations, dashboards, installed skills |

---

## Local Development

```bash
cd "/Users/corinnas/AI CODE" && python3 -m http.server 7755
# then open http://localhost:7755/ai-builder-dashboard.html
```

Local file: `/Users/corinnas/AI CODE/ai-builder-dashboard.html`

---

## Related

- [[wiki-system]] — wiki infrastructure (same VPS, same Traefik instance)
- [[morning-brief]] — sister automation on the same VPS stack
- `~/AI CODE/my-ai-tools.md` — source of truth for AI Toolkit section content
