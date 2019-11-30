import requests
import json

class Zone(object):



    def __init__(self, name):
        self.name = name
        self.pokemons = {}

        url = "https://pokeapi.co/api/v2/location-area/" + self.name

        data = requests.get(url).json()
        total_encounter_chance = 0
        index = 0
        while total_encounter_chance < 100:
            pokemon = {}
            total_encounter_chance += data['pokemon_encounters'][index]['version_details'][0]['max_chance']
            pokemon['name'] = data['pokemon_encounters'][index]['pokemon']['name']
            min_level = 100
            max_level = 0
            for encounter in data['pokemont_encounters'][index]['version_details'][0]:
                if encounter['min_level'] < min_level:
                    min_level = encounter['min_level']
                if encounter['max_level'] > max_level:
                    max_level = encounter['max_level']
            pokemon['min_level'] = min_level
            pokemon['max_level'] = max_level
            self.pokemons[index] = pokemon