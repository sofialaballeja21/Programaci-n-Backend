from django.db import models

# Create your models here.

class Bratz(models.Model):
    name = models.CharField(max_length=20)
    accesorio = models.BooleanField()
    collection = models.CharField(max_length=100)
    picture = models.ImageField()

    def __str__(self):
        return f'{self.name} - {self.collection}'
    