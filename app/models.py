from django.db import models
from django.utils import timezone
# Create your models here.


class Host(models.Model):
    name = models.CharField('主机名',max_length=200)
    ip = models.GenericIPAddressField('IP 地址')
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

    def __str__(self):
        return self.ip

    class Meta:
        unique_together = ['ip', 'type', 'name']


class Account(models.Model):
    username = models.CharField('用户名',max_length=200,unique=True)
    password = models.CharField('密码',max_length=200)
    addr = models.CharField('地址',max_length=200,blank=True,null=True)
    use = models.CharField('用途',max_length=255)
    created = models.DateTimeField('创建时间',default=timezone.now)


class Env(models.Model):
    name_cn = models.CharField('中文名',max_length=200,unique=True)
    name_en = models.CharField('英文名',max_length=200,unique=True)
    def __str__(self):
        return self.name_cn


class Software(models.Model):
    type_choices = [('general','general'),('special','special')]
    name = models.CharField('软件名称',max_length=200,unique=True)
    type = models.CharField('类型',max_length=200,default='general',choices=type_choices)
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField('项目名称',max_length=200,unique=True)
    software = models.ManyToManyField(Software)
    def __str__(self):
        return self.name


class JavaPackage(models.Model):
    name = models.CharField('包名',max_length=200,unique=True)
    port = models.IntegerField('端口号')
    project = models.ForeignKey(Project,related_name='java_package',on_delete=models.PROTECT)
    deploy_dir = models.CharField('部署路径',max_length=200)
    download_addr = models.CharField('下载地址',max_length=200)
    func = models.CharField('功能',max_length=200)
    created = models.DateTimeField('创建时间',default=timezone.now)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ProjectWeb(models.Model):
    host = models.ManyToManyField(Host)
    public_ip = models.GenericIPAddressField('公网 IP')
    domain = models.CharField('域名',max_length=200)
    url = models.CharField('访问地址',max_length=200)
    env = models.CharField('环境',max_length=200)
    project = models.ForeignKey(Project,on_delete=models.PROTECT)
    software = models.CharField('软件',max_length=200)
    use = models.CharField('用途',max_length=200)
    created = models.DateTimeField('创建时间',default=timezone.now)


class ProjectTomcat(models.Model):
    package_name = models.CharField('包名',max_length=200)
    env = models.CharField('环境', max_length=200)
    project = models.CharField('项目', max_length=200)
    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('package_name','env','project','host')


class MySQLDB(models.Model):
    name = models.CharField('数据库名',max_length=200,unique=True)
    project = models.ForeignKey(Project,on_delete=models.PROTECT)
    username = models.CharField('用户名',max_length=200)
    pro_password = models.CharField('测试环境密码',max_length=200)
    test_password = models.CharField('生产环境密码',max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)

    def __str__(self):
        return '__all__'


class ProjectMySQLDB(models.Model):
    mysqldb = models.ForeignKey(MySQLDB,related_name='project_mysql',on_delete=models.PROTECT)
    env = models.CharField('环境',max_length=200)
    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    version = models.CharField('版本',max_length=200,default='MySQL 5.7')
    port = models.IntegerField(default=3306)
    role = models.CharField('角色',max_length=200)
    root_password = models.CharField('ROOT 密码',max_length=200)
    data_dir = models.CharField('数据目录',max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ['mysqldb','host']


class Task(models.Model):
    name = models.CharField('名称',max_length=200,unique=True)
    script_dir = models.CharField('脚本路径', max_length=200)
    script_name = models.CharField('脚本名',max_length=200,unique=True)
    arg = models.CharField('参数',max_length=200,blank=True)
    type = models.CharField('类别',max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)


class ProjectGeneralSoftware(models.Model):
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project,on_delete=models.PROTECT)
    software = models.CharField('软件', max_length=200)
    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('env','project','host')


class ProjectMongoDB(models.Model):
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    type = models.CharField('类别',max_length=200)
    shard = models.CharField('分片',max_length=200,blank=True)
    role = models.CharField('角色', max_length=200, blank=True)
    port = models.IntegerField('端口号',blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('env','project','host','port')


class ProjectOracle(models.Model):
    env = models.CharField('环境', max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    type = models.CharField('类别',max_length=200)
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        unique_together = ('env','project','host','type')

