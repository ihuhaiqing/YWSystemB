from rest_framework import serializers
from app.models import L2Menu


# 二级菜单
class L2MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = '__all__'
