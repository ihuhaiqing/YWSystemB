from app.models import *
from rest_framework import serializers


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class AccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class JavaPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JavaPackage
        fields = '__all__'


class GetJavaPackageSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='project.name')
    class Meta:
        model = JavaPackage
        fields = '__all__'


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    java_package = JavaPackageSerializer(read_only=True,many=True)
    software = SoftwareSerializer(read_only=True,many=True)
    class Meta:
        model = Project
        fields = '__all__'


class ProjectWebSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(),write_only=True,many=True)
    class Meta:
        model = ProjectWeb
        fields = '__all__'


class GetProjectWebSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True,many=True)
    class Meta:
        model = ProjectWeb
        fields = '__all__'


class ProjectTomcatSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(),many=False)
    class Meta:
        model = ProjectTomcat
        fields = '__all__'


class GetProjectTomcatSerializer(serializers.ModelSerializer):
    # ManyToManyField: many=True
    # ForeignKey: many=False 默认值
    host = HostSerializer(many=False)
    class Meta:
        model = ProjectTomcat
        fields = '__all__'


class ProjectMySQLDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMySQLDB
        fields = '__all__'


class GetProjectMySQLDBSerializer(serializers.ModelSerializer):
    host = HostSerializer(many=False)
    class Meta:
        model = ProjectMySQLDB
        fields = '__all__'


class MySQLDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySQLDB
        fields = '__all__'


class GetMySQLDBSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=False)
    project_mysql = GetProjectMySQLDBSerializer(read_only=True,many=True)
    class Meta:
        model = MySQLDB
        fields = '__all__'