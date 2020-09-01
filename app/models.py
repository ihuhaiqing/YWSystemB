from django.db import models
from django.utils import timezone
# Create your models here.


# 账号
class Account(models.Model):
    username = models.CharField('用户名', max_length=200)
    password = models.CharField('密码', max_length=200)
    addr = models.CharField('地址', max_length=200, blank=True, null=True)
    use = models.CharField('用途', max_length=255)
    remark = models.CharField('备注', max_length=255, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# 环境
class Env(models.Model):
    name_cn = models.CharField('中文名', max_length=200, unique=True)
    name_en = models.CharField('英文名', max_length=200, unique=True)

    class Meta:
        verbose_name = '环境'
        verbose_name_plural = '环境'

    def __str__(self):
        return self.name_cn


# 软件
class Software(models.Model):
    name = models.CharField('软件名称', max_length=200,unique=True)

    class Meta:
        verbose_name = '软件语言'
        verbose_name_plural = '软件语言'

    def __str__(self):
        return self.name


# ------------------------------------- 实例 -------------------------------------
# MySQL 实例
class MySQLInstance(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    role = models.CharField('角色', max_length=200)
    data_dir = models.CharField('数据库路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    manager = models.CharField('管理员', max_length=200)
    password = models.CharField('密码', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Redis 实例
class RedisInstance(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    dir = models.CharField('路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    password = models.CharField('密码', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Zookeeper 实例
class ZookeeperInstance(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    dir = models.CharField('路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Activemq 实例
class ActivemqInstance(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    web_addr = models.CharField('Web 地址', max_length=200, blank=True)
    dir = models.CharField('路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    manager = models.CharField('管理员', max_length=200)
    password = models.CharField('密码', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Rabbitmq 实例
class RabbitmqInstance(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    web_addr = models.CharField('Web 地址', max_length=200, blank=True)
    dir = models.CharField('路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    manager = models.CharField('管理员', max_length=200)
    password = models.CharField('密码', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# ------------------------------------- 资源管理 -------------------------------------
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


# 项目
class Project(models.Model):
    name = models.CharField('项目名称', max_length=200, unique=True)
    software = models.ManyToManyField(Software)
    env = models.ManyToManyField(Env)
    sort = models.CharField('类别', max_length=200, default='other')

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name


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


# MySQL
class ProjectMySQLDB(models.Model):
    name = models.CharField('数据库名', max_length=200)
    instance = models.ForeignKey(MySQLInstance, on_delete=models.PROTECT, blank=True)
    username = models.CharField('用户名', max_length=200)
    password = models.CharField('密码', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Mongodb
class ProjectMongoDB(models.Model):
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    type = models.CharField('类别',max_length=200)
    shard = models.CharField('分片',max_length=200, blank=True)
    role = models.CharField('角色', max_length=200, blank=True)
    port = models.IntegerField('端口号',blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('env','project','host','port')


# Oracle
class ProjectOracle(models.Model):
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    type = models.CharField('类别', max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('env','project','host','type')


# SQLServer
class ProjectSQLServer(models.Model):
    name = models.CharField('数据库名', max_length=200)
    addr = models.CharField('地址', max_length=200)
    username = models.CharField('用户名', max_length=200)
    password = models.CharField('密码', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    created = models.DateTimeField('创建时间', default=timezone.now)


# Redis
class ProjectRedis(models.Model):
    instance = models.ForeignKey(RedisInstance, on_delete=models.PROTECT, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Jar
class ProjectJar(models.Model):
    name = models.CharField('名称', max_length=200)
    dir = models.CharField('路径', max_length=200)
    port = models.CharField('端口号', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ManyToManyField(Host)
    method = models.CharField('部署方式', max_length=200, default='normal')
    created = models.DateTimeField('创建时间', default=timezone.now)


# War
class ProjectWar(models.Model):
    name = models.CharField('名称', max_length=200)
    dir = models.CharField('路径', max_length=200)
    port = models.CharField('端口号', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ManyToManyField(Host)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Dotnet
class ProjectDotnet(models.Model):
    name = models.CharField('名称', max_length=200)
    dir = models.CharField('路径', max_length=200)
    port = models.CharField('端口号', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ManyToManyField(Host)
    method = models.CharField('部署方式', max_length=200, default='normal')
    created = models.DateTimeField('创建时间', default=timezone.now)


# PHP
class ProjectPHP(models.Model):
    name = models.CharField('名称', max_length=200)
    dir = models.CharField('路径', max_length=200)
    port = models.CharField('端口号', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ManyToManyField(Host)
    method = models.CharField('部署方式', max_length=200, default='normal')
    created = models.DateTimeField('创建时间', default=timezone.now)


# Python
class ProjectPython(models.Model):
    name = models.CharField('名称', max_length=200)
    dir = models.CharField('路径', max_length=200)
    port = models.CharField('端口号', max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ManyToManyField(Host)
    method = models.CharField('部署方式', max_length=200, default='normal')
    created = models.DateTimeField('创建时间', default=timezone.now)


# Rabbitmq
class ProjectRabbitmq(models.Model):
    instance = models.ForeignKey(RabbitmqInstance, on_delete=models.PROTECT, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    username = models.CharField('用户名', max_length=200, blank=True)
    password = models.CharField('密码', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Activemq
class ProjectActivemq(models.Model):
    instance = models.ForeignKey(ActivemqInstance, on_delete=models.PROTECT, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    username = models.CharField('用户名', max_length=200, blank=True)
    password = models.CharField('密码', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)


# Kafka
class ProjectKafka(models.Model):
    addr = models.CharField('地址', max_length=200)
    port = models.CharField('端口号', max_length=200, blank=True)
    dir = models.CharField('路径', max_length=200, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    created = models.DateTimeField('创建时间', default=timezone.now)


# Zookeeper
class ProjectZookeeper(models.Model):
    instance = models.ForeignKey(ZookeeperInstance, on_delete=models.PROTECT, blank=True)
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)


# ---------------------------------------------------------------------------------------
class Task(models.Model):
    name = models.CharField('名称',max_length=200,unique=True)
    script_dir = models.CharField('脚本路径', max_length=200)
    script_name = models.CharField('脚本名',max_length=200,unique=True)
    arg = models.CharField('参数',max_length=200,blank=True)
    type = models.CharField('类别',max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)
