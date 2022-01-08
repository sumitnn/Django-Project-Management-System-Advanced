
from django.urls import path
from .views import *

urlpatterns = [
    path('projectdetail/<int:pk>/',
         ProjectDetail.as_view(), name="projectdetail"),
]
