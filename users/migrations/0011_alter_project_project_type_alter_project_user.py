# Generated by Django 4.0.1 on 2022-01-24 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.IntegerField(choices=[(0, 'Not Selected'), (1, 'Python Project'), (2, 'Mern Project'), (3, 'React Project'), (4, 'Deeplearning Project'), (5, 'Machine Learning Project'), (6, 'DataScience Project'), (7, 'Javascript Project'), (8, 'Css Project'), (9, 'Django Project'), (10, 'Angular Project')], default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
