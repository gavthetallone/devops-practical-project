from . import app, db
from .models import Pokemon
from .forms import PokeForm
from flask import redirect, url_for, request, render_template, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import requests
import random

# poke_link = {
#     "Pikachu" : "https://th.bing.com/th/id/OIP.4NhV-E8QFbihBK2p6LU4tQHaG7?pid=ImgDet&rs=1",
#     "Charmander" : "https://th.bing.com/th/id/R.3826a0bbdcc9e12a949cc3080f9a4e55?rik=jtm4qBBiN1%2fz2g&riu=http%3a%2f%2fwww.pokemasters.net%2fpokedex%2fimages%2fpokemon%2f4000.png&ehk=F9WGO2TvAWorlVyAvA8SWEM0YTs8OjcRCK%2fveScYaDE%3d&risl=&pid=ImgRaw",
#     "Squirtle" : "https://th.bing.com/th/id/AMMS_7b9ddf692c6df64d86bbe4e96ef46a83?pid=ImgDet&rs=1",
#     "Bulbasaur" : "https://th.bing.com/th/id/AMMS_9ba4d684e64c19af7c99148ac36af46b?pid=ImgDet&rs=1",
#     "Cyndaquil" : "https://vignette.wikia.nocookie.net/nintendo/images/9/99/Cyndaquil.png/revision/latest?cb=20141003061613&path-prefix=en",
#     "Totodile" : "https://th.bing.com/th/id/R.32c471244f37286755a1b72a54cc2a80?rik=1gjd9oO%2by1QQNw&riu=http%3a%2f%2fstatic.giantbomb.com%2fuploads%2foriginal%2f0%2f5150%2f1106948-960099_20090814_screen001.jpg&ehk=AQem7YmVfyrTAWnWQHnePSN%2bE8%2f3s41jheqXSouY3aQ%3d&risl=&pid=ImgRaw&r=0",
#     "Chikorita" : "https://th.bing.com/th/id/R.189f539cfb66f53801aa4039b2d19611?rik=bLpW1CHTljLx6g&riu=http%3a%2f%2fimages2.wikia.nocookie.net%2f__cb20130105100827%2fpokemontowerdefense%2fimages%2fb%2fbf%2f152Chikorita.png&ehk=9buQXHcC6WYFHTTH1gxc0eSFlLCKLViR9xhwj2KbRT4%3d&risl=&pid=ImgRaw&r=0",
#     "Torchic" : "https://th.bing.com/th/id/R.abf178cee15982f2d8e404d18e1c9c03?rik=3hMmh8F%2box4glQ&riu=http%3a%2f%2fvignette2.wikia.nocookie.net%2fhelixpedia%2fimages%2f4%2f4f%2fTorchic.png%2frevision%2flatest%3fcb%3d20140613012734&ehk=%2f8fJqagM3dIPv6B7eSa%2bDM87SmAEomfuCLUt85JzIcc%3d&risl=&pid=ImgRaw&r=0",
#     "Mudkip" : "https://th.bing.com/th/id/R.479f79afbe259f711a640784f1ada10d?rik=SF3QyJiippOtbg&riu=http%3a%2f%2fpokemon3d.net%2fwiki%2fimages%2fa%2fae%2fMudkip.png&ehk=OACuigY8woj65Aemgz0bymGEoAVCbEy%2bX9ftRL%2bwG6c%3d&risl=&pid=ImgRaw&r=0",
#     "Treecko" : "https://th.bing.com/th/id/R.ad6a1e51e1315a8a45dec34a3cf3b356?rik=xQ9%2fX8h%2fXyvFxA&pid=ImgRaw&r=0",
#     "Chimchar" : "https://vignette.wikia.nocookie.net/nintendo/images/9/9f/Chimchar.png/revision/latest?cb=20160916201643&path-prefix=en",
#     "Piplup" : "https://cdn2.bulbagarden.net/upload/thumb/b/b1/393Piplup.png/1200px-393Piplup.png",
#     "Turtwig" : "https://th.bing.com/th/id/R.8a7002960abc336335ba2425d69f344b?rik=5c0dFivTOreYYw&riu=http%3a%2f%2fimages4.wikia.nocookie.net%2f__cb20110927000961%2fpokemon%2fimages%2f5%2f5c%2f387Turtwig.png&ehk=BuBj%2bOGpbEnf9fYuQ5IYzSEcR05cKWAjrIqMSKzZm80%3d&risl=&pid=ImgRaw&r=0"
# }

poke_link = {
    "Pikachu" : "https://gamingreinvented.com/wp-content/uploads/2017/09/OriginalCapPikachu.png",
    "Elgyem" : "https://vignette.wikia.nocookie.net/es.pokemon/images/c/c0/Elgyem.png/revision/latest?cb=20170617013310",
    "Mienfoo" : "https://th.bing.com/th/id/R.365abeca028202833190cd2c3ce19d38?rik=rJZjGx5YgqHLLQ&riu=http%3a%2f%2fbogleech.com%2fpokemon%2fallpokes%2f619Mienfoo.png&ehk=RqnM8zxcSt2S3aWR0ZOnK4bJyyXJha%2bSTMvc3Y%2f9kow%3d&risl=&pid=ImgRaw&r=0",
    "Axew" : "https://th.bing.com/th/id/R.02df78aab4a0adc32d4858039c33da5b?rik=ebuPy4SpkjYpNA&riu=http%3a%2f%2fmedia.pocketmonsters.net%2fimageboard%2f60%2f12814800850032.png&ehk=GPwlgIpSpVblediGaOao%2ff%2fPx22u5WuadRipfgPJ26I%3d&risl=&pid=ImgRaw&r=0",
    "Espurr" : "https://vignette.wikia.nocookie.net/omniversal-battlefield/images/1/1c/1871454-espurrpng-espurr-png-391_500_preview.png/revision/latest?cb=20190309054458",
    "Pancham" : "https://th.bing.com/th/id/R.1f7b8ed3b122c4fbfc571202e7720e12?rik=Vw44NVvZo3vi4Q&riu=http%3a%2f%2fpokemon3d.net%2fwiki%2fimages%2fthumb%2fc%2fc9%2fPancham.png%2f1200px-Pancham.png&ehk=keraLsY81iAd1GaKrmqP1S65ucB3HQ5IaSf47d2%2bzVA%3d&risl=&pid=ImgRaw&r=0",
    "Goomy" : "https://vignette.wikia.nocookie.net/pokemon/images/c/c6/704Goomy_XY_anime.png/revision/latest?cb=20160815051228",
    "Cosmog" : "https://2.bp.blogspot.com/-QBZpqa53Lnc/WIttJAUk6BI/AAAAAAAAIQc/CELqv22frBwNoi1cce3pWrkVSK3AC6NfQCLcB/s320/38.png",
    "Crabrawler" : "https://th.bing.com/th/id/R.f0737faa395266dc48986d164566902e?rik=cbGlKSmKGQPbTA&riu=http%3a%2f%2fcdn.staticneo.com%2fw%2fpokemon%2fa%2faa%2fCrabrawler.png&ehk=wSdohHgZpRCGlmO7zgj71B9M%2fAkO0QXn%2bCkvbCXw6Wk%3d&risl=&pid=ImgRaw&r=0",
    "Jangmo-o" : "https://vignette.wikia.nocookie.net/es.pokemon/images/0/0b/Jangmo-o.png/revision/latest?cb=20160906132555"
}

# poke_link_evolution = {
#     "Raichu" : "https://th.bing.com/th/id/OIP.odEpQFpV8Sg36niYBTNhbAHaHa?pid=ImgDet&rs=1",
#     "Charmeleon" : "https://th.bing.com/th/id/R.85fcab847827a839ccbf63c13acce7cf?rik=leNOOqWxcX2m7w&riu=http%3a%2f%2fwww.pokemasters.net%2fpokedex%2fimages%2fpokemon%2f5000.png&ehk=jm6TYNyPRGGFUdVlXtMaXh7omdy0r8qxp6pL17EB2N4%3d&risl=&pid=ImgRaw&r=0",
#     "Wartortle" : "https://img.pokemondb.net/artwork/large/wartortle.jpg",
#     "Ivysaur" : "https://th.bing.com/th/id/R.dcf25959e2fe6a40ab96570d65bbcfae?rik=HxI8CqhvU0hE7A&riu=http%3a%2f%2fvignette3.wikia.nocookie.net%2fnintendo%2fimages%2f8%2f86%2fIvysaur.png%2frevision%2flatest%3fcb%3d20141002083450%26path-prefix%3den&ehk=GL1go%2b4ytubCdRvwCZgElDzG5EbIsxNqrX1GQ8Y%2bXt0%3d&risl=&pid=ImgRaw&r=0",
#     "Quilava" : "https://th.bing.com/th/id/R.356bb2f6c017c951bdfc71c6391a7133?rik=%2b8ik2w374vzAiQ&riu=http%3a%2f%2fvignette2.wikia.nocookie.net%2fsonic-pokemon-unipedia%2fimages%2f4%2f44%2f188-1.png%2frevision%2flatest%3fcb%3d20140509210523&ehk=0VYP2Lanyh6umAzTraFxlQyS8P2SLyfPgv%2fgp%2fB3Gr4%3d&risl=&pid=ImgRaw&r=0",
#     "Croconaw" : "https://th.bing.com/th/id/R.e56886ba4f0cc10136f4432e98481eb0?rik=RbZa44%2fiSEARGw&riu=http%3a%2f%2f2.bp.blogspot.com%2f-zpn47JnUBvA%2fT_mPxkEKMKI%2fAAAAAAAAPfY%2fN8fbR3G9QKM%2fs1600%2f159Croconaw%2bwater%2bpokemon%2b2nd%2bgen%2bgold%2band%2bsilver%2bnintendo.png&ehk=RYFrwbdZsofUbEfe%2bPBHPjr3wkWa%2bi0DSvMwrJt07zI%3d&risl=&pid=ImgRaw&r=0",
#     "Bayleef" : "https://vignette.wikia.nocookie.net/pokemony/images/1/1b/Bayleef.png/revision/latest?cb=20150824101826&path-prefix=pl",
#     "Combusken" : "https://th.bing.com/th/id/R.558045b6df76691ad6ab4c51f2a2b92f?rik=W6B%2fCZYDN%2brPmQ&riu=http%3a%2f%2fwww.pokemasters.net%2fpokedex%2fimages%2fpokemon%2f256000.png&ehk=5s4L5ovJg9H18bsBzjNATrbKm5%2bc6NMZNqQK4lrTZjY%3d&risl=&pid=ImgRaw&r=0",
#     "Marshtomp" : "https://th.bing.com/th/id/OIP.7zqqJZIT8ugoFb2dE6w97AHaIj?pid=ImgDet&rs=1",
#     "Grovyle" : "https://img.pokemondb.net/artwork/large/grovyle.jpg",
#     "Monferno" : "https://img.pokemondb.net/artwork/large/monferno.jpg",
#     "Prinplup" : "https://th.bing.com/th/id/OIP.lTAlqPOC20BiU3mp95ojeAHaHa?pid=ImgDet&rs=1",
#     "Grotle" : "https://th.bing.com/th/id/OIP.qo9SSVMA6yoy7Glp-uaJWwHaHa?pid=ImgDet&rs=1"
# }

poke_link_evolution = {
    "Raichu" : "https://images.wikidexcdn.net/mwuploads/wikidex/3/34/latest/20160815220038/Raichu.png",
    "Beheeyem" : "https://vignette.wikia.nocookie.net/es.pokemon/images/a/a6/Beheeyem.png/revision/latest?cb=20170615174834",
    "Mienshao" : "https://assets.pokemon.com/assets/cms2/img/pokedex/full/620.png",
    "Fraxure" : "https://th.bing.com/th/id/R.9b6c55a509fd797837aed333cfb36c05?rik=T1dQuRr0FJnVXw&riu=http%3a%2f%2fstatic.pokemonpets.com%2fimages%2fmonsters-images-300-300%2f611-Fraxure.png&ehk=NYSK4moO%2bF3SFfeDrM8AzAUKjK%2f0z5Hg5RAtpSFcaqk%3d&risl=&pid=ImgRaw&r=0",
    "Meowstic" : "https://vignette.wikia.nocookie.net/pokemony/images/0/0b/Meowstic.png/revision/latest?cb=20160529081619&path-prefix=pl",
    "Pangoro" : "https://orig00.deviantart.net/8ac2/f/2017/072/3/5/pangoro_by_porygon2z-db2660z.png",
    "Sliggoo" : "https://th.bing.com/th/id/R.a2ed1883d635ee8d8eb67fce891f6593?rik=UEsVrdADEkhf9A&riu=http%3a%2f%2fcdn3.bulbagarden.net%2fuploads%2fpokemonsunmoon%2fpokemon_stat%2fimage%2f791%2f705Sliggoo.png&ehk=MoBR9TeasfjCE1aq%2fbCZ6AFMEqZcUtkg93qk278LDp8%3d&risl=&pid=ImgRaw&r=0",
    "Cosmoem" : "https://th.bing.com/th/id/R.9d20b4cab9dbebbd139e3da1aaa0219a?rik=pMD5muAzEiFpfQ&pid=ImgRaw&r=0",
    "Crabominable" : "https://www.pokepedia.fr/images/a/a4/Crabominable-SL.png",
    "Hakamo-o" : "https://images.wikidexcdn.net/mwuploads/wikidex/thumb/f/fc/latest/20161014162123/Hakamo-o.png/1200px-Hakamo-o.png",
}

# poke_number = {
#     "Pikachu" : "025",
#     "Charmander" : "004",
#     "Squirtle" : "007",
#     "Bulbasaur" : "001",
#     "Cyndaquil" : "155",
#     "Totodile" : "158",
#     "Chikorita" : "152",
#     "Torchic" : "255",
#     "Mudkip" : "258",
#     "Treecko" : "252",
#     "Chimchar" : "390",
#     "Piplup" : "393",
#     "Turtwig" : "387"
# }

poke_number = {
    "Pikachu" : "025",
    "Elgyem" : "605",
    "Mienfoo" : "619",
    "Axew" : "610",
    "Espurr" : "677",
    "Pancham" : "674",
    "Goomy" : "704",
    "Cosmog" : "789",
    "Crabrawler" : "739",
    "Jangmo-o" : "782"
}

# poke_evolution = {
#     "Pikachu" : "Raichu",
#     "Charmander" : "Charmeleon",
#     "Squirtle" : "Wartortle",
#     "Bulbasaur" : "Ivysaur",
#     "Cyndaquil" : "Quilava",
#     "Totodile" : "Croconaw",
#     "Chikorita" : "Bayleef",
#     "Torchic" : "Combusken",
#     "Mudkip" : "Marshtomp",
#     "Treecko" : "Grovyle",
#     "Chimchar" : "Monferno",
#     "Piplup" : "Prinplup",
#     "Turtwig" : "Grotle"
# }

poke_evolution = {
    "Pikachu" : "Raichu",
    "Elgyem" : "Beheeyem",
    "Mienfoo" : "Mienshao",
    "Axew" : "Fraxure",
    "Espurr" : "Meowstic",
    "Pancham" : "Pangoro",
    "Goomy" : "Sliggoo",
    "Cosmog" : "Cosmoem",
    "Crabrawler" : "Crabominable",
    "Jangmo-o" : "Hakamo-o"
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