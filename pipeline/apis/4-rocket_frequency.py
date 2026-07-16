#!/usr/bin/env python3
"""
Print the number of SpaceX launches per rocket.
"""
from collections import Counter
import requests


def get_rocket_names():
    """
    Return a dict mapping rocket id to rocket name.
    """

    r = requests.get(
        'https://api.spacexdata.com/v4/rockets',
        timeout=20
    )
    r.raise_for_status()
    rockets = r.json()
    return {
        rocket.get('id'): rocket.get('name') for rocket in rockets
    }


def get_launches():
    """
    Return the list of launches from the SpaceX API
    """

    r = requests.get(
        'https://api.spacexdata.com/v4/launches',
        timeout=20
    )
    r.raise_for_status()
    return r.json()


def main():
    """
    Count launches by rocket and print
    sorted frequencies.
    """

    launches = get_launches()
    rocket_names = get_rocket_names()

    counts = Counter()
    for launch in launches():
        rocket_id = launch.get('rocket')
        rocket_name = rocket_names.get(rocket_id)
        if rocket_name:
            counts[rocket_name] += 1

    ordered = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )
    for name, count in ordered:
        print(f'{name}: {count}')


if __name__ == '__main__':
    main()
