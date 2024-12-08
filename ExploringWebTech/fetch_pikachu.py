
#Task 2
import requests

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    pokemon_name = data['name']
    print(f"Pokémon Name: {pokemon_name.capitalize()}")

    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print("Abilities:")
    for ability in abilities:
        print(f"- {ability.capitalize()}")
else:
    print("Failed to retrieve data from the Pokémon API.")
