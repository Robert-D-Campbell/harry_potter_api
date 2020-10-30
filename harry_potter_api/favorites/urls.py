from django.urls import path
from . import views

urlpatterns = [
  path('', views.characters, name='characters'),
  path('list/', views.favorites_list, name='favorites_list'),
  path('<str:favorite_id>/', views.favorite_detail, name='favorite_detail'),
]