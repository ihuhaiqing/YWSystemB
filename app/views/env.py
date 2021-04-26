from rest_framework import viewsets
from app.models import Env
from app.serializers import EnvSerializer


# 环境
class EnvViewSet(viewsets.ModelViewSet):
    queryset = Env.objects.all().order_by('name_cn')
    serializer_class = EnvSerializer
