from rest_framework.response import Response
from app.serializers.resource import *
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from app.drf.viewsets import CheckPermViewSet


# -------------------------------------------- 实例 --------------------------------------------
# MySQL 实例
class MySQLInstanceViewSet(CheckPermViewSet):
    queryset = MySQLInstance.objects.all()
    serializer_class = MySQLInstanceSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        inside_addr = request.GET.get('inside_addr')
        objects = MySQLInstance.objects.filter(inside_addr__contains=inside_addr).order_by('inside_addr')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Redis 实例
class RedisInstanceViewSet(CheckPermViewSet):
    queryset = RedisInstance.objects.all()
    serializer_class = RedisInstanceSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        inside_addr = request.GET.get('inside_addr')
        objects = RedisInstance.objects.filter(inside_addr__contains=inside_addr).order_by('cluster', 'inside_addr')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Zookeeper 实例
class ZookeeperInstanceViewSet(CheckPermViewSet):
    queryset = ZookeeperInstance.objects.all()
    serializer_class = ZookeeperInstanceSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        inside_addr = request.GET.get('inside_addr')
        objects = ZookeeperInstance.objects.filter(inside_addr__contains=inside_addr).order_by('cluster', 'inside_addr')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Activemq 实例
class ActivemqInstanceViewSet(CheckPermViewSet):
    queryset = ActivemqInstance.objects.all()
    serializer_class = ActivemqInstanceSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        inside_addr = request.GET.get('inside_addr')
        objects = ActivemqInstance.objects.filter(inside_addr__contains=inside_addr).order_by('cluster', 'inside_addr')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Rabbitmq 实例
class RabbitmqInstanceViewSet(CheckPermViewSet):
    queryset = RabbitmqInstance.objects.all()
    serializer_class = RabbitmqInstanceSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        inside_addr = request.GET.get('inside_addr')
        objects = RabbitmqInstance.objects.filter(inside_addr__contains=inside_addr).order_by('cluster', 'inside_addr')
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
