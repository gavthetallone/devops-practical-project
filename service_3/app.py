from flask import Flask
import random

app = Flask(__name__)

poke_type = ["Fire", "Water", "Grass"]

@app.route("/get/pokemon_type")
def get_type():
    return random.choice(poke_type)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')