# Generated by Django 3.2.9 on 2021-12-01 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211202_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_img',
        ),
        migrations.AddField(
            model_name='account',
            name='user_img',
            field=models.ImageField(blank=True, upload_to='img/users'),
        ),
    ]