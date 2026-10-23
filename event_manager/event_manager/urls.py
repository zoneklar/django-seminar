"""
event_manager/urls.py
PROJEKT URLs

"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
    path("events/", include("events.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
