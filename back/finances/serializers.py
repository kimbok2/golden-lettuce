from rest_framework import serializers
from .models import SavingOption, SavingProduct, DepositOption, DepositProduct

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
    class Meta:
        model = DepositProduct
        fields = '__all__'