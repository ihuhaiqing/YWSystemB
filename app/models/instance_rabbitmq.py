from django.db import models
from django.utils import timezone


# Rabbitmq 实例
class RabbitmqInstance(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    web_addr = models.CharField('Web 地址', max_length=200, blank=True)
    dir = models.CharField('路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    manager = models.CharField('管理员', max_length=200)
    password = models.CharField('密码', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)
