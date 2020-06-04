from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeList, Home
from .forms import CreateNewList
# Create your views here.

def index(response, id):
    ls = HomeList.objects.get(id=id)
    return render(response, "list/list.html", {"ls":ls})

def home(response):
    return render(response, "list/home.html", {})

def create(response):
    form = CreateNewList()
    return render(response, "list/create.html", {"form":form})