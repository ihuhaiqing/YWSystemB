from django.db import models
from django.utils import timezone
from .project import Project
from .host import Host


# Mongodb
class ProjectMongoDB(models.Model):
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ForeignKey(Host, on_delete=models.PROTECT)
    type = models.CharField('类别', max_length=200)
    shard = models.CharField('分片', max_length=200, blank=True)
    role = models.CharField('角色', max_length=200, blank=True)
    port = models.IntegerField('端口号', blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('env', 'project', 'host', 'port')
