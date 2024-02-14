from django.urls import path
from .views import upload_json, create_location, edit_location, list_locations

urlpatterns = [
    # Your other URLs...
    path('upload-json/', upload_json, name='upload_json'),
    path('locations/', list_locations, name='list_locations'),
    path('create/', create_location, name='create_location'),
    path('locations/edit/<int:id>/', edit_location, name='edit_location'),

]