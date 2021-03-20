from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView

app_name = 'post'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='list_posts'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/update_post/<int:pk>/', PostUpdateView.as_view(), name='update_post')
]