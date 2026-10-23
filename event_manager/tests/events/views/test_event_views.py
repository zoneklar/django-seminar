import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from events.models import Category, Event

User = get_user_model()


@pytest.fixture
def logged_in_client(client):
    # oft macht man diese fixtures in dateien namens conftest.py
    user = create_user(name="bob", email="a@a.com")
    client.force_login(user)
    return client


def create_category(name: str) -> Category:
    """Erstellt eine Kategorie in der Testdatenbank."""
    return Category.objects.create(name=name)


def create_user(name: str, email: str):
    """Erstellt einen User, der als Author des Events fungiert."""
    return User.objects.create_user(
        username=name,
        email=email,
        password="abc",
    )


def create_event(name, author, category) -> Event:
    return Event.objects.create(
        name=name,
        author=author,
        category=category,
        date=timezone.now(),
    )


@pytest.mark.django_db
def test_event_overview_accessable(client):
    """Testen, ob die Überssichtseite der Events zugänglich ist.
    Erfolgreich: Statuscode 200, Template event_list.html,
    der angelegte Event mit Namen "Django Workshop" taucht im
    Ergebnis auf. @pytest.mark.django_db => Nutze Testdatenbank (in memory oder Rollback)
    """
    category = create_category("python")
    author = create_user(name="alice", email="a@a.com")
    event = create_event(
        name="Django Workshop",
        author=author,
        category=category,
    )
    url = reverse("events:event-list")
    response = client.get(url)

    assert response.status_code == 200
    # Prüfen, ob unser Template event_list.html genutzt wurde
    assert "events/event_list.html" in {template.name for template in response.templates}
    # prüfen, ob Django Workshop im Quellcode der Webseite enthalten?
    assert event.name in response.content.decode()


@pytest.mark.django_db
def test_event_created_successfully(logged_in_client):
    category = create_category("python")
    url = reverse("events:event-create")
    payload = {
        "name": "Python Workshop",
        "category": category.pk,
        "date": timezone.now(),
        "min_group": 0,
    }
    response = logged_in_client.post(url, payload)
    # print(response.context["form"]) Um Fehler im Formular aufzuspüren
    assert response.status_code == 302  # Weiterleitung nach POST
    # wenn sich in der DB ein Event mit name Python Workshop findet, erzeuge
    # daraus einen boolschen Wert (True)
    assert Event.objects.filter(name=payload["name"]).exists()


@pytest.mark.django_db
def test_event_created_failed_with_short_name(logged_in_client):
    """Test ob ein fehlerhaftes Event (kurzer Name) nicht eingetragen wird."""
    category = create_category("python")
    url = reverse("events:event-create")
    payload = {
        "name": "aa",
        "category": category.pk,
        "date": timezone.now(),
        "min_group": 0,
    }
    response = logged_in_client.post(url, payload)
    assert response.status_code == 200
    assert not Event.objects.filter(name=payload["name"]).exists()
