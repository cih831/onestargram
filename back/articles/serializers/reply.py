from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Reply

User = get_user_model()

class ReplySerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_img')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Reply
        fields = ('__all__')
        read_only_fields = ('comment', )