from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'None'),
)


class CreateAccount(AbstractUser):

    profile_img = models.ImageField(
        upload_to="profile/", null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER, null=True, blank=True)
    bio = models.TextField(blank=True, null=True, default="student")
