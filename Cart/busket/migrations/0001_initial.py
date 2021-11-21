# Generated by Django 3.2.9 on 2021-11-20 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_auto_20211120_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='busket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=205)),
                ('cart_date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='busketItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('busketItems_is_active', models.BooleanField(default=True)),
                ('busket_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busket.busket')),
                ('product_busket_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
