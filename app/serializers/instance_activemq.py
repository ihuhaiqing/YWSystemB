from rest_framework import serializers
from app.models import ActivemqInstance


# Activemq 实例
class ActivemqInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivemqInstance
        fields = '__all__'
