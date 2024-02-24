# blog/serializers.py

from rest_framework import serializers
from .models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'category', 'title', 'slug',
                  'content', 'created_at', 'comments']

    def get_comments(self, obj):
        active_comments = obj.comments.filter(is_active=True)
        return CommentSerializer(active_comments, many=True).data
