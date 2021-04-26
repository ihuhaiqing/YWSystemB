from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectPython
from app.serializers import ProjectPythonSerializer, GetProjectPythonSerializer


# Project Python
class ProjectPythonViewSet(viewsets.ModelViewSet):
    queryset = ProjectPython.objects.all()
    serializer_class = ProjectPythonSerializer


class GetProjectPythonViewSet(viewsets.ModelViewSet):
    queryset = ProjectPython.objects.all()
    serializer_class = GetProjectPythonSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectPython.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
