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
### Migration
- Explanation
  - db.sqlite3: light-weighted db
  - db browser for sqlite3
  - vidly/settings.py: 'movies.apps.MoviesConfig' added to register app movies 
- python manage.py makemigrations
  - Create model Genre
  - Create model Movie
- python manage.py runserver
- python manage.py migrate
  - Migrate the Unapplied migrations to db.sqlite3
  - Apply all migrations: admin,auth.contenttypes, movies,sessions
### Changing the Models
- Explanation
  - movies/models.py : In class movie a new attribute named date_created is added 
- python manage.py makemigrations
  - message returned in the terminal: Add field date_created to movie
- python manage.py migrate
- python manage.py sqlmigrate movies 0001
  - to see operations on sql 
### The Admin
- python manage.py runserver 
- python manage.py createsuperuser
  - When the last command is runing, open a new terminal and run this command to create a super user
  - username+email+password
- Explanation:
  - movies/admin.py : Register Genre and Movie to the admin
### Customizing the Admin
- Explanation
  - movies/models.py : Rewrite the magic method __str__ of class Genre to change  views displayed of Genre
  - movies/admin.py : Create a class GenreAdmin(admin.ModelAdmin) to overwrite the display_list to 'id' 'name' (in administrator views )
  - movies/admin.py : Create a class MovieAamin(admin.ModelAmin) to overwrite the fields or exclude (in administratror views)
### Database API
- Explanation
  - movies/models.py: In class Movie(models.Model) models.Model helps us operate on database  
  - (from django.db import models) models.Model is a database abstraction API
  - movies/views.py : (from .models import Movie) use database API to get the data to display to users
### Templates
- Explanation
  - movies/views.py (from django.shortcuts import render)  we use render function to render a template
  - Create a fold named template and a file named index.html zen coding
  - Change to django html to edit movies/templates/index.html
  - In case of index.html search_path misleading we create a fold named movies under the fold template and move index.html into it 
- pipenv install pylint-django
  - Create a file named .pylinrc:
    - echo load-plugins=pylint-django>.pylinrc 
  - Let pylint be aware of django 
### Adding Bootstrap
-Explanation
  - getbootstrap.com/docs 
  - movies/templates/movies/base.html: added and a template was pasted into it from url above
  - link base.html and index.html : to make our page look better.
### Customizing the layout
-Explanation
  - https://getbootstrap.com/docs/5.0/components/navbar/
  - add navbar container table-hover table-bordered : make our page look better.
### Sharing a Template
- Explanation
  - Create a fold named templates under . fold and move movies/templates/movie/base.html to templates/ fold 
  - vidly/settings.py : TEMPLATES['DIRS'] is modified to add the path templates/ created above to the search path.
  - So we can share one templates among multiple apps
### Url Parameters
- Explanation
  - target: click on something to see its details
  - movies/urls.py :Create a new page index
  - movies/views.py: Create a new page content
### Getting a Single Object
-Explanation
  - Create a page detail.html in the fold movies/templates/movies/
  - movies/views:Modified the return type of def detail function
  - So we can create make our page movies/{movie_id} look better
  - some tricks in writing html fast: dl>(dt+dd)*3 in html mode (not django html )
### Raising 404 Errors
- Explanation
  - movies.views.py :
    - from django.shortcuts import render, get_object_or_404
    - from django.http import HttpResponse, Http404
  - 'get_object_or_404' helps us easily raise 404 Errors
