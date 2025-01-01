from django.contrib import admin
from .models import *

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'price']
    list_display_links = ['id', 'type', 'name']
    list_filter = ['type', 'price']

class AdminBasket(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'created_timestamp']
    list_display_links = ['id', 'user', 'product', 'quantity', 'created_timestamp']


class AdminComments(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'time_add']
    list_display_links = ['id', 'user', 'product', 'time_add']
    list_filter = ['user', 'product', 'time_add']


admin.site.register(UserProfile)
admin.site.register(TypeProduct)
admin.site.register(Product, AdminProduct)
admin.site.register(Basket, AdminBasket)
admin.site.register(Favorite)
admin.site.register(Comments, AdminComments)


