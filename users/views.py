from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, ProjectForm
from .models import Project


# Create your views here.

User = get_user_model()


def profile(request):
    return render(request, "users/profile.html")


def upload(request):
    context = {}
    if request.method == "POST":
        User = get_user_model()
        u = User.objects.get(username=request.user)
        title = request.POST.get('title')
        project_img = request.POST.get('project_img')
        project_type = request.POST.get('project_type')
        notes = request.POST.get('notes')
        project_file = request.POST.get('project_file')
        description = request.POST.get('description')
        print(u.id)
        print(u)
        instance = Project(user=u, title=title, project_img=project_img,
                           project_type=project_type, notes=notes, project_file=project_file, description=description)

        if instance is not None:
            instance.save()
            return redirect("home")

        else:
            print("failed")

    context['form'] = ProjectForm(label_suffix=" ")

    return render(request, "users/upload.html", context)


def signup(request):
    context = {}
    form = SignupForm
    if request.method == "POST":
        print(request.POST)
        formv = SignupForm(request.POST)
        if formv.is_valid():
            formv.save()
            return redirect("login")
        else:
            print(formv.errors)
            context['form'] = form
            context['error'] = formv.errors
            return render(request, "users/Signup.html", context)

    context['form'] = form
    return render(request, "users/Signup.html", context)
