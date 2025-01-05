from rest_framework import serializers
from .models import User, Chat

class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
            # Extract password from validated data
            password = validated_data.pop('password')
            
            # Create the user object
            user = super().create(validated_data)
            
            # Set the password using the set_password method to ensure it's hashed
            user.set_password(password)
            
            # Save the user instance
            user.save()
            return user
    class Meta:
        model = User
        fields = ['username', 'password', 'tokens']
        extra_kwargs = {"password": {"write_only": True}}

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)


class ChatSerializer(serializers.ModelSerializer):
     class Meta:
          model = Chat
          fields = ['user', 'message', 'response', 'timestamp']


