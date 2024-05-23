Django Models

# back > accounts > models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

class User(AbstractUser):
    nickname = models.CharField(max_length=50)  # 이름(or 별명)
    email = models.EmailField(max_length=250, blank=True, null=True) # email
    date_of_birth = models.DateField(verbose_name = '생년월일', blank=True, null=True)
    profile_img = models.ImageField(upload_to='image/', default='image/userdefault.png')
    budget = models.IntegerField(blank=True, null=True)  # 보유 자산
    salary = models.IntegerField(blank=True, null=True) # 월 수익
    address = models.TextField(blank=True, null=True) # 거주지 주소
    deposit_able = models.IntegerField(blank=True, null=True) # 예금 예치 가능액
    saving_able = models.IntegerField(blank=True, null=True) # 적금 예치 가능액
    credit_score = models.IntegerField(blank=True, null=True) # 신용점수
    deposit_period = models.IntegerField(blank=True, null=True) # 예금 예치 기간
    saving_period = models.IntegerField(blank=True, null=True) # 적금 예치 기간
    deposit_recommend = models.JSONField(blank=True, null=True) # 예금 추천 상품
    saving_recommend = models.JSONField(blank=True, null=True) # 예금 추천 상품
    is_superuser = models.BooleanField(default=False) # 관리자여부
    
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        username = data.get('username')
        nickname = data.get('nickname')
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        date_of_birth = data.get('date_of_birth')
        email = data.get("email")
        profile_img = data.get("profile_img")
        address = data.get('address')
        credit_score = data.get('credit_score')
        age = data.get("age")
        budget = data.get("budget")
        salary = data.get("salary")
        deposit_able = data.get("deposit_able")
        saving_able = data.get("saving_able")
        deposit_period = data.get("deposit_period")
        saving_period = data.get("saving_period")
        
        
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, 'first_name', first_name)
        if last_name:
            user_field(user, 'last_name', last_name)
        if nickname:
            user_field(user, 'nickname', nickname)
        if date_of_birth:
            user.date_of_birth = date_of_birth
            # user_field(user, 'date_of_birth', date_of_birth)
        if credit_score:
            user.credit_score = credit_score
        if address:
            user.address = address
        if profile_img:
            user.profile_img = profile_img
        if age:
            user.age = age
        if budget:
            user.budget = budget
        if salary:
            user.salary = salary
        if deposit_able:
            user.deposit_able = deposit_able
        if saving_able:
            user.saving_able = saving_able
        if deposit_period:
            user.deposit_period = deposit_period
        if saving_period:
            user.saving_period = saving_period
            
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()

        return user


# back > communities > models.py

from django.db import models
from django.conf import settings

## 게시글 모델
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

## 댓글 모델 - 게시글 모델와 1:N 관계
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

# back > exchanges > models.py

from django.db import models

class Current(models.Model):
    cur_unit = models.CharField(max_length=10, unique=True) # 통화 단위
    cur_nm = models.CharField(max_length=50) # 통화 이름
    
class ExchangeRate(models.Model):
    current = models.ForeignKey(Current, on_delete=models.CASCADE, related_name='exchange_rates') # 통화 외래키
    date = models.DateField()   # 기준 날짜
    ttb = models.DecimalField(max_digits=10, decimal_places=2)  # 매입 환율
    tts = models.DecimalField(max_digits=10, decimal_places=2)  # 매도 환율
    deal_bas_r = models.DecimalField(max_digits=10, decimal_places=2)  # 매매 기준율
    bkpr = models.DecimalField(max_digits=10, decimal_places=2)  # 기준 가격
    
    class Meta:
        unique_together = ('current', 'date')

    def __str__(self):
        return f"{self.current.cur_unit} - {self.date}"

# back > finances > models.py

from django.db import models
from django.conf import settings

## 은행 모델
class Bank(models.Model):
    fin_co_no = models.CharField(max_length=100) # 금융회사코드
    kor_co_nm = models.CharField(max_length = 100) # 금융회사명
    dcls_month = models.CharField(max_length = 20) # 공시제출월
    dcls_chrg_man = models.TextField(null=True, blank=True) # 공시 담당자
    homp_url = models.URLField(null=True, blank=True) # 홈페이지 주소
    cal_tel = models.CharField(max_length=20) # 콜센터 전화번호


## 예금상품 모델
class DepositProduct(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    fin_prdt_cd = models.CharField(max_length=100) # 금융상품코드
    fin_prdt_nm = models.CharField(max_length=100) # 금융상품명
    fin_co_no = models.CharField(max_length=100) # 금융회사코드
    kor_co_nm = models.CharField(max_length = 100) # 금융회사명
    dcls_month = models.CharField(max_length = 20) # 공시제출월
    dcls_strt_day = models.CharField(max_length=20) # 공시시작일
    dcls_end_day = models.CharField(max_length=20, null=True, blank=True) # 공시종료일
    fin_co_subm_day = models.CharField(max_length=30) # 금융회사제출일
    join_deny = models.CharField(max_length=5) # 가입 제한
    join_member = models.TextField(blank=True, null=True) # 가입 대상
    join_way = models.TextField(blank=True, null=True) # 가입 방법
    etc_note = models.TextField(blank=True, null=True) # 기타 정보
    max_limit = models.IntegerField(blank=True, null=True) # 최대 한도
    mtrt_int = models.TextField(blank=True, null=True) # 만기 후 약정 이율
    spcl_cnd = models.TextField(blank=True, null=True) # 우대 조건
    join_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'join_deposit') # 가입 유저
    compare_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'compare_deposit') # 관심 유저

## 적금 상품 모델
class SavingProduct(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    fin_prdt_cd = models.CharField(max_length=100) # 금융상품코드
    fin_prdt_nm = models.CharField(max_length=100) # 금융상품명
    fin_co_no = models.CharField(max_length=100) # 금융회사코드
    kor_co_nm = models.CharField(max_length = 100) # 금융회사명
    dcls_month = models.CharField(max_length = 20) # 공시제출월
    dcls_strt_day = models.CharField(max_length=20) # 공시시작일
    dcls_end_day = models.CharField(max_length=20, null=True, blank=True) # 공시종료일
    fin_co_subm_day = models.CharField(max_length=30) # 금융회사제출일
    join_deny = models.CharField(max_length=5) # 가입 제한
    join_member = models.TextField(blank=True, null=True) # 가입 대상
    join_way = models.TextField(blank=True, null=True) # 가입 방법
    etc_note = models.TextField(blank=True, null=True) # 기타 정보
    max_limit = models.IntegerField(blank=True, null=True) # 최대 한도
    mtrt_int = models.TextField(blank=True, null=True) # 만기 후 약정 이율
    spcl_cnd = models.TextField(blank=True, null=True) # 우대 조건
    join_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'join_saving') # 가입 유저
    compare_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'compare_saving') # 관심 유저

## 예금 상품 옵션
class DepositOption(models.Model):
    deposit_product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    intr_rate = models.FloatField(blank=True, null=True) # 금리
    intr_rate2 = models.FloatField(blank=True, null=True) # 최고 우대 금리
    intr_rate_type = models.CharField(max_length=20) # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=20) # 저축 금리 유형명
    save_trm = models.CharField(max_length=20) # 저축 기간

## 적금 상품 옵션
class SavingOption(models.Model):
    saving_product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    intr_rate = models.FloatField(blank=True, null=True) # 금리
    intr_rate2 = models.FloatField(blank=True, null=True) # 최고 우대 금리
    intr_rate_type = models.CharField(max_length=20) # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=20) # 저축 금리 유형명
    save_trm = models.CharField(max_length=20) # 저축 기간
    rsrv_type = models.CharField(max_length=100) # 적립 유형
    rsrv_type_nm = models.CharField(max_length=100) # 적립 유형명

