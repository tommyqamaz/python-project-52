from .views import UsersView, SignUpView, DeleteUserView, UpdateUserView
from django.urls import path


app_name = "users"

urlpatterns = [
    path("", UsersView.as_view(), name="user_list"),
    path("create", SignUpView.as_view(), name="create_user"),
    path("<int:pk>/delete", DeleteUserView.as_view(), name="delete_user"),
    path("<int:pk>/update", UpdateUserView.as_view(), name="update_user"),
]
