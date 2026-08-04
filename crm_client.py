"""Starter CRM client — working, but naive.

It fetches conversations from the CRM API and works fine for a quick call.
Treat it as a starting point, not a finished integration — whether it holds up
inside an agent loop is for you to judge.
"""

import os

import requests

CRM_URL = os.environ.get("CRM_URL", "https://ai-challenge-crm.ngrok.app")


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
