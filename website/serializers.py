from rest_framework import serializers
from .models import Website

class WebsiteSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    title = serializers.CharField()
    content = serializers.JSONField()
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Website(**validated_data).save()

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
