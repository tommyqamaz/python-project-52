from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import MyUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    author = models.ForeignKey(
        MyUser,
        on_delete=models.PROTECT,
        null=False,
        related_name="author",
        verbose_name=_("Author"),
    )
    created_at = models.DateTimeField(_("Creation date"), auto_now_add=True)

    name = models.CharField(_("Name"), max_length=40, unique=True)
    description = models.CharField(_("Description"), max_length=256)
    executor = models.ForeignKey(
        MyUser,
        verbose_name=_("Executor"),
        on_delete=models.PROTECT,
        null=True,
        related_name="executor",
    )
    status = models.ForeignKey(
        Status, verbose_name=_("Status"), on_delete=models.PROTECT, null=False
    )

    label = models.ManyToManyField(Label, verbose_name=_("Label"), through="TaskLabels")

    class Meta(object):
        verbose_name = "task"

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
