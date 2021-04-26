from django.db import models
from django.utils import timezone
from .host import Host
from .project import Project


# Web
class ProjectWeb(models.Model):
    host = models.ManyToManyField(Host)
    public_ip = models.GenericIPAddressField('公网 IP')
    domain = models.CharField('域名', max_length=200)
    url = models.CharField('访问地址', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    software = models.CharField('软件', max_length=200)
    use = models.CharField('用途', max_length=200)
    dir = models.CharField('安装路径', max_length=200, blank=True)
    file_dir = models.CharField('文件路径', max_length=200, blank=True)
    username = models.CharField('用户名', max_length=200, blank=True)
    password = models.CharField('密码', max_length=200, blank=True)
    created = models.DateTimeField('创建时间',default=timezone.now)
