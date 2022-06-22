from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment, Reply
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentSerializer
from .serializers.reply import ReplySerializer


@api_view(['GET', 'POST'])
def article_list_or_create(request):
    def article_list():
        articles = Article.objects.annotate(
            comment_count= Count('comments', distinct=True),
            like_count = Count('like_users', distinct=True)
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return create_article()

    
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update_article():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_article():
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        if request.user == article.user:
            return update_article()
    elif request.method == 'DELETE':
        if request.user == article.user:
            return delete_article()
    

@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()


@api_view(['POST'])
def like_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        comment.like_users.add(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


@api_view(['POST'])
def create_reply(request, comment_pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(comment=comment, user=user)
        replies = comment.replies.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def reply_update_or_delete(request, comment_pk, reply_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)

    def update_reply():
        if request.user == reply.user:
            serializer = ReplySerializer(instance=reply, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                replies = comment.replies.all()
                serializer = ReplySerializer(replies, many=True)
                return Response(serializer.data)

    def delete_reply():
        if request.user == reply.user:
            reply.delete()
            replies = comment.replies.all()
            serializer = ReplySerializer(replies, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_reply()
    elif request.method == 'DELETE':
        return delete_reply()


@api_view(['POST'])
def like_reply(request, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk)
    user = request.user
    if reply.like_users.filter(pk=user.pk).exists():
        reply.like_users.remove(user)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    else:
        reply.like_users.add(user)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)