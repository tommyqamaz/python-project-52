from django.urls import path, include
from .views import StatusView, CreateStatusView, UpdateStatusView, DeleteStatusView

app_name = "statuses"

urlpatterns = [
    path("", StatusView.as_view(), name="status_list"),
    path("create", CreateStatusView.as_view(), name="create_status"),
    path("<int:pk>/delete", DeleteStatusView.as_view(), name="delete_status"),
    path("<int:pk>/update", UpdateStatusView.as_view(), name="update_status"),
]
