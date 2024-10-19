import requests

#get all the data you need about a Pokemon generation
def get_generation(generation):
  url = f"https://pokeapi.co/api/v2/generation/{generation}/"
  response = requests.get(url)
    
  if response.status_code == 200:

    generation_info = response.json()

    return generation_info
  else:
    return None

generation = input("Enter generation number: ")
generation_info = get_generation(generation)

if generation_info:
  print(generation_info)
else:
  print("Generation not found!")