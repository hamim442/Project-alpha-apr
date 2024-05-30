from django.shortcuts import render
from projects.models import Project

# Create your views here.


def list_view(request):
    project = Project.objects.all()
    context = {"list_view": project}
    return render(request, "projects/list.html", context)
