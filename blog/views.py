from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def landing(response):
    return HttpResponse('<h1> Blog Landing <h2>')
