from rest_framework import serializers
from app.models import L1Menu
from .l2_menu import L2MenuSerializer


# 一级菜单
class L1MenuSerializer(serializers.ModelSerializer):
    children = L2MenuSerializer(read_only=True, many=True)

    class Meta:
        model = L1Menu
        fields = '__all__'
