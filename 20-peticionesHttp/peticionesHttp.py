import requests
import json

class PokemonSearcher():
    URL_BASE = 'https://pokeapi.co/api/v2/pokemon/'

    @staticmethod
    def HTTPRequest():
        response = requests.get(PokemonSearcher.URL_BASE + '?limit=10&offset=0')
        return json.dumps(response.json(), indent=4)

    # extra
    @staticmethod
    def get_pokemon_data(pokemon_url):
        """
        Obtiene los datos de un Pokemon a partir de su URL.
        """
        pokemon_data = requests.get(pokemon_url).json()
        pokemon_id = pokemon_url.split('/')[-2]
        evolution_url = f'https://pokeapi.co/api/v2/evolution-chain/{pokemon_id}/'
        evolution_data = requests.get(evolution_url).json()
        types = [type_data['type']['name'] for type_data in pokemon_data['types']]
        evolution_names = [evolution['species']['name'] for evolution in evolution_data['chain']['evolves_to']]
        return {
            'name': pokemon_data['name'],
            'id': pokemon_data['id'],
            'peso': pokemon_data['weight'],
            'altura': pokemon_data['height'],
            'type': types,
            'evolution': evolution_names,
        }

    @staticmethod
    def search_pokemon_by_name():
        """
        Busca un Pokemon por su nombre.
        """
        search_name = input('Introduce el nombre del Pokemon: ')
        all_pokemons = requests.get(PokemonSearcher.URL_BASE + '?limit=2000&offset=0').json()
        for pokemon in all_pokemons['results']:
            if pokemon['name'].find(search_name) != -1:
                pokemon_data = PokemonSearcher.get_pokemon_data(pokemon['url'])
                print(json.dumps(pokemon_data, indent=4))
                break

    @staticmethod
    def search_pokemon_by_number():
        """
        Busca un Pokemon por su número.
        """
        number_pokemon = input('Introduce el número del Pokemon: ')
        all_pokemons = requests.get(PokemonSearcher.URL_BASE + '?limit=2000&offset=0').json()
        for pokemon in all_pokemons['results']:
            if pokemon['url'].find(number_pokemon) != -1:
                pokemon_data = PokemonSearcher.get_pokemon_data(pokemon['url'])
                print(json.dumps(pokemon_data, indent=4))
                break
    
    @staticmethod
    def searcher():
        option = input('¿Quieres buscar un Pokemon por nombre o número?\n' +
                       'Elije una opción:\n' +
                       '1) Nombre.\n' +
                       '2) Número.\n' +
                       'Opción elegida: ')
        if option == '1':
            PokemonSearcher.search_pokemon_by_name()
        elif option == '2':
            PokemonSearcher.search_pokemon_by_number()
        else:
            print('Opción no válida.')

# print(PokemonSearcher.HTTPRequest())
print(PokemonSearcher.searcher())