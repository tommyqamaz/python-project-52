from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(_("Creation date"), auto_now_add=True)

    class Meta(object):
        verbose_name = "status"
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.name
