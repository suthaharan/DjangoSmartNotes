## Python Basics

### Setting up Django on Windows
```
$ pip uninstall django
$ pip install Django==4.2
$ python -m django --version

$ django-admin startproject smartnotes .
$ python manage.py runserver 9000

$ django-admin startapp home
In settings.py, under installed_apps add in the newly created app
```

### Building your project
* Start project
* Create your first view
  * Modify views.py inside the new app "home" and add in the method
  * Modify smartnotes/urls.py to include the new route to the home app
* User -> /home -> urls.py -> views.py -> def home
* Django uses MVT design pattern
* Templates: typical organization pattern for django projects
  * DTL (Django Template Langugage) parses the html templates using the render function to create dynamic HTML pages with ease.
* Apps & Modularization
  * Organizing apps is essentials
  * Each app should be self-contained
  * Ideal app is one where you can delete the app folder and nothing else. Django app will work continuously.

### Django Admin Interface
* Admin dashboard comes by default. Entire authentication system ready to go.
* Visit http://127.0.0.1:8000/admin/
* Migrations explain what kind of tables that we need to use.
* $ python manage.py migrate (currently sqlite is used)
* $ python manage.py createsuperuser
* Django admin allows us to quickly access data and filter them

### Django ORM
* Each class is known as a model in a database table and each class attribute is called a column 
* Classes -> Make Migrations -> Migrate -> Database
* $ django-admin startapp notes (separate app for ORM)
* Add the app to settings.py
```python
from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
```
* $ python manage.py makemigrations
* $ python manage.py migrate


### Django Shell
* $ python manage.py shell
```shell
from notes.models import Notes
mynote = Notes.objects.get(pk='1')
mynote.title
mynote.text
Notes.objects.all()
new_note = Notes.objects.create(title='hello', text="this is just a text")
Notes.objects.filter(title__startswith="he")
Notes.objects.filter(text__icontains="is")
Notes.objects.exclude(text__icontains='django')

```

### Class based views
* extensive classes to help you crate powerful endpoints without too much effort
* Mixins are extra classes used with other classes to provide other useful methods

### Front-end development
* static files creation to store css, js, media
```python
# settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

```
* load the static file and reference the css 
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}"/>
    <title>Document</title>
</head>
<body>
    <h1>These are the notes:</h1>
    <ul>
        {% for note in notes %}
            <li class="note-li">{{note.title}}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

* Base template and extend it 
```python
# settings.py -->> 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'static/templates',
        ],
```

```html
<!-- base.html -->> 
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}"/>
    <title>Smart Notes</title>
</head>
<body>
    
    {% block content %} 
    {% endblock %}
   
</body>
</html>
```

```python
# notes.html
{% extends "base.html" %}
{% block content %}
    <h1>These are the notes:</h1>
    <ul>
        {% for note in notes %}
            <li class="note-li">{{note.title}}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

