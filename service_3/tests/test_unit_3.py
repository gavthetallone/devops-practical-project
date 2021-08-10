from flask import url_for
from flask_testing import TestCase

from service_3.app import app, poke_type

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_type(self):

        for i in range(0,20):
            response = self.client.get(url_for('get_type'))

            self.assert200(response)
            self.assertIn(response.data.decode(), poke_type)