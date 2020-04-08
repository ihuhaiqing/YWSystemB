# from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from app.serializers import *
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user, assign_perm
from django.contrib.auth.models import Group
from app.drf.viewsets import CheckPermViewSet
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


class ProjectWebViewSet(CheckPermViewSet):
    queryset = ProjectWeb.objects.all()
    serializer_class = ProjectWebSerializer


class GetProjectWebViewSet(CheckPermViewSet):
    queryset = ProjectWeb.objects.all()
    serializer_class = GetProjectWebSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        software = request.GET.get('software')
        objects = ProjectWeb.objects.filter(env=env,project=project,software=software)
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)

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


class ProjectTomcatViewSet(CheckPermViewSet):
    queryset = ProjectTomcat.objects.all()
    serializer_class = ProjectTomcatSerializer

    def create(self, request, *args, **kwargs):
        hosts = request.data['host']

        for h in hosts:
            request.data['host'] = h
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = request.user
            user_groups = Group.objects.filter(user=user)
            if user.has_perm('app.add_%s' % self.basename):
                self.perform_create(serializer)
                if not user.is_superuser:
                    mdl = self.get_serializer_class().Meta.model
                    instance = mdl.objects.get(pk=serializer.data['id'])
                    if len(user_groups) == 0:
                        assign_perm('change_%s' % self.basename, instance)
                        assign_perm('view_%s' % self.basename, instance)
                        assign_perm('delete_%s' % self.basename, instance)
                    else:
                        for user_group in user_groups:
                            assign_perm('change_%s' % self.basename, user_group, instance)
                            assign_perm('view_%s' % self.basename, user_group, instance)
                            assign_perm('delete_%s' % self.basename, user_group, instance)
            else:
                return Response(data='没有新增权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)
        return Response( status=status.HTTP_201_CREATED)


class GetProjectTomcatViewSet(CheckPermViewSet):
    queryset = ProjectTomcat.objects.all()
    serializer_class = GetProjectTomcatSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        package_name = request.GET.get('package_name')
        objects = ProjectTomcat.objects.filter(env=env,project=project,package_name=package_name)
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)

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


class ProjectMySQLDBViewSet(CheckPermViewSet):
    queryset = ProjectMySQLDB.objects.all()
    serializer_class = ProjectMySQLDBSerializer


class ProjectGeneralSoftwareViewSet(CheckPermViewSet):
    queryset = ProjectGeneralSoftware.objects.all()
    serializer_class = ProjectGeneralSoftwareSerializer

    def create(self, request, *args, **kwargs):
        hosts = request.data['host']
        for h in hosts:
            request.data['host'] = h
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = request.user
            user_groups = Group.objects.filter(user=user)
            if user.has_perm('app.add_%s' % self.basename):
                self.perform_create(serializer)
                if not user.is_superuser:
                    mdl = self.get_serializer_class().Meta.model
                    instance = mdl.objects.get(pk=serializer.data['id'])
                    if len(user_groups) == 0:
                        assign_perm('change_%s' % self.basename, instance)
                        assign_perm('view_%s' % self.basename, instance)
                        assign_perm('delete_%s' % self.basename, instance)
                    else:
                        for user_group in user_groups:
                            assign_perm('change_%s' % self.basename, user_group, instance)
                            assign_perm('view_%s' % self.basename, user_group, instance)
                            assign_perm('delete_%s' % self.basename, user_group, instance)
            else:
                return Response(data='没有新增权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_201_CREATED)


class GetProjectGeneralSoftwareViewSet(CheckPermViewSet):
    queryset = ProjectGeneralSoftware.objects.all()
    serializer_class = GetProjectGeneralSoftwareSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        software = request.GET.get('software')
        objects = ProjectGeneralSoftware.objects.filter(env=env,project=project,software=software)
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

