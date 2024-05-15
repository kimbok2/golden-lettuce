from django.urls import path
from . import views

urlpatterns = [
    # 프로필
    path('profile/<str:userid>/', views.profile),
    # 회원정보 수정
    path('profile/<str:userid>/info/', views.userinfo),
    # path('user/', views.UserDelete),
]
