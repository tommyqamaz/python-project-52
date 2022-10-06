from django.contrib.auth.models import User
from .forms import NewUserForm

from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class UsersView(ListView):
    model = User
    context_object_name = "user_list"
    template_name = "users/user_list.html"


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    form_class = NewUserForm
    success_message = _("Ваш профиль успешно создан")


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = "users/login.html"
    success_message = _("Вы залогинены")


class LogoutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _("Вы разлогинены"))
        return response
