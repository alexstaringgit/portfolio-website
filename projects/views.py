from django.shortcuts import render
from .models import Project

def overview(request):
    project_list = Project.objects.all()
    return render(request, "projects/overview.html", {
        "project_list": project_list
    })