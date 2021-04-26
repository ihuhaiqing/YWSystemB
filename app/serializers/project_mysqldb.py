from rest_framework import serializers
from app.models import ProjectMySQLDB
from .instance_mysql import MySQLInstanceSerializer


# Project MysSQL
class ProjectMySQLDBSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectMySQLDB
        fields = '__all__'


class GetProjectMySQLDBSerializer(serializers.ModelSerializer):
    instance = MySQLInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectMySQLDB
        fields = '__all__'
