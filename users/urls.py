
from django.urls import path
from . views import *


urlpatterns = [
    path("profile/", profile, name="profile"),
    path("upload/", upload, name="upload"),
    path("signup/", signup, name="signup"),


]
