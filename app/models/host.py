from django.db import models
from django.utils import timezone


# 主机
class Host(models.Model):
    name = models.CharField('主机名', max_length=200)
    ip = models.GenericIPAddressField('内网 IP')
    outside_ip = models.GenericIPAddressField('外网 IP', default='0.0.0.0')
    manage_port = models.IntegerField('管理端口号', default=22)
    version = models.CharField('版本', max_length=200)
    cpu = models.IntegerField('CPU 核数', default=4)
    memory = models.CharField('内存大小', max_length=10, default='8G')
    disk = models.CharField('硬盘大小', max_length=10, default='80G')
    position = models.CharField('位置', max_length=200)
    admin = models.CharField('系统管理员', max_length=200, default='root')
    password = models.CharField('密码', max_length=200)
    type = models.CharField('类别', max_length=200)
    env = models.CharField('环境', max_length=200, default='test')
    ins_num = models.IntegerField('实例数量', default='0')
    status = models.BooleanField('状态', default=True)
    created = models.DateTimeField('创建时间', default=timezone.now)

    def __str__(self):
        return self.ip

    class Meta:
        unique_together = ['ip', 'type', 'name']
