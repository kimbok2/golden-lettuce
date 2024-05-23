import random
import requests
import json
from collections import OrderedDict
from django.contrib.auth.hashers import make_password

# 랜덤한 이름 생성 함수
first_name_samples = '김이박최정강조윤장임전육안손송'
middle_name_samples = '민서예지도하주윤채현지원혜유육'
last_name_samples = '준윤우원호후서연아은진민빈환범'

def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 10000))

period_choices = [1, 3, 6, 12, 24, 36]

# JSON 파일 생성
file = OrderedDict()

username_list = []
N = 500
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1

save_dir = './back/goldenlettuce_back/accounts/fixtures/user_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')

    for i in range(N):
        # 랜덤한 데이터를 삽입
        file['model'] = 'accounts.user'
        file['pk'] = i + 1
        file['fields'] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            'nickname': username_list[i],
            'email': f'{username_list[i]}@example.com',
            'date_of_birth': f'{random.randint(1950, 2010)}-0{random.randint(1, 9)}-{random.randint(10, 28)}',
            'profile_img': 'image/userdefault.png',
            'budget': random.randrange(0, 1000000000, 1000000),  # 현재 가진 금액
            'salary': random.randrange(0, 15000000, 100000),  # 월급
            'address': '서울특별시 강남구 테헤란로 123',
            'deposit_able': random.randrange(0, 100000000, 1000000),
            'saving_able': random.randrange(0, 10000000, 100000),
            'credit_score': random.randint(200, 1000),
            'deposit_period': random.choice(period_choices),
            'saving_period': random.choice(period_choices),
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
            'password': 'qlalfqjsgh',  
        }


        json.dump(file, f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')