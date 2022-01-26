# Generated by Django 4.0.1 on 2022-01-24 10:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_project_flame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='notes',
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.RemoveField(
            model_name='project',
            name='team_members',
        ),
        migrations.AddField(
            model_name='project',
            name='team_members',
            field=models.ManyToManyField(default=None, related_name='project_team_members', to=settings.AUTH_USER_MODEL),
        ),
    ]