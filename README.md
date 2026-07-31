# AI Enablement Engineer — Tech Challenge (environment)

Welcome! This repo is **setup only**. It gives you a local environment — a mock
CRM API, a mock ticket tracker, and a naive CRM client — so we can start coding
right away in the interview. **The task itself is shared live at the start of
the interview**, so there's nothing to prepare beyond getting this running.

## Before the interview

1. **Install Docker and Docker Compose.** Docker 28.0.0+ and Docker Compose
   v2.36.2+ (or the built-in `docker compose`).
2. **Have your preferred Python environment ready** (3.10+). We'll build a small
   agent in Python. `pip install -r requirements.txt` covers the starter code;
   you'll add an LLM SDK (e.g. `anthropic`) during the interview.
3. **Start the environment and confirm the smoke test passes:**
   ```bash
   docker compose up          # pulls two images, serves on :8001 and :8002
   python smoke_test.py       # in another terminal
   ```
   A green smoke test means you're ready.
4. **Check your Google Meet setup** — microphone, camera, and full screen share.

Just before the interview, please `git pull` so you're on the latest version.

You do **not** need an LLM API key in advance — we'll share one with you at the
start of the interview (and revoke it afterwards).

## What's here

| File | What it is |
|------|------------|
| `docker-compose.yml` | Pulls the mock `crm-api` (`:8001`) and `tracker-api` (`:8002`). |
| `smoke_test.py` | Confirms both services are up. Setup check only. |
| `crm_client.py` | A **working but naive** CRM client — your starting point. |
| `requirements.txt` | Just `requests`, for the smoke test and starter client. |

## The services

- **CRM API** (`http://localhost:8001`) — `GET /conversations` returns support
  conversations with cursor pagination. It behaves like a real upstream: it can
  rate-limit and occasionally error.
- **Ticket tracker** (`http://localhost:8002`) — `POST /tickets` files a ticket;
  `GET /tickets` lists them. There's more to it, which we'll get into live.

Explore them with the naive client:

```bash
python crm_client.py
```

## Troubleshooting

- **Ports 8001/8002 already in use** — stop whatever's using them, or edit the
  port mappings in `docker-compose.yml`.
- **`docker compose up` can't pull the images** — check you're online; if you're
  on a VPN, try toggling it off.
- **Smoke test flaky** — it retries automatically; give it a few seconds after
  `docker compose up`. If it still fails, restart compose.

See you at the interview!
