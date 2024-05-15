from django.db import models
from django.conf import settings

# 게시글 모델
class Article(models.Model):
    
    # 카테고리에 사용될 선택지
    CATEGORY_CHOICES = [
        # (선택지의 값, 사용자에게 보일 문자)
        ('notice', '공지사항'),
        ('faq', 'FAQ'),
        ('free', '자유게시판'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # user와 1:N 관계
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 카테고리의 선택지
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='free')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

# 댓글 모델 - 게시글 모델와 1:N 관계
class Comment(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    # 자기 참조 외래키
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')