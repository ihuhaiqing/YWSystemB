from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectDotnet
from app.serializers import ProjectDotnetSerializer, GetProjectDotnetSerializer


# ProjectDotnet
class ProjectDotnetViewSet(viewsets.ModelViewSet):
    queryset = ProjectDotnet.objects.all()
    serializer_class = ProjectDotnetSerializer


class GetProjectDotnetViewSet(viewsets.ModelViewSet):
    queryset = ProjectDotnet.objects.all()
    serializer_class = GetProjectDotnetSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectDotnet.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
