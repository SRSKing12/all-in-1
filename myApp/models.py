from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=900)
    
class Message(models.Model):
    value = models.CharField(max_length=11111)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=11111)
    room = models.CharField(max_length=11111)

STATE_CHOICES=(
('Andaman','Andaman'),
('Maharashtra','Maharashtra'),
('Madhya Pradesh','Madhya Pradesh'),
('Rajasthan','Rajasthan'),
('Chattisgarh','Chattisgarh'),
('Daman & Diu','Daman & Diu'),
('Goa','Goa'),
('Uttar Pradesh','Uttar Pradesh'),
('West Bengal','West Bengal'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Karnataka','Karnataka')
)

class Userinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=60,default='none')


class CreateTodo(models.Model):
    title=models.CharField(max_length=10000)
    descr=models.TextField()
    

    def __str__(self):
        return self.title