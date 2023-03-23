from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Task


User = get_user_model()

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser1',
            password='testpass1',
            email='test1@test.com'
        )
        
        Task.objects.create(
            title='test1',
            description='description1',
            due_date='2023-03-23 1:00:00',
            completed=False,
            user=self.user
        )
        Task.objects.create(
            title='test2',
            description='description2',
            due_date='2023-03-23 2:00:00',
            completed=False,
            user=self.user
        )

    def test_authentication_required_task_list(self):
        response = self.client.get(reverse_lazy('tasks:tasks-list'))
        self.assertEqual(response.status_code, 302)

    def test_authentication_required_create_task(self):
        response = self.client.get(reverse_lazy('tasks:create-task'))
        self.assertEqual(response.status_code, 302)

    def test_authentication_required_update_task(self):
        task = Task.objects.get(pk=1)
        response = self.client.get(reverse_lazy('tasks:update-task', kwargs={'pk': task}))
        self.assertEqual(response.status_code, 302)

    def test_authentication_required_delete_task(self):
        task = Task.objects.get(pk=1)
        response = self.client.get(reverse_lazy('tasks:delete-task', kwargs={'pk': task}))
        self.assertEqual(response.status_code, 302)

    def test_own_user_update_task(self):
        task = Task.objects.filter(user = self.user).first().pk
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse_lazy('tasks:update-task', kwargs={'pk': task}))
        self.assertEqual(response.status_code, 200)

    def test_own_user_delete_task(self):
        task = Task.objects.filter(user = self.user).first().pk
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse_lazy('tasks:delete-task', kwargs={'pk': task}))
        self.assertEqual(response.status_code, 302)
