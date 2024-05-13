from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    userid = models.CharField(max_length=50, unique=True)  # id
    name = models.CharField(max_length=50)  # 이름(or 별명)
    email = models.EmailField(max_length=250, blank=True, null=True) # email
    date_of_birth = models.DateField(verbose_name = '생년월일')
    profile_img = models.ImageField(upload_to='image/', default='image/userdefault.png')
    budget = models.IntegerField(blank=True, null=True)  # 보유 자산
    salary = models.IntegerField(blank=True, null=True) # 월 수익
    address = models.TextField(blank=True, null=True) # 거주지 주소
    deposit_able = models.IntegerField(blank=True, null=True) # 예금 예치 가능액
    saving_able = models.IntegerField(blank=True, null=True) # 적금 예치 가능액
    credit_score = models.IntegerField(blank=True, null=True) # 신용점수
    deposit_period = models.IntegerField(blank=True, null=True) # 예금 예치 기간
    saving_period = models.IntegerField(blank=True, null=True) # 적금 예치 기간
    is_superuser = models.BooleanField(default=False) # 관리자여부
    
    USERNAME_FIELD = 'userid'
