import unittest
from flask import Flask
from flask_testing import TestCase

class TestGetRoute(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
    
    def test_get_route_with_id(self):
        teste_id = 1
        response = self.client.get(f'/api/empresa?id={teste_id}')

        #verificando se o codigo de status da resposta é 200
        self.assertEqual(response.status_code, 200)
        

if __name__ == "__main__":
    unittest.main()