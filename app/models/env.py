from django.db import models


# 环境
class Env(models.Model):
    name_cn = models.CharField('中文名', max_length=200, unique=True)
    name_en = models.CharField('英文名', max_length=200, unique=True)

    class Meta:
        verbose_name = '环境'
        verbose_name_plural = '环境'

    def __str__(self):
        return self.name_cn
