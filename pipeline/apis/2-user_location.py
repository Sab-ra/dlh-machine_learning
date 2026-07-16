#!/usr/bin/env python3
"""
Fetch and print a GitHub user's location from a given API URL.
"""
import sys
import time

import requests


def get_github_user_location(api_url):
    """
    Fetch the user location from the GitHub API and print expected output.
    """
    try:
        response = requests.get(api_url, timeout=10)

        if response.status_code == 200:
            user_data = response.json()
            location = user_data.get("location")
            if location:
                print(location)
            else:
                print("Not found")
        elif response.status_code == 404:
            print("Not found")
        elif response.status_code == 403:
            reset_raw = response.headers.get("X-RateLimit-Reset", "0")
            reset_timestamp = int(reset_raw) if reset_raw.isdigit() else 0
            if reset_timestamp > 0:
                current_timestamp = int(time.time())
                minutes_to_reset = (reset_timestamp - current_timestamp) // 60
                if minutes_to_reset < 0:
                    minutes_to_reset = 0
                print(f"Reset in {minutes_to_reset} min")
            else:
                print("Reset in 0 min")
        else:
            print("Not found")
    except requests.exceptions.RequestException:
        print("Not found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    get_github_user_location(sys.argv[1])
