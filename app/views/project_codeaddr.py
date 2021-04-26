from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectCodeaddr
from app.serializers import ProjectCodeaddrSerializer


# Project Codeaddr
class ProjectCodeaddrViewSet(viewsets.ModelViewSet):
    queryset = ProjectCodeaddr.objects.all()
    serializer_class = ProjectCodeaddrSerializer

    def list(self, request, *args, **kwargs):
        project = request.GET.get('project')
        queryset = ProjectCodeaddr.objects.filter(project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
