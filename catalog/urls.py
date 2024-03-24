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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add_movie/', views.add_movie, name='add_movie'),
    path('show_all_movies/', views.show_all_movies, name='show_all_movies'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie-detail'),
    path('movies/genre/<str:genre>/', views.GenreListView.as_view(), name='show-by-genre'),
    path('add_show/', views.add_show, name='add_show'),
    path('shows/genre/<str:genre>/', views.ShowGenreListView.as_view(), name='show-show-by-genre'),
    path('shows/<int:show_id>/', views.show_detail, name='show-detail'),
    path('show_all_shows/', views.show_all_shows, name='show_all_shows'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)