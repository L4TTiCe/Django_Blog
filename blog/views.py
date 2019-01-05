from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'PyCharm',
        'title': 'Django',
        'content': 'Django is the award-winning leader of Python web frameworks and PyCharm has long supported it. '
                   'Running, debugging, navigating, working productively... PyCharm has you covered for Django.',
        'date_posted': 'January 4, 2019'
    },
    {
        'author': 'PyCharm',
        'title': 'Flask',
        'content': 'The fast-growing Flask microframework has strong and growing PyCharm support: templates, '
                   'navigation, completion, and more.',
        'date_posted': 'January 5, 2019'
    }
]

# Create your views here.
def landing(response):
    context = {
        'posts' : posts
    }
    return render(response, 'blog/home.html', context)
    # return HttpResponse('<h1> Blog Landing </h1>')


def about(response):
    return render(response, 'blog/about.html', { 'title': 'About' })
    # return HttpResponse('<h1> About Placehonder </h1>')
