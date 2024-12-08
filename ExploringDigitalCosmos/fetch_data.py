# Task 2

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
   
    response = requests.get(url)
    
   
    if response.status_code == 200:
        data = response.json()
        planets = data['bodies']

        
        for planet in planets:
            if planet['isPlanet']:  
                name = planet.get('englishName', 'Unknown')
                mass = planet.get('mass', {}).get('massValue', 'N/A')  
                orbit_period = planet.get('sideralOrbit', 'N/A')  

                # Print the planet details
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    else:
        print(f"Failed to retrieve data, status code: {response.status_code}")

fetch_planet_data()
