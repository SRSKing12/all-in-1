
from django.urls import path
from myApp import views
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete

urlpatterns=[
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('mynewroom',views.mynewroom,name='mynewroom'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('register', views.regst, name='register'),
    path('sin', views.sgin, name='sin'),
    path('sout', views.sout, name="sout"),
    path('email_sent', views.email_sent, name="email_sent"),
    path('blog', views.blog, name="blog"),
    path('tasks', TaskList.as_view(), name="tasks"),
    path('create-task', TaskCreate.as_view(), name="create-task"),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name="update-task"),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name="delete-task"),
    
]