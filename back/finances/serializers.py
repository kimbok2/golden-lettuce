from rest_framework import serializers
from .models import *

# 은행 시리얼라이저
class BankSerializer(serializers.ModelSerializer):
    class DepositListSerializer(serializers.ModelSerializer):
    
        class DepositOptionDetailSerializer(serializers.ModelSerializer):
            class Meta:
                model = DepositOption
                fields = ('intr_rate', 'intr_rate2','save_trm', 'intr_rate_type_nm','deposit_product',)
                
        depositoption_set = DepositOptionDetailSerializer(read_only=True, many=True)
        class Meta:
            model = DepositProduct
            fields = '__all__'
    class SavingListSerializer(serializers.ModelSerializer):
        class SavingOptionSerializer(serializers.ModelSerializer):
            # 적금 상품은 읽기 전용으로
            class Meta:
                model = SavingOption
                fields = '__all__'
                read_only_fields = ('saving_product', )
        savingoption_set = SavingOptionSerializer(read_only=True, many=True)
        class Meta:
            model = SavingProduct
            fields = '__all__'
    depositproduct_set = DepositListSerializer(read_only=True, many=True)
    savingproduct_set = SavingListSerializer(read_only=True, many=True)
    class Meta:
        model = Bank
        fields = '__all__'

# 예금 옵션 시리얼라이저
class DepositOptionSerializer(serializers.ModelSerializer):
    # 예금 상품은 읽기 전용으로
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('deposit_product',)

class DepositListSerializer(serializers.ModelSerializer):
    
    class DepositOptionDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositOption
            fields = ('intr_rate', 'intr_rate2','save_trm', 'intr_rate_type_nm','deposit_product',)
            
    depositoption_set = DepositOptionDetailSerializer(read_only=True, many=True)
    class Meta:
        model = DepositProduct
        fields = '__all__'


class DepositDetailSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializer(read_only=True, many=True)
    class Meta:
        model = DepositProduct
        fields = '__all__'
        read_only_fields = ('bank',)

# 적금 옵션 시리얼라이저
class SavingOptionSerializer(serializers.ModelSerializer):
    # 적금 상품은 읽기 전용으로
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('saving_product', )

# 적금 전체 조회 시리얼라이저
class SavingListSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializer(read_only=True, many=True)
    class Meta:
        model = SavingProduct
        fields = '__all__'


# 적금 단일 저장용 시리얼라이저
class SavingDetailSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializer(read_only=True, many=True)
    class Meta:
        model = SavingProduct
        fields = '__all__'
        read_only_fields = ('bank',)