# AI Enablement Engineer — Tech Challenge (environment)

Welcome! This repo is **setup only**. It gives you a local environment — a mock
CRM API, a mock ticket tracker, and a naive CRM client — so we can start coding
right away in the interview. **The task itself is shared live at the start of
the interview**, so there's nothing to prepare beyond getting this running.

## Before the interview

1. **Install Docker and Docker Compose.** Docker 28.0.0+ and Docker Compose
   v2.36.2+ (or the built-in `docker compose`).
2. **Set up a Python environment (3.10+) and install the requirements.** We'll
   build a small agent in Python. Use your preferred setup; if in doubt, a
   plain venv works everywhere:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   (If you use `uv`, `conda`, or similar: anything that gives you Python 3.10+
   with the requirements installed is fine — the smoke test verifies it.)
3. **Start the environment and confirm the smoke test passes:**
   ```bash
   docker compose up          # pulls two images, serves on :8001 and :8002
   python smoke_test.py       # in another terminal, inside your venv
   ```
   A green smoke test means you're ready — it checks your Python environment
   and both services.
4. **Check your Google Meet setup** — microphone, camera, and full screen share.

Just before the interview, please `git pull` so you're on the latest version.

You do **not** need any keys in advance. At the start of the interview we'll
share two things with you: an LLM API key (revoked afterwards) and a
`CHALLENGE_KEY` that unlocks the full challenge dataset — until then the CRM
serves a small demo dataset, which is all the smoke test needs.

## What's here

| File | What it is |
|------|------------|
| `docker-compose.yml` | Pulls the mock `crm-api` (`:8001`) and `tracker-api` (`:8002`). |
| `smoke_test.py` | Confirms both services are up. Setup check only. |
| `crm_client.py` | A **working but naive** CRM client — your starting point. |
| `requirements.txt` | Everything to install before the interview. |

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
