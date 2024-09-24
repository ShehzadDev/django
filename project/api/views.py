from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


def home(request):
    authors = Author.objects.all()
    return render(request, "index.html", {"authors": authors})


def about(request):
    return render(request, "about.html")


def index(request):
    return HttpResponse("Hello, World!")


def hello(request):
    return HttpResponse("Hello, World!")


# Middleware
def middleware(request):
    custom_message = request.custom_message
    return HttpResponse(f"{custom_message} This is my view response!")
