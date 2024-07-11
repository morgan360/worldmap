from django.db import models


class WorldData(models.Model):
    worldKey = models.CharField(max_length=255, unique=False)
    dataFile = models.FileField(upload_to='worlddata/')

    def __str__(self):
        return self.worldKey