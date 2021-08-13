from flask import Flask
import random

app = Flask(__name__)

# poke_type = ["Fire", "Water", "Grass"]
poke_type = ["Psychic", "Fighting", "Dragon"]

@app.route("/get/pokemon_type")
def get_type():
    return random.choice(poke_type)

if __name__ == "__main__":
    app.run(host='0.0.0.0')