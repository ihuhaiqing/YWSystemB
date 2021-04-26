from django.db import models
from django.utils import timezone
from .project import Project


# Kafka
class ProjectKafka(models.Model):
    addr = models.CharField('地址', max_length=200)
    port = models.CharField('端口号', max_length=200, blank=True)
    dir = models.CharField('路径', max_length=200, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    created = models.DateTimeField('创建时间', default=timezone.now)
