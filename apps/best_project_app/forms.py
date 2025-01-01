from .models import UserProfile, Comments
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'})
    )
    password1 = forms.CharField(
        label='Пароль',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ведите пароль'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите ваш пароль'})
    )
    email = forms.EmailField(
        label='Эмаил',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        label='Имя',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
    )

    password = forms.CharField(
        label='Пароль',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nickname', 'birth_date', 'address', 'number', 'twitter_link', 'telegram_link',
                  'facebook_link', 'bio', 'avatar')
        widgets = {
            'nickname': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите ваш никнейм'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения (YYYY-MM-DD)',
                'type': 'date'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш адрес'
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1234567890'
            }),
            'twitter_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на Twitter'
            }),
            'telegram_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на Telegram'
            }),
            'facebook_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на Facebook'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Расскажите о себе...'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeolder': 'Напишите ваш отзыв о продукте'})
        }
