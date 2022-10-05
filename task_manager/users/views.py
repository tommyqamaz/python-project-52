from django.views.generic import ListView
from django.contrib.auth.models import User


class UsersView(ListView):
    model = User
    context_object_name = "user_list"
    template_name = "users/user_list.html"


class CreateView(ListView):
    pass


class LoginView(ListView):
    pass
