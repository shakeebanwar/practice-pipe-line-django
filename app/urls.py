from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',index , name="index"),
    path('page1',page1 , name="page1"),
    path('page2',page2 , name="page2"),
    path('<str:room_name>/', room, name='room'),

]
