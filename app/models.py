from django.db import models
from django.utils import timezone
from django.contrib.auth.models import ContentType


# 一级菜单
class L1Menu(models.Model):
    name = models.CharField('名称', max_length=255, unique=True)
    title = models.CharField('显示名称', max_length=255)
    path = models.CharField('URI', max_length=255, unique=True, help_text='需要 /，例如: /resource')
    redirect = models.CharField('定向', max_length=255, help_text='访问一级菜单跳转到子节点 URI，例如: /resource/host')
    icon = models.CharField('菜单图标', max_length=255, default='tree')
    order = models.IntegerField('排序', default=10, help_text='菜单排序，小的排前面')

    class Meta:
        verbose_name = '一级菜单'
        verbose_name_plural = '一级菜单'
        ordering = ['order']

    def __str__(self):
        return self.title


# 二级菜单
class L2Menu(models.Model):
    parent = models.ForeignKey(L1Menu, on_delete=models.PROTECT, verbose_name='父菜单', related_name='children')
    title = models.CharField('显示名称', max_length=255)
    # name = models.CharField('名称', max_length=255, unique=True)
    name = models.ForeignKey(
        ContentType, verbose_name='模型',
        on_delete=models.PROTECT,
        limit_choices_to={'app_label': 'app'},
        blank=True, null=True,
        help_text='绑定模型'
    )
    path = models.CharField('URI', max_length=255, unique=True, help_text='不需要 /，例如: user')
    component = models.CharField('部件', max_length=255, help_text='相对于 /views 的路径, 例如: /resource/host')
    order = models.IntegerField('排序', default=10, help_text='菜单排序，小的排前面')
    is_model = models.BooleanField('是否对应模型', default=True)

    class Meta:
        verbose_name = '二级菜单'
        verbose_name_plural = '二级菜单'
        ordering = ['order']

    def __str__(self):
        return self.title


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
    name = models.CharField('名称', max_length=200, unique=True)

    class Meta:
        verbose_name = '项目组件'
        verbose_name_plural = '项目组件'

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
    status = models.CharField('状态', max_length=200, default='使用')

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


# Codeaddr
class ProjectCodeaddr(models.Model):
    name = models.CharField('名称', max_length=200)
    type = models.CharField('类别', max_length=200)
    addr = models.CharField('地址', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)


# ---------------------------------------------------------------------------------------
class Task(models.Model):
    name = models.CharField('名称', max_length=200, unique=True)
    script_dir = models.CharField('脚本路径', max_length=200)
    script_name = models.CharField('脚本名', max_length=200, unique=True)
    arg = models.CharField('参数', max_length=200, blank=True)
    type = models.CharField('类别', max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)
