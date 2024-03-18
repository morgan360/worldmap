from django.db import models


class WorldData(models.Model):
    worldKey = models.CharField(max_length=255, unique=True)
    dataFile = models.FileField(upload_to='worlddata/')
