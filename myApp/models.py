from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, default="g")

    def __str__(self):
        return self.name
    
class Message(models.Model):
    value = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)

# STATE_CHOICES=(
# ('Andaman','Andaman'),
# ('Maharashtra','Maharashtra'),
# ('Madhya Pradesh','Madhya Pradesh'),
# ('Rajasthan','Rajasthan'),
# ('Chattisgarh','Chattisgarh'),
# ('Daman & Diu','Daman & Diu'),
# ('Goa','Goa'),
# ('Uttar Pradesh','Uttar Pradesh'),
# ('West Bengal','West Bengal'),
# ('Tamil Nadu','Tamil Nadu'),
# ('Telangana','Telangana'),
# ('Karnataka','Karnataka')
# )
      
class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_Name=models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    # email = models.EmailField(max_length=100, unique=True)
    state=models.CharField(max_length=60)#choices=STATE_CHOICES,default='none'
    address = models.CharField(max_length=200)
    # username = models.CharField(max_length=30, unique=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.full_Name


class CreateTodo(models.Model):
    title=models.CharField(max_length=200)
    descr=models.TextField()

    def __str__(self):
        return self.title