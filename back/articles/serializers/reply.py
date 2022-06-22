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

    class Meta:
        model = Reply
        fields = ('pk', 'user', 'content', 'comment', 'created_at')
        read_only_fields = ('comment', )