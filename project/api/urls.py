from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello/", views.hello, name="hello"),
    path("home/", views.home, name="home"),
    path("middleware/", views.middleware, name="middleware"),
    path("about/", views.about, name="about"),
]
