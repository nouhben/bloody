from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse('<p>Hello World!</p>')


def home(request):
    context = {
        'title': 'Django Review'
    }
    return render(request, 'handy_api/home.html', context=context)
