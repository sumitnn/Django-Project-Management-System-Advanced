
from django.urls import path
from . views import *


urlpatterns = [
    path("profile/", profile, name="profile"),
    path("profile/<int:id>/", profile, name="profile"),
    path("upload/", upload, name="upload-project"),
    path("signup/", signup, name="signup"),


]
