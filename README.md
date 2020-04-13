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

```
content_type = models.ForeignKey(
    ContentType,
    models.CASCADE,
    verbose_name=_('content type'),
    related_name='permission'
)
```

