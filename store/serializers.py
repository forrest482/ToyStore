# store/serializers.py

from rest_framework import serializers
from .models import Category, Product, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description',
                  'thumbnail', 'created_at', 'price', 'comments']

    def get_comments(self, obj):
        active_comments = obj.store_comments.filter(is_active=True)
        return CommentSerializer(active_comments, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']
