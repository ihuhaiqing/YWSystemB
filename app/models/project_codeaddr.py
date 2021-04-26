from django.db import models
from django.utils import timezone
from .project import Project


# Codeaddr
class ProjectCodeaddr(models.Model):
    name = models.CharField('名称', max_length=200)
    type = models.CharField('类别', max_length=200)
    addr = models.CharField('地址', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)
