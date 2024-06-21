from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def say_hello(request, name):
    return render(request, 'index.html',  {"name": name})


def welcome(request, name):
    return HttpResponse(f"Welcome {name}")
