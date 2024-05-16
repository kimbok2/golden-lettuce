from django.urls import path
from . import views

urlpatterns = [
    path('save_deposit/', views.save_deposit),
    path('save_saving/', views.save_saving),
    path('get_deposit_all/', views.get_deposit_list),
    path('get_saving_all/', views.get_saving_list),
    path('get_deposit_option_all/', views.get_deposit_option),
]
