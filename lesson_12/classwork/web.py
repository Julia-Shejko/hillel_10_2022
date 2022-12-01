import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
data = response.json()
print(data["name"])
