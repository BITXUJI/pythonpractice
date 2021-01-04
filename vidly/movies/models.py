from django.db import models
from django.utils import timezone
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    releas_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        default=timezone.now)  # pass the function name

    # def __str__(self):
    #     return self.title, self.releas_year, self.number_in_stock, self.daily_rate, self.genre, self.date_created
