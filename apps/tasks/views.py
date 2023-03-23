from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm



class ListTaskListView(ListView):
    """
    Class that allow to list tasks
    """
    queryset = Task.objects.all()
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'


class CreateTaskCreateView(CreateView):
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


class UpdateTaskUpdateView(UpdateView):
    """
    Class that allow to update a task
    """
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:tasks-list')


class DeleteTaskDeleteView(DeleteView):
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

