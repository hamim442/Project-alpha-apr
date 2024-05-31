from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = TaskForm()
    context = {"create_task": form}
    return render(request, "tasks/createTask.html", context)


@login_required
def task_list_view(request):
    task_list = Task.objects.filter(assignee=request.user)
    context = {"task_list": task_list}
    return render(request, "tasks/task_list.html", context)
