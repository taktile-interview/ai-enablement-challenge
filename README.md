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

You do **not** need Docker or any keys. The service URLs are already in the
starter code; at the start of the interview we'll share an LLM API key
(revoked afterwards).

## At the start of the interview

The service URLs are already configured in the starter code — we switch the
services on for the session. Re-run `python smoke_test.py` when we begin; it
will confirm you can reach them. The only thing to export is the LLM API key
we share in the chat:

```bash
export ANTHROPIC_API_KEY=<key from chat>
```

## What's here

| File | What it is |
|------|------------|
| `smoke_test.py` | Verifies your Python env, and the services when they're online. |
| `crm_client.py` | A **working but naive** CRM client — your starting point. |
| `requirements.txt` | Everything to install before the interview. |

## The services

- **CRM API** (`https://ai-challenge-crm.ngrok.app`) — `GET /conversations`
  returns support conversations with cursor pagination. It behaves like a real
  upstream: it can rate-limit and occasionally error.
- **Ticket tracker** (`https://ai-challenge-issue-tracker.ngrok.app`) —
  `POST /tickets` files a ticket; `GET /tickets` lists them. There's more to
  it, which we'll get into live.

They're only online during interview sessions. Once they are, explore with the
naive client:

```bash
python crm_client.py
```

(Both URLs can be overridden with the `CRM_URL` / `TRACKER_URL` env vars if we
ever need to point you elsewhere.)

## Troubleshooting

- **Smoke test fails on the Python check** — make sure you're inside the venv
  where you ran `pip install -r requirements.txt`.
- **"Services are not online" before the interview** — expected; they're only
  switched on for the session.
- **"Services are not online" during the interview** — tell us; they run on
  our side and we can fix them.

See you at the interview!
