from . import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    region = db.Column(db.String(10), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    evolution = db.Column(db.String(50), nullable=False)
    link_evolution = db.Column(db.String(350), nullable=False)