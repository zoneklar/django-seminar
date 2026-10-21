# Tag 3: Bücher anlegen und bearbeiten

Erweitere die `books`-App um Formulare zum Anlegen und Bearbeiten von Büchern. Verwende dafür das vorhandene `Book`-Modell.

## 1. ModelForm anlegen

Erstelle in `books/forms.py` eine `BookForm` auf Basis von `ModelForm`.

- Binde das vorhandene `Book`-Modell ein.
- Wähle geeignete Felder aus, zum Beispiel Titel, Beschreibung, Erscheinungsdatum und Genre.

## 2. Views erstellen

Erstelle Views für:

- **Buch anlegen**
- **Buch bearbeiten**

Verwende `CreateView` und `UpdateView`. Nach dem Speichern soll jeweils die Detailseite des betreffenden Buchs angezeigt werden.

## 3. URLs verbinden

Ergänze in `books/urls.py` diese Routen:

- `/books/create/` zum Anlegen
- `/books/<id>/edit/` zum Bearbeiten

Vergib passende Namen für die URLs.

## 4. Templates erstellen

Erstelle ein gemeinsames Formular-Template für das Anlegen und Bearbeiten.

Das Template soll:

- einen passenden Seitentitel anzeigen
- das Formular mit `method="post"` darstellen
- `{% csrf_token %}` enthalten
- einen Speichern-Button und einen Zurück-Link enthalten

## 5. Seiten verlinken

Ergänze die Links:

- In der Bücherübersicht: **Neues Buch anlegen**
- Auf der Buchdetailseite: **Buch bearbeiten**

## Fertig, wenn

- Ein Buch angelegt und anschließend auf seiner Detailseite angezeigt wird.
- Ein vorhandenes Buch bearbeitet werden kann.
- Beide Formulare dasselbe Template verwenden.
- Die Links zwischen Übersicht, Formular und Detailseite funktionieren.