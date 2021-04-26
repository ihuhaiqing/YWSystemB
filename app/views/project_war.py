from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectWar
from app.serializers import ProjectWarSerializer, GetProjectWarSerializer


# Project War
class ProjectWarViewSet(viewsets.ModelViewSet):
    queryset = ProjectWar.objects.all()
    serializer_class = ProjectWarSerializer


class GetProjectWarViewSet(viewsets.ModelViewSet):
    queryset = ProjectWar.objects.all()
    serializer_class = GetProjectWarSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectWar.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
