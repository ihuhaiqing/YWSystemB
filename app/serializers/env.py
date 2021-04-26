from rest_framework import serializers
from app.models import Env


# 环境
class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env
        fields = '__all__'
