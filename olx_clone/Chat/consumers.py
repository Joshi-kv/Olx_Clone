from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
import json
from channels.db import database_sync_to_async

User=get_user_model()

# used to accept websocket connection

class chatConsumer(AsyncWebsocketConsumer):
    
    #it is called when connection established
    async def websocket_connect(self, event):
        print("Connected", event)
        user = self.scope['user'] #to get the user object from websocket scope
        print(user)
        chat_room = f'user_chatroom_{user.id}' #creating a chat room using user id
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
        
        #retreive user objects from db using get_user_object function
        send_by_user = await self.get_user_object(send_by_id)
        send_to_user = await self.get_user_object(send_to_id)

        user_chatroom = f'other_user_chatroom_{send_to_id}'
        user = self.scope['user']
        response = {
            'message':message,
            'send_by':user.id
        }
        
        #sending msg received on server to client
        response_str = json.dumps(response) #converting python objects into json string
        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type':'chat_message',
                'text':response_str
            }
        )
        
        await self.channel_layer.group_send(
            user_chatroom,
            {
                'type':'chat_message',
                'text':response_str
            }
        )
        
               
            
    #it is called when connection disconnected
    async def websocket_disconnect(self,event):
        print("Disconnected",event)
         
         
    async def chat_message(self,event):
        print('chat message',event)
        await self.send(event['text'])
        
    #function to fetch user object from db asychronously
        
    @database_sync_to_async
    def get_user_object(self,user_id):
        qs = User.objects.filter(id=user_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj