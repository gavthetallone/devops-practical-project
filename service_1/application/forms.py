from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class PokeForm(FlaskForm):
    poke_type = SelectField("Filter by type:", choices=["All", "Electric", "Fire", "Water", "Grass"])
    poke_region = SelectField("Filter by region:", choices=["All", "Kanto", "Johto", "Hoenn", "Sinnoh"])
    poke_order = SelectField("Order by:", choices=["", "#", "Name"])
    submit = SubmitField("Submit")