
from django.urls import path
from . views import *


urlpatterns = [
    path("login/", loginn, name="login"),
    path("logout/", logoutt, name="logout"),

]
