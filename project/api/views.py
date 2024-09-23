from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


def home(request):
    authors = Author.objects.all()
    return render(request, "index.html", {"authors": authors})


def index(request):
    return HttpResponse("Hello, World!")


def hello(request):
    return HttpResponse("Hello, World!")
