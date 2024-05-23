import os
import requests
import logging
import time
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from communities.models import Article, Comment
from exchanges.models import Current, ExchangeRate
from finances.models import Bank, DepositProduct, SavingProduct, DepositOption, SavingOption

# ERD.md 파일 경로 설정
ERD_FILE_PATH = os.path.join(settings.BASE_DIR, 'docs', 'ERD.md')

API_KEY_OPENAI = settings.API_KEY_OPENAI


# ERD.md 파일 읽기
def read_erd_file():
    with open(ERD_FILE_PATH, 'r', encoding='utf-8') as file:
        return file.read()

# Create your views here.

User = get_user_model()

logger = logging.getLogger(__name__)


def get_user_data():
    users = User.objects.all().values('nickname', 'email', 'budget', 'salary', 'address', 'credit_score')
    return list(users)

def get_article_data():
    articles = Article.objects.all().values('title', 'content', 'category')
    return list(articles)

def get_comment_data():
    comments = Comment.objects.all().values('content', 'article_id')
    return list(comments)

def get_exchange_rate_data():
    currents = Current.objects.all().values('cur_unit', 'cur_nm')
    current_data = list(currents)
    
    exchange_rates = ExchangeRate.objects.all().values('current_id', 'date', 'ttb', 'tts', 'deal_bas_r')
    exchange_rate_data = list(exchange_rates)
    
    return {'currents': current_data, 'exchange_rates': exchange_rate_data}

def get_bank_data():
    banks = Bank.objects.all().values('kor_co_nm', 'cal_tel')
    bank_data = list(banks)
    
    deposit_products = DepositProduct.objects.all().values('fin_prdt_nm', 'kor_co_nm')
    deposit_product_data = list(deposit_products)
    
    saving_products = SavingProduct.objects.all().values('fin_prdt_nm', 'kor_co_nm')
    saving_product_data = list(saving_products)
    
    deposit_options = DepositOption.objects.all().values('intr_rate', 'intr_rate2', 'save_trm')
    deposit_option_data = list(deposit_options)
    
    saving_options = SavingOption.objects.all().values('intr_rate', 'intr_rate2', 'save_trm')
    saving_option_data = list(saving_options)
    
    return {
        'banks': bank_data,
        'deposit_products': deposit_product_data,
        'saving_products': saving_product_data,
        'deposit_options': deposit_option_data,
        'saving_options': saving_option_data,
    }

def get_combined_data(message):
    if any(keyword in message.lower() for keyword in ['user', '유저', '사용자']):
        return get_user_data()
    elif any(keyword in message.lower() for keyword in ['article', '글', '게시글']):
        return get_article_data()
    elif any(keyword in message.lower() for keyword in ['comment', '댓글']):
        return get_comment_data()
    elif any(keyword in message.lower() for keyword in ['exchange rate', '환율']):
        return get_exchange_rate_data()
    elif any(keyword in message.lower() for keyword in ['bank', '은행']):
        return get_bank_data()
    else:
        return {'message': '다른 질문을 해주세요.'}

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        
        if not message:
            return JsonResponse({'error': 'No message provided'}, status=400)
        
        # 메시지에 따라 필요한 데이터를 선택적으로 가져오기
        data = get_combined_data(message)
        
        # 모델 데이터를 GPT-4 API에 전달할 형식으로 변환
        combined_message = f"{message}\n\n여기에 요청하신 정보가 있습니다.:\n{data}"
        
        try:
            response = send_request_to_openai(combined_message)
            
            print('#######', response, '#######')
            
            return JsonResponse({'response': response['choices'][0]['message']['content']})
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Request to OpenAI API failed: {e}")
            return JsonResponse({'error': 'Failed to connect to the OpenAI API'}, status=500)
        except KeyError:
            logger.error("Unexpected response format from OpenAI API")
            return JsonResponse({'error': 'Unexpected response format from OpenAI API'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def send_request_to_openai(combined_message, retries=3, delay=1):
    """
    OpenAI API에 요청을 보내는 함수입니다. 429 오류 발생 시 재시도 로직을 포함합니다.
    """
    
    # ERD 파일 읽기
    erd_content = read_erd_file()
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {API_KEY_OPENAI}',
                'Content-Type': 'application/json',
            },
            json={
                'model': 'gpt-4o',
                    # {'role': 'system', 'content': f'유저 질문에 대한 정보는 장고 모델의 내용을 참고해서 데이터를 DB에서 직접 찾아서 답변해줘. / {erd_content}'},
                'messages': [
                    {'role': "system", "content": "우리 프로젝트 이름은 금상추야. 너의 이름도 금상추라고 알고 있어줘."},
                    {'role': "system", "content": "너는 금상추 프로젝트 서비스에 도움이 되는 유능한 조수야."},
                    {'role': 'system', 'content': f'유저 질문에 대한 정보는 장고 모델의 내용을 참고해서 데이터를 DB에서 직접 찾아서 답변해줘. / {erd_content}'},
                    {'role': 'system', "content": '예금 상품 정보는 deposit_products야. 유저에게 알려줄 정보는 은행명 (kor_co_nm), 상품 이름(fin_prdt_nm)이야.'},
                    {'role': 'system', "content": '적금 상품 정보는 saving_products야. 유저에게 알려줄 정보는 은행명 (kor_co_nm), 상품 이름(fin_prdt_nm)이야.'},
                    {'role': 'system', "content": "유저에게 장고 모델의 필드 이름을 직접적으로 말하지 않았으면 해. 필요하다면 필드 이름을 적절하게 한글로 번역해서 알려줘."},
                    {'role': 'user', 'content': combined_message},
                    {'role': 'system', 'content': '유저에게 절대로 장고 프로젝트 동작에 대한 얘기를 하지 마.'},
                    {'role': 'system', 'content': '유저가 명확하게 답변을 요청하지 않았으면, 명확한 질문을 다시 요청해줘'},
                ],
            }
        )
        response.raise_for_status()
        return response.json()
    except  requests.exceptions.RequestException as e:
        print(e)
        raise requests.exceptions.RequestException(f"Failed to connect to OpenAI API")