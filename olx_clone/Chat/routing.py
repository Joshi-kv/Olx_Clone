from django.urls import path
from . consumers import *

websocket_urlpatterns = [
    path('chat/new-chat/',chatConsumer.as_asgi())
]