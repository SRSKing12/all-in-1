# Generated by Django 3.1.6 on 2021-09-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_auto_20210929_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='createtodo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
