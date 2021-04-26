from rest_framework import serializers
from app.models import RedisInstance
from .project_redis import GetProjectRedisSerializer


# Redis 实例
class RedisInstanceSerializer(serializers.ModelSerializer):
    redis_db = GetProjectRedisSerializer(read_only=True, many=True)

    class Meta:
        model = RedisInstance
        fields = '__all__'
