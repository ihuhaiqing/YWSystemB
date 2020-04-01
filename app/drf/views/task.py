import paramiko
import json
from channels.generic.websocket import WebsocketConsumer


class TaskConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self,close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data=json.loads(text_data)
        print(data['test'])
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        try:
            s.connect(hostname='188.188.1.11', username='root', password='bsbneta', port=22)
        except Exception as e:
            self.send(text_data='连接服务器失败 %s' %e)
        cmd = 'cat /etc/rc.local'
        stdin, stdout, stderr = s.exec_command('%s 2>&1' %cmd)
        null_line_count = 0
        while True:
            text_data = stdout.readline()
            self.send(text_data=text_data)
            if not text_data:
                null_line_count += 1
            if null_line_count == 100:
                break
        s.close()
        self.send(text_data='closed')
