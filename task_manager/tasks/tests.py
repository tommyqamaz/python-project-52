from django.test import TestCase
from task_manager.users.models import MyUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from .models import Task
from django.urls import reverse
from django import test


@test.modify_settings(
    MIDDLEWARE={
        "remove": [
            "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
        ]
    }
)
class TaskTest(TestCase):
    fixtures = ["user.json", "status.json", "task.json", "label.json"]

    def setUp(self):
        self.user = MyUser.objects.last()
        self.task = Task.objects.last()
        self.status = Status.objects.last()
        self.labels = Label.objects.last()
        self.client.force_login(self.user)

    def test_setup(self):
        self.assertEqual(self.task.pk, 77)
        self.assertEqual(self.user.pk, 777)
        self.assertEqual(self.status.pk, 100)
        self.assertEqual(self.labels.pk, 1)

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
            "description": "description for task_test2",
            "status": self.status.pk,
            "executor": self.user.pk,
            "labels": self.labels.pk,
        }

        response = self.client.post(reverse("tasks:create_task"), new_task_create_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)

        task = Task.objects.last()
        self.assertEqual(task.name, "name_test2")
        self.assertEqual(task.description, "description for task_test2")
        self.assertEqual(task.status.name, "status_test")
        self.assertEqual(task.executor.username, "username_test")
        self.assertEqual(task.author.username, "username_test")
        self.assertEqual(task.labels.all()[0].name, "label_test")

    def test_delete_task(self):
        response = self.client.get(
            reverse("tasks:delete_task", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="tasks/delete.html")

        response = self.client.post(
            reverse("tasks:delete_task", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_update_task(self):
        new_user = MyUser.objects.create(
            username="newbie",
            first_name="new",
            last_name="bie",
            password="secret",
        )

        new_label = Label.objects.create(name="new")

        update_task_create_data = {
            "name": "name_update2",
            "description": "description for task_update2",
            "status": self.status.pk,
            "executor": new_user.pk,
            "labels": {self.labels.pk, new_label.pk},
        }

        response = self.client.get(
            reverse("tasks:update_task", kwargs={"pk": self.task.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="tasks/update.html")

        response = self.client.post(
            reverse("tasks:update_task", kwargs={"pk": self.task.pk}),
            update_task_create_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.last()
        self.assertEqual(task.name, "name_update2")
        self.assertEqual(task.description, "description for task_update2")
        self.assertEqual(task.status.name, "status_test")
        self.assertEqual(task.author.username, "username_test")

        self.assertEqual(task.executor.pk, new_user.pk)

        self.assertEqual(task.labels.last().name, "new")
        self.assertEqual(task.labels.count(), 2)

    def test_detail_task(self):
        response = self.client.get(
            reverse("tasks:detail_task", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="tasks/detail.html")
