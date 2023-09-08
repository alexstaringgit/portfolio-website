from django.shortcuts import render

def index(request):
    return render(request, "landingpage/index.html")


def projects(request):
    return render(request, "landingpage/projects.html")