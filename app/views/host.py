from app.drf.viewsets import CheckPermViewSet
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from rest_framework.response import Response
from app.models import Host
from app.serializers import HostSerializer


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

