from rest_framework import serializers
from .host import HostSerializer
from app.models import ProjectPython


# Project Python
class GetProjectPythonSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectPython
        fields = '__all__'


class ProjectPythonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPython
        fields = '__all__'
