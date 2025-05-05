from rest_framework.test import APITestCase
from rest_framework import status

class SimpleTest(APITestCase):
    def test_process_endpoint(self):
        response = self.client.post('/api/process/', {'email': 'test@example.com', 'message': 'Hello!'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
