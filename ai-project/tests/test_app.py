import unittest
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the AI Project', response.data)

    def test_model_prediction(self):
        response = self.app.post('/predict', json={'data': [1, 2, 3]})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'prediction', response.data)

if __name__ == '__main__':
    unittest.main()