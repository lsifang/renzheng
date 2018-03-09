"""renz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from renzheng import views as rz_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',rz_view.login,name="login"),
    path('login/',rz_view.login,name='login'),
    path('register/',rz_view.register,name="register"),
    path('code/',rz_view.code,name="code"),
    path('coded/',rz_view.coded,name="coded"),
    path('logout/',rz_view.logout,name="logout"),
]
