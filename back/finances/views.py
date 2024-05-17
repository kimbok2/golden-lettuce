from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import *
from .serializers import *
import requests

# Create your views here.
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

API_KEY='b5c8f98021e7c5f65ecd69ba1a050e5e'

@api_view(['GET'])
def save_bank(request):
    url = BASE_URL + f'companySearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    baseList = response.get('result').get('baseList')
    for bank in baseList:
        save_data = {
            'fin_co_no' : bank.get('fin_co_no', ''),
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
    url = BASE_URL + f'depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')
    for product in baseList:
        bank = Bank.objects.get(fin_co_no=product.get('fin_co_no'))
        save_data = {
            'fin_prdt_cd' : product.get('fin_prdt_cd'),
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
        if product:
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
    url = BASE_URL + f'savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')
    for product in baseList:
        bank = Bank.objects.get(fin_co_no=product.get('fin_co_no'))
        save_data = {
            'fin_prdt_cd' : product.get('fin_prdt_cd'),
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
        if product:
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
def get_deposit_list(request):
    # 상품 목록 반환하기
    products = DepositProduct.objects.all()
    serializer = DepositListSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_deposit_products(request, period):
    period = period.split(',')
    products = DepositProduct.objects.filter(depositoption__save_trm__in = period).order_by('-depositoption__intr_rate').distinct()
    # 중복 제거를 위한 set 사용
    seen = set()
    unique_products = []
    for product in products:
        if product.id not in seen:
            unique_products.append(product)
            seen.add(product.id)
    serializer = DepositListSerializer(unique_products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_saving_list(request):
    # 상품 목록 반환하기
    products = SavingProduct.objects.all()
    serializer = SavingListSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_saving_products(request, period):
    period = period.split(',')
    products = SavingProduct.objects.filter(savingoption__save_trm__in = period).order_by('-savingoption__intr_rate').distinct()
    # 중복 제거를 위한 set 사용
    seen = set()
    unique_products = []
    for product in products:
        if product.id not in seen:
            unique_products.append(product)
            seen.add(product.id)
    serializer = SavingListSerializer(unique_products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_bank_detail(request, id):
    bank = Bank.objects.get(pk=id)
    serializer = BankSerializer(bank)
    return Response(serializer.data)

@api_view(['GET'])
def get_deposit_detail(request, id):
    product = DepositProduct.objects.get(pk=id)
    serializer = DepositDetailSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def get_saving_detail(request, id):
    product = SavingProduct.objects.get(pk=id)
    serializer = SavingDetailSerializer(product)
    return Response(serializer.data)

# 예금 상품 가입
@api_view(['POST'])
def join_deposit(request, deposit_id):
    deposit = DepositProduct.objects.get(id=deposit_id)
    if request.user in deposit.join_user.all():
        pass
    else:
        deposit.join_user.add(request.user)
        return Response(status=status.HTTP_200_OK)
    
# 예금 상품 가입
@api_view(['POST'])
def join_saving(request, saving_id):
    saving = SavingProduct.objects.get(id=saving_id)
    if request.user in saving.join_user.all():
        pass
    else:
        saving.join_user.add(request.user)
        return Response(status=status.HTTP_200_OK)