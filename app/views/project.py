from rest_framework import viewsets
from rest_framework.response import Response
from app.serializers.resource import *
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from app.drf.viewsets import CheckPermViewSet
from app.models import Project


# -------------------------------------------- 项目 --------------------------------------------
# 项目
class ProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class GetProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        sort = request.GET.get('sort')
        name = request.GET.get('name')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        objects = Project.objects.filter(sort__contains=sort, name__contains=name)
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Web
class ProjectWebViewSet(viewsets.ModelViewSet):
    queryset = ProjectWeb.objects.all()
    serializer_class = ProjectWebSerializer


class GetProjectWebViewSet(viewsets.ModelViewSet):
    queryset = ProjectWeb.objects.all()
    serializer_class = GetProjectWebSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        software = request.GET.get('software')
        queryset = ProjectWeb.objects.filter(env=env,project=project,software=software)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project MySQL
class GetProjectMySQLDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMySQLDB.objects.all()
    serializer_class = GetProjectMySQLDBSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectMySQLDB.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectMySQLDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMySQLDB.objects.all()
    serializer_class = ProjectMySQLDBSerializer


# Project SQLServer
class ProjectSQLServerViewSet(viewsets.ModelViewSet):
    queryset = ProjectSQLServer.objects.all()
    serializer_class = ProjectSQLServerSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectSQLServer.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project MongoDB
class ProjectMongoDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMongoDB.objects.all()
    serializer_class = ProjectMongoDBSerializer


class GetProjectMongoDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMongoDB.objects.all()
    serializer_class = GetProjectMongoDBSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectMongoDB.objects.filter(env=env,project=project).order_by('type','shard','host__ip')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Oracle
class ProjectOracleViewSet(viewsets.ModelViewSet):
    queryset = ProjectOracle.objects.all()
    serializer_class = ProjectOracleSerializer


class GetProjectOracleViewSet(viewsets.ModelViewSet):
    queryset = ProjectOracle.objects.all()
    serializer_class = GetProjectOracleSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectOracle.objects.filter(env=env,project=project).order_by('host__ip')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Redis
class ProjectRedisViewSet(viewsets.ModelViewSet):
    queryset = ProjectRedis.objects.all()
    serializer_class = ProjectRedisSerializer


class GetProjectRedisViewSet(viewsets.ModelViewSet):
    queryset = ProjectRedis.objects.all()
    serializer_class = GetProjectRedisSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectRedis.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Jar
class ProjectJarViewSet(viewsets.ModelViewSet):
    queryset = ProjectJar.objects.all()
    serializer_class = ProjectJarSerializer


class GetProjectJarViewSet(viewsets.ModelViewSet):
    queryset = ProjectJar.objects.all()
    serializer_class = GetProjectJarSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectJar.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project War
class ProjectWarViewSet(viewsets.ModelViewSet):
    queryset = ProjectWar.objects.all()
    serializer_class = ProjectWarSerializer


class GetProjectWarViewSet(viewsets.ModelViewSet):
    queryset = ProjectWar.objects.all()
    serializer_class = GetProjectWarSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectWar.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# ProjectDotnet
class ProjectDotnetViewSet(viewsets.ModelViewSet):
    queryset = ProjectDotnet.objects.all()
    serializer_class = ProjectDotnetSerializer


class GetProjectDotnetViewSet(viewsets.ModelViewSet):
    queryset = ProjectDotnet.objects.all()
    serializer_class = GetProjectDotnetSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectDotnet.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# ProjectPHP
class ProjectPHPViewSet(viewsets.ModelViewSet):
    queryset = ProjectPHP.objects.all()
    serializer_class = ProjectPHPSerializer


class GetProjectPHPViewSet(viewsets.ModelViewSet):
    queryset = ProjectPHP.objects.all()
    serializer_class = GetProjectPHPSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectPHP.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Python
class ProjectPythonViewSet(viewsets.ModelViewSet):
    queryset = ProjectPython.objects.all()
    serializer_class = ProjectPythonSerializer


class GetProjectPythonViewSet(viewsets.ModelViewSet):
    queryset = ProjectPython.objects.all()
    serializer_class = GetProjectPythonSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectPython.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Rabbitmq
class ProjectRabbitmqViewSet(viewsets.ModelViewSet):
    queryset = ProjectRabbitmq.objects.all()
    serializer_class = ProjectRabbitmqSerializer


class GetProjectRabbitmqViewSet(viewsets.ModelViewSet):
    queryset = ProjectRabbitmq.objects.all()
    serializer_class = GetProjectRabbitmqSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectRabbitmq.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Activemq
class ProjectActivemqViewSet(viewsets.ModelViewSet):
    queryset = ProjectActivemq.objects.all()
    serializer_class = ProjectActivemqSerializer


class GetProjectActivemqViewSet(viewsets.ModelViewSet):
    queryset = ProjectActivemq.objects.all()
    serializer_class = GetProjectActivemqSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectActivemq.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Kafka
class ProjectKafkaViewSet(viewsets.ModelViewSet):
    queryset = ProjectKafka.objects.all()
    serializer_class = ProjectKafkaSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectKafka.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Zookeeper
class ProjectZookeeperViewSet(viewsets.ModelViewSet):
    queryset = ProjectZookeeper.objects.all()
    serializer_class = ProjectZookeeperSerializer


class GetProjectZookeeperViewSet(viewsets.ModelViewSet):
    queryset = ProjectZookeeper.objects.all()
    serializer_class = GetProjectZookeeperSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectZookeeper.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Codeaddr
class ProjectCodeaddrViewSet(viewsets.ModelViewSet):
    queryset = ProjectCodeaddr.objects.all()
    serializer_class = ProjectCodeaddrSerializer

    def list(self, request, *args, **kwargs):
        project = request.GET.get('project')
        queryset = ProjectCodeaddr.objects.filter(project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
