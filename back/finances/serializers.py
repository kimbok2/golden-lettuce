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
        
# 은행 시리얼라이저
class BankMapSerializer(serializers.ModelSerializer):
    
    # class DepositListSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = DepositProduct
    #         fields = '__all__'
            
    # class SavingListSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = SavingProduct
    #         fields = '__all__'
    
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

# 적금 옵션 시리얼라이저
class SavingOptionSerializer(serializers.ModelSerializer):
    # 적금 상품은 읽기 전용으로
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('saving_product', )

# 예금 전체 조회 시리얼라이저
class DepositListSerializer(serializers.ModelSerializer):
    join_user_count = serializers.IntegerField(source='join_user.count', read_only=True)
    depositoption_set = DepositOptionSerializer(read_only=True, many=True)
    class Meta:
        model = DepositProduct
        fields = '__all__'

# 적금 전체 조회 시리얼라이저
class SavingListSerializer(serializers.ModelSerializer):
    join_user_count = serializers.IntegerField(source='join_user.count', read_only=True)
    savingoption_set = SavingOptionSerializer(read_only=True, many=True)
    class Meta:
        model = SavingProduct
        fields = '__all__'

# 예금 저장 시리얼라이저
class DepositSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializer(read_only=True, many=True)
    class Meta:
        model = DepositProduct
        fields = '__all__'
        read_only_fields = ('bank', 'join_user', 'compare_user',)

# 적금 단일 저장용 시리얼라이저
class SavingSerializer(serializers.ModelSerializer):
    # savingoption_set = SavingOptionSerializer(read_only=True, many=True)
    class Meta:
        model = SavingProduct
        fields = '__all__'
        read_only_fields = ('bank', 'join_user','compare_user',)

# 예금 단일 조회 시리얼라이저
class DepositDetailSerializer(serializers.ModelSerializer):
    join_user_count = serializers.IntegerField(source='join_user.count', read_only=True)
    compare_user_count = serializers.IntegerField(source='compare_user.count', read_only=True)
    depositoption_set = DepositOptionSerializer(read_only=True, many=True)
    class Meta:
        model = DepositProduct
        fields = '__all__'
        read_only_fields = ('bank', )
    
# 적금 단일 조회 시리얼라이저
class SavingDetailSerializer(serializers.ModelSerializer):
    join_user_count = serializers.IntegerField(source='join_user.count', read_only=True)
    compare_user_count = serializers.IntegerField(source='compare_user.count', read_only=True)
    savingoption_set = SavingOptionSerializer(read_only=True, many=True)
    class Meta:
        model = SavingProduct
        fields = '__all__'
        read_only_fields = ('bank', )

# 예금 옵션 수정 시리얼라이저
class DepositOptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'