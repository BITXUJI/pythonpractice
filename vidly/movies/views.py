from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
    # output = ', '.join([m.title for m in movies])
    # # SELECT * FROM movies_movie
    # Movie.objects.filter(releas_year=1989)
    # # SELECT * FROM movies_movie WHERE releas_year=1989
    # Movie.objects.get(id=1)
    # # SELECT * FROM movies_moviw WHERE id=1
    # return HttpResponse(output)


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # return HttpResponse(movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
