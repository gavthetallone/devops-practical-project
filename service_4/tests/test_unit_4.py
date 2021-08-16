from flask import url_for
from flask_testing import TestCase
import requests

from service_4.app import app, poke_dict_region

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_post_name(self):

        region = "Unova"
        pokemon_type = "Psychic"

        payload = {'region' : region, 'pokemon_type' : pokemon_type}
        response = self.client.post(url_for('post_name'), json=payload)

        self.assert200(response)
        
        expected_name = poke_dict_region[region][pokemon_type]
        self.assertEqual(response.data.decode(), expected_name)