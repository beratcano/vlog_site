"""
URL configuration for vlog_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.urls import path, include
from vlog_app.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/vlog/', permanent=False), name='index'),
    path("vlog/", include("vlog_app.urls")),
    path("login/",auth_views.LoginView.as_view(redirect_authenticated_user=True, next_page='/vlog/'), name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page='/vlog/'), name="logout"),
    path("register/",register, name="register"),
]
