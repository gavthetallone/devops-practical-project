from flask import Flask
import random

app = Flask(__name__)

poke_region = ["Kanto", "Johto", "Hoenn", "Sinnoh"]

@app.route("/get/region")
def get_region():
    return random.choice(poke_region)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')