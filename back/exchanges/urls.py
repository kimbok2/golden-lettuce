from django.urls import path
from . import views

urlpatterns = [
    path('get_current_info/', views.get_current_info),
]
