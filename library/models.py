from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    GENRE_CHOICES = [
        ('SCIENCE_FICTION', 'Science Fiction'),
        ('HISTORY', 'History'),
        ('DRAMA', 'Drama'),
        ('BIOGRAPHY', 'Biography'),
        ('BUSINESS', 'Business'),
        ('COMEDY', 'Comedy'),
    ]
    genre = models.CharField(
        max_length = 15,
        choices = GENRE_CHOICES,)
    summary = models.TextField(max_length = 1000)
    ISBN =  models.CharField(max_length=13)
    location = models.CharField(max_length=25)
    availability = models.BooleanField(default=True)