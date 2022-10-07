from django.test import TestCase
from task_manager.users.models import MyUser
from task_manager.statuses.models import Status
from django.urls import reverse


class StatusesTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            username="test", password="12test12", first_name="bla", last_name="blabla"
        )
        self.status = Status.objects.create(name="test11")

    def test_status_page(self):
        response = self.client.get(reverse("statuses:status_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="statuses/status_list.html")

    def test_create_status(self):
        response = self.client.post(
            reverse("statuses:create_status"), {"name": "test_status228"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)
        self.assertEqual(Status.objects.last().name, "test_status228")

    def test_update_status_unauthorized(self):
        response = self.client.post(
            reverse("statuses:update_status", kwargs={"pk": self.status.id}),
            {"name": "bipki"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("statuses:status_list"))
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, "test11")

    def test_update_status_authorized(self):
        status = Status.objects.create(name="test111")
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("statuses:update_status", kwargs={"pk": self.status.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="statuses/update.html")

        response = self.client.post(
            reverse("statuses:update_status", kwargs={"pk": status.id}),
            {"name": "bipki"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("statuses:status_list"))
        status.refresh_from_db()
        self.assertEqual(status.name, "bipki")
        self.client.logout()

    def test_delete_status(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("statuses:delete_status", kwargs={"pk": self.status.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="statuses/delete.html")
        response = self.client.post(
            reverse("statuses:delete_status", kwargs={"pk": self.status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 0)
