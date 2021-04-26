from rest_framework import serializers
from app.models import ProjectZookeeper
from .instance_zookeeper import ZookeeperInstanceSerializer


# Project Zookeeper
class ProjectZookeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectZookeeper
        fields = '__all__'


class GetProjectZookeeperSerializer(serializers.ModelSerializer):
    instance = ZookeeperInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectZookeeper
        fields = '__all__'

