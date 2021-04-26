from rest_framework import viewsets
from app.models import Software
from app.serializers import SoftwareSerializer


# 软件
class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
