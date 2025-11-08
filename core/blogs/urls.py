from django.urls import path
from .views import IndexView, PostDetailView, PostListView,PostCreateView

urlpatterns = [
    path('class-based/', IndexView.as_view(), name='index_class_based'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
]
