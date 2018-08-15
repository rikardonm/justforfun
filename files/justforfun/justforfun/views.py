from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello fucking world")


def login(request):
    #context = {}        #empty list
    context = list(User.objects.get())
    return render(request, 'jsutforfun/login.html', context)
