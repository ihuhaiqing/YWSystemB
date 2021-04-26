from rest_framework import serializers
from app.models import ZookeeperInstance


# Zookeeper 实例
class ZookeeperInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZookeeperInstance
        fields = '__all__'
