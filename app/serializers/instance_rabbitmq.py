from rest_framework import serializers
from app.models import RabbitmqInstance


# Rabbitmq 实例
class RabbitmqInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RabbitmqInstance
        fields = '__all__'

