from .views import UsersView, SignUpView
from django.urls import path


app_name = "users"

urlpatterns = [
    path("", UsersView.as_view(), name="user_list"),
    path("create", SignUpView.as_view(), name="create"),
]
