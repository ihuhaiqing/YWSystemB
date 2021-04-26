from rest_framework import serializers
from app.models import ProjectPHP
from .host import HostSerializer


# Project PHP
class GetProjectPHPSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectPHP
        fields = '__all__'


class ProjectPHPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPHP
        fields = '__all__'
