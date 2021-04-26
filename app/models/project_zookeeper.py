from django.db import models
from django.utils import timezone
from .instance_zookeeper import ZookeeperInstance
from .project import Project


# Zookeeper
class ProjectZookeeper(models.Model):
    instance = models.ForeignKey(ZookeeperInstance, on_delete=models.PROTECT, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)
