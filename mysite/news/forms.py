from django import forms
from django.core.exceptions import ValidationError
import re
from .models import News
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={
        'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')






# from .models import Category
#
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150,
#                             label='Название',
#                             widget=forms.TextInput(attrs={
#                                 "class": "form-control"}))
#     content = forms.CharField(label='Текст',
#                               required=False,
#                               widget=forms.Textarea(attrs={
#                                 "class": "form-control",
#                                 "rows": 5
#                             }))
#     is_published = forms.BooleanField(label='Статус',
#                                       initial=True)
#     category = forms.ModelChoiceField(empty_label='Выберите категорию',
#                                       label='Категория',
#                                       queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={
#
#                                           "class": "form-control"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News

        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'content' : forms.Textarea(attrs={
                'class' : 'form-control'
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control'
            })
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if re.match(r'\d', title):
                raise ValidationError('Название не должно начинаться с цифры')
            return title