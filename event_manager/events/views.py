# events/views.py
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import EventForm
from .models import Category, Event
from .services.booking import booking

logger = logging.getLogger(__name__)


def event_cancel(request: HttpRequest, pk: int):
    """Einen Event canceln.

    /events/3/cancel
    """
    event = get_object_or_404(Event, pk=pk)
    try:
        booking.cancel_booking(event)
    except booking.BookingError as e:
        # message.error()
        # logging.warning()
        logger.warning("Es ist ein Fehler aufgetreten: %s", str(e))
    return redirect("events:event-detail", pk=pk)


class EventDeleteView(DeleteView):
    """Event nach Rückfrage löschen.

    /events/42/delete
    template: events/event_delete_confirm.html
    """

    model = Event
    success_url = reverse_lazy("events:event-list")


class EventUpdateView(LoginRequiredMixin, UpdateView):
    """Event via Formular editieren.
    /events/42/update

    template: events/event_form.html
    """

    model = Event
    form_class = EventForm

    def get_success_url(self):
        return reverse_lazy(
            "events:event-detail",
            kwargs={"pk": self.object.pk},
        )


class EventCreateView(LoginRequiredMixin, CreateView):
    """Event via Formular anlegen.
    /events/create

    template: events/event_form.html
    """

    model = Event
    form_class = EventForm
    # nach dem erfolgreichen Eintrag geht die Reise weiter:
    # success_url = reverse_lazy("events:event-list")  # /events

    def form_valid(self, form):
        """Wenn das Formular valide ist, setzen wir den author mit dem
        aktuell eingeloggten User."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """Wir landen hier nach erfolgreichem Create.
        Die Methode erzeugt eine Success-URL auf die Detailseite des
        neu angelegten Objekts."""
        return reverse_lazy(
            "events:event-detail",
            kwargs={"pk": self.object.pk},
        )


class EventDetailView(DetailView):
    """Anzeigen eines Events
    /events/42

    template: events/event_detail.html
    default: queryset = Event.objects.get(pk=pk)
    """

    model = Event


class EventListView(ListView):
    """Anzeigen aller Events in einer Liste.
    /events

    template: events/event_list.html
    default: queryset = Event.objects.all()
    """

    model = Event
    # join auf category-Tabelle und User-Tabelle
    queryset = Event.objects.select_related("category", "author")


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
