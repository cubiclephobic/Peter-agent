Source: Claude Code session 2026-06-05 — full Cloudflare migration
Confidence: 0.95

# Cloudflare

## What It Is

Cloudflare is the DNS, SSL, and security layer in front of zaradigm.com and all subdomains. Migrated from Hostinger nameservers on 2026-06-05. Provides DNS management, SSL termination, DDoS protection, and Zero Trust Access for protected subdomains.

---

## Account

- **Plan:** Free
- **Login:** corinna@zaradigm.com
- **Account ID:** b2d2161b36025b32efc136902701ff72
- **Zone ID (zaradigm.com):** 50ce35a5f9fe57060baca7cadd0de845
- **Nameservers:** doug.ns.cloudflare.com + laura.ns.cloudflare.com

---

## DNS

- **34 records** migrated from Hostinger on 2026-06-05
- Backup of all Hostinger records saved at: `/Users/corinnas/AI CODE/Zaradigm DNS/zaradigm.com.txt`
- Cloudflare import file saved at: `/Users/corinnas/AI CODE/Zaradigm DNS/zaradigm-cloudflare-import.txt`
- Key proxy settings: wiki + dashboard = orange cloud (proxied); MX, DKIM, SPF = grey cloud (DNS only)

---

## SSL/TLS

- **Mode:** Full (strict)
- **Certificate:** Cloudflare Origin Certificate — wildcard `*.zaradigm.com` + `zaradigm.com`
- **Validity:** 15 years (expires ~Jun 2041)
- **Cert files on VPS:** `/docker/n8n/certs/origin.pem` + `/docker/n8n/certs/origin.key`
- **Local backup:** `/Users/corinnas/AI CODE/Zaradigm DNS/origin.pem` + `origin.key`
- **Traefik config:** file provider at `/docker/n8n/traefik-dynamic/tls.yml` — no longer uses Let's Encrypt

---

## Zero Trust Access

- **Plan:** Free (up to 50 users)
- **Protected apps:**

| App | Domain | Policy | Session |
|-----|--------|---------|---------|
| Knowledge Wiki | wiki.zaradigm.com | Allow: corinna@zaradigm.com | 1 week |
| AI Builder Dashboard | dashboard.zaradigm.com | Allow: corinna@zaradigm.com | 1 week |

- Both apps also have a **Service Auth policy** (`claude-automations`) allowing automated scripts to bypass the login screen using the service token.

### Service Token (Claude Automations)
- **Name:** claude-automations
- **Token ID:** b9143595-dc7f-412a-a475-704e4d10d20c
- **Client ID:** stored in `/Users/corinnas/AI CODE/.env` as `CF_ACCESS_CLIENT_ID`
- **Client Secret:** stored in `/Users/corinnas/AI CODE/.env` as `CF_ACCESS_CLIENT_SECRET`
- **Usage:** Pass both as headers on any request to Access-protected URLs:
  ```
  CF-Access-Client-Id: <value from .env>
  CF-Access-Client-Secret: <value from .env>
  ```

---

## VPS Firewall

Ports 80 and 443 on the VPS are restricted to Cloudflare IP ranges only (DOCKER-USER iptables chain). Direct-IP access is blocked. Rules persisted via iptables-persistent at `/etc/iptables/rules.v4`.

If Cloudflare IPs change: re-run the firewall script at `/docker/cf-firewall.sh` or fetch fresh ranges from cloudflare.com/ips-v4.

---

## Dashboard Shortcuts

| What | URL |
|------|-----|
| DNS records | dash.cloudflare.com/b2d2161b36025b32efc136902701ff72/zaradigm.com/dns/records |
| SSL/TLS | dash.cloudflare.com/b2d2161b36025b32efc136902701ff72/zaradigm.com/ssl-tls |
| Access apps | dash.cloudflare.com/b2d2161b36025b32efc136902701ff72/one/access-controls/apps |
| Service credentials | dash.cloudflare.com/b2d2161b36025b32efc136902701ff72/one/access-controls/service-credentials |

---

## Related

- [[ai-builder-dashboard]] — protected by Access
- [[wiki-system]] — protected by Access
