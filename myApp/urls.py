
from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('mynewroom',views.mynewroom,name='mynewroom'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('kk', views.index, name='index'),
    path('delete/<str:pk>', views.deleteTodo, name='delete'),
    



    
]