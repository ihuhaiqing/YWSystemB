from django.db import models
from .env import Env
from .software import Software


# 项目
class Project(models.Model):
    name = models.CharField('项目名称', max_length=200, unique=True)
    software = models.ManyToManyField(Software)
    env = models.ManyToManyField(Env)
    sort = models.CharField('类别', max_length=200, default='other')
    status = models.CharField('状态', max_length=200, default='使用')

    class Meta:
        ordering = ['name']
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name
