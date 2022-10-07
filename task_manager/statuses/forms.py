from django import forms
from .models import Status


class CreateStatusForm(forms.ModelForm):
    name = forms.CharField(max_length=30)

    class Meta:
        model = Status
        fields = ("name",)
