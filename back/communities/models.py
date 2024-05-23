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
    title = models.CharField(max_length=50) # 게시글(글) 제목
    content = models.TextField()    # 게시글 내용
    # 카테고리의 선택지
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='free')    # 게시글 카테고리
    created_at = models.DateTimeField(auto_now_add=True)    # 게시글 작성 일자, 생성 일자
    updated_at = models.DateTimeField(auto_now=True)    # 게시글 수정 일자
    
    def __str__(self):
        return self.title

# 댓글 모델 - 게시글 모델와 1:N 관계
class Comment(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # 댓글 작성 유저
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE) # 댓글 외래키
    content = models.CharField(max_length=200)  # 댓글 내용
    # 자기 참조 외래키
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies') # 대댓글(reply)의 부모 댓글
    created_at = models.DateTimeField(auto_now_add=True)    # 댓글 작성 시간
    updated_at = models.DateTimeField(auto_now=True)    # 댓글 수정 시간
    
    
    def __str__(self):
        return f'{self.article} 게시글의 댓글 - {self.id}'