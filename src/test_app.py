import unittest
import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
    
    def test_hello_world_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Pagina de Prueba')
    
    def test_invalid_route(self):
        response = self.app.get("/invalid")
        self.assertEqual(response.status_code, 404)


if __name__== '__main__':
    unittest.main()
