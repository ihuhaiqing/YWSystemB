#### 上传代码

将 python 代码上传到服务器目录 /data/ywsystem/YWSystemB

将静态代码上传到服务器目录 /data/ywsystem/YWSystemF



#### 准备数据库

> 需要修改 YWSystemB/.prod 中数据库连接相关的配置

创建数据库 ywsystem



#### 启动

```
cd /data/ywsystem/YWSystemB
docker-compose up -d
```



#### 初始化数据

初始化数据库

```
docker exec ywsystem_django_1 sh -c 'python manage.py makemigrations'
docker exec ywsystem_django_1 sh -c 'python manage.py migrate'
```

创建认证应用

> SQL 脚本 data/oauth2_provider_application.sql

创建一级菜单

> SQL 脚本 data/app_l1menu.sql

创建二级菜单

> SQL 脚本 data/app_l2menu.sql

创建组成项目的模块

> SQL 脚本 data/app_software.sql

创建超级管理员

```
docker exec -it ywsystem_django_1 sh -c 'python3.7 manage.py createsuperuser'
```



#### django 源码修改

django.contrib.auth.models.Permission

> content_type 添加 related_name='permission'  属性
>
> 文件路径: /usr/local/lib/python3.7/site-packages/django/contrib/auth/models.py

```
content_type = models.ForeignKey(
    ContentType,
    models.CASCADE,
    verbose_name=_('content type'),
    related_name='permission'
)
```



#### 验证

登录 http://ip:90 验证

