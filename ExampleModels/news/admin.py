from django.contrib import admin

from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'update_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title','content')


admin.site.register(News, NewsAdmin)
