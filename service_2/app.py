from flask import Flask
import random

app = Flask(__name__)

# poke_region = ["Kanto", "Johto", "Hoenn", "Sinnoh"]
poke_region = ["Unova", "Kalos", "Alola"]

@app.route("/get/region")
def get_region():
    return random.choice(poke_region)

if __name__ == "__main__":
    app.run(host='0.0.0.0')