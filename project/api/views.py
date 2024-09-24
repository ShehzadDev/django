from django.http import HttpResponse
from django.shortcuts import render
from .models import Author
from .AuthorProxy import AuthorProxy


def home(request):
    authors = AuthorProxy.objects.all()
    return render(request, "index.html", {"authors": authors})


def about(request):
    authors = AuthorProxy.objects.all()
    return render(request, "about.html", {"authors": authors})


def index(request):
    return HttpResponse("Hello, World!")


def hello(request):
    return HttpResponse("Hello, World!")


# Middleware
def middleware(request):
    custom_message = request.custom_message
    return HttpResponse(f"{custom_message} This is my view response!")
