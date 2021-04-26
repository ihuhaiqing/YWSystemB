from django.db import models
from django.utils import timezone
from .project import Project
from .host import Host


# Jar
class ProjectJar(models.Model):
    name = models.CharField('名称', max_length=200)
    dir = models.CharField('路径', max_length=200)
    port = models.CharField('端口号', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ManyToManyField(Host)
    method = models.CharField('部署方式', max_length=200, default='normal')
    created = models.DateTimeField('创建时间', default=timezone.now)
