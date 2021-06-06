from django.urls import path
from . import views

urlpatterns = [
    path('ajax/get_warehouse_data', views.index, name = 'index'),
]
