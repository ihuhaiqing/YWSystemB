from django.db import models
from django.utils import timezone
from .project import Project
from .host import Host


# Oracle
class ProjectOracle(models.Model):
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ForeignKey(Host, on_delete=models.PROTECT)
    type = models.CharField('类别', max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('env', 'project', 'host', 'type')
