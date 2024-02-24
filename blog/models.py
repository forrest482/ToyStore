from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def get_images(self):
    #     return self.media.


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author.username}'


class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = 'IMG', _('Image')
        VIDEO = 'VID', _('Video')
        AUDIO = 'AUD', _('Audio')

    post = models.ForeignKey(Post, related_name='media',
                             on_delete=models.CASCADE)
    media_type = models.CharField(
        max_length=3, choices=MediaType.choices, default=MediaType.IMAGE)
    file = models.FileField(upload_to='blog_media/')
    caption = models.CharField(max_length=255, blank=True)
