from rest_framework import serializers
from app.models import ProjectWar, Host
from .host import HostSerializer


# Project War
class ProjectWarSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=True)

    class Meta:
        model = ProjectWar
        fields = '__all__'


class GetProjectWarSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectWar
        fields = '__all__'

