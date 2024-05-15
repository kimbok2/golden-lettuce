from django.urls import path
from . import views

urlpatterns = [
    # 프로필
    path('<str:userid>/', views.profile),
    # 회원정보 수정
    path('<str:userid>/info/', views.userinfo),
    # path('user/', views.UserDelete),
]
