
from django.urls import path
from . views import *


urlpatterns = [
    path("login/", loginn, name="login"),
    path("logout/", logoutt, name="logout"),
    path('password/reset/', PrView.as_view(), name="password_reset"),
    path('password/reset/done/', PrdView.as_view(), name="password_reset_done"),
    path('password/reset/confirm/<uidb64>/<token>', PrcView.as_view(),
         name="password_reset_confirm"),
    path('password/reset/complete/', PrcomView.as_view(),
         name="password_reset_complete"),
    path('password-change/', passwordchange, name="passwordchange")


]
