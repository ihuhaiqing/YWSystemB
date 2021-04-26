from rest_framework import serializers
from app.models import Software


# 软件
class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'
