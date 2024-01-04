from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView

from .forms import MovieForm, ShowForm
from .models import Movie, Show, Genre


# Create your views here.
def latest_movies(request):
    return render(request, "movies/all_latest.html")


def show_movie(request):
    return render(request, "movies/show_movie.html")

@login_required
def register_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['movie_title']
            year = form.cleaned_data['movie_year']
            genre = form.cleaned_data['movie_genres']
            synopsis = form.cleaned_data['movie_synopsis']
            poster = form.cleaned_data['movie_poster']

            movie = Movie.objects.create(
                title=title,
                year=year,
                synopsis=synopsis,
                poster=poster
                )

            movie.genre.set(genre)
            movie.save()
            messages.success(request, "Filme adicionado com sucesso!", "alert-success alert-dismissible")
            
            return redirect('index')
            
        else:
            messages.success(request, "Houve um erro ao registrar o filme. Tente novamente.", "alert-danger alert-dismissible")
    
    else:
        form = MovieForm()
    
    
    return render(request, "movies/add_movie.html", {"form": form})



def register_show(request):
    if request.method == "POST":
        form = ShowForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['show_title']
            year = form.cleaned_data['show_year']
            genre = form.cleaned_data['show_genres']
            synopsis = form.cleaned_data['show_synopsis']
            poster = form.cleaned_data['show_poster']

            show = Show.objects.create(
                title=title,
                year=year,
                synopsis=synopsis,
                poster=poster
                )

            show.genre.set(genre)
            show.save()
            messages.success(request, "Série adicionada com sucesso!", "alert-success alert-dismissible")
            
            return redirect('index')
            
        else:
            messages.success(request, "Houve um erro ao registrar a série. Tente novamente.", "alert-danger alert-dismissible")
    
    else:
        form = ShowForm()
    
    
    return render(request, "shows/add_show.html", {"form": form})