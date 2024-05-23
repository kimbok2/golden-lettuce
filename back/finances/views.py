from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.db.models import Count
from .models import *
from .serializers import *
from accounts.serializers import ProfileSerializer
import requests
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

API_KEY_FINANCE=settings.API_KEY_FINANCE

@api_view(['GET'])
def save_bank(request):
    url = BASE_URL + f'companySearch.json?auth={API_KEY_FINANCE}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    baseList = response.get('result').get('baseList')
    for bank in baseList:
        fin_co_no = bank.get('fin_co_no', '')
        # 이미 존재하는 데이터인지 확인
        if Bank.objects.filter(fin_co_no=fin_co_no).exists():
            continue
        save_data = {
            'fin_co_no' : fin_co_no,
            'dcls_month' : bank.get('dcls_month', ''),
            'kor_co_nm' : bank.get('kor_co_nm', ''),
            'dcls_chrg_man' : bank.get('dcls_chrg_man', ''),
            'homp_url' : bank.get('homp_url', ''),
            'cal_tel' : bank.get('cal_tel', ''),
        }
        bankserializer = BankSerializer(data=save_data)
        # 저장
        if bankserializer.is_valid(raise_exception=True):
            bankserializer.save()
    return JsonResponse({'message':'save!'})

@api_view(['GET'])
def save_deposit(request):
    url = BASE_URL + f'depositProductsSearch.json?auth={API_KEY_FINANCE}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')
    existeds = []
    for product in baseList:
        # 존재하는 지 검증
        fin_prdt_cd = product.get('fin_prdt_cd')
        deposit = DepositProduct.objects.filter(fin_prdt_cd=fin_prdt_cd).first()
        if deposit:
            existeds.append(deposit.id)
            continue
        bank = Bank.objects.get(fin_co_no=product.get('fin_co_no'))
        
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'fin_prdt_nm' : product.get('fin_prdt_nm', ''),
            'fin_co_no' : product.get('fin_co_no', ''),
            'kor_co_nm' : product.get('kor_co_nm', ''),
            'dcls_month' : product.get('dcls_month', ''),
            'dcls_strt_day' : product.get('dcls_strt_day', ''),
            'dcls_end_day' : product.get('dcls_end_day', ''),
            'fin_co_subm_day' : product.get('fin_co_subm_day', ''),
            'join_deny' : product.get('join_deny', 1),
            'join_member' : product.get('join_member', ''),
            'join_way' : product.get('join_way', ''),
            'etc_note' : product.get('etc_note', ''),
            'max_limit' : product.get('max_limit', ''),
            'mtrt_int' : product.get('mtrt_int', ''),
            'spcl_cnd' : product.get('spcl_cnd', ''),
        }
        productserializer = DepositSerializer(data=save_data)
        # 유효할 경우 저장
        if productserializer.is_valid(raise_exception=True):
            productserializer.save(bank=bank)
            
    
    for option in optionList:
        product = DepositProduct.objects.get(fin_prdt_cd = option.get('fin_prdt_cd'),
                                             fin_co_no = option.get('fin_co_no'),
                                             dcls_month = option.get('dcls_month'))
        if product.id not in existeds:
            save_data= {
                'intr_rate' : option.get('intr_rate', -1),
                'intr_rate2' : option.get('intr_rate2', -1),
                'intr_rate_type' : option.get('intr_rate_type', ''),
                'intr_rate_type_nm' : option.get('intr_rate_type_nm', ''),
                'save_trm' : option.get('save_trm', ''),
            }
            optionserializer = DepositOptionSerializer(data=save_data)
            if optionserializer.is_valid(raise_exception=True):
                optionserializer.save(deposit_product=product)
    
    return JsonResponse({'message':'save!'})
    
@api_view(['GET'])
def save_saving(request):
    url = BASE_URL + f'savingProductsSearch.json?auth={API_KEY_FINANCE}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')
    existeds = []
    for product in baseList:
        # 존재하는 지 검증
        fin_prdt_cd = product.get('fin_prdt_cd')
        saving = SavingProduct.objects.filter(fin_prdt_cd=fin_prdt_cd).first()
        if saving:
            existeds.append(saving.id)
            continue
        bank = Bank.objects.get(fin_co_no=product.get('fin_co_no'))
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'fin_prdt_nm' : product.get('fin_prdt_nm', ''),
            'fin_co_no' : product.get('fin_co_no', ''),
            'kor_co_nm' : product.get('kor_co_nm', ''),
            'dcls_month' : product.get('dcls_month', ''),
            'dcls_strt_day' : product.get('dcls_strt_day', ''),
            'dcls_end_day' : product.get('dcls_end_day', ''),
            'fin_co_subm_day' : product.get('fin_co_subm_day', ''),
            'join_deny' : product.get('join_deny', 1),
            'join_member' : product.get('join_member', ''),
            'join_way' : product.get('join_way', ''),
            'etc_note' : product.get('etc_note', ''),
            'max_limit' : product.get('max_limit', ''),
            'mtrt_int' : product.get('mtrt_int', ''),
            'spcl_cnd' : product.get('spcl_cnd', ''),
        }
        productserializer = SavingSerializer(data=save_data)
        # 유효할 경우 저장
        if productserializer.is_valid(raise_exception=True):
            productserializer.save(bank=bank)
    
    for option in optionList:
        product = SavingProduct.objects.get(fin_prdt_cd = option.get('fin_prdt_cd'),
                                             fin_co_no = option.get('fin_co_no'),
                                             dcls_month = option.get('dcls_month'))
        if product.id not in existeds:
            save_data= {
                'intr_rate' : option.get('intr_rate', -1),
                'intr_rate2' : option.get('intr_rate2', -1),
                'intr_rate_type' : option.get('intr_rate_type', ''),
                'intr_rate_type_nm' : option.get('intr_rate_type_nm', ''),
                'rsrv_type' : option.get('rsrv_type', ''),
                'rsrv_type_nm' : option.get('rsrv_type_nm', ''),
                'save_trm' : option.get('save_trm', ''),
            }
            optionserializer = SavingOptionSerializer(data=save_data)
            if optionserializer.is_valid(raise_exception=True):
                optionserializer.save(saving_product=product)
    
    return JsonResponse({'message':'save!'})

@api_view(['GET'])
def get_bank_list(request):
    # 상품 목록 반환하기
    banks = Bank.objects.all()
    serializer = DepositListSerializer(banks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_deposit_list(request):
    # 상품 목록 반환하기
    products = DepositProduct.objects.all()
    serializer = DepositListSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_saving_list(request):
    # 상품 목록 반환하기
    products = SavingProduct.objects.all()
    serializer = SavingListSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_deposit_products(request, period, option, banks):
    period = period.split(',')
    banks = banks.split(',')
    order = ''
    if option[-1] == '-':
        order = '-'
        option = option[:-1]
    products = DepositProduct.objects.filter(depositoption__save_trm__in = period,
                                             kor_co_nm__in = banks).order_by(f'{order}depositoption__{option}').distinct()
    # 중복 제거를 위한 set 사용
    seen = set()
    unique_products = []
    for product in products:
        if product.id not in seen:
            unique_products.append(product)
            seen.add(product.id)
    serializer = DepositListSerializer(unique_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_saving_products(request, period, option, banks):
    period = period.split(',')
    banks = banks.split(',')
    order = ''
    if option[-1] == '-':
        order = '-'
        option = option[:-1]
    products = SavingProduct.objects.filter(savingoption__save_trm__in = period,
                                            kor_co_nm__in = banks).order_by(f'{order}savingoption__{option}').distinct()
    # 중복 제거를 위한 set 사용
    seen = set()
    unique_products = []
    for product in products:
        if product.id not in seen:
            unique_products.append(product)
            seen.add(product.id)
    serializer = SavingListSerializer(unique_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 은행 상세 조회
@api_view(['GET'])
def get_bank_detail(request, id):
    bank = Bank.objects.get(pk=id)
    serializer = BankSerializer(bank)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def get_bank_map(request):
    print('==========')
    response_json = []
    
    for id in range(1, 19):
        
        bank = Bank.objects.get(pk=id)

        deposit_products = bank.depositproduct_set.all()
        top_deposit_product = deposit_products.annotate(join_user_count=Count('join_user')).order_by('-join_user_count').first()

        saving_products = bank.savingproduct_set.all()
        top_saving_product = saving_products.annotate(join_user_count=Count('join_user')).order_by('-join_user_count').first()


        response_json.append({
            'bank_id': id,
            'top_deposit_product': 
                { 'id': top_deposit_product.id,
                    'fin_prdt_nm': top_deposit_product.fin_prdt_nm,
                    'user_count': top_deposit_product.join_user_count},
            'top_saving_product': 
                {'id': top_saving_product.id, 
                    'fin_prdt_nm': top_saving_product.fin_prdt_nm,
                    'user_count': top_saving_product.join_user_count},
        })
    
    return Response(response_json, status=status.HTTP_200_OK)

# 예금 상품 조회
@api_view(['GET'])
def get_deposit_detail(request, id):
    product = DepositProduct.objects.get(pk=id)
    serializer = DepositDetailSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 적금 상품 조회
@api_view(['GET'])
def get_saving_detail(request, id):
    product = SavingProduct.objects.get(pk=id)
    serializer = SavingDetailSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 예금 옵션 수정
@api_view(['PUT'])
def update_deposit_option(request, option_id):
    option = DepositOption.objects.get(pk=option_id)
    if request.method == 'PUT':
        serializer = DepositOptionSerializer(instance=option, data=request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
# 적금 옵션 수정
@api_view(['PUT'])
def update_saving_option(request, option_id):
    option = SavingOption.objects.get(pk=option_id)
    if request.method == 'PUT':
        serializer = SavingOptionSerializer(instance=option, data=request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

# 예금 상품 가입 및 해지
@api_view(['POST', 'DELETE'])
def join_deposit(request, deposit_id):
    deposit = DepositProduct.objects.get(id=deposit_id)
    if request.method == 'POST':
        if request.user in deposit.join_user.all():
            pass
        else:
            deposit.join_user.add(request.user)
            return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        if request.user in deposit.join_user.all():
            deposit.join_user.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
    
# 적금 상품 가입 및 해지
@api_view(['POST', 'DELETE'])
def join_saving(request, saving_id):
    saving = SavingProduct.objects.get(id=saving_id)
    if request.method == 'POST':
        if request.user in saving.join_user.all():
            pass
        else:
            saving.join_user.add(request.user)
            return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        if request.user in saving.join_user.all():
            saving.join_user.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
# 예금 상품 비교 등록 및 해제
@api_view(['POST', 'DELETE'])
def compare_deposit(request, deposit_id):
    deposit = DepositProduct.objects.get(id=deposit_id)
    if request.method == 'POST':
        if request.user in deposit.compare_user.all():
            pass
        else:
            deposit.compare_user.add(request.user)
            return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        if request.user in deposit.compare_user.all():
            deposit.compare_user.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)

# 적금 상품 비교 등록 및 해제
@api_view(['POST', 'DELETE'])
def compare_saving(request, saving_id):
    saving = SavingProduct.objects.get(id=saving_id)
    if request.method == 'POST':
        if request.user in saving.compare_user.all():
            pass
        else:
            saving.compare_user.add(request.user)
            return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        if request.user in saving.compare_user.all():
            saving.compare_user.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)

# 예금 추천 알고리즘
@api_view(['GET'])
@permission_classes(['IsAuthenticated'])
def recommend_deposit(request):
    dp_cnt = 37
    me = get_object_or_404(get_user_model(), username=request.user.username)
    me_year = me.date_of_birth.year
    me_salary = me.salary
    me_budget = me.budget
    max_year = max(2010, me_year)
    min_year = min(1950, me_year)
    max_budget = max(1000000000, me_budget)
    min_budget = 0
    max_salary = max(15000000, me_salary)
    min_salary = 0
    scores = [[0, i+1] for i in range(dp_cnt)]
    users = get_list_or_404(get_user_model())
    
    for user in users:
        if (user.salary and user.budget) :
            score = 100
            score *= abs(me_year-user.date_of_birth.year)/(max_year-min_year)
            score *= abs(me_salary-user.salary)/(max_salary-min_salary)
            score *= abs(me_budget-user.budget)/(max_budget-min_budget)
            score = 100 - score
        
            for deposit in user.join_deposit.all():
                scores[deposit.id-1][0] += score
    
    scores.sort()
    recommend_list = []
    for i in range(5):
        product = DepositProduct.objects.get(pk=scores[i][1])
        recommend_list.append(product)
    
    serialized_data = DepositListSerializer(recommend_list, many=True).data
    
    serializer = ProfileSerializer(instance = me, data={'deposit_recommend':serialized_data}, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        
    return Response(data=serializer.data, status=status.HTTP_200_OK)
    
# 적금 추천 알고리즘
@api_view(['GET'])
def recommend_saving(request):
    sv_cnt = 64
    me = get_object_or_404(get_user_model(), username=request.user.username)
    me_year = me.date_of_birth.year
    me_salary = me.salary
    me_budget = me.budget
    max_year = max(2010, me_year)
    min_year = min(1950, me_year)
    max_budget = max(1000000000, me_budget)
    min_budget = 0
    max_salary = max(15000000, me_salary)
    min_salary = 0
    scores = [[0, i+1] for i in range(sv_cnt)]
    users = get_list_or_404(get_user_model())
    
    for user in users:
        if (user.salary and user.budget) :
            score = 100
            score *= abs(me_year-user.date_of_birth.year)/(max_year-min_year)
            score *= abs(me_salary-user.salary)/(max_salary-min_salary)
            score *= abs(me_budget-user.budget)/(max_budget-min_budget)
            score = 100 - score
            
            for saving in user.join_saving.all():
                scores[saving.id-1][0] += score
    
    scores.sort()
    recommend_list = []
    for i in range(5):
        product = SavingProduct.objects.get(pk=scores[i][1])
        recommend_list.append(product)
    serialized_data = SavingListSerializer(recommend_list, many=True).data
    serializer = ProfileSerializer(instance = me, data={'saving_recommend':serialized_data}, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    
    return Response(data=serializer.data, status=status.HTTP_200_OK)

# 이메일 보내는 함수
@api_view(['GET'])
def send_deposit_email(request, product_id):
    product = DepositProduct.objects.get(pk=product_id)
    users = product.join_user.all()
    bank = Bank.objects.get(fin_co_no = product.fin_co_no)
    for user in users:
        if user.id > 10000 and user.email:
            subject = f'{product.fin_prdt_nm} 상품 금리 변경 관련 안내'
            to = [user.email]
            from_email = 'goldenlettuce@naver.com'
            intro = f'{user.username} 고객님께, \n\n'
            greeting = f'{user.username} 고객님 안녕하세요? 금상추 서비스에요.\n'
            body1 = f'고객님께서 가입하신 {product.fin_prdt_nm} 상품에 대한 금리 변동 내역이 확인되어 안내드려요.\n'
            body2 = '자세한 내용은 금상추 홈페이지와 담당 은행 홈페이지를 참고해주세요.\n'
            body3 = f'담당 은행 홈페이지 : {bank.homp_url}\n'
            closing = '항상 금상추를 사랑해주시는 고객님께 진심으로 감사드려요.\n\n'
            finish = '금상추 드림.\n'
            
            message = intro + greeting + body1 + body2 + body3 + closing + finish
            EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
            
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def send_saving_email(request, product_id):
    product = SavingProduct.objects.get(pk=product_id)
    users = product.join_user.all()
    bank = Bank.objects.get(fin_co_no=product.fin_co_no)
    for user in users:
        if user.id > 10000 and user.email:
            subject = f'{product.fin_prdt_nm} 상품 금리 변경 관련 안내'
            to = [user.email]
            from_email = 'goldenlettuce@naver.com'
            intro = f'{user.username} 고객님께, \n\n'
            greeting = f'{user.username} 고객님 안녕하세요? 금상추 서비스에요.\n'
            body1 = f'고객님께서 가입하신 {product.fin_prdt_nm} 상품에 대한 금리 변동 내역이 확인되어 안내드려요.\n'
            body2 = '자세한 내용은 금상추 홈페이지와 담당 은행 홈페이지를 참고해주세요.\n'
            body3 = f'담당 은행 홈페이지 : {bank.homp_url}\n'
            closing = '항상 금상추를 사랑해주시는 고객님께 진심으로 감사드려요.\n\n'
            finish = '금상추 드림.\n'
            
            message = intro + greeting + body1 + body2 + body3 + closing + finish
            
            EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
            
    return Response(status=status.HTTP_200_OK)