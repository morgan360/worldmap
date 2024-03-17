import json
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from .models import Actors, WorldData
from .serializers import ActorsSerializer, WorldDataSerializer
from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404


class ActorsListCreate(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer


class WorldDataView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WorldDataSerializer(data=request.data)
        if serializer.is_valid():
            worldKey = serializer.validated_data['worldKey']
            worldData = serializer.validated_data['worldData']

            # Convert the worldData dictionary to a JSON string
            worldDataStr = json.dumps(worldData)
            data_file = ContentFile(worldDataStr.encode(), name=f"{worldKey}.json")

            # Create or update the WorldData object
            world_data_obj, created = WorldData.objects.update_or_create(
                worldKey=worldKey,
                defaults={'dataFile': data_file}
            )

            return JsonResponse({"message": "World data saved successfully", "worldKey": worldKey})
        else:
            return JsonResponse(serializer.errors, status=400)


def serve_world_data_file(request, world_key):
    # Attempt to retrieve the WorldData object by the worldKey
    world_data = get_object_or_404(WorldData, worldKey=world_key)

    # Assuming dataFile is the FileField in your WorldData model
    file_path = world_data.dataFile.path
    file_name = world_data.dataFile.name

    try:
        # Open the file for reading in binary mode
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    except IOError:
        # File not found or some other error
        raise Http404('World data file does not exist')
