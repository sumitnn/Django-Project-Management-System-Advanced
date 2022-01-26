
from django.urls import path
from . views import *


urlpatterns = [

    path('', home, name="home"),
    path('add-comment/<int:id>/', AddComment, name="addcomment"),
    path('post-like/<int:id>/', like, name="like"),
    path('post-update/<int:id>/', UpdatePost, name="updatepost"),
    path('post-delete/<int:id>/', DeletePost, name="deletepost"),
    path("project-detail/<int:id>/", projectdetail, name="project-detail"),

]
