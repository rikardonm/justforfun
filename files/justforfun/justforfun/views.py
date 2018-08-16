from django.http import HttpResponse

from django.shortcuts import render

from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello fucking world")


def login(request):
    #context = {}        #empty list
    #context = list(User.objects.get())
    return render(request, 'registration/login.html')


def logout(request):
    return 'fuck'
