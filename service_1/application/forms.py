from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class PokeForm(FlaskForm):
    # poke_type = SelectField("Filter by type:", choices=["All", "Electric", "Fire", "Water", "Grass"])
    poke_type = SelectField("Filter by type:", choices=["All", "Electric", "Psychic", "Fighting", "Dragon"])
    # poke_region = SelectField("Filter by region:", choices=["All", "Kanto", "Johto", "Hoenn", "Sinnoh"])
    poke_region = SelectField("Filter by region:", choices=["All", "Kanto", "Unova", "Kalos", "Alola"])
    poke_order = SelectField("Order by:", choices=["", "#", "Name"])
    submit = SubmitField("Submit")