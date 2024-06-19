from django.db import models

# Create your models here.
class Simpson (models.Model):
    name = models.CharField(max_length = 50)
    apellido = models.CharField(max_length=50)
    chapter = models.IntegerField()
    name_chapter = models.CharField(max_length=100)
    temporada = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.apellido}'
    