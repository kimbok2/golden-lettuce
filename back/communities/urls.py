from django.urls import path
from . import views

urlpatterns = [
    # 게시글
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comment/', views.article_comment),
    path('comment/<int:comment_pk>/', views.comment_delete),
]
