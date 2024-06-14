1. 3 Apps erstellen
2. 3 Apps in Settings hinzufügen
3. ***myrestaurant/urls.py imp****
4. die 3 urls für die 3 apps erstellen und imp
5. die Views jeweils entsprechend programmieren (classes/funktionen)
6. templates-Ordner erstellen und jeweils mit passenden Namen (html-Datei)


7. Create 2 Models for Menu App "MenuCategory", "MenuItem"
8. Create Model "Reservation" name, date and time and number of guests.
9. Admin Configuration for Menu App und Reservations App
9.5 Makemigrations----> Migrate
10. Views easy for Menu App
11. urls Menu App
12. ////Views for Reservations////
13. urls for Reservations
14. templates: menu.html, view_reservations.html, reserve_table.html


- Setup einer Programmiersprache/Framework der Wahl für die Implementierung der API (Django)
- Anbindung der Datenbank/Speicher auf dem Server/in der Infrastruktur (Sqlite)
15. Install Django REST Framework
16. Update settings
17. seriallizers
18. Views
19. URLs 





python3 manage.py makemigrations
python3 manage.py migrate

Delete Migrations:
python3 manage.py migrate blog 0002
python3 manage.py makemigrations your_app_name





restaurant/
│
├── pages/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── pages/
│           ├── home.html
│           └── about.html
│
├── menu/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│           └── menu.html
│
├── reservations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│           ├── reserve_table.html
│           └── view_reservations.html
│
├── myrestaurant/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/
│   └── base.html
│
├── manage.py
└── db.sqlite3
