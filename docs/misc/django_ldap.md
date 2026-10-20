# LDAP mit Django verwenden

Dieses Tutorial verbindet Django über `django-auth-ldap` mit einem LDAP-Verzeichnis. Nutzer melden sich mit ihrem LDAP-Benutzernamen und LDAP-Passwort an. Django legt beim ersten erfolgreichen Login einen lokalen Benutzer an.

## 1. Paket installieren

```bash
uv add django-auth-ldap
```

Das Paket benötigt `python-ldap` und OpenLDAP-Bibliotheken. Auf manchen Systemen müssen dafür zusätzlich Systempakete installiert werden. Das LDAP-Backend kommt nicht in `INSTALLED_APPS`. [django-auth-ldap.readthedocs.io](https://django-auth-ldap.readthedocs.io/en/latest/install.html?utm_source=chatgpt.com)

## 2. LDAP-Einstellungen konfigurieren

Importiere in `settings.py` die benötigten Klassen:

```python
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType
```

Konfiguriere anschließend Server, Benutzer- und Gruppensuche. Ersetze die Beispielwerte durch die Werte deines LDAP-Servers.

```python
AUTH_LDAP_SERVER_URI = "ldap://192.168.178.40"

AUTH_LDAP_BIND_DN = "cn=django-reader,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "aus-umgebungsvariable-laden"

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "dc=example,dc=com",
    ldap.SCOPE_SUBTREE,
    "(uid=%(user)s)",
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "ou=groups,dc=example,dc=com",
    ldap.SCOPE_SUBTREE,
    "(objectClass=posixGroup)",
)

AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")
```

Der Bind-Account sollte nur die nötigen Leserechte besitzen. Die Gruppensuche beschränkt sich hier auf POSIX-Gruppen. `AUTH_LDAP_GROUP_SEARCH` muss alle Gruppen finden, die in den weiteren Einstellungen referenziert werden. [django-auth-ldap.readthedocs.io](https://django-auth-ldap.readthedocs.io/en/stable/groups.html?utm_source=chatgpt.com)

## 3. Zugriff über Gruppen steuern

Die folgenden Einstellungen erlauben nur Mitgliedern der Gruppe `enabled` die Anmeldung und sperren Mitglieder von `disabled`.

```python
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled+gidNumber=501,ou=groups,dc=example,dc=com"

AUTH_LDAP_DENY_GROUP = "cn=disabled+gidNumber=504,ou=groups,dc=example,dc=com"
```

Django kann außerdem Benutzerfelder anhand der Gruppenmitgliedschaft setzen:

```python
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": ("cn=active+gidNumber=500,ou=groups,dc=example,dc=com"),
    "is_staff": ("cn=staff+gidNumber=502,ou=groups,dc=example,dc=com"),
    "is_superuser": ("cn=superuser+gidNumber=503,ou=groups,dc=example,dc=com"),
}
```

Die Gruppen-DNs sind Beispiele und müssen exakt zu deinem LDAP-Verzeichnis passen. `is_superuser` gibt vollständige Administratorrechte. Verwende dafür eine eng begrenzte Gruppe.

## 4. Django-Benutzer mit LDAP-Daten befüllen

```python
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "username": "uid",
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
```

`AUTH_LDAP_USER_ATTR_MAP` ordnet LDAP-Attribute Feldern des Django-User-Modells zu. Passwörter gehören nicht in diese Zuordnung. Django speichert das LDAP-Passwort nicht; neu angelegte Django-Benutzer erhalten ein unbrauchbares lokales Passwort. [django-auth-ldap.readthedocs.io](https://django-auth-ldap.readthedocs.io/en/stable/users.html?utm_source=chatgpt.com)

## 5. Gruppen synchronisieren und Berechtigungen verwenden

```python
AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600

AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]
```

`AUTH_LDAP_MIRROR_GROUPS` übernimmt LDAP-Gruppen beim Login in die Django-Datenbank. 
`ModelBackend` wird benötigt, damit Django seine Gruppen und Berechtigungen verwendet. Die Synchronisierung erfolgt beim Login. [django-auth-ldap.readthedocs.io](https://django-auth-ldap.readthedocs.io/en/5.3.0/permissions.html?utm_source=chatgpt.com)

## 6. Login-Seite einrichten

In der Projektdatei `urls.py`:

```python
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path(
        "accounts/login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
]
```

Erstelle das Template `templates/registration/login.html`:

```html
<h1>Anmelden</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Anmelden</button>
</form>
```

Django prüft die Anmeldung über die eingetragenen Authentication Backends. Bei erfolgreichem LDAP-Login wird der Django-Benutzer angelegt oder aktualisiert.

## 7. Anmeldung testen

Führe die Migrationen aus und starte den Server:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

Öffne `/accounts/login/` und melde dich mit einem LDAP-Benutzer an.

## Hinweise zur Konfiguration

- Lege das Bind-Passwort in einer Umgebungsvariable ab, nicht direkt in `settings.py`.
- Die Beispielkonfiguration verwendet `ldap://`. Für produktive Verbindungen sollte LDAP verschlüsselt über LDAPS oder StartTLS laufen; andernfalls werden Passwörter unverschlüsselt übertragen. [django-auth-ldap.readthedocs.io](https://django-auth-ldap.readthedocs.io/en/stable/authentication.html?utm_source=chatgpt.com)
- `AUTH_LDAP_PROFILE_ATTR_MAP` ist nicht Teil der aktuellen Standardkonfiguration von `django-auth-ldap`. Zusätzliche Profilfelder brauchen eine eigene Lösung, etwa ein Signal oder eine angepasste Backend-Logik.
- Prüfe, dass jede Gruppen-DN korrekt ist und die `gidNumber`-Werte in deinem Verzeichnis stimmen. In deinem Beispiel hatten `disabled` und `superuser` beide `gidNumber=504`; ich habe für `superuser` im Tutorial beispielhaft `503` eingesetzt.