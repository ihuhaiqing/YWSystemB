from django.db import models


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
