from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Task
from .forms import TaskForm



class ListTaskListView(LoginRequiredMixin, ListView):
    """
    Class that allow to list tasks
    """
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        """
        Get new queryset filtering by user
        """
        task_by_user = self.model.objects.filter(user=self.request.user)
        return task_by_user


class CreateTaskCreateView(LoginRequiredMixin, CreateView):
    """
    Class that allow to create a new task
    """
    model = Task
    template_name = 'tasks/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:tasks-list')

    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.user = self.request.user 
        return super().form_valid(form)


class UpdateTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Class that allow to update a task
    """
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:tasks-list')

    def test_func(self):
        """
        Check that only the owner user can update
        """
        return self.get_object().user == self.request.user


class DeleteTaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class that allow to delete a task
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:tasks-list')

    def get(self, *args, **kwargs):
        """
        Override get method for delete task without confirmation and template
        """
        return self.delete(*args, **kwargs)
    
    def test_func(self):
        """
        Check that only the owner user can delete
        """
        return self.get_object().user == self.request.user

