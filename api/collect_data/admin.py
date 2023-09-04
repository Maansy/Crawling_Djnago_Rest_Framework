from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'created_at')
    list_filter = ('writer', 'created_at')
    search_fields = ('title', 'content', 'writer')


admin.site.register(Article, ArticleAdmin)