from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectJar
from app.serializers import ProjectJarSerializer, GetProjectJarSerializer


# Project Jar
class ProjectJarViewSet(viewsets.ModelViewSet):
    queryset = ProjectJar.objects.all()
    serializer_class = ProjectJarSerializer


class GetProjectJarViewSet(viewsets.ModelViewSet):
    queryset = ProjectJar.objects.all()
    serializer_class = GetProjectJarSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectJar.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
