from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    amazonlink = models.CharField(max_length=200)
    jOwns = models.BinaryField()
    eOwns = models.BinaryField()
    jRead = models.BinaryField()
    eRead = models.BinaryField()
    isbn = models.CharField(max_length=200)