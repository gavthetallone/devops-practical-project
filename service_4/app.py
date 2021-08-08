from flask import Flask, request, jsonify
import random

app = Flask(__name__)

poke_dict_kanto = {
    "Fire" : "Charmander", 
    "Water" : "Squirtle", 
    "Grass" : "Bulbasaur"
}

poke_dict_johto = {
    "Fire" : "Cyndaquil",
    "Water" : "Totodile",
    "Grass" : "Chikorita"
}

poke_dict_hoenn = {
    "Fire" : "Torchic",
    "Water" : "Mudkip",
    "Grass" : "Treecko"
}

poke_dict_sinnoh = {
    "Fire" : "Chimchar",
    "Water" : "Piplup",
    "Grass" : "Turtwig"
}

@app.route("/post/name", methods=['POST'])
def post_name():
    region = request.json['region']
    pokemon_type = request.json['pokemon_type']

    if region == "Kanto":
        name = poke_dict_kanto[pokemon_type]

    elif region == "Johto":
        name = poke_dict_johto[pokemon_type]
    
    elif region == "Hoenn":
        name = poke_dict_hoenn[pokemon_type]
    
    elif region == "Sinnoh":
        name = poke_dict_sinnoh[pokemon_type]
    
    return name

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')