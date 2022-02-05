from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, ProjectForm, UpdateProfileForm
from .models import Project, CreateAccount
from django.contrib.auth.decorators import login_required

# Create your views here.

User = get_user_model()


@login_required(login_url="/login/")
def profile(request):
    context = {}

    u = User.objects.get(username=request.user)
    project = Project.objects.filter(user=u)
    projectuser = Project.objects.filter(user=u).first()
    print(projectuser.user.username)
    context['pobj'] = project
    context['projecttuser'] = projectuser.user.username

    return render(request, "users/profile.html", context)


@login_required(login_url="/login/")
def profileid(request, id):
    context = {}

    u = User.objects.get(id=id)
    project = Project.objects.filter(user=u)
    projectuser = Project.objects.filter(user=u).first()

    context['pobj'] = project 
    context['projecttuser'] = projectuser.user.username if projectuser else None
    context['projecttdetails'] = projectuser

    return render(request, "users/profile.html", context)


@login_required(login_url="/login/")
def upload(request):
    context = {}
    if request.method == "POST":
        instance = ProjectForm(request.POST, request.FILES)

        if instance.is_valid():
            instance.save()
            return redirect("home")

        else:
            context['form'] = instance
            return render(request, "users/upload.html", context)

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


@login_required(login_url="/login/")
def profileedit(request, id):
    context = {}
    u = User.objects.get(id=id)
    if request.method == 'POST':
        f = UpdateProfileForm(request.POST or None,
                              request.FILES or None, instance=u)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect("home")
    context['form'] = UpdateProfileForm
    context['formvalues'] = u
    return render(request, "users/Editprofile.html", context)


@login_required(login_url="/login/")
def profiledelete(request, id):
    if request.method == "POST":
        u = User.objects.get(id=id)
        u.delete()

        return redirect("login")

    return redirect("home")
