# VividComm/routing.py
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import ChatConsumer # Import the new consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})