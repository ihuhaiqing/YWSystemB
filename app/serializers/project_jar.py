from rest_framework import serializers
from app.models import ProjectJar, Host
from .host import HostSerializer


# Project Jar
class ProjectJarSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=True)

    class Meta:
        model = ProjectJar
        fields = '__all__'


class GetProjectJarSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectJar
        fields = '__all__'
