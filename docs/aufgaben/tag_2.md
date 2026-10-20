# Nachmittagsaufgabe: Bücher anzeigen

Erweitere die App `books`. Besucher sollen eine Übersicht aller Bücher und eine Detailseite für ein einzelnes Buch aufrufen können.

## 1. Views erstellen

Lege in `books/views.py` zwei Views an:

- `book_list`: lädt alle Bücher und zeigt sie in einer Übersicht an.
- `book_detail`: lädt ein Buch anhand seiner ID und zeigt die Details an.

Wird ein Buch mit der angegebenen ID nicht gefunden, soll eine 404-Seite erscheinen.

## 2. URLs verbinden

1. Erstelle `books/urls.py`.
2. Lege dort diese Routen an:

   - `/books/` für die Bücherübersicht
   - `/books/<id>/` für die Detailseite eines Buches

3. Verbinde die URLs der App mit den Projekt-URLs.
4. Gib den Routen Namen.

## 3. Templates erstellen

Erstelle die Templates im Verzeichnis `books/templates/books/`.

### Bücherübersicht

`book_list.html` soll:

- die Überschrift „Bücher“ anzeigen
- alle Bücher auflisten
- für jedes Buch einen Link zur Detailseite enthalten
- eine passende Meldung anzeigen, wenn noch keine Bücher vorhanden sind

### Buchdetail

`book_detail.html` soll mindestens Titel und Beschreibung eines Buches anzeigen.

Ergänze einen Link zurück zur Übersicht.

## 4. Gemeinsames Grundtemplate

Wenn Übersicht und Detailseite funktionieren:

1. Erstelle ein gemeinsames Template `base.html`.
2. Verschiebe wiederkehrendes HTML wie `html`, `head`, `body` und die Navigation dorthin.
3. Definiere in `base.html` einen Block für den Seitentitel und einen Block für den Seiteninhalt.
4. Lass `book_list.html` und `book_detail.html` von `base.html` erben.
5. Überschreibe die Blöcke in beiden Templates passend.

## Fertig, wenn

- `/books/` die Bücherübersicht zeigt.
- Ein Klick auf einen Buchtitel die passende Detailseite öffnet.
- Eine unbekannte Buch-ID zu einer 404-Seite führt.