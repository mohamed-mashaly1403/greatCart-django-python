# Generated by Django 3.2.9 on 2021-11-29 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpoduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderpoduct',
            name='size',
        ),
    ]
