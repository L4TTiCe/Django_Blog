from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def landing(response):
    return render(response, 'blog/home.html')
    # return HttpResponse('<h1> Blog Landing </h1>')


def about(response):
    return render(response, 'blog/about.html')
    # return HttpResponse('<h1> About Placehonder </h1>')
