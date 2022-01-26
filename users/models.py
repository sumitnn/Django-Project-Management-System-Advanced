from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from crum import get_current_user
# import uuid
# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'None'),
)
Project_Type = (
    (0, 'Not Selected'),
    (1, 'Python Project'),
    (2, 'Mern Project'),
    (3, 'React Project'),
    (4, 'Deeplearning Project'),
    (5, 'Machine Learning Project'),
    (6, 'DataScience Project'),
    (7, 'Javascript Project'),
    (8, 'Css Project'),
    (9, 'Django Project'),
    (10, 'Angular Project'),
)


class CreateAccount(AbstractUser):
    profile_img = models.ImageField(
        upload_to="profile/", null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER, null=True, blank=True)
    bio = models.TextField(blank=True, null=True, default="student")
    country = models.CharField(
        blank=True, null=True, default="India", max_length=25)
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
        CreateAccount, on_delete=models.CASCADE, related_name="project", blank=True, null=True, default=None)

    title = models.CharField(max_length=20, blank=True, null=True)

    current_time = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)

    project_img = models.ImageField(
        upload_to="project_img/", blank=True, null=True)
    project_type = models.IntegerField(
        default=0, choices=Project_Type)

    project_file = models.FileField(
        upload_to="project-files/", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    team_members = models.ManyToManyField(
        CreateAccount, default=None, blank=True, related_name="project_team_members")

    flame = models.ManyToManyField(
        CreateAccount, default=None, related_name="project_flame",  blank=True)

    def __str__(self):
        return self.title or ''

    def count_flame(self):
        return self.flame.count()

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.user:
            self.user = user

        super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-current_time']


class Comment(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="comment", blank=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    current_time = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(
        CreateAccount, on_delete=models.CASCADE, blank=True, null=True)
