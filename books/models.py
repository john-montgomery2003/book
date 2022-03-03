from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    amazonlink = models.CharField(max_length=200)
    jOwns = models.BooleanField()
    eOwns = models.BooleanField()
    jRead = models.BooleanField()
    eRead = models.BooleanField()
    isbn = models.CharField(max_length=200)