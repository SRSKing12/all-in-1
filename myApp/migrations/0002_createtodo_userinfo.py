# Generated by Django 3.2.4 on 2021-09-25 08:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('descr', models.TextField()),
                ('dateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman', 'Andaman'), ('Maharashtra', 'Maharashtra'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Rajasthan', 'Rajasthan'), ('Chattisgarh', 'Chattisgarh'), ('Daman & Diu', 'Daman & Diu'), ('Goa', 'Goa'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Karnataka', 'Karnataka')], default='none', max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]