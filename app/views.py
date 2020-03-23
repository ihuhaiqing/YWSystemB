# from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from app.models import Host,Account,Project,Software
from app.serializers import *
from rest_framework import pagination
# Create your views here.


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            pagination.PageNumberPagination.page_size = None
        else:
            pagination.PageNumberPagination.page_size = page_size
        ip = request.GET.get('ip')
        type = request.GET.get('type')
        env = request.GET.get('env')
        queryset = Host.objects.filter(ip__contains=ip,type__contains=type,env__contains=env).order_by('ip')
        page = self.paginate_queryset(queryset)

        pagination.PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerialize

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        pagination.PageNumberPagination.page_size = request.GET.get('limit')
        page = self.paginate_queryset(queryset)
        pagination.PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SoftwareViewSet(viewsets.ModelViewSet):
    pagination.PageNumberPagination.page_size = None
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
        print(env)
        queryset = ProjectWeb.objects.filter(env=env,project=project,software=software)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

