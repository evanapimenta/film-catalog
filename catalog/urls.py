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
from django.urls import path, include

from catalog import views

urlpatterns = [
    path('add_movie/', views.register_movie, name='add_movie'),
    path('latest_movies/', views.latest_movies, name='latest_movies'),
    # path('show_movie/', views.show_movie, name='movie'),
    path('add_show/', views.register_show, name='add_show'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie-detail'),
]