"""
events/forms.py

Definiert Formular-Klassen für die event-app
"""

from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # __all__ => Alle Felder im Formular darstellen
        # fields = "__all__"
        exclude = ("author",)

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"),
                attrs={"type": "datetime-local"},
            ),
        }
        labels = {
            "min_group": "Mindestgröße",
        }
