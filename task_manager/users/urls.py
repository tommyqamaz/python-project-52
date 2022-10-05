from .views import UsersView, LoginView, CreateView
from django.urls import path


app_name = "users"

urlpatterns = [
    path("", UsersView.as_view(), name="user_list"),
    path("login/", LoginView.as_view(), name="login"),
    path("create/", CreateView.as_view(), name="create"),
]
