# Generated by Django 5.0.1 on 2024-02-01 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('registered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('applied_date', models.DateTimeField(auto_now=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shopapp.clientmodel')),
                ('products', models.ManyToManyField(to='shopapp.productmodel')),
            ],
        ),
    ]
