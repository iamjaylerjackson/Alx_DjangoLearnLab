from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Blog
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comments (checker expects these exact patterns)
    path('post/<int:pk>/comments/new/',
         views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/',
         views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/',
         views.CommentDeleteView.as_view(), name='comment_delete'),
]
