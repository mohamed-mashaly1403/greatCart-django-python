# Generated by Django 3.2.9 on 2021-11-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20211129_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpoduct',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='orderpoduct',
            name='size',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
