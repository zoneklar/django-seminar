# events/urls.py
from django.urls import path

from .views import (
    EventCreateView,
    EventDeleteView,
    EventDetailView,
    EventListView,
    EventUpdateView,
    category_detail,
    category_list,
    event_cancel,
    hello_world,
)

app_name = "events"
# Eine Url wird im Template aufgelöst: {% url 'app_name:path_name' %}
# Beispiel Liste der kategorien: {% url 'events:category-list' %}
# url(app_name, path_name)
# Beispiel Detail der kategorie: {% url 'events:category-detail' category.pk %}

urlpatterns = [
    # Event-Routen
    # /events/42/cancel
    path("<int:pk>/cancel", event_cancel, name="event-cancel"),
    # /events
    path("", EventListView.as_view(), name="event-list"),
    # /events/42/delete
    path("<int:pk>/delete", EventDeleteView.as_view(), name="event-delete"),
    # /events/42/update
    path("<int:pk>/update", EventUpdateView.as_view(), name="event-update"),
    # /events/create
    path("create", EventCreateView.as_view(), name="event-create"),
    # /events/42
    path("<int:pk>", EventDetailView.as_view(), name="event-detail"),
    # Categorie-Routen
    # /events/categories/1
    path("categories/<int:pk>", category_detail, name="category-detail"),
    # /events/categories
    path("categories", category_list, name="category-list"),
    path("hello", hello_world, name="hello"),
]
