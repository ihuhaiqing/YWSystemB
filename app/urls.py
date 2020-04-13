from django.urls import path, include
from rest_framework import routers
from app.views import *
from app.drf.views.auth import *
from app.drf.views.task import TaskViewSet

router = routers.DefaultRouter()
router.register(r'contentType', ContentTypeViewSet)
router.register(r'hosts',HostViewSet)
router.register(r'accounts',AccountViewSet)
router.register(r'getProjects',GetProjectViewSet)
router.register(r'projects',ProjectViewSet)
router.register(r'softwares',SoftwareViewSet)
router.register(r'projectWeb',ProjectWebViewSet)
router.register(r'getProjectWeb',GetProjectWebViewSet)
router.register(r'javaPackages',JavaPackageViewSet)
router.register(r'getJavaPackages',GetJavaPackageViewSet)
router.register(r'projectTomcat',ProjectTomcatViewSet)
router.register(r'getProjectTomcat',GetProjectTomcatViewSet)
router.register(r'mysqldb',MySQLDBViewSet)
router.register(r'getMysqldb',GetMySQLDBViewSet)
router.register(r'projectMysqldb',ProjectMySQLDBViewSet)
router.register(r'users', UserViewSet)
router.register(r'getUsers', GetUserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'getGroups', GetGroupViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'projectGeneralSoftware', ProjectGeneralSoftwareViewSet)
router.register(r'getProjectGeneralSoftware', GetProjectGeneralSoftwareViewSet)
router.register(r'projectMongoDB', ProjectMongoDBViewSet)
router.register(r'getProjectMongoDB', GetProjectMongoDBViewSet)
router.register(r'projectOracle', ProjectOracleViewSet)
router.register(r'getProjectOracle', GetProjectOracleViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('changeMyPassword/',UserPassword.as_view()),
    path('getGroupObjectPerms/', GetGroupObjectPermsView.as_view()),
    path('setGroupObjectPerms/', SetGroupObjectPermsView.as_view()),
    path('getGroupPerms/', GetGroupPermsView.as_view()),
    path('getDashboardData/', GetDashboardDataView.as_view())
]