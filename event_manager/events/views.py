# events/views.py
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def hello_world(request: HttpRequest):
    """Jede View hat zwei Eigenschaften:
    - sie bekommt ein http request objekt übereben
    - sie muss ein HttpResponse Objekt zurückgeben
    """
    print(request.method)
    return HttpResponse("Hello world")
