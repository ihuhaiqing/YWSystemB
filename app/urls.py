from django.urls import path, include
from rest_framework import routers
from app.views import HostViewSet,AccountViewSet,ProjectViewset

router = routers.DefaultRouter()
router.register(r'hosts',HostViewSet)
router.register(r'accounts',AccountViewSet)
router.register(r'projects',ProjectViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]