from django.db import models

# Create your models here.
class Current(models.Model):
    cur_unit = models.CharField(max_length=10, unique=True) # 통화 단위
    cur_nm = models.CharField(max_length=50) # 통화 이름
    
# class ExchangeRate(models.Model):
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