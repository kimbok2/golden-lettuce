from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
# Create your models here.
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
    saving_recommend = models.JSONField(blank=True, null=True) # 적금 추천 상품
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