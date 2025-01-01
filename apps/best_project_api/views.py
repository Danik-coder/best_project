from django.shortcuts import render
import json
from apps.best_project_app.models import *
from django.http import JsonResponse

# Type Products
def get_TypeProducts(request):
    type_products = TypeProduct.objects.all()
    type_products_list = [{'id': tp.id, 'name': tp.name} for tp in type_products]
    return JsonResponse({'type_products': type_products_list})

# Products
def get_Products(request):
    products = Product.objects.all()
    products_list = [{'id': p.id, 'name': p.name, 'price': p.price} for p in products]
    return JsonResponse({'products': products_list})


# Baskets
def get_Baskets(request):
    baskets = Basket.objects.all()
    baskets_list = [{'id': b.id, 'user': b.user.username, 'product': b.product.name, 'quantity': b.quantity} for b in baskets]
    return JsonResponse({'baskets': baskets_list})

# Favorites
def get_Favorites(request):
    favorites = Favorite.objects.all()
    favorites_list = [{'user': f.user.username, 'product': f.product.name} for f in favorites]
    return JsonResponse({'favorites': favorites_list})

# Comments
def get_Comments(request):
    comments = Comments.objects.all()
    comments_list = [{'user': c.user.username, 'product': c.product.name, 'comment': c.comment} for c in comments]
    return JsonResponse({'comments': comments_list})

