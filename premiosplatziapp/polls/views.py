from django.http import HttpRequest, HttpResponse
from django.shortcuts import render  # noqa: F401

# Create your views here.


def index(request: HttpRequest):
    return HttpResponse("Hello World")
