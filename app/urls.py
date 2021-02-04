from django.urls import path, include
from rest_framework import routers
from app.views.views import *
from app.views.instance import *
from app.views.project import *
from app.drf.views.auth import *
from app.drf.views.task import TaskViewSet

router = routers.DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'getEnv', EnvViewSet)
router.register(r'softwares', SoftwareViewSet)

router.register(r'contentType', ContentTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'getUsers', GetUserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'getGroups', GetGroupViewSet)

router.register(r'projects', ProjectViewSet)
router.register(r'getProjects', GetProjectViewSet)
router.register(r'projectWeb', ProjectWebViewSet)
router.register(r'getProjectWeb',GetProjectWebViewSet)

router.register(r'projectMysqldb', ProjectMySQLDBViewSet)
router.register(r'getProjectMysqldb', GetProjectMySQLDBViewSet)
router.register(r'projectMongoDB', ProjectMongoDBViewSet)
router.register(r'getProjectMongoDB', GetProjectMongoDBViewSet)
router.register(r'projectOracle', ProjectOracleViewSet)
router.register(r'getProjectOracle', GetProjectOracleViewSet)
router.register(r'projectSQLServer', ProjectSQLServerViewSet)
router.register(r'projectRedis', ProjectRedisViewSet)
router.register(r'getProjectRedis', GetProjectRedisViewSet)

router.register(r'projectJar', ProjectJarViewSet)
router.register(r'getProjectJar', GetProjectJarViewSet)
router.register(r'projectWar', ProjectWarViewSet)
router.register(r'getProjectWar', GetProjectWarViewSet)
router.register(r'projectDotnet', ProjectDotnetViewSet)
router.register(r'getProjectDotnet', GetProjectDotnetViewSet)
router.register(r'projectPHP', ProjectPHPViewSet)
router.register(r'getProjectPHP', GetProjectPHPViewSet)
router.register(r'projectPython', ProjectPythonViewSet)
router.register(r'getProjectPython', GetProjectPythonViewSet)
router.register(r'projectCodeaddr', ProjectCodeaddrViewSet)
router.register(r'getProjectCodeaddr', ProjectCodeaddrViewSet)

router.register(r'projectRabbitmq', ProjectRabbitmqViewSet)
router.register(r'getProjectRabbitmq', GetProjectRabbitmqViewSet)
router.register(r'projectActivemq', ProjectActivemqViewSet)
router.register(r'getProjectActivemq', GetProjectActivemqViewSet)
router.register(r'projectKafka', ProjectKafkaViewSet)
router.register(r'projectZookeeper', ProjectZookeeperViewSet)
router.register(r'getProjectZookeeper', GetProjectZookeeperViewSet)
# 实例
router.register(r'mysqlInstance', MySQLInstanceViewSet)
router.register(r'redisInstance', RedisInstanceViewSet)
router.register(r'zookeeperInstance', ZookeeperInstanceViewSet)
router.register(r'activemqInstance', ActivemqInstanceViewSet)
router.register(r'rabbitmqInstance', RabbitmqInstanceViewSet)

router.register(r'tasks', TaskViewSet)
router.register(r'accounts', AccountViewSet)

router.register(r'getL1Menu', L1MenuViewSet)
router.register(r'getL2Menu', L2MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('changeMyPassword/', UserPassword.as_view()),
    path('getGroupObjectPerms/', GetGroupObjectPermsView.as_view()),
    path('setGroupObjectPerms/', SetGroupObjectPermsView.as_view()),
    path('getGroupPerms/', GetGroupPermsView.as_view()),
    path('getGroupL2menu/', GetGroupL2menuView.as_view()),
    path('getDashboardData/', GetDashboardDataView.as_view()),
    path('getUserInfo/', GetUserInfoView.as_view())
]
