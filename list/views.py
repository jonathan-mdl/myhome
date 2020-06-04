from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeList, Home
# Create your views here.

def index(response, id):
    ls = HomeList.objects.get(id=id)
    return render(response, "list/base.html", {})

def home(response):
    return render(response, "list/home.html", {})