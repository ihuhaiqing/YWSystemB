from rest_framework import serializers
from django.contrib.auth.models import User,Group,Permission,ContentType


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
      model = ContentType
      fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer(many=False)
    class Meta:
      model = Permission
      fields = '__all__'


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
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'

