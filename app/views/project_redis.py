from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectRedis
from app.serializers import ProjectRedisSerializer, GetProjectRedisSerializer


# Project Redis
class ProjectRedisViewSet(viewsets.ModelViewSet):
    queryset = ProjectRedis.objects.all()
    serializer_class = ProjectRedisSerializer


class GetProjectRedisViewSet(viewsets.ModelViewSet):
    queryset = ProjectRedis.objects.all()
    serializer_class = GetProjectRedisSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectRedis.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
