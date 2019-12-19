from rest_framework import serializers

from app.api.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['key', 'name']

