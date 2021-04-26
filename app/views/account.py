from app.drf.viewsets import CheckPermViewSet
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from rest_framework.response import Response
from app.models import Account
from app.serializers import AccountSerializer


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
