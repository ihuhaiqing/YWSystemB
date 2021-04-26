from rest_framework import serializers
from .instance_activemq import ActivemqInstanceSerializer
from app.models import ProjectActivemq


# Project Activemq
class ProjectActivemqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectActivemq
        fields = '__all__'


class GetProjectActivemqSerializer(serializers.ModelSerializer):
    instance = ActivemqInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectActivemq
        fields = '__all__'

