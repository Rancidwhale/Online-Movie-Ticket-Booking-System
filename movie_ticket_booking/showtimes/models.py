from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.IntegerField()  # Duration in minutes
    synopsis = models.TextField()

    def __str__(self):
        return self.title


class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} at {self.theater.name} ({self.date_time})"
