# Generated by Django 4.0.1 on 2022-01-22 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_createaccount_fb_alter_createaccount_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='flame',
            field=models.ManyToManyField(blank=True, default=None, related_name='project_flame', to=settings.AUTH_USER_MODEL),
        ),
    ]