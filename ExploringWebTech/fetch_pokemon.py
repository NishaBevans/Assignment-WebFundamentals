# Task 3
import requests


def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}.")
        return None


def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    average_weight = total_weight / len(pokemon_list)
    return average_weight


pokemon_names = ["pikachu", "bulbasaur", "charmander"]


pokemon_data = []
for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data.append(data)

average_weight = calculate_average_weight(pokemon_data)

for data in pokemon_data:
    pokemon_name = data['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print(f"Pokémon Name: {pokemon_name}")
    print("Abilities:")
    for ability in abilities:
        print(f"- {ability.capitalize()}")
    print()

print(f"Average Weight of the Pokémon: {average_weight} hectograms")

