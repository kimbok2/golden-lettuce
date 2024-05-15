from django.urls import path
from . import views

urlpatterns = [
    # 프로필
    path('profile/<str:username>/', views.profile),
    # 회원정보 수정
    path('profile/<str:username>/info/', views.userinfo),
    # path('user/', views.UserDelete),
]
