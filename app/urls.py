from django.urls import path, include
from rest_framework import routers
from app.views import HostViewSet,AccountViewSet

router = routers.DefaultRouter()
router.register(r'hosts',HostViewSet)
router.register(r'accounts',AccountViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]