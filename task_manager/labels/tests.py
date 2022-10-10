from django.test import TestCase
from task_manager.users.models import MyUser
from task_manager.labels.models import Label
from django.urls import reverse
from django import test


@test.modify_settings(
    MIDDLEWARE={
        "remove": [
            "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
        ]
    }
)
class LabelsTest(TestCase):
    fixtures = ["user.json"]

    def setUp(self):
        self.label = Label.objects.create(name="test")
        self.user = MyUser.objects.last()

    def test_label_page(self):
        response = self.client.get(reverse("labels:label_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="labels/label_list.html")

    def test_create_label(self):
        self.assertEqual(Label.objects.count(), 1)
        response = self.client.post(
            reverse("labels:create_label"), {"name": "test_label"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), 2)
        self.assertEqual(Label.objects.last().name, "test_label")

    def test_update_label_unauthorized(self):
        self.client.logout()
        response = self.client.post(
            reverse("labels:update_label", kwargs={"pk": self.label.id}),
            {"name": "bipki"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("labels:label_list"))
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, "test")

    def test_update_label_authorized(self):
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("labels:update_label", kwargs={"pk": self.label.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="labels/update.html")

        response = self.client.post(
            reverse("labels:update_label", kwargs={"pk": self.label.id}),
            {"name": "bipki"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("labels:label_list"))
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, "bipki")
        self.client.logout()

    def test_delete_label(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("labels:delete_label", kwargs={"pk": self.label.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="labels/delete.html")
        response = self.client.post(
            reverse("labels:delete_label", kwargs={"pk": self.label.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), 0)
