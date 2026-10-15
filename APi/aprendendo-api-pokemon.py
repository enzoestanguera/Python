import requests

url = f'https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20'
count = 1

response = requests.get(url)

dados = response.json()

lista_pokemons = dados['results']

for pokemon in lista_pokemons:
    print(f'{count} - {pokemon["name"]}')
    count+=1

