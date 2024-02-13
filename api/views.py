from rest_framework import generics
from .models import Actors
from .serializers import ActorsSerializer


class ActorsListCreate(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
