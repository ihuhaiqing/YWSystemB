from app.models import *
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


# 二级菜单
class L2MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = '__all__'


# 一级菜单
class L1MenuSerializer(serializers.ModelSerializer):
    children = L2MenuSerializer(read_only=True, many=True)

    class Meta:
        model = L1Menu
        fields = '__all__'
