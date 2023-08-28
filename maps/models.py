from django.db import models


class Coordinates(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    additional_info = models.TextField(blank=True)  # Add this field

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
