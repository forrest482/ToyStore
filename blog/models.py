from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        upload_to='category_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    thumbnail = models.ImageField(
        upload_to='post_thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_images(self):
        return self.media.filter(media_type='IMG')

    def get_videos(self):
        return self.media.filter(media_type='VID')

    def get_audios(self):
        return self.media.filter(media_type='AUD')


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
    MEDIA_TYPE_CHOICES = (
        ('IMG', _('Image')),
        ('VID', _('Video')),
        ('AUD', _('Audio')),
    )

    post = models.ForeignKey(Post, related_name='media',
                             on_delete=models.CASCADE)
    media_type = models.CharField(
        max_length=3,
        choices=MEDIA_TYPE_CHOICES,
        default='IMG'
    )
    file = models.FileField(upload_to='blog_media/')
    caption = models.CharField(max_length=255, blank=True)
