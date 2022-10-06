from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.utils.translation import gettext_lazy as _

# Create your forms here.


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label=_("Имя"))
    last_name = forms.CharField(max_length=30, required=True, label=_("Фамилия"))

    class Meta:
        model = MyUser
        fields = ("first_name", "last_name", "username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
