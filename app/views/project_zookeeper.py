from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectZookeeper
from app.serializers import ProjectZookeeperSerializer, GetProjectZookeeperSerializer


# Project Zookeeper
class ProjectZookeeperViewSet(viewsets.ModelViewSet):
    queryset = ProjectZookeeper.objects.all()
    serializer_class = ProjectZookeeperSerializer


class GetProjectZookeeperViewSet(viewsets.ModelViewSet):
    queryset = ProjectZookeeper.objects.all()
    serializer_class = GetProjectZookeeperSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectZookeeper.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
