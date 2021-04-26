from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectSQLServer
from app.serializers import ProjectSQLServerSerializer


# Project SQLServer
class ProjectSQLServerViewSet(viewsets.ModelViewSet):
    queryset = ProjectSQLServer.objects.all()
    serializer_class = ProjectSQLServerSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectSQLServer.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
