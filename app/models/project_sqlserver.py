from django.db import models
from django.utils import timezone
from .project import Project


# SQLServer
class ProjectSQLServer(models.Model):
    name = models.CharField('数据库名', max_length=200)
    addr = models.CharField('地址', max_length=200)
    username = models.CharField('用户名', max_length=200)
    password = models.CharField('密码', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    created = models.DateTimeField('创建时间', default=timezone.now)
