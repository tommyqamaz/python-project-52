from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import MyUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        max_length=150,
        null=False,
        blank=False,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    executor = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Исполнитель",
        related_name="executors",
    )
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="authors",
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        verbose_name="Метки",
        related_name="labels",
        through="TaskLabels",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
