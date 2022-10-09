from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(_("Creation date"), auto_now_add=True)
