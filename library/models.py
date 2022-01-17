from django.db import models
from django.contrib.auth.models import AbstractUser

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

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length = 100)
    bits_id = models.CharField(max_lngth = 15)
    HOSTEL_CHOICES = [
        ('KR', 'Krishna Bhavan'),
        ('GB', 'Gandhi Bhavan'),
        ('VB', 'Vyas Bhavan'),
        ('SB', 'Shankar Bhavan'),
        ('SR', 'Srinivas Ramanujan Bhavan'),
        ('RB', 'Ram Bhavan'),
        ('BB', 'Budh Bhavan'),
        ('MB', 'Malviya Bhavan'),
    ]
    hostel = models.CharField(
        max_length = 2,
        choices = HOSTEL_CHOICES,
    )
    room_no = models.CharField(max_length=4)
    mob_no = models.CharField(max_length=10)