from rest_framework import serializers
from app.models import Host, ProjectWeb
from .host import HostSerializer


# Project Web
class ProjectWebSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), write_only=True, many=True)

    class Meta:
        model = ProjectWeb
        fields = '__all__'


class GetProjectWebSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectWeb
        fields = '__all__'
