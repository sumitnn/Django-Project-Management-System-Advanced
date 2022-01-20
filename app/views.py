from django.shortcuts import render, HttpResponse
from users.models import Project
from users.forms import ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login/")
def home(request):
    context = {}
    project = Project.objects.all()

    context['pobj'] = project
    context['form'] = ProjectForm()

    return render(request, "app/index.html", context)


def like(request, id):
    pass
