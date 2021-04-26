from django.db import models
from django.utils import timezone
from .instance_mysql import MySQLInstance
from .project import Project


# MySQL
class ProjectMySQLDB(models.Model):
    name = models.CharField('数据库名', max_length=200)
    instance = models.ForeignKey(MySQLInstance, on_delete=models.PROTECT, blank=True)
    username = models.CharField('用户名', max_length=200)
    password = models.CharField('密码', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)
