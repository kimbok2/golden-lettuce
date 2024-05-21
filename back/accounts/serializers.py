from rest_framework import serializers
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from finances.serializers import DepositDetailSerializer, SavingDetailSerializer

class CustomRegisterSerializer(RegisterSerializer):
    # 필요한 필드들을 추가
    # 별명 필드
    nickname = serializers.CharField(
        allow_blank=True,   # 빈 문자열 허용
        max_length=50      # 최대 길이는 50자
    )
    # 사용자 생년월일 필드
    date_of_birth = serializers.DateField(required=True)  # 필수 입력 항목

    # 입력된 데이터를 정제하여 반환하는 메서드
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),  # 사용자 아이디
            'password1': self.validated_data.get('password1', ''),  # 비밀번호
            'password2': self.validated_data.get('password2', ''),  # 비밀번호 확인
            'nickname': self.validated_data.get('nickname', ''),  # 사용자 이름
            'date_of_birth': self.validated_data.get('date_of_birth', ''),  # 생년월일
        }

    # 사용자를 저장하는 메서드
    def save(self, request):
        adapter = get_adapter()  # 사용자 어댑터 가져오기
        user = adapter.new_user(request)  # 새로운 사용자 생성
        self.cleaned_data = self.get_cleaned_data()  # 입력 데이터 정제
        adapter.save_user(request, user, self)  # 사용자 저장
        self.custom_signup(request, user)  # 사용자 추가 가입 과정 처리
        return user  # 생성된 사용자 반환

# 프로필에 노출될 serializer    
class ProfileSerializer(serializers.ModelSerializer):
    join_deposit = DepositDetailSerializer(many=True)
    join_saving = SavingDetailSerializer(many=True)
    compare_deposit = DepositDetailSerializer(many=True)
    compare_saving = SavingDetailSerializer(many=True)
    profile_img = serializers.ImageField(use_url=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'date_of_birth', 'address', 
                  'budget', 'salary', 'deposit_able', 'saving_able', 
                  'deposit_period', 'saving_period','credit_score',
                  'join_deposit', 'join_saving', 'compare_deposit',
                  'compare_saving', 'profile_img','nickname',
                  'deposit_recommend', 'saving_recommend',)
        read_only_fields = ('id', 'username','nickname',)
    
# 전체 프로필 정보를 수정, 조회, 삭제할 serializer
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'username',)
    
    profile_img = serializers.ImageField(use_url=True)
    # 예금 set
    # 적금 set
    # 대출 set
