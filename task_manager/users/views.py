from .forms import NewUserForm
from .models import MyUser

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    # AccessMixin,
)

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class UsersView(ListView):
    model = MyUser
    context_object_name = "user_list"
    template_name = "users/user_list.html"


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    form_class = NewUserForm
    success_message = _("Your profile was successfully created")


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")
    success_message = _("You are logged in")


class LogoutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _("You are logged out"))
        return response


class UpdateUserView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = MyUser
    success_url = reverse_lazy("users:user_list")
    template_name = "users/update.html"
    form_class = NewUserForm
    success_message = _("The user has been successfully updated")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def test_func(self):
        return self.request.user.pk == self.get_object().pk

    def handle_no_permission(self):
        messages.error(
            self.request, _("You don't have the rights to change another user")
        )
        return redirect("users:user_list")


class DeleteUserView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = MyUser
    success_url = reverse_lazy("users:user_list")
    template_name = "users/delete.html"
    success_message = _("The user has been successfully deleted")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def test_func(self):
        return self.request.user.pk == self.get_object().pk

    def handle_no_permission(self):
        messages.error(
            self.request, _("You don't have the rights to delete another user")
        )
        return redirect("users:user_list")
