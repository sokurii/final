from django.urls import path
from . import views

app_name = 'finlifes'
urlpatterns = [
    path('deposit-products/', views.deposit_products),
    path('deposit-products/<fin_prdt_cd>/', views.deposit_product_detail),
    path('saving-products/', views.saving_products),
    path('saving-products/<fin_prdt_cd>/', views.saving_product_detail),
    path('exchangeinfo/', views.exchangeinfo),
    
    path('deposit-products/<fin_prdt_cd>/likes/', views.like_deposit_products),
    path('saving-products/<fin_prdt_cd>/likes/', views.like_saving_products),
    
    # path('like_products/', views.user_liked_products),
    # path('deposit-products/top-rate/', views.top_rate),
]