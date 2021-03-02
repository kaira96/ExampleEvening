from django.http import HttpResponse
from django.shortcuts import render

from news.models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories=Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news':news, 'categories':categories, 'category':category})
