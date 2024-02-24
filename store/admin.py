from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Price, Comment, Media


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail_preview')
    search_fields = ('title',)

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.thumbnail.url))
        return "No Image"

    thumbnail_preview.short_description = "Thumbnail"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price',
                    'created_at', 'thumbnail_preview')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('price',)

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.thumbnail.url))
        return "No Image"
    thumbnail_preview.short_description = "Thumbnail"


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('product__name', 'price')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'author',
                    'text', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('product__name', 'author__username', 'text')
    list_editable = ('is_active',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'media_type', 'file', 'caption')
    list_filter = ('media_type',)
    search_fields = ('product__name', 'caption')
