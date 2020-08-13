# from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from app.serializers import *
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from app.drf.viewsets import CheckPermViewSet
from rest_framework.views import APIView
from app.models import Project, Host, MySQLDB, JavaPackage
# Create your views here.


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
        objects = Host.objects.filter(ip__contains=ip,type__contains=type,env__contains=env).order_by('ip')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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


class ProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class GetProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer


class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer

class EnvViewSet(viewsets.ModelViewSet):
    queryset = Env.objects.all()
    serializer_class = EnvSerializer

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


class JavaPackageViewSet(CheckPermViewSet):
    queryset = JavaPackage.objects.all()
    serializer_class = JavaPackageSerializer


class GetJavaPackageViewSet(CheckPermViewSet):
    queryset = JavaPackage.objects.all()
    serializer_class = GetJavaPackageSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        name = request.GET.get('name')
        project = request.GET.get('project')
        objects = JavaPackage.objects.filter(name__contains=name,project__name__contains=project).order_by('name')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectTomcatViewSet(viewsets.ModelViewSet):
    queryset = ProjectTomcat.objects.all()
    serializer_class = ProjectTomcatSerializer

    def create(self, request, *args, **kwargs):
        hosts = request.data['host']

        for h in hosts:
            request.data['host'] = h
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return Response( status=status.HTTP_201_CREATED)


class GetProjectTomcatViewSet(CheckPermViewSet):
    queryset = ProjectTomcat.objects.all()
    serializer_class = GetProjectTomcatSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        package_name = request.GET.get('package_name')
        queryset = ProjectTomcat.objects.filter(env=env,project=project,package_name=package_name)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MySQLDBViewSet(CheckPermViewSet):
    queryset = MySQLDB.objects.all().order_by('name')
    serializer_class = MySQLDBSerializer


class GetMySQLDBViewSet(CheckPermViewSet):
    queryset = MySQLDB.objects.all().order_by('name')
    serializer_class = GetMySQLDBSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        name = request.GET.get('name')
        project = request.GET.get('project')
        if project == '':
            objects = MySQLDB.objects.filter(name__contains=name).order_by('name')
            queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        else:
            objects = MySQLDB.objects.filter(name__contains=name,project__id=project).order_by('name')
            queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectMySQLDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMySQLDB.objects.all()
    serializer_class = ProjectMySQLDBSerializer


class ProjectGeneralSoftwareViewSet(viewsets.ModelViewSet):
    queryset = ProjectGeneralSoftware.objects.all()
    serializer_class = ProjectGeneralSoftwareSerializer

    def create(self, request, *args, **kwargs):
        hosts = request.data['host']
        for h in hosts:
            request.data['host'] = h
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED)


class GetProjectGeneralSoftwareViewSet(viewsets.ModelViewSet):
    queryset = ProjectGeneralSoftware.objects.all()
    serializer_class = GetProjectGeneralSoftwareSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        software = request.GET.get('software')
        queryset = ProjectGeneralSoftware.objects.filter(env=env,project=project,software=software)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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


class GetDashboardDataView(APIView):
    def get(self,request):
        project_count = Project.objects.count()
        host_count = Host.objects.count()
        java_package_count = JavaPackage.objects.count()
        mysqldb_count = MySQLDB.objects.count()

        return Response({'project_count':project_count,'host_count':host_count, 'java_package_count':java_package_count, 'mysqldb_count':mysqldb_count})


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


class ProjectRedisViewSet(viewsets.ModelViewSet):
    queryset = ProjectRedis.objects.all()
    serializer_class = ProjectRedisSerialize

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectRedis.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
