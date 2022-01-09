from django.shortcuts import render, HttpResponse
from users.models import Project
from users.forms import ProjectForm

# Create your views here.


def home(request):
    context = {}
    project = Project.objects.all()
    context['pobj'] = project
    context['form'] = ProjectForm()

    return render(request, "app/index.html", context)
