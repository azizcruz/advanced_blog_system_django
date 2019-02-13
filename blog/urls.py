from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('user/posts/<str:username>', views.UserPostListView.as_view(), name='user_posts_page'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete')
]