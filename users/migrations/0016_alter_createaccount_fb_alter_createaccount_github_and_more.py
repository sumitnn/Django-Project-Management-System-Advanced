# Generated by Django 4.0.1 on 2022-02-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createaccount',
            name='fb',
            field=models.URLField(blank=True, default='www.facebook.com', null=True),
        ),
        migrations.AlterField(
            model_name='createaccount',
            name='github',
            field=models.URLField(blank=True, default='github.com', null=True),
        ),
        migrations.AlterField(
            model_name='createaccount',
            name='insta',
            field=models.URLField(blank=True, default='instagram.com', null=True),
        ),
        migrations.AlterField(
            model_name='createaccount',
            name='linkedin',
            field=models.URLField(blank=True, default='linkedin.com', null=True),
        ),
        migrations.AlterField(
            model_name='createaccount',
            name='website',
            field=models.URLField(blank=True, default='myportfoilo.com', null=True),
        ),
    ]