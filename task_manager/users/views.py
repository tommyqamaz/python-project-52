from django.views.generic import ListView
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


class UsersView(ListView):
    model = User
    context_object_name = "user_list"
    template_name = "users/user_list.html"


def create(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("task_manager:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="users/register.html",
        context={"register_form": form},
    )


def login_user(request):
    return redirect("task_manager:index")
