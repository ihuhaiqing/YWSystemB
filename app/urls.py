from django.urls import path, include
from rest_framework import routers
from app.views import *
from app.drf.views.auth import UserViewSet, GetUserViewSet, GroupViewSet,GetGroupViewSet,UserPassword

router = routers.DefaultRouter()
router.register(r'hosts',HostViewSet)
router.register(r'accounts',AccountViewSet)
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

urlpatterns = [
    path('',include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('changeMyPassword/',UserPassword.as_view())
]