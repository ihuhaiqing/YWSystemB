from channels.routing import ProtocolTypeRouter
from app.drf.views import task
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

application = ProtocolTypeRouter({
    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^api/task/$", task.TaskConsumer)
        ])
    ),
})