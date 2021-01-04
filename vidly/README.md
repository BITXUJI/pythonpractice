Python Django
 ---
### Your First Django Project
- pipenv install django==2.1 
  - Just use the latest version will be OK
- pipenv shell
- django-admin startproject vidly .
- code .
- pipenv install pylint --dev
- pipenv install autopep8 --dev
- python manage.py runserver
### Create an App
- python manage.py startapp movies
### Views
- Explanations (Not command line):
  - movies/views.py : create function index()
  - movies/urls.py :urls.py is created and add urlpatterns(list)
  - vidly.urls.py :add a new item to urlpatterns 
### Models
- Explanation(Not command line)
  - movies/models.py: Two classed created(Genre and Movies) and some attributes are set
  - 