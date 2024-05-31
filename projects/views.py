from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from tasks.models import Task

# Create your views here.


@login_required
def detail_view(request, id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project=project)
    context = {"project_object": project, "task": task}
    return render(request, "projects/detail.html", context)


@login_required
def list_view(request):
    project = Project.objects.filter(owner=request.user)
    context = {"list_view": project}
    return render(request, "projects/list.html", context)
