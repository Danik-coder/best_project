from itertools import product

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, HttpResponseRedirect

from apps.best_project_app.forms import LoginForm, RegistrationForm, ProfileForm, CommentForm
from apps.best_project_app.models import UserProfile, Product, TypeProduct, Basket, Favorite, Comments


def index(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'pages/index.html', context)


def login_(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'pages/login.html', context)


def register_(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(
                user=user
            )
            user_profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'pages/register.html', context)


def logout_(request):
    logout(request)
    return redirect('index')


def about_page(request):
    return render(request, 'pages/about.html')


def chocolate_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pages/chocolate.html', context)


def contact_page(request):
    return render(request, 'pages/contact.html')


def testimonial_page(request):
    return render(request, 'pages/testimonial.html')


def categories_page(request):
    type_products = TypeProduct.objects.all()
    context = {
        'type_products': type_products
    }

    return render(request, 'pages/categories.html', context)


def category_detail(request, type_product_pk):
    products_of_type = Product.objects.filter(type=type_product_pk)
    type_product = TypeProduct.objects.get(pk=type_product_pk)
    if request.user.is_authenticated:
        in_favorite = Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        in_favorite = []

    context = {
        'products_of_type': products_of_type,
        'type_product': type_product,
        'in_favorite': in_favorite,
    }

    return render(request, 'pages/detail_category.html', context)


def detail_product(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    comments = Comments.objects.filter(product=product_pk)
    if request.user.is_authenticated:
        in_basket = Basket.objects.filter(user=request.user, product=product).exists()
        basket = Basket.objects.filter(user=request.user, product=product).first()
    else:
        in_basket = False
        basket = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()
    context = {
        'product': product,
        'in_basket': in_basket,
        'basket': basket,
        'form': form,
        'comments': comments,
    }
    return render(request, 'pages/detail_product.html', context)


def profile_page(request):
    if not request.user.is_authenticated:
        return HttpResponse('Пожалуйста, войдите в систему.')
    user_profile = get_object_or_404(UserProfile, user=request.user)

    baskets = Basket.objects.filter(user=request.user)
    favorite_products = Favorite.objects.filter(user=request.user)

    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)

    context = {
        'user_profile': user_profile,
        'baskets': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
        'favorite_products': favorite_products,
    }
    return render(request, 'pages/profile.html', context)


def profile_change(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    context = {
        'form': form,
    }
    return render(request, 'pages/profile_change.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if baskets.exists():
        basket = baskets.first()
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search_view(request):
    query = request.GET.get('query', '')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'pages/search.html', {
        'results': results,
        'query': query,
    })


def add_to_favorites(request, product_pk):
    product = Product.objects.get(id=product_pk)
    favourite_user = request.user.favorites.all()
    if not favourite_user.filter(product=product_pk).exists():
        Favorite.objects.create(user=request.user, product=product)
    return redirect(request.META.get('HTTP_REFERER'))


def remove_from_favorites(request, product_pk):
    favourite_user = request.user.favorites.all()
    if favourite_user.filter(product=product_pk).exists():
        favorite = Favorite.objects.get(user=request.user, product=product_pk)
        favorite.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def favorite_view(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'pages/favourite.html', {'favorites': favorites})\



def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect(product.get_absolute_url())
    else:
        form = CommentForm()

    return render(request, 'components/_comment-form.html', {'form': form, 'product': product})


def remove_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def super_user_page(request):
    if request.user.is_superuser:
        return render(request, 'super_user_page.html')
    return redirect('index')


