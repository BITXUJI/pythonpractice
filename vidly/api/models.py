from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()  # lazy loading
        resource_name = 'movies'  # url: .../api/movies
        excludes = ['date_created']  # hide movie.date_create attribute api
