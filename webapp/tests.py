import os
import django
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()


class TestTaskAPITestCase(APITestCase):
    def setUp(self):
        self.token_url = reverse('token_obtain_pair')
        self.task_url = reverse('task-list')
        self.username = 'admin'
        self.password = 'taskapi'

        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

        self.authenticate()

        self.task = Task.objects.create(
            title='Initial Task',
            description='Setup task',
            status='Started',
            due_date='2025-06-01',
        )

    def authenticate(self):
        response = self.client.post(self.token_url, {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def test_create_task_authenticated(self):
        data = {
            'title': 'Test Task',
            'description': 'Test description',
            'status': 'Started',
            'due_date': '2025-06-01'
        }
        response = self.client.post(self.task_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_create_task_unauthenticated(self):
        self.client.credentials()
        data = {
            'title': 'No Auth Task',
            'status': 'In progress',
            'due_date': '2025-06-01'
        }
        response = self.client.post(self.task_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_task_status(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.patch(url, {'status': 'Done'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, 'Done')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
