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