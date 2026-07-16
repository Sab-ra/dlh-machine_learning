#!/usr/bin/env python3
"""
Dive into starships
"""
import requests


def availableShips(passengerCount):
    """
    You can see how JavaScript-ish this function
    is named, boo
    """

    base_url = "https://swapi.dev/api/starships/"
    psgr_count = passengerCount
    suitable_ships = []
    current_url = base_url

    while current_url:
        try:
            r = requests.get(current_url)
            r.raise_for_status()
            data = r.json()

            for ship in data.get('results', []):
                psgr_str = ship.get('passengers', '0').replace(',', '')

                try:
                    # If it's a range like '30-40', take the upper bound
                    if '-' in psgr_str:
                        capacity = int(
                            psgr_str.split('-')[-1].strip()
                        )
                    else:
                        capacity = int(psgr_str)
                except ValueError:
                    capacity = 0
                
                if capacity >= psgr_count:
                    suitable_ships.append(ship.get('name'))
            
            current_url = data.get('next')
        
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data: {e}')
            return []
    
    return suitable_ships
