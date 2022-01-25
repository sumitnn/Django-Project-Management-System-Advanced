from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def loginn(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home")

        else:
            print(user)
            context['error'] = "Invalid Credentials !!"
            # Return an 'invalid login' error message.
            return render(request, "authentication/login.html", context)

    return render(request, "authentication/login.html")


@login_required(login_url="/login/")
def logoutt(request):
    logout(request)
    return redirect("login")


class PrView(PasswordResetView):
    template_name = "authentication/password-reset.html"


class PrcView(PasswordResetConfirmView):
    template_name = "authentication/password-reset-confirm.html"


class PrdView(PasswordResetDoneView):
    template_name = "authentication/password-reset-done.html"


class PrcomView(PasswordResetCompleteView):
    template_name = "authentication/password-reset-complete.html"


@login_required(login_url="/login/")
def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!

            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    # else:
    #     form = PasswordChangeForm(request.user)
    return render(request, 'authentication/change_password.html')
