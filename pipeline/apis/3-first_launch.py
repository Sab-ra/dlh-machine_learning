#!/usr/bin/env python3
"""
SpaceX API discovery
"""
import time
import requests


def fetch_first_launch_name():
    """
    Return the first SpaceX launch name
    by acsending date_unix
    """

    url = "https://api.spacexdata.com/v4/launches"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
    }

    try:
        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )
        if r.status_code == 200:
            launches = r.json()
            first = min(
                launches,
                key=lambda item: item.get('date_unix', float('inf'))
            )
            return first.get('name')
    except (requests.RequestException, ValueError, TypeError):
        pass

    payload = {
        "query": {},
        "options": {
            "sort": {"date_unix": "asc"},
            "limit": 1,
            "select": ["name"],
        },
    }
    headers = {
        "Accept": "application/json",
        "User-agent": "Mozilla/5.0",
    }

    try:
        r = requests.post(
            f'{url}/query',
            json=payload,
            headers=headers,
            timeout=20
        )
        if r.status_code == 200:
            data = r.json()
            docs = data.get('docs', [])
            if docs and docs[0].get('name'):
                return docs[0]['name']
    except (requests.RequestException, ValueError, TypeError):
        pass
    time.sleep(1)

    return None

def main():
    """
    Print the first name if found.
    """

    launch_name = fetch_first_launch_name()
    if launch_name:
        print(launch_name)

if __name__ == "__main__":
    main()
