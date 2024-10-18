import requests

def get_pokemon_info():
  url = "https://pokeapi.co/api/v2/pokemon?limit=151"
  response = requests.get(url)
    
  if response.status_code == 200:

    pokemon_info = response.json()

    assert len(pokemon_info['results']) == 151, "The number of Pokémon is not 151"

    print(pokemon_info['results'])
  else:
    return None
  
get_pokemon_info()