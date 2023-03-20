from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

User=get_user_model()

# used to accept websocket connection

class chatConsumer(AsyncWebsocketConsumer):
    
    #it is called when connection established
    async def websocket_connect(self, event):
        print("Connected", event)
        await self.accept()

    #it is called when message received
    async def websocket_receive(self,event):
        print("Recieved",event)
    
    #it is called when connection disconnected
    async def websocket_disconnect(self,event):
        print("Disconnected",event)