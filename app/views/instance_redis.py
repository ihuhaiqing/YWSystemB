from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from app.drf.viewsets import CheckPermViewSet
from app.models import RedisInstance
from app.serializers import RedisInstanceSerializer


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
