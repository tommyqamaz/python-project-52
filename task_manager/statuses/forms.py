from django import forms
from .models import Status
from django.utils.translation import gettext_lazy as _


class CreateStatusForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label=_("Name"))

    class Meta:
        model = Status
        fields = ("name",)
