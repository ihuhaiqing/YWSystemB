import paramiko
from dwebsocket.decorators import accept_websocket
import time
import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.send(text_data='closed')

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        # text_data = text_data.decode('utf-8')
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        s.connect(hostname='188.188.1.141', username='root', password='bsbnet', port=22)
        cmd = 'ls /'
        stdin, stdout, stderr = s.exec_command(cmd)
        while True:
            text_data = stdout.readline().strip()
            self.send(text_data=text_data)
            if not text_data:
                break

        s.close()
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        self.disconnect(1000)

@accept_websocket
def execScript(request):
    for message in request.websocket:
        print('aaaa')
        print(message)
        message = message.decode('utf-8')
        filename = message
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        s.connect(hostname='188.188.1.141', username='root', password='bsbnet', port=22)
        cmd = 'ls /'
        stdin, stdout, stderr = s.exec_command(cmd)
        nullcount = 0
        while True:
            # outline = stdout.readline().strip().encode('utf-8')
            request.websocket.send(stdout)
            if not stdout:
                nullcount = nullcount + 1
                if nullcount == 100:
                    break
        time.sleep(5)
        s.close()

        request.websocket.send('closed')