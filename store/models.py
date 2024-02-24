from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        upload_to='category_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(
        upload_to='product_thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        latest_price = self.prices.filter(is_active=True).last()
        return latest_price.price if latest_price else None

    def __str__(self):
        return self.name

    def get_images(self):
        return self.media.filter(media_type='IMG')

    def get_videos(self):
        return self.media.filter(media_type='VID')

    def get_audios(self):
        return self.media.filter(media_type='AUD')


class Price(models.Model):
    product = models.ForeignKey(
        Product, related_name='prices', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.price}"


class Comment(models.Model):
    product = models.ForeignKey(
        Product, related_name='store_comments', on_delete=models.PROTECT)
    author = models.ForeignKey(
        User, related_name='store_comments', on_delete=models.PROTECT)
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

    product = models.ForeignKey(Product, related_name='media',
                                on_delete=models.CASCADE)
    media_type = models.CharField(
        max_length=3,
        choices=MEDIA_TYPE_CHOICES,
        default='IMG'
    )
    file = models.FileField(upload_to='product_media/')
    caption = models.CharField(max_length=255, blank=True)
