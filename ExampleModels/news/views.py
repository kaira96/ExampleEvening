from django.http import HttpResponse
from django.shortcuts import render

from news.models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)

