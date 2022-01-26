from django.shortcuts import render, HttpResponse, redirect
from users.models import Project, Comment
from users.forms import ProjectForm
from django.contrib.auth.decorators import login_required
from users.models import CreateAccount

# Create your views here.


@login_required(login_url="/login/")
def home(request):
    context = {}
    project = Project.objects.all()

    context['pobj'] = project
    context['users'] = CreateAccount.objects.all()

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
    context['comments'] = Comment.objects.filter(project=project)
    context['lenofcomment'] = Comment.objects.filter(project=project).count()
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


@login_required(login_url="/login/")
def AddComment(request, id):
    if request.method == 'POST':
        project = Project.objects.get(id=id)
        text = request.POST.get('cmttext')
        user = CreateAccount.objects.get(id=request.user.id)
        print(request.user.id)
        print(request.user.username)
        com = Comment(project=project, text=text, user=user)
        com.save()
        return redirect("home")
