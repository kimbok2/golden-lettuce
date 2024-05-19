from datetime import datetime, timedelta    # 날짜를 불러오는 파이썬의 내자 ㅇ라이브러리
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import requests
import sys
from .models import Current, ExchangeRate
from .serializers import CurrentSerializer, ExchangeRateSerializer

API_KEY_EXCHANGE = settings.API_KEY_EXCHANGE
BASE_URL_EXCHANGE = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
url = BASE_URL_EXCHANGE

# 날짜는 전역으로 선언
today_date = datetime.now().date()
previous_date = today_date - timedelta(days=1)
next_date = today_date + timedelta(days=1)
# DB가 비어있을 때 통화의 정보 (통화 코드, 통화 이름)을 받는 함수
def get_current_info(request):
    
    # 환율 API 기준, 일단위 환율만 알려주므로 어제의 환율 기준으로 검색
    params = {
        'authkey': API_KEY_EXCHANGE,
        'searchdate': previous_date,
        'data': 'AP01'
    }
    
    # 오늘 날짜의 API 요청을 보냄
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data_list = response.json()
        for data in data_list:
            save_data = {
                'cur_unit': data.get('cur_unit', ''),
                'cur_nm': data.get('cur_nm', ''),
            }
            serializer = CurrentSerializer(data=save_data)
            if serializer.is_valid():
                serializer.save()
            else:
                break
        
        return JsonResponse(data_list, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
    
    
# 기준일(오늘)로부터 하루씩 거슬러가며 DB에 날짜 정보를 저장하는 메서드
# 최대로 조회할 날짜를 인자로 받음 (최대 오늘로부터 10년)
def __get_exchange_rate_infos(max_days=3650):
    
    # 환율 API 기준, 일단위 환율만 알려주므로 어제를 기준으로 시작
    target_date = datetime.now().date() - timedelta(days=1) - timedelta(days=1365)
    max_date = datetime.now().date() - timedelta(days=max_days) - timedelta(days=1365)
    
    max_fail_cnt = 100
    fail_cnt = 0
    
    # 현재 날짜가 저장돼있는지 확인
    while target_date != max_date:
        # 확인 ORM
        data_exists = ExchangeRate.objects.filter(date=target_date).exists()
        
        if data_exists or target_date.weekday() in (5, 6):
            # 이미 저장돼있거나 주말 (토/일요일에 요처을 보내면) 그 전날로 이동
            target_date -= timedelta(days=1)
            # 바로 다음 반복으로 넘어가며 저장 여부 재확인
            continue
        else:
            # 저장이 안돼있으면 API 요청을 보낸 뒤 
            # 해당 데이터를 저장하고, 다시 전날 저장여부 확인
            if __get_exchange_rate_api(target_date):
                target_date -= timedelta(days=1)
                continue
            else:
                print(f'failed to fetch data - {target_date}')
                fail_cnt += 1
                target_date -= timedelta(days=1)
                if fail_cnt == max_fail_cnt:
                    return print(f'fetch failed more than {max_fail_cnt} times - last tried date : {target_date}')
            
    print('while문 종료')

            
def __get_exchange_rate_api(get_date):

    # API 요청시 활용할 파라미터
    params = {
        'authkey': API_KEY_EXCHANGE,
        'searchdate': get_date,
        'data': 'AP01',
    }
    
    # 오늘 날짜의 API 요청을 보냄
    response = requests.get(url, params=params)
    print(f'api get request - {response}')
    if response.status_code == 200 and response.json():
        data_list = response.json()
        if data_list[0]['result'] != 1:
            sys.stdout.write(f"api response code= {data_list[0]['result']}\n")
            return False
        for data in data_list:
            # 통화 외래키
            current = Current.objects.get(cur_unit=data['cur_unit'])
            save_data = {
                'current': current.pk,
                'date': get_date,
                'ttb': data.get('ttb', '').replace(',', ''),
                'tts': data.get('tts', '').replace(',', ''),
                'deal_bas_r': data.get('deal_bas_r', '').replace(',', ''),
                'bkpr': data.get('bkpr', '').replace(',', ''),
            }
            serializer = ExchangeRateSerializer(data=save_data)
            if serializer.is_valid():
                serializer.save()
                print(f'data saved - date: {get_date}')
            else:
                print('=====================')
                print(save_data)
                print(serializer.errors)
        return True
    else:
        return False
    
# __get_exchange_rate_infos()