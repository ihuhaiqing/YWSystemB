from rest_framework import serializers
from app.models import Host, ProjectOracle
from .host import HostSerializer


# Project Oracle
class ProjectOracleSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(),many=False)

    class Meta:
        model = ProjectOracle
        fields = '__all__'


class GetProjectOracleSerializer(serializers.ModelSerializer):
    # ManyToManyField: many=True
    # ForeignKey: many=False 默认值
    host = HostSerializer(many=False)

    class Meta:
        model = ProjectOracle
        fields = '__all__'

