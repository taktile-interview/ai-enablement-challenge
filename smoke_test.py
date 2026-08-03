"""Smoke test — confirms your environment is ready for the interview.

This only checks that the two services are up and answering. It does NOT test
the challenge task (that's shared live). Run it after `docker compose up`:

    python smoke_test.py

A green run means you're set. Note the CRM API deliberately rate-limits and
occasionally returns 500s — this script retries so setup stays reliable; making
your own client resilient to that is part of the interview.
"""

import sys
import time

CRM_URL = "http://localhost:8001"
TRACKER_URL = "http://localhost:8002"


def check_python_env() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit(
            f"FAILED: Python 3.10+ required, you are on {sys.version.split()[0]}. "
            "Create a venv with a newer Python before the interview."
        )
    missing = []
    for module in ("requests", "anthropic"):
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    if missing:
        raise SystemExit(
            f"FAILED: missing package(s): {', '.join(missing)}. "
            "Run: pip install -r requirements.txt (inside your venv)."
        )


check_python_env()

import requests  # noqa: E402  (import verified above)


def _get(url: str, attempts: int = 8) -> requests.Response:
    last = None
    for i in range(attempts):
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                return r
            last = f"HTTP {r.status_code}"
        except requests.RequestException as exc:
            last = str(exc)
        time.sleep(1.0 + i * 0.5)
    raise SystemExit(f"FAILED: {url} did not become healthy ({last}).")


def main() -> None:
    print(f"Python {sys.version.split()[0]} with required packages ... ok")
    print("Checking crm-api ...", end=" ", flush=True)
    _get(f"{CRM_URL}/health")
    convs = _get(f"{CRM_URL}/conversations").json()["conversations"]
    print(f"ok ({len(convs)} conversations on the first page)")

    print("Checking tracker-api ...", end=" ", flush=True)
    _get(f"{TRACKER_URL}/health")
    _get(f"{TRACKER_URL}/tickets")
    print("ok")

    print("\nSmoke test passed — your environment is ready. See you at the interview!")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        print(exc, file=sys.stderr)
        raise
