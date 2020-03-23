from django.urls import path, include
from rest_framework import routers
from app.views import *

router = routers.DefaultRouter()
router.register(r'hosts',HostViewSet)
router.register(r'accounts',AccountViewSet)
router.register(r'projects',ProjectViewSet)
router.register(r'softwares',SoftwareViewSet)
router.register(r'projectWeb',ProjectWebViewSet)
router.register(r'getProjectWeb',GetProjectWebViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]