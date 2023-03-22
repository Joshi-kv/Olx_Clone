from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
import json

User=get_user_model()

# used to accept websocket connection

class chatConsumer(AsyncWebsocketConsumer):
    
    #it is called when connection established
    async def websocket_connect(self, event):
        print("Connected", event)
        user = self.scope['user']
        print(user)
        chat_room = f'user_chatroom_{user.id}'#creating a chat room using user id
        self.chat_room = chat_room
        #adding channel to the group
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        print(chat_room)
        #to accept established connection
        await self.accept()

    #it is called when message form submitted
    async def websocket_receive(self, event):
        print(f"Received {event}")
        #deserializing js string  into python objects 
        received_msg = json.loads(event['text'])
        message = received_msg.get('message')
        send_by_id = received_msg.get('send_by')
        send_to_id = received_msg.get('send_to')

        
        
        if not message : 
            return False
        response = {
            'message':message
        }
        
        #sending msg received on server to client
        response_str = json.dumps(response) #converting python objects into json string
        await self.send(response_str)
            
    #it is called when connection disconnected
    async def websocket_disconnect(self,event):
        print("Disconnected",event)