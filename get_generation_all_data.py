import requests

def get_generation(generation):
  url = f"https://pokeapi.co/api/v2/pokemon/{generation}"
  response = requests.get(url)
    
  if response.status_code == 200:

    generation_info = response.json()

    return generation_info
  else:
    return None

# Example usage
generation = input("Enter generation number: ")
generation_info = get_generation(generation)

if generation_info:
  print(generation_info)
else:
  print("Generation not found!")