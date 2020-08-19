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
router.register(r'projectMysqldb', ProjectMySQLDBViewSet)
router.register(r'projectRabbitmq', ProjectRabbitmqViewSet)
router.register(r'projectActivemq', ProjectActivemqViewSet)
router.register(r'users', UserViewSet)
router.register(r'getUsers', GetUserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'getGroups', GetGroupViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'projectMongoDB', ProjectMongoDBViewSet)
router.register(r'getProjectMongoDB', GetProjectMongoDBViewSet)
router.register(r'projectOracle', ProjectOracleViewSet)
router.register(r'getProjectOracle', GetProjectOracleViewSet)
router.register(r'getEnv', EnvViewSet)
router.register(r'projectJar', ProjectJarViewSet)
router.register(r'getProjectJar', GetProjectJarViewSet)
router.register(r'projectWar', ProjectWarViewSet)
router.register(r'getProjectWar', GetProjectWarViewSet)
router.register(r'projectRedis', ProjectRedisViewSet)
router.register(r'projectDotnet', ProjectDotnetViewSet)
router.register(r'getProjectDotnet', GetProjectDotnetViewSet)
router.register(r'projectPHP', ProjectPHPViewSet)
router.register(r'getProjectPHP', GetProjectPHPViewSet)
router.register(r'projectPython', ProjectPythonViewSet)
router.register(r'getProjectPython', GetProjectPythonViewSet)
router.register(r'projectKafka', ProjectKafkaViewSet)
router.register(r'projectZookeeper', ProjectZookeeperViewSet)
router.register(r'projectSQLServer', ProjectSQLServerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('changeMyPassword/',UserPassword.as_view()),
    path('getGroupObjectPerms/', GetGroupObjectPermsView.as_view()),
    path('setGroupObjectPerms/', SetGroupObjectPermsView.as_view()),
    path('getGroupPerms/', GetGroupPermsView.as_view()),
    path('getDashboardData/', GetDashboardDataView.as_view()),
    path('getUserInfo/', GetUserInfoView.as_view())
]