from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Article, Comment, Reply
from .comment import CommentSerializer


User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_img',)

    class CommentsSerializer(serializers.ModelSerializer):

        class RepliesSerializer(serializers.ModelSerializer):
            class Meta:
                model = Reply
                fields = ('__all__')

        replies = RepliesSerializer(many=True, read_only=True)

        class Meta:
            model = Comment
            fields = ('__all__')

    user = UserSerializer(read_only=True)
    comments = CommentsSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('__all__')



class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_img')

    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'content', 'comment_count', 'like_count')