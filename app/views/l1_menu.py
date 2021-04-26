from rest_framework import viewsets
from app.models import L1Menu
from app.serializers import L1MenuSerializer


# 一级菜单
class L1MenuViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuSerializer

