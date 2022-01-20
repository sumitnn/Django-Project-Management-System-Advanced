from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
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
    github = models.URLField(max_length=200, blank=True, default="github.com")
    fb = models.URLField(max_length=200, blank=True,
                         default="www.facebook.com")
    insta = models.URLField(max_length=200, blank=True,
                            default="instagram.com")
    linkedin = models.URLField(
        max_length=200, blank=True,   default="linkedin.com")
    website = models.URLField(
        max_length=200, blank=True, default="myportfoilo.com")


class Project(models.Model):
    user = models.ForeignKey(
        CreateAccount, on_delete=models.CASCADE, related_name="project")

    title = models.CharField(max_length=20, blank=True, null=True)

    current_time = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    team_members = models.CharField(max_length=20, blank=True, null=True)
    project_img = models.ImageField(
        upload_to="project_img/", blank=True, null=True)
    project_type = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    project_file = models.FileField(
        upload_to="project-files/", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    flame = models.ManyToManyField(
        CreateAccount, related_name="flame",  blank=True)

    def __str__(self):
        return self.title

    def count_flame(self):
        return self.flame.count()

    class Meta:
        ordering = ['-current_time']
