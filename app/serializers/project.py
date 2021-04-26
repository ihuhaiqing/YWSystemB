from rest_framework import serializers
from app.models import Project, Software, Env
from .software import SoftwareSerializer
from .env import EnvSerializer


# 增删改项目
class ProjectSerializer(serializers.ModelSerializer):
    software = serializers.PrimaryKeyRelatedField(queryset=Software.objects.all(), many=True)
    env = serializers.PrimaryKeyRelatedField(queryset=Env.objects.all(), many=True)

    class Meta:
        model = Project
        fields = '__all__'


# 查询项目
class GetProjectSerializer(serializers.ModelSerializer):
    software = SoftwareSerializer(read_only=True, many=True)
    env = EnvSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'

