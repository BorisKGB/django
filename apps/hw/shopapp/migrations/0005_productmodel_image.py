# Generated by Django 5.0.1 on 2024-02-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_alter_ordermodel_applied_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='shopapp/images/'),
        ),
    ]