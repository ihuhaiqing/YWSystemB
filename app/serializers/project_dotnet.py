from rest_framework import serializers
from app.models import ProjectDotnet
from .host import HostSerializer


# Project Dotnet
class GetProjectDotnetSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectDotnet
        fields = '__all__'


class ProjectDotnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDotnet
        fields = '__all__'

