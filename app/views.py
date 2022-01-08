from django.shortcuts import render, HttpResponse
from users.models import Project

# Create your views here.


def home(request):
    context = {}
    project = Project.objects.all()
    context['pobj'] = project

    return render(request, "app/index.html", context)
