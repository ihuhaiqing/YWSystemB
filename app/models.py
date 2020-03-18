from django.db import models
from django.utils import timezone

# Create your models here.


class Host(models.Model):
    name = models.CharField('主机名',max_length=200,unique=True)
    ip = models.GenericIPAddressField('IP 地址',unique=True)
    version = models.CharField('版本',max_length=200)
    cpu = models.IntegerField('CPU 核数',default=4)
    memory = models.CharField('内存大小',max_length=10,default='8G')
    disk = models.CharField('硬盘大小',max_length=10,default='80G')
    position = models.CharField('位置',max_length=200)
    admin = models.CharField('系统管理员',max_length=200,default='root')
    password = models.CharField('密码',max_length=200)
    type = models.CharField('类别',max_length=200)
    env = models.CharField('环境',max_length=200,default='test')
    ins_num = models.IntegerField('实例数量',default='0')
    status = models.BooleanField('状态',default=True)
    created = models.DateTimeField('创建时间',default=timezone.now)


class Account(models.Model):
    username = models.CharField('用户名',max_length=200,unique=True)
    password = models.CharField('密码',max_length=200)
    use = models.CharField('用途',max_length=255)
    created = models.DateTimeField('创建时间',default=timezone.now)

