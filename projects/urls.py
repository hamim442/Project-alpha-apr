from django.urls import path
from projects.views import list_view, detail_view, create_project

urlpatterns = [
    path("", list_view, name="list_projects"),
    path("<int:id>/", detail_view, name="show_project"),
    path("create/", create_project, name="create_project"),
]
