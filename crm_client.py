"""Starter CRM client — working, but naive.

This is intentionally the *before* state. It walks the cursor pagination and
returns conversations, and it works fine for a single quick call. Under a real
agent loop it will show its seams: no retry/backoff (the API rate-limits and
occasionally 500s) and no deduplication (the API's pagination can hand you the
same conversation on two adjacent pages). Hardening it is part of the task.
"""

import requests

CRM_URL = "http://localhost:8001"


class CRMClient:
    def __init__(self, base_url: str = CRM_URL):
        self.base_url = base_url.rstrip("/")

    def list_conversations(self) -> list[dict]:
        conversations: list[dict] = []
        cursor = None
        while True:
            params = {"cursor": cursor} if cursor else {}
            response = requests.get(f"{self.base_url}/conversations", params=params, timeout=10)
            response.raise_for_status()
            page = response.json()
            conversations.extend(page["conversations"])
            cursor = page["next_cursor"]
            if cursor is None:
                return conversations


if __name__ == "__main__":
    convs = CRMClient().list_conversations()
    print(f"Fetched {len(convs)} conversations:")
    for c in convs:
        print(f"  {c['id']}  {c['customer']}  ({c['status']})")
