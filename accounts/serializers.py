from rest_framework import serializers
from django.contrib.auth import get_user_model
from .task import send_test_email

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)               
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_test_email.delay(user.email)
        return user