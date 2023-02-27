from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {'gretting':'sedlyar'})


def home(request):
    return HttpResponse('age')
