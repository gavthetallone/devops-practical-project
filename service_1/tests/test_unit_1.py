from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from service_1.application import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///"
        )
        return app
    
    def setUp(self):
        db.create_all()
    
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