Python Django
 ---
### Your First Django Project
- pipenv install django==2.1
- pipenv shell
- django-admin startproject vidly .
- code .
- pipenv install pylint --dev
- pipenv install autopep8 --dev
- python manage.py runserver
### Create an App
- python manage.py startapp movies
### Views
- movies/views.py : create function index()
- movies/urls.py :created and add urlpatterns(list)
- vidly.urls.py :add a new item to urlpatterns 
