from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey
from decimal import Decimal
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=58, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}\'s profile'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class TypeProduct(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    background = models.ImageField(upload_to='TypeProducts/backgrounds/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type Product'
        verbose_name_plural = 'Type Products'


class Product(models.Model):
    type = ForeignKey(TypeProduct, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Basket(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='baskets')
    product = ForeignKey(Product, on_delete=models.CASCADE, related_name='baskets')
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"корзина {self.user}'s | Продукт {self.product.name}"

    def sum(self):
        return self.quantity * self.product.price


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f"{self.user}'s | {self.product.name}"


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=550)
    time_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s | {self.product.name} | {self.comment[:20]}..."




