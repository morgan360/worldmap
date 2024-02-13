from django.urls import path
from api.views import  ActorsListCreate

urlpatterns = [
    path('actors/', ActorsListCreate.as_view(), name='actors-list-create'),
]

