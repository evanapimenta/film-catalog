"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from catalog import views as catalog_views
from authentication import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('select2/', include("django_select2.urls")),
    path('', catalog_views.index, name='index'),
    path('add_movie', catalog_views.register_movie, name='add_movie'),
    path('latest_movies', catalog_views.latest_movies, name='latest_movies'),
    path('show_movie', catalog_views.show_movie, name='movie'),
    path('add_show', catalog_views.register_show, name='add_show'),
    path('login', auth_views.login_page, name='login')
]
