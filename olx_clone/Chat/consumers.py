from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
import json

User=get_user_model()

# used to accept websocket connection

class chatConsumer(AsyncWebsocketConsumer):
    
    #it is called when connection established
    async def websocket_connect(self, event):
        print("Connected", event)
        #to accept established connection
        await self.accept()

    #it is called when message form submitted
    async def websocket_receive(self, event):
        print(f"Received {event}")

    
    #it is called when connection disconnected
    async def websocket_disconnect(self,event):
        print("Disconnected",event)