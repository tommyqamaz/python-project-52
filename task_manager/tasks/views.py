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
from django.utils.translation import gettext_lazy as _

from .forms import CreateTaskForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"


class CreatTaskView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "tasks/create.html"
    success_url = reverse_lazy("index")
    form_class = CreateTaskForm
    success_message = _("Task created successfully")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailTaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"


class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task_list")
    template_name = "tasks/delete.html"
    success_message = _("Task deleted successfully")
    login_url = reverse_lazy("login")
    redirect_field_name = None


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("tasks:task_list")
    template_name = "statuses/update.html"
    form_class = CreateTaskForm
    success_message = _("Task updated successfully")
    login_url = reverse_lazy("tasks:task_list")
    redirect_field_name = None
