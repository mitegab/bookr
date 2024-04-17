from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = request.GET.get("name")  or "World"
    return HttpResponse("Hello, {}!".format(name))
