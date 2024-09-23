from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World!")


def hello(request):
    return HttpResponse("Hello, World!")
