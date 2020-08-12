import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    print('lorem')
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print("Connect")
        self.room_group_name = 'live_%s' % self.room_name

        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_groupe_name,
        #     self.channel_name
        # )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('recive',text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        # async_to_sync(self.channel_layer.group_send)({
        #     'type': 'char_message',
        #     'message': message
        # })
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))


    async def chat_message(self, event):
        message = event['message']
        print('chat_message', message)
        await self.send(
            text_data = json.dumps({
                'message': message
            })
        )