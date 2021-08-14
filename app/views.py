from django.shortcuts import render , HttpResponse , redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,'index.html')
    
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


def page1(request):
    return render(request,'page1.html')


def page2(request):
    return render(request,'page2.html')