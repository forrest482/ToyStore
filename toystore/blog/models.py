from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.PROTECT)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
