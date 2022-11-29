from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import Profile, Mobile

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = "__all__"

class RegisterMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ["mobile"]

class MobileVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ["mobile", "sms_code"]

class UserResgisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "isAdmin", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_isAdmin(self, obj):
        return obj.is_staff

class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProfileOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ="__all__"