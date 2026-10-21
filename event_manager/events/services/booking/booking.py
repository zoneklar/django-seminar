"""Beispiel für Booking-Modul mit einer Funktion zur Stornierung
eines Events."""

from django.utils import timezone

from events.models import Event


class BookingError(Exception):
    pass


def cancel_booking(event: Event) -> Event:
    """Einen Event stornieren (simulation)."""
    if event.date < timezone.now():
        raise BookingError("Ein vergangener Event kann nicht gelöscht werden!")

    event.is_active = False
    event.save(update_fields=["is_active", "updated_at"])
    return event
