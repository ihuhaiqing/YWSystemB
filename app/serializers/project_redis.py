from rest_framework import serializers
from app.models import ProjectRedis
from .project import GetProjectSerializer


# 增删改项目 redis
class ProjectRedisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRedis
        fields = '__all__'


# 查询项目 redis
class GetProjectRedisSerializer(serializers.ModelSerializer):
    project = GetProjectSerializer(read_only=True)

    class Meta:
        model = ProjectRedis
        fields = '__all__'

