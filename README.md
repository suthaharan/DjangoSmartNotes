Python 3.8.6 virtualenv
Django 3.2

$ pip uninstall django
$ pip install Django==4.2
$ python -m django --version

$ django-admin startproject smartnotes .
$ python manage.py runserver 9000

$ django-admin startapp home
In settings.py, under installed_apps add in the newly created app


Building your project
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
* Admin dashboard comes by default
* Visit http://127.0.0.1:8000/admin/