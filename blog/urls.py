from django.urls import path
from .views import post_list, category_posts, post_detail
from .api_views import CategoryList, CategoryDetail, PostList, PostDetail, PostComment

urlpatterns = [
    # Template-based views
    path('', post_list, name='post_list'),
    path('category/<int:category_id>/',
         category_posts, name='category_posts'),
    path('<int:post_id>/', post_detail, name='post_detail'),

    # API endpoints
    path('api/categories/', CategoryList.as_view(), name='category-list'),
    path('api/categories/<int:pk>/',
         CategoryDetail.as_view(), name='category-detail'),
    path('api/posts/', PostList.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('api/posts/<int:post_id>/comment/',
         PostComment.as_view(), name='post_comment')
]
