from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=100)
    movie = models.ForeignKey



