# AI Enablement Engineer — Tech Challenge (environment)

Welcome! This repo is **setup only**. The task itself is shared live at the
start of the interview, so there's nothing to prepare beyond a working Python
environment — we host the mock services and share their URLs when we begin.

## Before the interview

1. **Set up a Python environment (3.10+) and install the requirements.** We'll
   build a small agent in Python. Use your preferred setup; if in doubt, a
   plain venv works everywhere:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   (If you use `uv`, `conda`, or similar: anything that gives you Python 3.10+
   with the requirements installed is fine — the smoke test verifies it.)
2. **Run the smoke test:**
   ```bash
   python smoke_test.py
   ```
   "Python environment ready" means you're set.
3. **Check your Google Meet setup** — microphone, camera, and full screen share.

Just before the interview, please `git pull` so you're on the latest version.

You do **not** need Docker or any keys. At the start of the interview we'll
share the service URLs and an LLM API key (revoked afterwards).

## At the start of the interview

We'll paste two service URLs into the chat. Export them and re-run the smoke
test to confirm you can reach everything:

```bash
export CRM_URL=https://...
export TRACKER_URL=https://...
python smoke_test.py
```

## What's here

| File | What it is |
|------|------------|
| `smoke_test.py` | Verifies your Python env; with URLs set, also checks the services. |
| `crm_client.py` | A **working but naive** CRM client — your starting point. |
| `requirements.txt` | Everything to install before the interview. |
| `docker-compose.yml` | Fallback for running the services locally — only used if we ask you to. |

## The services

- **CRM API** (`$CRM_URL`) — `GET /conversations` returns support conversations
  with cursor pagination. It behaves like a real upstream: it can rate-limit
  and occasionally error.
- **Ticket tracker** (`$TRACKER_URL`) — `POST /tickets` files a ticket;
  `GET /tickets` lists them. There's more to it, which we'll get into live.

Once you have the URLs, explore with the naive client:

```bash
python crm_client.py
```

## Troubleshooting

- **Smoke test fails on the Python check** — make sure you're inside the venv
  where you ran `pip install -r requirements.txt`.
- **Smoke test can't reach the services (interview only)** — double-check the
  exported URLs against the chat; if it persists, tell us — the services run on
  our side and we can fix them.

See you at the interview!
