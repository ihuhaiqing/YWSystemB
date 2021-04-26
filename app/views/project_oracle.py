from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ProjectOracle
from app.serializers import ProjectOracleSerializer, GetProjectOracleSerializer


# Project Oracle
class ProjectOracleViewSet(viewsets.ModelViewSet):
    queryset = ProjectOracle.objects.all()
    serializer_class = ProjectOracleSerializer


class GetProjectOracleViewSet(viewsets.ModelViewSet):
    queryset = ProjectOracle.objects.all()
    serializer_class = GetProjectOracleSerializer

    def list(self, request, *args, **kwargs):
        env = request.GET.get('env')
        project = request.GET.get('project')
        queryset = ProjectOracle.objects.filter(env=env,project=project).order_by('host__ip')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
