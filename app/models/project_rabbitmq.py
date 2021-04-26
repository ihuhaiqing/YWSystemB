from django.db import models
from django.utils import timezone
from .instance_rabbitmq import RabbitmqInstance
from .project import Project


# Rabbitmq
class ProjectRabbitmq(models.Model):
    instance = models.ForeignKey(RabbitmqInstance, on_delete=models.PROTECT, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    username = models.CharField('用户名', max_length=200, blank=True)
    password = models.CharField('密码', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)
