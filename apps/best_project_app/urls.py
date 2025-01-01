from apps.best_project_app import admin, views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_, name='login'),
    path('register/', views.register_, name='register'),
    path('logout/', views.logout_, name='logout'),
    path('about/', views.about_page, name='about'),
    path('chocolate/', views.chocolate_page, name='chocolate'),
    path('contact/', views.contact_page, name='contact'),
    path('testimonial/', views.testimonial_page, name='testimonial'),
    path('categories/', views.categories_page, name='categories'),
    path('categories/detail/<int:type_product_pk>/', views.category_detail, name='category_detail'),
    path('product/<int:product_pk>/', views.detail_product, name='detail_product'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/change/', views.profile_change, name='profile_change'),
    path('basket-add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', views.basket_delete, name='basket_delete'),
    path('basket-remove/<int:product_id>/', views.basket_remove, name='basket_remote'),
    path('search/', views.search_view, name='search_page'),
    path('add-to-favourite/<int:product_pk>', views.add_to_favorites, name='add_to_favorites'),
    path('remove-from-favourite/<int:product_pk>', views.remove_from_favorites, name='remove_from_favorites'),
    path('profile/favourite/', views.favorite_view, name='favorite'),
    path('remove-comment/<int:comment_id>/', views.remove_comment, name='remove_comment'),
    path('super_user_page/', views.super_user_page, name='super_user_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)