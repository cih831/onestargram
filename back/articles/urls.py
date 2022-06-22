from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/like/', views.like_article),
    path('<int:article_pk>/comments/', views.create_comment),
    path('comments/<int:comment_pk>/', views.comment_update_or_delete),
    path('comments/<int:comment_pk>/like/', views.like_comment),
    path('comments/<int:comment_pk>/replies/', views.create_reply),
    path('comments/<int:comment_pk>/replies/<int:reply_pk>/', views.reply_update_or_delete),
    path('replies/<int:reply_pk>/like/', views.like_reply),
]
