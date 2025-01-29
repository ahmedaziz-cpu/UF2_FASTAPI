import requests

# URL de la API de Pokémon para obtener información sobre Pikachu
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Hacer la petición GET
response = requests.get(url)

# Imprimir la respuesta
if response.status_code == 200:
    # Mostrar datos del Pokémon
    data = response.json()
    print("Nombre del Pokémon:", data['name'])
    print("Peso:", data['weight'])
    print("Altura:", data['height'])
    print("Habilidades:", [ability['ability']['name'] for ability in data['abilities']])
else:
    print("Error en la petición:", response.status_code)
