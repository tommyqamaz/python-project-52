from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTestCase(TestCase):

    fixtures = ["user.json"]

    def setUp(self):
        user_logged = get_user_model().objects.first()
        self.client.force_login(user_logged)

    def test_users_list(self):
        response = self.client.get(reverse("users:user_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="users/user_list.html")

    def test_user_add(self):
        response = self.client.get(reverse("users:create_user"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="users/register.html")
        self.assertEqual(get_user_model().objects.count(), 1)
        user_add = {
            "first_name": "user2_first_name",
            "last_name": "user2_last_name",
            "username": "user2_username",
            "password1": "Nx7sDQ9D",
            "password2": "Nx7sDQ9D",
        }
        response = self.client.post(reverse("users:create_user"), user_add)
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse("login"))

        user = get_user_model().objects.get(username=user_add["username"])
        self.assertEqual(user.username, "user2_username")
        self.assertEqual(get_user_model().objects.count(), 2)

    def test_user_update(self):
        user = get_user_model().objects.first()
        response = self.client.get(reverse("users:update_user", args=[user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="users/update.html")

        user_update_info = {
            "first_name": "user3_first_name",
            "last_name": "user3_last_name",
            "username": "user3_username",
            "password1": "Nx7sDQ9D3",
            "password2": "Nx7sDQ9D3",
        }
        response = self.client.post(
            reverse("users:update_user", args=[user.pk]), user_update_info
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("users:user_list"))

        user_updated = get_user_model().objects.first()
        self.assertEqual(user_updated.first_name, "user3_first_name")
        self.assertTrue(user_updated.check_password("Nx7sDQ9D3"))

    def test_user_delete(self):
        user = get_user_model().objects.first()
        response = self.client.get(reverse("users:delete_user", args=[user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="users/delete.html")

        response = self.client.post(reverse("users:delete_user", args=[user.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.count(), 0)
