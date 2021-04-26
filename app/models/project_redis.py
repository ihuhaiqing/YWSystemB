from django.db import models
from django.utils import timezone
from .instance_redis import RedisInstance
from .project import Project


# Redis
class ProjectRedis(models.Model):
    instance = models.ForeignKey(RedisInstance, on_delete=models.PROTECT, blank=True, related_name='redis_db')
    db = models.CharField('数据库', max_length=10, default=0)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)
