from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.utils.translation import gettext_lazy as _

# Create your forms here.


class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = _(
            "<ul><li>Your password should contain at least 3 symbols.</li></ul>"
        )

    first_name = forms.CharField(max_length=30, required=True, label=_("First name"))
    last_name = forms.CharField(max_length=30, required=True, label=_("Last name"))

    class Meta:
        model = MyUser
        fields = ("first_name", "last_name", "username", "password1", "password2")
