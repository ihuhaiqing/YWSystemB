# from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from app.models import Host,Account,Project,Software
from app.serializers import *
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class HostViewSet(viewsets.ModelViewSet):
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
        queryset = Host.objects.filter(ip__contains=ip,type__contains=type,env__contains=env).order_by('ip')
        page = self.paginate_queryset(queryset)

        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerialize
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        PageNumberPagination.page_size = request.GET.get('limit')
        page = self.paginate_queryset(queryset)
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


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


class JavaPackageViewSet(viewsets.ModelViewSet):
    queryset = JavaPackage.objects.all()
    serializer_class = JavaPackageSerializer


class GetJavaPackageViewSet(viewsets.ModelViewSet):
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
        queryset = JavaPackage.objects.filter(name__contains=name,project__name__contains=project).order_by('name')
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
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetProjectTomcatViewSet(viewsets.ModelViewSet):
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

