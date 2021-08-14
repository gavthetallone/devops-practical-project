from . import app, db
from .models import Pokemon
from .forms import PokeForm
from flask import redirect, url_for, request, render_template, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import requests
import random

poke_link = {
    "Pikachu" : "../images/pikachu.png",
    "Charmander" : "../images/charmander.png",
    "Squirtle" : "../images/squirtle.png",
    "Bulbasaur" : "../images/bulbasaur.png",
    "Cyndaquil" : "../images/cyndaquil.png",
    "Totodile" : "../images/totodile.png",
    "Chikorita" : "../images/chikorita.png",
    "Torchic" : "../images/torchic.png",
    "Mudkip" : "../images/mudkip.png",
    "Treecko" : "../images/treecko.png",
    "Chimchar" : "../images/chimchar.png",
    "Piplup" : "../images/piplup.png",
    "Turtwig" : "../images/turtwig.png"
}

poke_link_evolution = {
    "Raichu" : "../images/raichu.png",
    "Charmeleon" : "../images/charmeleon.png",
    "Wartortle" : "../images/wartortle.png",
    "Ivysaur" : "../images/ivysaur.png",
    "Quilava" : "../images/quilava.png",
    "Croconaw" : "../images/croconaw.png",
    "Bayleef" : "../images/bayleef.png",
    "Combusken" : "../images/combusken.png",
    "Marshtomp" : "../images/marshtomp.png",
    "Grovyle" : "../images/grovyle.png",
    "Monferno" : "../images/monferno.png",
    "Prinplup" : "../images/prinplup.png",
    "Grotle" : "../images/grotle.png"
}

poke_number = {
    "Pikachu" : "025",
    "Charmander" : "004",
    "Squirtle" : "007",
    "Bulbasaur" : "001",
    "Cyndaquil" : "155",
    "Totodile" : "158",
    "Chikorita" : "152",
    "Torchic" : "255",
    "Mudkip" : "258",
    "Treecko" : "252",
    "Chimchar" : "390",
    "Piplup" : "393",
    "Turtwig" : "387"
}

poke_evolution = {
    "Pikachu" : "Raichu",
    "Charmander" : "Charmeleon",
    "Squirtle" : "Wartortle",
    "Bulbasaur" : "Ivysaur",
    "Cyndaquil" : "Quilava",
    "Totodile" : "Croconaw",
    "Chikorita" : "Bayleef",
    "Torchic" : "Combusken",
    "Mudkip" : "Marshtomp",
    "Treecko" : "Grovyle",
    "Chimchar" : "Monferno",
    "Piplup" : "Prinplup",
    "Turtwig" : "Grotle"
}

@app.route("/")
def start():

    return render_template("start.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    form = PokeForm()

    region = requests.get('http://service-2:5000/get/region').text
    pokemon_type = requests.get('http://service-3:5000/get/pokemon_type').text

    payload = {'region' : region, 'pokemon_type' : pokemon_type}
    name = requests.post('http://service-4:5000/post/name', json=payload).text

    link = poke_link[name]
    number = poke_number[name]
    evolution = poke_evolution[name]
    link_evolution = poke_link_evolution[evolution]

    rand = random.randint(1,25)
    if rand == 25:
        new_pokemon = Pokemon(name="Pikachu", type="Electric", region="Kanto", link=poke_link["Pikachu"], number=poke_number["Pikachu"], evolution=poke_evolution["Pikachu"], link_evolution=poke_link_evolution["Raichu"])
    else:
        new_pokemon = Pokemon(name=name, type=pokemon_type, region=region, link=link, number=number, evolution=evolution, link_evolution=link_evolution)

    db.session.add(new_pokemon)
    db.session.commit()

    route = "home"

    if request.method == "POST":

        order_attr = {
            "#" : Pokemon.number.asc(),
            "Name" : Pokemon.name.asc(),
            "" : Pokemon.id.desc()
        } [form.poke_order.data]

        if form.poke_region.data == "All" and form.poke_type.data == "All":

            pokemons = Pokemon.query.order_by(order_attr).all()
            
        elif form.poke_region.data != "All" and form.poke_type.data == "All":

            pokemons = Pokemon.query.filter_by(region=form.poke_region.data).order_by(order_attr).all()
        
        elif form.poke_region.data == "All" and form.poke_type.data != "All":

            pokemons = Pokemon.query.filter_by(type=form.poke_type.data).order_by(order_attr).all()
            
        else:
            pokemons = Pokemon.query.filter_by(region=form.poke_region.data, type=form.poke_type.data).all()
        
        return render_template("home.html", pokemons=pokemons, new_pokemon=new_pokemon, form=form, route=route)

    else:
        pokemons = Pokemon.query.order_by(Pokemon.id.desc()).all()

    return render_template("home.html", pokemons=pokemons, new_pokemon=new_pokemon, form=form, route=route)


@app.route("/delete_pokemon/<int:id>")
def delete_pokemon(id):
    pokemon = Pokemon.query.get(id)
    db.session.delete(pokemon)
    db.session.commit()

    new_pokemon = Pokemon.query.get(id-1)
    pokemons = Pokemon.query.order_by(Pokemon.id.desc()).all()

    route = "delete"

    return render_template("home.html", pokemons=pokemons, new_pokemon=new_pokemon, route=route)