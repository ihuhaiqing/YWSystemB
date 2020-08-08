# YWSystemB

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

##### 1、django.contrib.auth.models.Permission

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