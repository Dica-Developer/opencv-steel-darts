import json

from channels.generic.websocket import WebsocketConsumer

from darts_ui.darts_recognition.Darts import Darts, state


class StatusConsumer(WebsocketConsumer):
    def __init__(self, args):
        state.connect(self.update)

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.darts = Darts()
        self.darts.start()

    def update(self, sender, **kwargs):
        self.send(text_data=json.dumps({
            'message': kwargs['status']
        }))
