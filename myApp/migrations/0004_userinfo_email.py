# Generated by Django 3.1.6 on 2021-09-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_userinfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='abc', max_length=100, unique=True),
        ),
    ]
