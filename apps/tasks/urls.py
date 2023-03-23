from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.ListTaskListView.as_view(), name='tasks-list'),
    path('create-task', views.CreateTaskCreateView.as_view(), name='create-task'),
    path('update-task/<pk>', views.UpdateTaskUpdateView.as_view(), name='update-task'),
    path('delete-task/<pk>', views.DeleteTaskDeleteView.as_view(), name='delete-task'),
]
