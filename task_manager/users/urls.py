from .views import UsersView, create, login_user
from django.urls import path


app_name = "users"

urlpatterns = [
    path("", UsersView.as_view(), name="user_list"),
    path("create", create, name="create"),
    path("login", login_user, name="login"),
]
