from django.shortcuts import render, HttpResponse, redirect
from users.models import Project
from users.forms import ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login/")
def home(request):
    context = {}
    project = Project.objects.all()

    context['pobj'] = project

    return render(request, "app/index.html", context)


@login_required(login_url="/login/")
def like(request, id):

    project = Project.objects.get(id=id)

    if request.method == 'POST':
        if request.user in project.flame.all():
            project.flame.remove(request.user)
        else:
            project.flame.add(request.user)
    return redirect('home')


@login_required(login_url="/login/")
def projectdetail(request, id):
    context = {}
    project = Project.objects.get(id=id)
    context['project'] = project
    context['form'] = ProjectForm(instance=project)
    return render(request, 'app\projectdetail.html', context)


@login_required(login_url="/login/")
def DeletePost(request, id):
    if request.method == 'POST':
        project = Project.objects.get(id=id)
        project.delete()
        return redirect('home')

    else:
        return HttpResponse("<h2>this method is not allowed </h2>")


@login_required(login_url="/login/")
def UpdatePost(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
        print(form.errors)
