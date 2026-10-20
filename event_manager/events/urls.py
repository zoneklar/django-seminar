# events/urls.py
from django.urls import path

from .views import category_detail, category_list, hello_world

app_name = "events"
# Eine Url wird im Template aufgelöst: {% url 'app_name:path_name' %}
# Beispiel Liste der kategorien: {% url 'events:category-list' %}
# url(app_name, path_name)
# Beispiel Detail der kategorie: {% url 'events:category-detail' category.pk %}

urlpatterns = [
    # /events/categories/1
    path("categories/<int:pk>", category_detail, name="category-detail"),
    # /events/categories
    path("categories", category_list, name="category-list"),
    path("hello", hello_world, name="hello"),
]
