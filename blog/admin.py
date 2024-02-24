from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Post, Comment, Media


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail_preview')
    search_fields = ('title',)

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.thumbnail.url))
        return ""

    thumbnail_preview.short_description = "Thumbnail Preview"


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category',
                    'created_at', 'thumbnail_preview')
    list_filter = ('created_at', 'category')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.thumbnail.url))
        return ""

    thumbnail_preview.short_description = "Thumbnail Preview"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at',
                    'is_active', 'text')
    list_filter = ('created_at', 'author', 'is_active')
    search_fields = ('text', 'author')
    list_editable = ('is_active',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'media_type', 'post')
    list_filter = ('media_type',)
    search_fields = ('caption',)
