from app.models import *
from rest_framework import serializers


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env
        fields = '__all__'


# ------------------------------------------ 实例 ----------------------------------------------
# MySQL 实例
class MySQLInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySQLInstance
        fields = '__all__'


# Redis 实例
class RedisInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedisInstance
        fields = '__all__'


# Zookeeper 实例
class ZookeeperInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZookeeperInstance
        fields = '__all__'


# Activemq 实例
class ActivemqInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivemqInstance
        fields = '__all__'


# Rabbitmq 实例
class RabbitmqInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RabbitmqInstance
        fields = '__all__'


# ------------------------------------------ 资源管理 ----------------------------------------------
class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


# Project
class ProjectSerializer(serializers.ModelSerializer):
    software = serializers.PrimaryKeyRelatedField(queryset=Software.objects.all(),many=True)
    env = serializers.PrimaryKeyRelatedField(queryset=Env.objects.all(),many=True)

    class Meta:
        model = Project
        fields = '__all__'


class GetProjectSerializer(serializers.ModelSerializer):
    software = SoftwareSerializer(read_only=True,many=True)
    env = EnvSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


# Project Web
class ProjectWebSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), write_only=True,many=True)

    class Meta:
        model = ProjectWeb
        fields = '__all__'


class GetProjectWebSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectWeb
        fields = '__all__'


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


# Project MongoDB
class ProjectMongoDBSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=False)

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


# Project SQLServer
class ProjectSQLServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSQLServer
        fields = '__all__'


# Project Redis
class ProjectRedisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRedis
        fields = '__all__'


class GetProjectRedisSerializer(serializers.ModelSerializer):
    instance = RedisInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectRedis
        fields = '__all__'


# Project Jar
class ProjectJarSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=True)

    class Meta:
        model = ProjectJar
        fields = '__all__'


class GetProjectJarSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectJar
        fields = '__all__'


# Project War
class ProjectWarSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(), many=True)

    class Meta:
        model = ProjectWar
        fields = '__all__'


class GetProjectWarSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectWar
        fields = '__all__'


# Project Dotnet
class GetProjectDotnetSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectDotnet
        fields = '__all__'


class ProjectDotnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDotnet
        fields = '__all__'


# Project PHP
class GetProjectPHPSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectPHP
        fields = '__all__'


class ProjectPHPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPHP
        fields = '__all__'


# Project Python
class GetProjectPythonSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectPython
        fields = '__all__'


class ProjectPythonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPython
        fields = '__all__'


# Project Rabbitmq
class ProjectRabbitmqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRabbitmq
        fields = '__all__'


class GetProjectRabbitmqSerializer(serializers.ModelSerializer):
    instance = RabbitmqInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectRabbitmq
        fields = '__all__'


# Project Activemq
class ProjectActivemqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectActivemq
        fields = '__all__'


class GetProjectActivemqSerializer(serializers.ModelSerializer):
    instance = ActivemqInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectActivemq
        fields = '__all__'


# Project Kafka
class ProjectKafkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectKafka
        fields = '__all__'


# Project Zookeeper
class ProjectZookeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectZookeeper
        fields = '__all__'


class GetProjectZookeeperSerializer(serializers.ModelSerializer):
    instance = ZookeeperInstanceSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectZookeeper
        fields = '__all__'


# Project Codeaddr
class ProjectCodeaddrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCodeaddr
        fields = '__all__'
