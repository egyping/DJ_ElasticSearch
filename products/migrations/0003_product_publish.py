# Generated by Django 3.1.6 on 2021-02-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210212_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publish',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
