from django.contrib import admin
from .models import Category, Post, Comment, Media


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('created_at', 'category')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at',
                    'is_active', 'text')
    list_filter = ('created_at', 'author', 'is_active')
    search_fields = ('text', 'author')
    list_editable = ('is_active',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('caption', 'media_type', 'post')
    list_filter = ('media_type',)
    search_fields = ('caption',)
