from django.contrib import admin
from .models import Actors ,WorldData # Adjust the import path if necessary

# Register your models here.
admin.site.register(Actors)
admin.site.register(WorldData)