from django.db import models

# Create your models here.

class Song(models.Model):
    name_song = models.CharField(max_length=50)
    duration = models.IntegerField()
    name_autor = models.CharField(max_length=50)
    name_discografica = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    id_song = models.IntegerField()

    def __str__(self):
        return f'{self.name_song} - {self.id_song}'