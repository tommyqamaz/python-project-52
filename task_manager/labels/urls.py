from django.urls import path
from .views import LabelView, CreateLabelView, UpdateLabelView, DeleteLabelView

app_name = "labels"

urlpatterns = [
    path("", LabelView.as_view(), name="label_list"),
    path("create", CreateLabelView.as_view(), name="create_label"),
    path("<int:pk>/delete", DeleteLabelView.as_view(), name="delete_label"),
    path("<int:pk>/update", UpdateLabelView.as_view(), name="update_label"),
]
