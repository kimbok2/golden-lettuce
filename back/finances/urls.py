from django.urls import path
from . import views

urlpatterns = [
    path('save_deposit/', views.save_deposit),
    path('save_saving/', views.save_saving),
    path('get_deposit_all/', views.get_deposit_list),
    path('get_saving_all/', views.get_saving_list),
    path('get_deposit/<int:id>/', views.get_deposit_detail),
    path('get_saving/<int:id>/', views.get_saving_detail),
    path('get_deposit_option_all/', views.get_deposit_option),
    path('get_deposit_products/<str:period>/', views.get_deposit_products),
    path('get_saving_products/<str:period>/', views.get_saving_products),
]
