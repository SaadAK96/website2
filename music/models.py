from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.charfield(max_lenght=250)
    album_title=models.charfield(max_lenght=500)
    genre=models.charfield(max_lenght=100)
    album_logo=models.charfield(max_lenght=1000)