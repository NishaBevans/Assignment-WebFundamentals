# Task 3

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
        data = response.json()
        planets = []
        
        
        for planet in data['bodies']:
            if planet.get('isPlanet'):  
                
                name = planet.get('englishName', 'Unknown')
                mass = planet.get('mass', {}).get('massValue', None)  
                orbit_period = planet.get('sideralOrbit', None)  
                
                
                if mass is not None and orbit_period is not None:
                    planets.append({
                        'name': name,
                        'mass': mass,
                        'orbit_period': orbit_period
                    })
        
        return planets
    else:
        print(f"Failed to retrieve data, status code: {response.status_code}")
        return []

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0
    
    for planet in planets:
        if planet['mass'] > max_mass:
            heaviest_planet = planet
            max_mass = planet['mass']
    
    return heaviest_planet['name'], heaviest_planet['mass']


planets = fetch_planet_data()


if planets:
    name, mass = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")

