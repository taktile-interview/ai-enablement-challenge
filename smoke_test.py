"""Smoke test — confirms you are ready for the interview.

Run it before the interview:

    python smoke_test.py

It always verifies your Python environment. The mock services are hosted by
us and are switched on for the interview itself — if they're reachable, the
test checks them too; if not, that's expected before the interview.
"""

import os
import sys
import time

CRM_URL = os.environ.get("CRM_URL", "https://ai-challenge-crm.ngrok.app").rstrip("/")
TRACKER_URL = os.environ.get("TRACKER_URL", "https://ai-challenge-issue-tracker.ngrok.app").rstrip("/")


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
    print(f"Python {sys.version.split()[0]} with required packages ... ok")


def _services_online() -> bool:
    import requests

    try:
        return requests.get(f"{CRM_URL}/health", timeout=5).status_code == 200
    except requests.RequestException:
        return False


def _get(url: str, attempts: int = 5):
    import requests

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
    raise SystemExit(f"FAILED: {url} did not respond ({last}).")


def check_services() -> None:
    print("Checking CRM API ...", end=" ", flush=True)
    _get(f"{CRM_URL}/conversations")
    print("ok")

    print("Checking ticket tracker ...", end=" ", flush=True)
    _get(f"{TRACKER_URL}/health")
    _get(f"{TRACKER_URL}/tickets")
    print("ok")


def main() -> None:
    check_python_env()

    if _services_online():
        check_services()
        print("\nSmoke test passed — you can reach the services. Let's go!")
    else:
        print(
            "\nServices are not online right now — that's expected before the\n"
            "interview (we switch them on for the session itself).\n"
            "Your Python environment is ready, which is everything the pre-work needs.\n"
            "If you're seeing this DURING the interview, tell us — the services run\n"
            "on our side."
        )


if __name__ == "__main__":
    main()
