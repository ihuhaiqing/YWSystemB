import paramiko
import json
from channels.generic.websocket import WebsocketConsumer
from app.models import Task
from app.drf.serializers.task import TaskSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from app.drf.viewsets import CheckPermViewSet
from guardian.shortcuts import get_objects_for_user
from app.models import JavaPackage


class TaskViewSet(CheckPermViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        name = request.GET.get('name')
        type = request.GET.get('type')

        objects = Task.objects.filter(name__contains=name,type__contains=type)
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TaskConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self,close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        task = data['task']
        if task['arg']:
            arg = task['arg'] + ' '
        else:
            arg = ''
        hosts = data['hosts']
        cmd = 'sh ' + task['script_dir'] + '/' + task['script_name'] + ' ' + arg + '2>&1'
        for host in hosts:
            ip = host['ip']
            username = host['admin']
            password = host['password']
            s = paramiko.SSHClient()
            s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            try:
                s.connect(hostname=ip, username=username, password=password, port=22)
            except Exception as e:
                self.send(text_data='连接服务器 %s 失败 %s \n' %(ip,e))
                continue
            self.send(text_data='开始在服务器 %s 上 %s \n' % (ip,task['name']))
            stdin, stdout, stderr = s.exec_command(cmd)
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


class ControlJarConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self,close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
        jar = JavaPackage.objects.get(name=data['jar'])
        hosts = data['hosts']
        script = '/data/scripts/%s_jar.sh' %data['cmd']
        cmd = 'sh ' + script + ' ' + data['jar'] + ' 2>&1'
        for host in hosts:
            ip = host['ip']
            username = host['admin']
            password = host['password']
            s = paramiko.SSHClient()
            s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            try:
                s.connect(hostname=ip, username=username, password=password, port=22)
            except Exception as e:
                self.send(text_data='连接服务器 %s 失败 %s \n' %(ip,e))
                continue
            self.send(text_data='开始在服务器 %s 上执行 \n' % (ip))
            print(cmd)
            stdin, stdout, stderr = s.exec_command(cmd)
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
