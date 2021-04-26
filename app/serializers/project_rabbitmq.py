from rest_framework import serializers
from app.models import ProjectRabbitmq
from .instance_rabbitmq import RabbitmqInstanceSerializer


# Project Rabbitmq
class ProjectRabbitmqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRabbitmq
        fields = '__all__'


class GetProjectRabbitmqSerializer(serializers.ModelSerializer):
    instance = RabbitmqInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectRabbitmq
        fields = '__all__'
