# Generated by Django 3.2.9 on 2021-11-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
        ('busket', '0002_rename_busket_buskett'),
    ]

    operations = [
        migrations.AddField(
            model_name='busketitems',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]