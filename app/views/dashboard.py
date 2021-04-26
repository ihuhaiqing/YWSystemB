from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Project, Host, Account


# 首页数据
class GetDashboardDataView(APIView):
    def get(self, request):
        project_count = Project.objects.count()
        host_count = Host.objects.count()
        account_count = Account.objects.count()

        return Response({'project_count': project_count, 'host_count': host_count, 'account_count': account_count})
