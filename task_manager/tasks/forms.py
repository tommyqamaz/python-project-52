from django.forms import ModelForm
from .models import Task
from django import forms
from django.utils.translation import gettext_lazy as _


class CreateTaskForm(ModelForm):
    description = forms.CharField(
        label=_("Task description"),
        widget=forms.Textarea(
            attrs={"style": "height: 13em; resize: none;"},
        ),
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "status",
            "executor",
            "labels",
        )
