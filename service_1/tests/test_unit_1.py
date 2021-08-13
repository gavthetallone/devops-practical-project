from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from service_1.application import app, db
from service_1.application.models import Pokemon

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///"
        )
        return app
    
    def setUp(self):
        db.create_all()

        db.session.add(Pokemon(name="Bulbasaur", type="Grass", region="Kanto", link="", number="", evolution="", link_evolution=""))
        db.session.add(Pokemon(name="Charmander", type="Fire", region="Kanto", link="", number="", evolution="", link_evolution=""))

    def tearDown(self):
        db.drop_all()

class TestViews(TestBase):
    def test_start(self):
        response = self.client.get(url_for("start"))
        self.assert200(response)
    
class TestResponse(TestBase):

    def test_home(self):

        with mock() as m:
            m.get('http://service-2:5000/get/region', text='Kanto')
            m.get('http://service-3:5000/get/pokemon_type', text='Electric')
            m.post('http://service-4:5000/post/name', text='Pikachu')

            response = self.client.get(url_for('home'))
        
        self.assert200(response)

        self.assertIn('Pikachu', response.data.decode())
        self.assertIn('Kanto', response.data.decode())
        self.assertIn('Electric', response.data.decode())
    
    def test_form(self):

        with mock() as m:
            m.get('http://service-2:5000/get/region', text='Kanto')
            m.get('http://service-3:5000/get/pokemon_type', text='Electric')
            m.post('http://service-4:5000/post/name', text='Pikachu')

            response = self.client.post(url_for('home'), 
        
                data = dict(
                    poke_order = "#",
                    poke_type = "Electric",
                    poke_region = "Kanto"
                )
            )
        
        self.assert200(response)
        self.assertIn('Pikachu', response.data.decode())
        self.assertIn('Kanto', response.data.decode())
        self.assertIn('Electric', response.data.decode())


class TestDelete(TestBase):

    def test_delete_pokemon(self):

        response = self.client.get(
            url_for("delete_pokemon", id=1),
            follow_redirects=True
        )
        
        self.assert200(response)
        assert "Bulbasaur" not in response.data.decode()
        self.assertIn('Charmander', response.data.decode())