from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('finance/', include('finance.urls')),
    path('store/', include('store.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
