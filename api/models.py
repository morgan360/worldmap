from django.db import models


class Actors(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class WorldData(models.Model):
    worldKey = models.CharField(max_length=255, unique=True)
    dataFile = models.FileField(upload_to='worlddata/')
