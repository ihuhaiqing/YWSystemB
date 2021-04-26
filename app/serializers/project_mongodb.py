from rest_framework import serializers
from app.models import ProjectMongoDB, Host
from .host import HostSerializer


# Project MongoDB
class ProjectMongoDBSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=False)

    class Meta:
        model = ProjectMongoDB
        fields = '__all__'


class GetProjectMongoDBSerializer(serializers.ModelSerializer):
    # ManyToManyField: many=True
    # ForeignKey: many=False 默认值
    host = HostSerializer(many=False)

    class Meta:
        model = ProjectMongoDB
        fields = '__all__'
