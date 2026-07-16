#!/usr/bin/env python3
"""
List Interesting Planets
"""
import requests


def sentientPlanets():
    """
    Returns all planets from SWAPI API. Handles pagination
    """

    api_url = 'https://swapi.dev/api/species/'
    sentient_homeworld_urls = set()     # unique values because set
    planet_names = set()

    # Fetch all homeworld URLs
    current_species_url = api_url

    while current_species_url:
        try:
            r = requests.get(current_species_url)
            r.raise_for_status()
            data = r.json()

            for species in data.get('results', []):
                classification = (
                    species.get('classification', '').lower()
                    )
                designation = (
                    species.get('designation', '').lower()
                )

                if (
                    'sentient' in classification or
                    'sentient' in designation
                ):
                    homeworld_url = species.get('homeworld')
                    if homeworld_url:
                        sentient_homeworld_urls.add(homeworld_url)

            current_species_url = data.get('next')

        except requests.exceptions.RequestException as e:
            print(f'Error fetching species data: {e}')
            return []

    # Fetch planet names
    for homeworld_url in sentient_homeworld_urls:
        try:
            r = requests.get(homeworld_url)
            r.raise_for_status()
            planet_data = r.json()
            planet_names.add(planet_data.get('name'))
        except requests.exceptions.RequestException as e:
            print(f'Error fetching homeworld data from {homeworld_url}: {e}')

    return sorted(list(planet_names))
