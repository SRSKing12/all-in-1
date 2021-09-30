from django.contrib import admin
from myApp.models import Group,Message,Userinfo,CreateTodo
# Register your models here.
admin.site.register(Group)
admin.site.register(Message)

@admin.register(Userinfo)
class UserDisp(admin.ModelAdmin):
    list_display=['id', 'full_Name', 'phone','state', 'date']


# Register your models here.
@admin.register(CreateTodo)
class TodoDisp(admin.ModelAdmin):
    list_display=['id', 'title', 'descr']