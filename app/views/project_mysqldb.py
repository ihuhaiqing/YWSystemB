from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectMySQLDB
from app.serializers import ProjectMySQLDBSerializer, GetProjectMySQLDBSerializer


# Project MySQL
class GetProjectMySQLDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMySQLDB.objects.all()
    serializer_class = GetProjectMySQLDBSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectMySQLDB.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectMySQLDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMySQLDB.objects.all()
    serializer_class = ProjectMySQLDBSerializer
