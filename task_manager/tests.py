from django.test import TestCase


class AppTest(TestCase):
    def test_availability(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
