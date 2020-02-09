from django.db import models


# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    picture = models.FileField()
    author = models.CharField(max_length=30, default='')
    describe = models.TextField(default='')

    def __str__(self):
        return self.name
