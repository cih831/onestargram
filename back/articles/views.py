from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers.article import ArticleListSerializer, articleSerializer
from .serializers.comment import CommentSerializer

@api_view(['GET', 'POST'])
def article_list_or_create(request):
    def article_list():
        articles = Article.objects.annotate(
            like_count = Count('like_users', distinct=True)
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)