from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('finance/', include('finance.urls')),
    path('store/', include('store.urls')),
]
