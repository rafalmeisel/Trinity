from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    author = models.CharField(max_length=64)
    year = models.IntegerField()
    amount = models.IntegerField()