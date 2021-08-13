from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# poke_dict_region = {
#         "Kanto" : {
#             "Fire" : "Charmander", 
#             "Water" : "Squirtle", 
#             "Grass" : "Bulbasaur"
#         },
#         "Johto" : {
#             "Fire" : "Cyndaquil",
#             "Water" : "Totodile",
#             "Grass" : "Chikorita"
#         },
#         "Hoenn" : {
#             "Fire" : "Torchic",
#             "Water" : "Mudkip",
#             "Grass" : "Treecko"
#         },
#         "Sinnoh" : {
#             "Fire" : "Chimchar",
#             "Water" : "Piplup",
#             "Grass" : "Turtwig"
#         }
# }

poke_dict_region = {
        "Unova" : {
            "Psychic" : "Elgyem",
            "Fighting" : "Mienfoo",
            "Dragon" : "Axew"
        },
        "Kalos" : {
            "Psychic" : "Espurr",
            "Fighting" : "Pancham",
            "Dragon" : "Goomy"
        },
        "Alola" : {
            "Psychic" : "Cosmog",
            "Fighting" : "Crabrawler",
            "Dragon" : "Jangmo-o"
        },
}

@app.route("/post/name", methods=['POST'])
def post_name():
    region = request.json['region']
    pokemon_type = request.json['pokemon_type']
    
    name = poke_dict_region[region][pokemon_type]

    return name

if __name__ == "__main__":
    app.run(host='0.0.0.0')