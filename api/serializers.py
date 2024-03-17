from rest_framework import serializers
from .models import Actors


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'


class WorldDataSerializer(serializers.Serializer):
    worldKey = serializers.CharField(max_length=255)
    worldData = serializers.JSONField()
