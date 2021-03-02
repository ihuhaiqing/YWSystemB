#### 软件版本

> 安装示例：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python==3.7.0

- python==3.7.0
- django==2.2.11
- mysqlclient==1.4.4
- djangorestframework==3.11.0
- django-oauth-toolkit==1.3.0
- paramiko==2.6.0
- channels==2.4.0
- webssh==1.5.2
- django-guardian==2.1.0



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



#### 应用注册信息

> client_id: 
>
> uJfDugEBMRPFGabdsPUcQ85JMrkO0B0US5nvu7pz
>
> client_secret: JNLRcIDlHH3bBzpdy0evZZ36zNh0ghZWHpqNIeDVKH7arwWsvFHyeF2p37sUDLik7knkrPGzXnKBuTlMjG3jyeSQUNBC0veFyPVzqI4YcVYfJDYvhCAB8xsaDpWx8ZkW



#### 使用 docker-compose 部署

在目录 /data/ywsystem 中创建 docker-compose.yml 文件

```
version: '3.1'
services:
  mysql:
    image: registry.cn-shenzhen.aliyuncs.com/huhaiqing/mysql:5.7.30
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=MySQL5.7
    ports:
      - 3306:3306
    volumes:
      - /data/mysql-data:/var/lib/mysql
      - /data/mysql-conf:/etc/mysql/conf.d
  django:
    image: registry.cn-shenzhen.aliyuncs.com/huhaiqing/ywsystem:1.2.5
    entrypoint: ["docker-entrypoint.sh"]
    volumes:
      - /data/YWSystemB:/YWSystemB
      - /data/YWSystemF:/usr/share/nginx/html
    ports:
      - "80:80"
    depends_on:
      - mysql
```

在目录 /data/YWSystemB 中拉取后端代码

```
mkdir /data/YWSystemB
cd /data/YWSystemB
git init
git remote add origin https://github.com/huhaiqng/YWSystemB.git
git pull https://github.com/huhaiqng/YWSystemB.git master
```

将前端文件上传到目录 /data/YWSystemF 中

```
mkdir /data/YWSystemF
```

启动

```
cd /data/ywsystem
docker-compose up -d
```

创建数据库

```
docker exec -i ywsystem_mysql_1 sh -c 'exec mysql -uroot -p"MySQL5.7" -e"create database YWSystem default character set utf8mb4"'
```

执行数据迁移

```
docker exec ywsystem_django_1 sh -c 'python3.7 manage.py makemigrations'
docker exec ywsystem_django_1 sh -c 'python3.7 manage.py migrate'
```

可以使用的组成系统的模块

```
activemq jar nginx python tomcat apache kafka oracle rabbitmq war dotnet mongodb php redis zookeeper mysql ProjectList sqlserver iis codeaddr other
```

提取 django 静态文件

```
docker exec ywsystem_django_1 sh -c 'python3.7 manage.py collectstatic'
```

创建超级管理员

```
docker exec -it ywsystem_django_1 sh -c 'python3.7 manage.py createsuperuser'
```

登录后台 http://ip/admin ，创建应用认证

>Client id: uJfDugEBMRPFGabdsPUcQ85JMrkO0B0US5nvu7pz
>
>Client secret: JNLRcIDlHH3bBzpdy0evZZ36zNh0ghZWHpqNIeDVKH7arwWsvFHyeF2p37sUDLik7knkrPGzXnKBuTlMjG3jyeSQUNBC0veFyPVzqI4YcVYfJDYvhCAB8xsaDpWx8ZkW
>
>Client type: Confidential
>
>Authorization grant type: Resource owner password-based

登录 http://ip 验证

#### 初始化父菜单

```
INSERT INTO `app_l1menu`(`id`, `name`, `path`, `redirect`, `title`, `icon`, `order`) VALUES (3, 'Resource', '/resource', '/resource/host', '资源管理', 'tree', 10);
INSERT INTO `app_l1menu`(`id`, `name`, `path`, `redirect`, `title`, `icon`, `order`) VALUES (4, 'Project', '/project', '/project/index', '项目管理', 'component', 20);
INSERT INTO `app_l1menu`(`id`, `name`, `path`, `redirect`, `title`, `icon`, `order`) VALUES (5, 'AuthPermission', '/auth_permission', '/auth_permission/user', '认证权限', 'password', 50);
INSERT INTO `app_l1menu`(`id`, `name`, `path`, `redirect`, `title`, `icon`, `order`) VALUES (6, 'TaskCenter', '/task-cener', '/task-center/task', '任务中心', 'list', 30);
INSERT INTO `app_l1menu`(`id`, `name`, `path`, `redirect`, `title`, `icon`, `order`) VALUES (7, 'Account', '/account', '/account/software', '账号管理', 'peoples', 40);

```

#### 初始化子菜单

```
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (4, 'Host', 'host', '/resource/host', '主机', 3, 1);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (5, 'MySQLInstance', 'mysqlInstance', '/resource/instance/MySQLInstance', 'MySQL 实例', 3, 3);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (6, 'RedisInstance', 'redisInstance', '/resource/instance/RedisInstance', 'Redis 实例', 3, 5);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (7, 'ZookeeperInstance', 'zookeeperInstance', '/resource/instance/ZookeeperInstance', 'Zookeeper 实例', 3, 11);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (8, 'activemqInstance', 'activemqInstance', '/resource/instance/ActivemqInstance', 'Activemq 实例', 3, 7);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (9, 'RabbitmqInstance', 'rabbitmqInstance', '/resource/instance/RabbitmqInstance', 'Rabbitmq 实例', 3, 9);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (10, 'Project', 'index', '/resource/project', '项目管理', 4, 41);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (11, 'User', 'user', '/auth-permission/user', '系统用户', 5, 51);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (12, 'Group', 'group', '/auth-permission/group', '用户组', 5, 52);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (13, 'Task', 'task', '/task-center/task', '任务', 6, 61);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (14, 'ExecTask', 'ExecTask', '/task-center/ExecTask', '执行任务', 6, 62);
INSERT INTO `app_l2menu`(`id`, `name`, `path`, `component`, `title`, `parent_id`, `order`) VALUES (15, 'Software', 'software', '/account/index', '账号管理', 7, 71);
```

#### Nginx 配置

```
server {
    listen      80;
    server_name localhost; 
    charset     utf-8;

    location / {
        root /usr/share/nginx/html;
    }

    location /djstatic {
        root /YWSystemB;
    }

    location /api {
        proxy_pass    http://127.0.0.1:8000;
        keepalive_timeout  600;
        proxy_read_timeout 600;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location /admin {
        proxy_pass    http://127.0.0.1:8000;
        keepalive_timeout  600;
        proxy_read_timeout 600;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

