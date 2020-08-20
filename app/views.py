# from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from app.serializers import *
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from app.drf.viewsets import CheckPermViewSet
from rest_framework.views import APIView
from app.models import Project, Host
# Create your views here.


# 用户
class AccountViewSet(CheckPermViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerialize
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        objects = self.filter_queryset(self.get_queryset())
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)

        PageNumberPagination.page_size = request.GET.get('limit')
        page = self.paginate_queryset(queryset)
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 软件
class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


# 环境
class EnvViewSet(viewsets.ModelViewSet):
    queryset = Env.objects.all()
    serializer_class = EnvSerializer


# 首页数据
class GetDashboardDataView(APIView):
    def get(self, request):
        project_count = Project.objects.count()
        host_count = Host.objects.count()

        return Response({'project_count':project_count,'host_count':host_count})


# 主机
class HostViewSet(CheckPermViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        ip = request.GET.get('ip')
        type = request.GET.get('type')
        env = request.GET.get('env')
        objects = Host.objects.filter(ip__contains=ip, type__contains=type, env__contains=env).order_by('ip')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 项目
class ProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class GetProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer


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
class ProjectMySQLDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMySQLDB.objects.all()
    serializer_class = ProjectMySQLDBSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectMySQLDB.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project SQLServer
class ProjectSQLServerViewSet(viewsets.ModelViewSet):
    queryset = ProjectSQLServer.objects.all()
    serializer_class = ProjectSQLServerSerialize

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
    serializer_class = ProjectRedisSerialize

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectRedis.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Jar
class ProjectJarViewSet(viewsets.ModelViewSet):
    queryset = ProjectJar.objects.all()
    serializer_class = ProjectJarSerialize


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
    serializer_class = ProjectWarSerialize


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
    serializer_class = ProjectDotnetSerialize


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
    serializer_class = ProjectPHPSerialize


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
    serializer_class = ProjectPythonSerialize


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

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectActivemq.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Kafka
class ProjectKafkaViewSet(viewsets.ModelViewSet):
    queryset = ProjectKafka.objects.all()
    serializer_class = ProjectKafkaSerialize

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectKafka.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Project Zookeeper
class ProjectZookeeperViewSet(viewsets.ModelViewSet):
    queryset = ProjectZookeeper.objects.all()
    serializer_class = ProjectZookeeperSerialize

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectZookeeper.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
