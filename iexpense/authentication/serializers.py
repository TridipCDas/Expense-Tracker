from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length = 6, write_only = True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['username','password','email']

    def validate(self, attrs):
        username = attrs.get('username','')
        email = attrs.get('email','')
        password = attrs.get('password','')

        if not username.isalnum():
            raise serializers.ValidationError("The username should only contain alphanumeric characters")

        return attrs