from pyexpat import model
from statistics import mode
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

def validate_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))

class Author(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    bio = models.TextField()
    country = models.CharField(max_length=64, blank=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)

class Novel(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

class Genreext(models.Model):
    genre_id = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    novel_id = models.ForeignKey(Novel, null=True, on_delete=models.SET_NULL)

class Publisher(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    country = models.CharField(max_length=128, blank=False, null=True)