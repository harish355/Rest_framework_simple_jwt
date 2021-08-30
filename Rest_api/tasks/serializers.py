from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import jwt


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        user = authenticate(
            username=attrs['username'], password=attrs['password'])
        if user is not None:
            if user.is_active:
                data = super().validate(attrs)
                refresh = self.get_token(self.user)
                user_data = {}
                user_data['username'] = self.user.username
                user_data['password'] = self.user.password
                user_data['email'] = self.user.email
                user_data['email'] = self.user.email
                user_data['access_token'] = jwt.encode(
                    {'username': self.user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")
                user_data['refresh_token'] = str(refresh)
                return user_data
            else:
                raise serializers.ValidationError('Account is Blocked')
        else:
            raise serializers.ValidationError(
                'Incorrect userid/email and password combination!')
