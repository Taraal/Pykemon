import requests
import json
import traceback

class Pokemon(object):

    stats = {
        "speed" : {
            "value" : 0,
            "display" : "speed"
        },
        "special-defense" : {
            "value": 0,
            "display": "Def. Spe"
        },
        "special-attack" : {
            "value" : 0,
            "display" : "Atk. Spe"
        },
        "defense" : {
            "value" : 0,
            "display" : "Def"
        },
        "attack" : {
            "value" : 0,
            "display" : "Atk"
        },
        "hp" : {
            "value" : 0,
            "display" : "Hp"
        },
    }

    types = []

    def __init__(self, id, level):

        data = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(id)).json()


        self.id = id
        self.name = data['name']
        self.level = level

        try:
            for stat in data['stats']:
                self.stats[stat['stat']['name']]['value'] = stat['base_stat'] + int((self.level * (1/50 * stat['base_stat'])))
        except Exception as e:
            print(e)

        try:
            for item in data['types']:
                new_type = item['type']['name']
                self.types.append(new_type)
        except Exception as e:
            print(e)

        print(self.types)

        print(self.stats)
        azegf = input("a")