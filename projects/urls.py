from django.urls import path
from projects.views import list_view

urlpatterns = [(path("", list_view, name="list_view"))]
