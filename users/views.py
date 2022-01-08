from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm


# Create your views here.

User = get_user_model()


def profile(request):
    return render(request, "users/profile.html")


def upload(request):
    return render(request, "users/upload.html")


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
