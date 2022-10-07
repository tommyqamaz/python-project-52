from django.contrib import admin
from django.urls import path, include
from task_manager import views
from .users.views import LoginUserView, LogoutUserView
from django.conf import settings
from django.conf.urls.static import static

app_name = "task_manager"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("users/", include("task_manager.users.urls"), name="users"),
    path("statuses/", include("task_manager.statuses.urls"), name="statuses"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
