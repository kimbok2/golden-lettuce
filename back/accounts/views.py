from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import *
from .serializers import *

# Create your views here.
# 유저 프로필(GET O, POST? PUT? DELETE?)
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    print(request.user.username, username)
    # userid가 같은 경우에만
    if request.user.username == username:
        user = get_object_or_404(get_user_model(), username=username)
        if request.method == 'GET':
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(instance=user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

# 유저 정보 조회, 수정, 삭제(생성은 가입 과정에서 생성)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def userinfo(request, username):
    if request.user.username == username:
        user = get_object_or_404(get_user_model(), username=username)
        # 회원정보 조회(프로필이랑 겹침)
        if request.method == 'GET':
            serializer = UserInfoSerializer(user)
            return Response(serializer.data)
        # 회원정보 수정
        elif request.method == 'PUT':
            serializer = UserInfoSerializer(instance = user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        # 회원정보 삭제(되는지 확인)
        elif request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 회원삭제
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def UserDelete(request):
#     if request.method == 'POST':
#         user = request.user
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def test(request):
    print(30)
    return Response(status=status.HTTP_200_OK)

# 최우수 팀은 프로필 정보 수정도 구현

def signup(request):
    return render(request, 'accounts/signup.html')
    
    