from django.urls import path
from . import views

urlpatterns = [
    # 게시글
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail)
]
