from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Status
from django.utils.translation import gettext_lazy as _

from .forms import CreateTaskForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = "task_list"
    template_name = "tasks/tsks_list.html"


class CreatTaskView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "tasks/create.html"
    success_url = reverse_lazy("index")
    form_class = CreateTaskForm
    success_message = _("Task created successfully")


class DetailTaskView(LoginRequiredMixin, DetailView):
    pass


class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    pass


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    pass
