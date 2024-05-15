from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

User = get_user_model()

# 게시글을 표시해줄 Serializer
class ArticleListSerializer(serializers.ModelSerializer):
    
    class ArticleUsernameSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)
            
    user = ArticleUsernameSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        
# 게시글 작성할 때 호출할 Serializer
class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

# class CommentSerializer(serializers.CommentSerializer):
    
#     class Meta:
#         model = Comment
#         fields = ()