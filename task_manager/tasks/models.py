from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import MyUser
from task_manager.statuses.models import Status


class Task(models.Model):
    author = models.ForeignKey(
        MyUser, on_delete=models.PROTECT, null=False, related_name="author"
    )
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=256)
    executor = models.ForeignKey(
        MyUser, on_delete=models.PROTECT, null=False, related_name="executor"
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=False)

    class Meta(object):
        verbose_name = "task"

    def __str__(self):
        return self.name
