from rest_framework import serializers

class WorldDataSerializer(serializers.Serializer):
    worldKey = serializers.CharField(max_length=255)
    worldData = serializers.JSONField()
