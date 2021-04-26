from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectWeb
from app.serializers import ProjectWebSerializer, GetProjectWebSerializer


# Project Web
class ProjectWebViewSet(viewsets.ModelViewSet):
    queryset = ProjectWeb.objects.all()
    serializer_class = ProjectWebSerializer


class GetProjectWebViewSet(viewsets.ModelViewSet):
    queryset = ProjectWeb.objects.all()
    serializer_class = GetProjectWebSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        software = request.GET.get('software')
        queryset = ProjectWeb.objects.filter(env=env,project=project,software=software)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
