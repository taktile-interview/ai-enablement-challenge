"""Smoke test — confirms you are ready for the interview.

Before the interview (all you need to do):

    python smoke_test.py

This verifies your Python environment. The mock services are hosted by us; we
share their URLs at the start of the session, and the test then also checks
you can reach them:

    CRM_URL=https://... TRACKER_URL=https://... python smoke_test.py
"""

import os
import sys
import time

CRM_URL = os.environ.get("CRM_URL", "")
TRACKER_URL = os.environ.get("TRACKER_URL", "")


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


def _get(url: str, attempts: int = 8):
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
    _get(f"{CRM_URL.rstrip('/')}/health")
    convs = _get(f"{CRM_URL.rstrip('/')}/conversations").json()["conversations"]
    print(f"ok ({len(convs)} conversations on the first page)")

    print("Checking ticket tracker ...", end=" ", flush=True)
    _get(f"{TRACKER_URL.rstrip('/')}/health")
    _get(f"{TRACKER_URL.rstrip('/')}/tickets")
    print("ok")


def main() -> None:
    check_python_env()

    if CRM_URL and TRACKER_URL:
        check_services()
        print("\nSmoke test passed — you can reach the services. Let's go!")
    elif CRM_URL or TRACKER_URL:
        raise SystemExit("FAILED: set both CRM_URL and TRACKER_URL (or neither).")
    else:
        print(
            "\nPython environment ready — that's everything for the pre-work.\n"
            "We'll share the service URLs at the start of the interview; re-run then with:\n"
            "  CRM_URL=<url> TRACKER_URL=<url> python smoke_test.py"
        )


if __name__ == "__main__":
    main()
