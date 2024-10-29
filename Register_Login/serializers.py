from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'password', 'profile_name', 'phone_number', 'Position', 'is_staff', 'is_active', 'img', 'date_joined')
