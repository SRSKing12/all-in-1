from django.contrib import admin
from myApp.models import Group,Message,Userinfo
# Register your models here.
admin.site.register(Group)
admin.site.register(Message)

@admin.register(Userinfo)
class UserDisp(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']


from .models import CreateTodo

# Register your models here.
admin.site.register(CreateTodo)