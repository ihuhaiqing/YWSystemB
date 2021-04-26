from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectKafka
from app.serializers import ProjectKafkaSerializer


# Project Kafka
class ProjectKafkaViewSet(viewsets.ModelViewSet):
    queryset = ProjectKafka.objects.all()
    serializer_class = ProjectKafkaSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectKafka.objects.filter(env=env, project=project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
