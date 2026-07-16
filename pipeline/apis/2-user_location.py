#!/usr/bin/env python3
"""
Finde GitHub User Locations
"""
import requests
import sys
import time


def get_github_user_location(api_url):
    """
    Fetches location from GitHub API
    """

    try:
        r = requests.get(api_url)

        if r.status_code == 200:
            user_data = r.json()
            location = user_data.get('location')
            if location:
                print(location)
            else:
                print('Not found')  # User and no location
        elif r.status_code == 404:
            print('Not found')
        elif r.status_code == 403:
            # Rate limit exeeded
            reset_timestamp = int(
                r.headers.get('X-Ratelimit-Reset', 0)
            )
            if reset_timestamp > 0:
                current_timestamp = int(time.time())
                # Calculate minutes from now
                minutes_to_reset = (
                    (reset_timestamp - current_timestamp) // 60
                )
                if minutes_to_reset < 0:
                    minutes_to_reset = 0
                print(f'Reset in {minutes_to_reset} min')
            else:
                print('Rate limit exceeded, X-Ratelimit-Reset header not found.')
        else:
            print(f"Error: Unexpected status code {r.status_code}")

    except requests.exceptions.RequestException as e:
        print(f'An error occured during the request: {e}')
