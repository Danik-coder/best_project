from django.urls import path
from . import views

urlpatterns = [
    path('type_products/', views.get_TypeProducts, name='get_type_products'),
    path('products/', views.get_Products, name='get_products'),
    path('baskets/', views.get_Baskets, name='get_baskets'),
    path('favorites/', views.get_Favorites, name='get_favorites'),
    path('comments/', views.get_Comments, name='get_comments'),
]