from django.db import models
from django.conf import settings

class WorldData(models.Model):
    worldKey = models.CharField(max_length=255, unique=True)
    dataFile = models.FileField(upload_to='worlddata/')
 #   owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='worlds')

    def __str__(self):
        return self.worldKey