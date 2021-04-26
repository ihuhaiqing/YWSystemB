from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField('名称', max_length=200, unique=True)
    script_dir = models.CharField('脚本路径', max_length=200)
    script_name = models.CharField('脚本名', max_length=200, unique=True)
    arg = models.CharField('参数', max_length=200, blank=True)
    type = models.CharField('类别', max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)
