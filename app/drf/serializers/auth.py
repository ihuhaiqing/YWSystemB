from rest_framework import serializers
from django.contrib.auth.models import User,Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GetUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'


class GetGroupSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'
