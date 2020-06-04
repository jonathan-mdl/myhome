from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeList, Home
# Create your views here.

def index(response, name):
    ls = HomeList.objects.get(name=name)
    home = ls.home_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, str(home.commentary)))

