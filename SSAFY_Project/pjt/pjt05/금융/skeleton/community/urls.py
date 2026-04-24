from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm
from .models import Post

app_name = "community"

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html', success_url='/'
    ), name='password_change'),
    path('profile/', profile_view, name='profile'),
    path('post/create/', post_create_view, name='post_create'),
    path('post/<int:post_id>/update/', post_update_view, name='post_update'),
    path('post/<int:post_id>/delete/', views.post_delete_view, name='post_delete'),
]