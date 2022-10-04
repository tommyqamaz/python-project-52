from .views import UsersView
from django.urls import path

urlpatterns = [
    path("", UsersView.as_view()),
]
