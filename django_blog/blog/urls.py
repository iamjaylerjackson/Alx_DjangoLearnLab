from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    create_comment,
    CommentUpdateView,
    CommentDeleteView,
    # ... other imports
)


urlpatterns = [
    # Authentication
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Blog CRUD
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('posts/<int:post_pk>/comments/new/',
         create_comment, name='comment_create'),
    path('posts/<int:post_pk>/comments/<int:pk>/edit/',
         CommentUpdateView.as_view(), name='comment_edit'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment_delete'),
]
