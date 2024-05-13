from rest_framework import serializers
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의
    # 사용자 아이디 필드
    userid = serializers.CharField(
        # required=False,     # 필수 입력 항목이 아님
        allow_blank=True,   # 빈 문자열 허용
        max_length=50      # 최대 길이는 50자
    )
    # 사용자 이름 필드
    name = serializers.CharField(max_length=50)  # 최대 길이는 50자
    # 사용자 생년월일 필드
    date_of_birth = serializers.DateField(required=True)  # 필수 입력 항목

    # 입력된 데이터를 정제하여 반환하는 메서드
    def get_cleaned_data(self):
        return {
            'userid': self.validated_data.get('username', ''),  # 사용자 아이디
            'password1': self.validated_data.get('password1', ''),  # 비밀번호
            'password2': self.validated_data.get('password2', ''),  # 비밀번호 확인
            'name': self.validated_data.get('name', ''),  # 사용자 이름
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
    
class ProfileSerializer(serializers):
    class Meta:
        model = User
        fields = ('userid', 'name', 'date_of_birth', 'address', 
                  'budget', 'salary', 'deposit_able', 'saving_able', 
                  'deposit_period', 'saving_period',)
        read_only_fields = ('id','userid', 'name')