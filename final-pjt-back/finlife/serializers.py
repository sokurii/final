from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, ExchangeInfos
# , DepositOptions

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)

class DepositProductsSerializer(serializers.ModelSerializer):
    depositoptions = DepositOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)
        
class SavingProductsSerializer(serializers.ModelSerializer):
    savingoptions = SavingOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'


class ExchangeInfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeInfos
        fields = '__all__'