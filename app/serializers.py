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


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    software = serializers.PrimaryKeyRelatedField(queryset=Software.objects.all(),many=True)
    env = serializers.PrimaryKeyRelatedField(queryset=Env.objects.all(),many=True)
    class Meta:
        model = Project
        fields = '__all__'


class GetJavaPackageSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=False)
    class Meta:
        model = JavaPackage
        fields = '__all__'


class GetProjectSerializer(serializers.ModelSerializer):
    java_package = JavaPackageSerializer(read_only=True,many=True)
    software = SoftwareSerializer(read_only=True,many=True)
    env = EnvSerializer(many=True)
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


# class GetProjectMySQLDBSerializer(serializers.ModelSerializer):
#     host = HostSerializer(many=False)
#     class Meta:
#         model = ProjectMySQLDB
#         fields = '__all__'


# class MySQLDBSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MySQLDB
#         fields = '__all__'
#
#
# class GetMySQLDBSerializer(serializers.ModelSerializer):
#     project = GetProjectSerializer(many=False)
#     project_mysql = GetProjectMySQLDBSerializer(read_only=True,many=True)
#     class Meta:
#         model = MySQLDB
#         fields = '__all__'


class ProjectGeneralSoftwareSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(),many=False)
    class Meta:
        model = ProjectGeneralSoftware
        fields = '__all__'


class GetProjectGeneralSoftwareSerializer(serializers.ModelSerializer):
    # ManyToManyField: many=True
    # ForeignKey: many=False 默认值
    host = HostSerializer(many=False)
    class Meta:
        model = ProjectGeneralSoftware
        fields = '__all__'


class ProjectMongoDBSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(),many=False)
    class Meta:
        model = ProjectMongoDB
        fields = '__all__'


class GetProjectMongoDBSerializer(serializers.ModelSerializer):
    # ManyToManyField: many=True
    # ForeignKey: many=False 默认值
    host = HostSerializer(many=False)
    class Meta:
        model = ProjectMongoDB
        fields = '__all__'


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


class ProjectJarSerialize(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=True)

    class Meta:
        model = ProjectJar
        fields = '__all__'


class GetProjectJarSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectJar
        fields = '__all__'


class ProjectWarSerialize(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=True)

    class Meta:
        model = ProjectWar
        fields = '__all__'


class GetProjectWarSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectWar
        fields = '__all__'


class ProjectRedisSerialize(serializers.ModelSerializer):
    class Meta:
        model = ProjectRedis
        fields = '__all__'


class GetProjectDotnetSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectDotnet
        fields = '__all__'


class ProjectDotnetSerialize(serializers.ModelSerializer):
    class Meta:
        model = ProjectDotnet
        fields = '__all__'


class GetProjectPHPSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectPHP
        fields = '__all__'


class ProjectPHPSerialize(serializers.ModelSerializer):
    class Meta:
        model = ProjectPHP
        fields = '__all__'
