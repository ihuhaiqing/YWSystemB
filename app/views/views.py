# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from app.serializers.serializers import *
from app.serializers.resource import *
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from app.drf.viewsets import CheckPermViewSet
from rest_framework.views import APIView
from app.models import Project, Host
# Create your views here.


# 用户
class AccountViewSet(CheckPermViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        use = request.GET.get('use')
        objects = Account.objects.filter(use__icontains=use)
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)

        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
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
    queryset = Env.objects.all().order_by('name_cn')
    serializer_class = EnvSerializer


# 首页数据
class GetDashboardDataView(APIView):
    def get(self, request):
        project_count = Project.objects.count()
        host_count = Host.objects.count()
        account_count = Account.objects.count()

        return Response({'project_count': project_count, 'host_count': host_count, 'account_count': account_count})


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


# 一级菜单
class L1MenuViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuSerializer


# 二级模型菜单
class L2MenuViewSet(CheckPermViewSet):
    queryset = L2Menu.objects.all()
    serializer_class = L2MenuSerializer

    def list(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        objects = L2Menu.objects.filter()
        queryset = get_objects_for_user(request.user, '%s.view_%s' %(app, self.basename), objects)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
