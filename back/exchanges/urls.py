from django.urls import path
from . import views

urlpatterns = [
    path('get_current_info/', views.get_current_info),
    path('get_graph_data/<int:current_pk>/', views.get_graph_data),
]
