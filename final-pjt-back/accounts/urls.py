from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('', views.profile),
    path('create/', views.create_profile),
    path('user/<username>', views.get_user),
]