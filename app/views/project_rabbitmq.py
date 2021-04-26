from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectRabbitmq
from app.serializers import ProjectRabbitmqSerializer, GetProjectRabbitmqSerializer


# Project Rabbitmq
class ProjectRabbitmqViewSet(viewsets.ModelViewSet):
    queryset = ProjectRabbitmq.objects.all()
    serializer_class = ProjectRabbitmqSerializer


class GetProjectRabbitmqViewSet(viewsets.ModelViewSet):
    queryset = ProjectRabbitmq.objects.all()
    serializer_class = GetProjectRabbitmqSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectRabbitmq.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
