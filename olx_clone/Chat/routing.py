from django.urls import path
from . consumers import *

websocket_urlpatterns = [
    path('chat/new-chat/<int:product_id>/',chatConsumer.as_asgi())
]