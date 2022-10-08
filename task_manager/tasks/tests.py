from django.test import TestCase
from task_manager.users.models import MyUser
from task_manager.statuses.models import Status
from .models import Task
from django.urls import reverse


class TaskTest(TestCase):
    fixtures = ["user.json", "status.json", "task.json"]

    def setUp(self):
        self.user = MyUser.objects.last()
        self.task = Task.objects.last()
        self.status = Status.objects.last()
        self.client.force_login(self.user)

    def test_setup(self):
        self.assertEqual(self.task.pk, 77)
        self.assertEqual(self.user.pk, 777)
        self.assertEqual(self.status.pk, 100)

    def test_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse("tasks:task_list"))
        self.assertEqual(response.status_code, 302)

    def test_task_page(self):
        response = self.client.get(reverse("tasks:task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="tasks/task_list.html")

    def test_get_create_task(self):
        response = self.client.get(reverse("tasks:create_task"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="tasks/create.html")

    def test_post_create_task(self):
        new_task_create_data = {
            "name": "name_test2",
            "description": "describe for task_test2",
            "status": self.status.pk,
            "executor": self.user.pk,
        }

        response = self.client.post(reverse("tasks:create_task"), new_task_create_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)

        task = Task.objects.last()
        self.assertEqual(task.name, "name_test2")
        self.assertEqual(task.description, "describe for task_test2")
        self.assertEqual(task.status.name, "status_test")
        self.assertEqual(task.executor.username, "username_test")
        self.assertEqual(task.author.username, "username_test")

    def test_delete_task():
        pass
