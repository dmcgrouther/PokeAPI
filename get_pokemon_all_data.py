import requests

def get_pokemon_info(pokemon_name):
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
  response = requests.get(url)
    
  if response.status_code == 200:

    pokemon_info = response.json()

    return pokemon_info
  else:
    return None

# Example usage
pokemon_name = input("Enter the Pokémon name: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
  print(pokemon_info)
else:
  print("Pokémon not found!")