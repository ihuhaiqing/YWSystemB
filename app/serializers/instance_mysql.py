from rest_framework import serializers
from app.models import MySQLInstance


# MySQL 实例
class MySQLInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySQLInstance
        fields = '__all__'
