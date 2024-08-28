from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Маршрут для главной страницы
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('post/new/', views.create_post, name='create_post'),
    path('subscribe/<int:user_id>/', views.subscribe, name='subscribe'),
    path('feed/', views.subscriptions_feed, name='subscriptions_feed'),
    path('public/', views.public_posts, name='public_posts'),
    path('request_post/<int:post_id>/', views.request_post, name='request_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
