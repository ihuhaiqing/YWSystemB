from rest_framework import serializers
from app.models import ProjectCodeaddr


# Project Codeaddr
class ProjectCodeaddrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCodeaddr
        fields = '__all__'
