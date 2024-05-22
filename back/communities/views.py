from django.shortcuts import render
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    # GET 요청을 받으면 게시글 목록 반환
    if request.method == 'GET':
        articles = Article.objects.annotate(comment_count=Count('comments')).order_by('-created_at')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # POST 요청을 받으면 게시글 작성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):

    article = Article.objects.get(pk=article_pk)    # 단일 게시글 조회
    # GET 요청을 받으면 단일 게시글의 정보 반환
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # DELETE 요청을 받으면 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # PUT 요청을 받으면 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 댓글 작성 함수
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)    # 단일 게시글 조회
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 댓글 삭제 함수
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)    # 삭제할 댓글 조회
    if request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)