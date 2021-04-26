from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectMongoDB
from app.serializers import ProjectMongoDBSerializer, GetProjectMongoDBSerializer


# Project MongoDB
class ProjectMongoDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMongoDB.objects.all()
    serializer_class = ProjectMongoDBSerializer


class GetProjectMongoDBViewSet(viewsets.ModelViewSet):
    queryset = ProjectMongoDB.objects.all()
    serializer_class = GetProjectMongoDBSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectMongoDB.objects.filter(env=env,project=project).order_by('type','shard','host__ip')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
