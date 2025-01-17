from django.urls import path
from . import views

urlpatterns = [
    path('save_bank/', views.save_bank),
    path('save_deposit/', views.save_deposit),
    path('save_saving/', views.save_saving),
    path('get_deposit_all/', views.get_deposit_list),
    path('get_saving_all/', views.get_saving_list),
    path('get_bank/<int:id>/', views.get_bank_detail),
    path('get_bank_map/', views.get_bank_map),
    path('get_deposit/<int:id>/', views.get_deposit_detail),
    path('get_saving/<int:id>/', views.get_saving_detail),
    path('get_deposit_products/<str:period>/<str:option>/<str:banks>/', views.get_deposit_products),
    path('get_saving_products/<str:period>/<str:option>/<str:banks>/', views.get_saving_products),
    path('join_deposit/<int:deposit_id>/', views.join_deposit),
    path('join_saving/<int:saving_id>/', views.join_saving),
    path('compare_deposit/<int:deposit_id>/', views.compare_deposit),
    path('compare_saving/<int:saving_id>/', views.compare_saving),
    path('recommend_deposit1/', views.recommend_deposit),
    path('recommend_saving1/', views.recommend_saving),
    path('update_deposit_option/<int:option_id>/', views.update_deposit_option),
    path('update_saving_option/<int:option_id>/', views.update_saving_option),
    path('send_deposit_email/<int:product_id>/', views.send_deposit_email),
    path('send_saving_email/<int:product_id>/', views.send_saving_email),
]
