
from django.urls import path
from myApp import views

urlpatterns=[
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('mynewroom',views.mynewroom,name='mynewroom'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('kk', views.index, name='index'),
    path('delete/<str:pk>', views.deleteTodo, name='delete'),
    path('register', views.regst, name='register'),
    path('sin', views.sgin, name='sin'),
    path('sginpg', views.sginpg, name='sginpg'),
    path('sout', views.sout, name="sout"),
    path('email_sent', views.email_sent, name="email_sent"),
    
]