import unittest
from app import app

class TestApp(unittest.TestCase):

    # This method tests the '/' route
    def test_hello_route(self):
        # Create a test client for the Flask app
        tester = app.test_client(self)
        
        # Send a GET request to the '/' route
        response = tester.get('/')
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response data matches the expected value
        self.assertEqual(response.data, b'First DevOps Project!<br>Git integration success')

if __name__ == '__main__':
    unittest.main()

