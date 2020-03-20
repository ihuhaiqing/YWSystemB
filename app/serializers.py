from app.models import Host,Account,Project,JavaPackage,Software,ProjectWeb
from rest_framework import serializers


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class AccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class JavaPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JavaPackage
        fields = '__all__'


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    java_package = JavaPackageSerializer(read_only=True,many=True)
    software = SoftwareSerializer(read_only=True,many=True)
    class Meta:
        model = Project
        fields = '__all__'


class ProjectWebSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all(),write_only=True,many=True)
    class Meta:
        model = ProjectWeb
        fields = '__all__'


class GetProjectWebSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True,many=True)
    class Meta:
        model = ProjectWeb
        fields = '__all__'

