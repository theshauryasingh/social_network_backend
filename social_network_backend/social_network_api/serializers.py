from rest_framework import serializers
from .models import CustomUser, Friendrequest


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}} #to not return password

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendrequest
        fields = ['id', 'fromuser', 'touser', 'created_at', 'status']
        read_only_fields = ['fromuser']