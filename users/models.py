from django.db import models
from django.contrib.auth.models import AbstractUser
# import uuid
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


class Project(models.Model):
    user = models.ForeignKey(
        CreateAccount, on_delete=models.CASCADE, related_name="project")
    project_img = models.ImageField(
        upload_to="project_img/", blank=True, null=True)
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    current_time = models.DateTimeField(auto_now_add=True)
    team_members = models.CharField(max_length=20)
    project_type = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-current_time']
