from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer
from django.http import JsonResponse, HttpResponse
from django.http import QueryDict

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    

@api_view(['PUT', 'POST'])
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        rd = QueryDict('', mutable=True)
        print(request)
        rd.update(request.data)
        serializer = ProfileSerializer(user, data=rd)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def follow(request, username):
    if request.user.is_authenticated:
        person = get_object_or_404(User, username=username)
        user = request.user
        if person != user:
            if person.followers.filter(username=user.username).exists():
                person.followers.remove(user)
                follow = False
            else:
                person.followers.add(user)
                follow = True
            
            follow_data = {
                'follow':follow,
                'followers_count':person.followers.count(),
                'followings_count':person.followings.count(),
            }
            serializer = ProfileSerializer(person)
        return JsonResponse(serializer.data)
    return HttpResponse(status=401)


@api_view(['POST'])
def edit_profile_img(request, username):
    user = User.objects.get(username=username)
    user.profile_img = request.data['profile_img']
    user.save()

    data = {
        'user': 'changed'
    }
    
    return Response(data, status=status.HTTP_200_OK)