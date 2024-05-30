from django.contrib import admin
from projects.models import Project

# Register your models here.


@admin.register(Project)
class projectAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
