# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # This is called when a WebSocket connection is made.
        # We'll accept all connections for now.
        await self.accept()

    async def disconnect(self, close_code):
        # This is called when the WebSocket connection is closed.
        pass

    async def receive(self, text_data):
        # This is called when a message is received from the WebSocket.
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send the received message back to the client.
        await self.send(text_data=json.dumps({
            'message': message
        }))