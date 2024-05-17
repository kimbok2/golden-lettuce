from django.db import models
from django.conf import settings

# Create your models here.
# 은행 모델
class Bank(models.Model):
    fin_co_no = models.CharField(max_length=100) # 금융회사코드
    kor_co_nm = models.CharField(max_length = 100) # 금융회사명
    dcls_month = models.CharField(max_length = 20) # 공시제출월
    dcls_chrg_man = models.TextField(null=True, blank=True) # 공시 담당자
    homp_url = models.URLField(null=True, blank=True) # 홈페이지 주소
    cal_tel = models.CharField(max_length=20) # 콜센터 전화번호


# 예금상품 모델
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

# 적금 상품 모델
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

# 예금 상품 옵션
class DepositOption(models.Model):
    deposit_product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    intr_rate = models.FloatField(blank=True, null=True) # 금리
    intr_rate2 = models.FloatField(blank=True, null=True) # 최고 우대 금리
    intr_rate_type = models.CharField(max_length=20) # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=20) # 저축 금리 유형명
    save_trm = models.CharField(max_length=20) # 저축 기간

# 적금 상품 옵션
class SavingOption(models.Model):
    saving_product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    intr_rate = models.FloatField(blank=True, null=True) # 금리
    intr_rate2 = models.FloatField(blank=True, null=True) # 최고 우대 금리
    intr_rate_type = models.CharField(max_length=20) # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=20) # 저축 금리 유형명
    save_trm = models.CharField(max_length=20) # 저축 기간
    rsrv_type = models.CharField(max_length=100) # 적립 유형
    rsrv_type_nm = models.CharField(max_length=100) # 적립 유형명
