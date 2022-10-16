import django_filters
from django_filters import ModelChoiceFilter, BooleanFilter
from django.forms import CheckboxInput

from task_manager.labels.models import Label
from task_manager.tasks.models import Task

from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    labels = ModelChoiceFilter(
        field_name="labels",
        queryset=Label.objects.all(),
        label="Метка",
    )
    self_tasks = BooleanFilter(
        method="filter_tasks",
        widget=CheckboxInput,
        label="Только свои задачи",
    )

    def filter_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = (
            "status",
            "executor",
            "labels",
            "self_tasks",
        )
