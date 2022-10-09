from django.forms import ModelForm
from .models import Task
from django import forms


class CreateTaskForm(ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"style": "height: 13em; resize: none;"})
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "status",
            "executor",
            # "labels",
        )
