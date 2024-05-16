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
def save_deposit(request):
    url = BASE_URL + f'depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')
    for product in baseList:
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
        productserializer = DepositDetailSerializer(data=save_data)
        # 유효할 경우 저장
        if productserializer.is_valid(raise_exception=True):
            productserializer.save()
            
    
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
    print(2)
    return JsonResponse({'message':'save!'})
    

@api_view(['GET'])
def get_deposit_list(request):
    # 상품 목록 반환하기
    products = DepositProduct.objects.all()
    serializer = DepositListSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_deposit_option(request):
    options = DepositOption.objects.all()
    serializer = DepositOptionSerializer(options, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)