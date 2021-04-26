from django.db import models


# 软件
class Software(models.Model):
    name = models.CharField('名称', max_length=200, unique=True)

    class Meta:
        verbose_name = '项目组件'
        verbose_name_plural = '项目组件'

    def __str__(self):
        return self.name
