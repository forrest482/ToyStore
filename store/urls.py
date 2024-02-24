from django.urls import path
from .views import category_list, category_detail, product_list, product_detail
from .api_views import CategoryList, CategoryDetail, ProductList, ProductDetail, ProductComment

urlpatterns = [
    # Template-based views
    path('', product_list, name='product_list'),
    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>/', category_detail,
         name='category_detail'),
    path('product/<int:product_id>/', product_detail,
         name='product_detail'),

    # API endpoints
    path('api/categories/', CategoryList.as_view(), name='category-list'),
    path('api/categories/<int:pk>/',
         CategoryDetail.as_view(), name='category-detail'),
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/products/<int:product_id>/comment/',
         ProductComment.as_view(), name='product_comment'),
]
