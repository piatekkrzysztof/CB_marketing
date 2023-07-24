from django.contrib import admin
from .models import *


class BlogPostImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "blogpost"]


admin.site.register(BlogPostImage, BlogPostImageAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", 'text', 'category']


admin.site.register(BlogPost, BlogPostAdmin)


class BlogPostCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", 'description']


admin.site.register(BlogPostCategory, BlogPostCategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", 'text', 'category']


admin.site.register(Article, ArticleAdmin)


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", 'description']


admin.site.register(ArticleCategory, ArticleCategoryAdmin)


class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "article"]


admin.site.register(ArticleImage, ArticleImageAdmin)
