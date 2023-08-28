from django.db import models


# Create your models here.
class Coordinates(models.Model):
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
