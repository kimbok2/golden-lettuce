from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

User = get_user_model()

# Article 혹은 ArticleList를 호출할 때 user 객체의 정보를 수정하는 Serializer
class ArticleUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'username',)
    
    profile_img = serializers.ImageField(use_url=True)
# 게시글을 표시해줄 Serializer
class ArticleListSerializer(serializers.ModelSerializer):

    user = ArticleUsernameSerializer(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        
# 댓글 Serializer
class CommentSerializer(serializers.ModelSerializer):
    
    user = ArticleUsernameSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', )
        
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []
        
# 게시글 작성할 때 호출할 Serializer
class ArticleSerializer(serializers.ModelSerializer):

    user = ArticleUsernameSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

