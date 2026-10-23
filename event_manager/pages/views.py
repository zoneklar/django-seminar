from django.shortcuts import render
from django.views.generic import TemplateView

from events.models import Category, Event


class HomePageView(TemplateView):
    """Stellt Homepage des Projekts dar.

    Pfad: / (example.com)
    """

    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(f"context: {type(context)}")
        # context["name"] = "bob"
        events = Event.objects.all()
        categories = Category.objects.all()
        context["events"] = events
        context["categories"] = categories
        return context
