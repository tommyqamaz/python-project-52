from django.urls import path
from .views import (
    TaskListView,
    CreatTaskView,
    DetailTaskView,
    DeleteTaskView,
    UpdateTaskView,
)

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create", CreatTaskView.as_view(), name="create_task"),
    path("<int:pk>/", DetailTaskView.as_view(), name="detail_task"),
    path("<int:pk>/delete", DeleteTaskView.as_view(), name="delete_task"),
    path("<int:pk>/update", UpdateTaskView.as_view(), name="update_task"),
]
