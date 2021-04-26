from django.db import models
from django.utils import timezone


# 账号
class Account(models.Model):
    use = models.CharField('名称', max_length=255, unique=True)
    username = models.CharField('用户名', max_length=200)
    password = models.CharField('密码', max_length=200)
    addr = models.CharField('地址', max_length=200, blank=True, null=True)
    remark = models.CharField('备注', max_length=255, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        ordering = ['use']
