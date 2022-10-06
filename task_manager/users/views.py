from .forms import NewUserForm
from django.contrib.auth.models import User

from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    AccessMixin,
)

from django.urls import reverse_lazy
from django.shortcuts import redirect
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


class UpdateUserView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = User
    success_url = reverse_lazy("users:user_list")
    template_name = "users/update.html"
    form_class = NewUserForm
    success_message = _("Пользователь успешно изменён")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def test_func(self):
        return self.request.user.pk == self.get_object().pk

    def handle_no_permission(self):
        messages.error(
            self.request, _("У вас нет прав для изменения другого пользователя.")
        )
        return redirect("users:user_list")


class DeleteUserView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = User
    success_url = reverse_lazy("users:user_list")
    template_name = "users/delete.html"
    success_message = _("Пользователь успешно удалён")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def test_func(self):
        return self.request.user.pk == self.get_object().pk

    def handle_no_permission(self):
        messages.error(
            self.request, _("У вас нет прав для изменения другого пользователя.")
        )
        return redirect("users:user_list")
