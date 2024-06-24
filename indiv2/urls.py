"""
URL configuration for indiv2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_indiv2.views import landing, user_detail, register, register_success, welcome, restricted_view, color_celeste
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing, name='landing'),
    path('user_detail/', user_detail, name='user_detail'),
    path('register/', register, name='register'),
    path('register_success/', register_success, name='register_success'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
    path('welcome/', welcome, name='welcome'),
    path('restricted/', restricted_view, name='restricted'),
    path('color_celeste/', color_celeste, name='color_celeste'),
]
