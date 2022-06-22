from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Comment, Reply
from .reply import ReplySerializer

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_img')

    class RepliesSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Reply
            fields = ('__all__')

    user = UserSerializer(read_only=True)
    replies = RepliesSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('article', )