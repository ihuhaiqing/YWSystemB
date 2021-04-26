from app.drf.viewsets import CheckPermViewSet
from guardian.shortcuts import get_objects_for_user
from rest_framework.response import Response
from app.models import L2Menu
from app.serializers import L2MenuSerializer


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
