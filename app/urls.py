
from django.urls import path
from . views import *


urlpatterns = [

    path('', home, name="home"),
    path('post-like/<int:id>/', like, name="like"),
]
