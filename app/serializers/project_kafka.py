from rest_framework import serializers
from app.models import ProjectKafka


# Project Kafka
class ProjectKafkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectKafka
        fields = '__all__'

