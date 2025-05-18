from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm
from .services import get_all_tasks, create_task, update_task, delete_task
import logging

logger = logging.getLogger(__name__)

ms_identity_web = settings.MS_IDENTITY_WEB


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def unauth_401(request):
    # redirecting unauthenticated users
    return render(request, "auth/401.html")


@ms_identity_web.login_required
def index(request):
    tasks = get_all_tasks()
    return render(request, "webapp/dashboard.html", {'tasks': tasks})


@ms_identity_web.login_required
def dashboard(request):
    tasks = get_all_tasks()
    return render(request, 'webapp/dashboard.html', {'tasks': tasks})


@ms_identity_web.login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        try:
            create_task(title, description, status, due_date)
            messages.success(request, "Task added successfully!")
        except Exception as e:
            logger.exception(f"Failed to add task: {e}")
            messages.error(request, "Failed to add task")
    return redirect('dashboard')


@ms_identity_web.login_required
def update_task_status(request, task_id):
    if request.method == 'POST':
        try:
            status = request.POST.get('status')
            update_task(task_id, status)
            messages.success(request, "Task updated successfully!")
        except Exception as e:
            logger.exception(f"Failed to update task: {e}")
            messages.error(request, "Failed to uppdate task")
    return redirect('dashboard')


@ms_identity_web.login_required
def delete_user_task(request, task_id):
    if request.method == 'POST':
        try:
            delete_task(task_id)
            messages.success(request, "Task deleted successfully!")
        except Exception as e:
            logger.exception(f"Failed to delete task: {e}")
            messages.error(request, "Failed to delete task")
    return redirect('dashboard')
