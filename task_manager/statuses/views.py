# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Status
from django.utils.translation import gettext_lazy as _

from .forms import CreateStatusForm


class StatusView(ListView):
    model = Status
    context_object_name = "status_list"
    template_name = "statuses/statuses_list.html"


class CreateStatusView(SuccessMessageMixin, CreateView):
    template_name = "statuses/create.html"
    success_url = reverse_lazy("index")
    form_class = CreateStatusForm
    success_message = _("Status created successfully")

    # change dublication in templates and add translate in views
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["to_do"] = "create"
    #     context["status"] = "Status"
    #     return context


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    success_url = reverse_lazy("statuses:status_list")
    template_name = "statuses/update.html"
    form_class = CreateStatusForm
    success_message = _("Status updated successfully")
    login_url = reverse_lazy("statuses:status_list")
    redirect_field_name = None


class DeleteStatusView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy("statuses:status_list")
    template_name = "statuses/delete.html"
    success_message = _("Status deleted successfully")
    login_url = reverse_lazy("login")
    redirect_field_name = None
