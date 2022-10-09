from django import forms
from .models import Label
from django.utils.translation import gettext_lazy as _


class CreateLabelForm(forms.ModelForm):
    name = forms.CharField(max_length=40, label=_("Name"))

    class Meta:
        model = Label
        fields = ("name",)
