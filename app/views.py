# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Host,Account
from app.serializers import HostSerializer,AccountSerialize
from rest_framework import pagination
# Create your views here.


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def list(self, request, *args, **kwargs):
        pagination.PageNumberPagination.page_size = request.GET.get('limit')
        ip = request.GET.get('ip')
        type = request.GET.get('type')
        env = request.GET.get('env')
        queryset = Host.objects.filter(ip__contains=ip,type__contains=type,env__contains=env).order_by('ip')

        page = self.paginate_queryset(queryset)
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
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

