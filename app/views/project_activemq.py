from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectActivemq
from app.serializers import ProjectActivemqSerializer, GetProjectActivemqSerializer


# Project Activemq
class ProjectActivemqViewSet(viewsets.ModelViewSet):
    queryset = ProjectActivemq.objects.all()
    serializer_class = ProjectActivemqSerializer


class GetProjectActivemqViewSet(viewsets.ModelViewSet):
    queryset = ProjectActivemq.objects.all()
    serializer_class = GetProjectActivemqSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectActivemq.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
