from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectPHP
from app.serializers import ProjectPHPSerializer, GetProjectPHPSerializer


# ProjectPHP
class ProjectPHPViewSet(viewsets.ModelViewSet):
    queryset = ProjectPHP.objects.all()
    serializer_class = ProjectPHPSerializer


class GetProjectPHPViewSet(viewsets.ModelViewSet):
    queryset = ProjectPHP.objects.all()
    serializer_class = GetProjectPHPSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectPHP.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
