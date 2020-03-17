from app.models import Host,Account
from rest_framework import serializers


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

class AccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

