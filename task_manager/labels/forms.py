from django import forms
from .models import Label


class CreateLabelForm(forms.ModelForm):
    name = forms.CharField(max_length=40)

    class Meta:
        model = Label
        fields = ("name",)
