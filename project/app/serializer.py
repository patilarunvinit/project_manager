from .models import login1,data
from rest_framework import serializers

class login1serializer(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    option = serializers.CharField(max_length=50)


    def create(self,validated_data):
        return login1.objects.create(**validated_data)

class dataserializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    task = serializers.CharField(max_length=30)
    asignto = serializers.CharField(max_length=50)
    review = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return data.objects.create(**validated_data)