from django.contrib import admin
from .models import Location, Character  # Adjust the import path if necessary

# Register your models here.
admin.site.register(Location)
admin.site.register(Character)
