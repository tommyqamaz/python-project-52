from django.test import TestCase
from task_manager.users.models import MyUser
from .models import Task
from django.urls import reverse


class TaskTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            username="test", password="12test12", first_name="bla", last_name="blabla"
        )
        self.status = Task.objects.create(name="test11")

    def test_status_page(self):
        response = self.client.get(reverse("tasks:task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="tasks/task_list.html")

    def test_create_status(self):
        response = self.client.post(
            reverse("tasks:create_task"), {"name": "test_status228"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.last().name, "test_status228")
