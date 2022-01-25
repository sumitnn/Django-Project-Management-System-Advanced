
from django.urls import path
from . views import *


urlpatterns = [

    path("profile/<int:id>/", profileid, name="profilewithid"),
    path("profile-edit/<int:id>/", profileedit, name="profileedit"),
    path("profile-delete/<int:id>/", profiledelete, name="profiledelete"),
    path("upload/", upload, name="upload-project"),
    path("signup/", signup, name="signup"),


]
