from flask import url_for
from flask_testing import TestCase

from service_2.app import app, poke_region

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_region(self):

        for i in range(0,20):
            response = self.client.get(url_for('get_region'))

            self.assert200(response)
            self.assertIn(response.data.decode(), poke_region)
