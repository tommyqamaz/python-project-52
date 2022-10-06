# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractUser):
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)

    def __str__(self):
        """String representation of user model."""
        return self.get_full_name()
