from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('profile/<username>/follow/', views.follow),
    path('profile/<username>/edit/', views.edit_profile),
    path('profile/<username>/edit_profile_img/', views.edit_profile_img),
]
