# events/views.py
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Event


def category_detail(request: HttpRequest, pk: int):
    """Anzeigen der Detailseite einer Kategorie
    pk = der übergebene Primary Key einer Kategorie
    /events/categories/3
    """
    # hole die Kategorie mit dem pk=pk, oder löse 404 aus
    category = get_object_or_404(Category, pk=pk)
    # category = Category.objects.get(pk=pk)
    return render(
        request,
        "events/category_detail.html",
        {
            "category": category,
        },
    )


def category_list(request: HttpRequest):
    """Auflisten aller Kategorien

    /events/categories
    """
    # select * from cat (Selektiert alle Kategorien)
    qs = Category.objects.all()
    context = {"categories": qs}
    return render(
        request,
        "events/category_list.html",
        context,
    )


def hello_world(request: HttpRequest):
    """Jede View hat zwei Eigenschaften:
    - sie bekommt ein http request objekt übereben
    - sie muss ein HttpResponse Objekt zurückgeben
    """
    print(request.user)
    return HttpResponse("Hello world")
