from rest_framework import serializers
from app.models import ProjectSQLServer


# Project SQLServer
class ProjectSQLServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSQLServer
        fields = '__all__'
