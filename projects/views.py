from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_view(request):
    project = Project.objects.filter(owner=request.user)
    context = {"list_view": project}
    return render(request, "projects/list.html", context)
