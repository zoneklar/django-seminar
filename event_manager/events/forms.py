"""
events/forms.py

Definiert Formular-Klassen für die event-app
"""

from django import forms

from .models import Event
from .normalizers import normalize_name
from .validators import check_illegal


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

    def clean_name(self):
        """Eine Methode, die zur Normalisierung und Validierung gedacht ist.
        Alle clean-Methoden haben folgendes Schema: clean_<FELDNAME>.
        Der Rückgabewert von diesen Funktionen ist immer der neue Feldwert."""

        # in cleaned_data stehen die aktuellen, von Django schon technisch
        # validierten Feldwert holen
        name = self.cleaned_data["name"]
        return normalize_name(name)

    def clean_sub_title(self):
        """Prüfe, ob der Sub-Title ein illegales Zeichen verwendet."""
        sub_title = self.cleaned_data["sub_title"]
        if isinstance(sub_title, str):
            check_illegal(sub_title)  # hier wird u.U. ein Validation Error ausgelöst
        return sub_title
