from django.test import TestCase
from .models import MyUser

# from django.urls import reverse


class UserTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            first_name="Ivan",
            last_name="John",
            username="testuser",
            email="test@email.com",
            password="secret",
        )

    def test_availability(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/user_list.html")

    def test_create_user(self):
        pass

    def test_update_user(self):
        pass

    def test_delete_user(self):
        pass
