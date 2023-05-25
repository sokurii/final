from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile
from articles.serializers import ArticleSerializer
from finlife.serializers import DepositProductsSerializer, SavingProductsSerializer

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user',)
        
class CustomUserSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True, read_only=True)
    articles_count = serializers.IntegerField(source='article_set.count', read_only=True)
    likedeposits = DepositProductsSerializer(many=True, read_only=True)
    likedeposits_count = serializers.IntegerField(source='likedeposits.count', read_only=True)
    likesavings = SavingProductsSerializer(many=True, read_only=True)
    likesavings_count = serializers.IntegerField(source='likesavings.count', read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'article_set', 'articles_count', 'likedeposits', 'likedeposits_count', 'likesavings', 'likesavings_count',)
        read_only_fields = ('user',)