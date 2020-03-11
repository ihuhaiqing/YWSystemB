from django.urls import path, include
from rest_framework import routers
from app.views import HostViewSet

router = routers.DefaultRouter()
router.register(r'hosts',HostViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]