from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView
from django.utils.translation import gettext as _

from requests import request


from .forms import MovieForm, ShowForm
from .models import Movie, Show, Genre


from django.db.models import Q

def show_all_movies(request):
    m_qs = Movie.objects.all()
    movie_title = request.GET.get('movie_title')
    movie_year = request.GET.get('movie_year')
    movie_genres = request.GET.getlist('movie_genres')

    if movie_title:
        m_qs = m_qs.filter(title__icontains=movie_title)
    if movie_year:
        m_qs = m_qs.filter(year=movie_year)
    if movie_genres:
        genre_ids = Genre.objects.filter(name__in=movie_genres).values_list('id', flat=True)
        m_qs = m_qs.filter(genre__in=genre_ids)

    print(m_qs)
    context = {
        'movies': m_qs
    }

    return render(request, "catalog/movie/movie_catalog.html", context=context)


def show_all_shows(request):
    m_qs = Show.objects.all()
    show_title = request.GET.get('show_title')
    show_year = request.GET.get('show_year')
    show_genres = request.GET.getlist('show_genres')

    if show_title:
        m_qs = m_qs.filter(title__icontains=show_title)
    if show_year:
        m_qs = m_qs.filter(year=show_year)
    if show_genres:
        genre_ids = Genre.objects.filter(name__in=show_genres).values_list('id', flat=True)
        m_qs = m_qs.filter(genre__in=genre_ids)

    print(m_qs)
    context = {
        'shows': m_qs
    }

    return render(request, "catalog/show/show_catalog.html", context=context)



class GenreListView(ListView):    
    model = Movie
    template_name = "catalog/movie/movies_by_genre.html"


    def get_queryset(self):
        genre_name = self.kwargs.get('genre')
        return Movie.objects.filter(genre__name__icontains=genre_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_name'] = _(self.kwargs.get('genre').capitalize())
        return context
    


class ShowGenreListView(ListView):    
    model = Show
    template_name = "catalog/show/shows_by_genre.html"


    def get_queryset(self):
        genre_name = self.kwargs.get('genre')
        return Show.objects.filter(genre__name__icontains=genre_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_name'] = _(self.kwargs.get('genre').capitalize())
        return context


def show_movie(request):
    return render(request, "catalog/movie/display_movie.html")


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    genre_names = ', '.join(genre.name for genre in movie.genre.all())
    context = {
        'movie': movie,
        'genre_list': genre_names,
    }
    
    return render(request, 'catalog/movie/movie_details.html', context)


def show_detail(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    genre_names = ', '.join(genre.name for genre in show.genre.all())
    context = {
        'show': show,
        'genre_list': genre_names,
    }
    
    return render(request, 'catalog/show/show_details.html', context)

# add titles

@login_required
def add_movie(request):
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
            # messages.success(request, "Filme adicionado com sucesso!", "alert-success alert-dismissible")
            
            return redirect('index')
            
        # else:
        #     messages.success(request, "Houve um erro ao registrar o filme. Tente novamente.", "alert-danger alert-dismissible")
    
    else:
        form = MovieForm()
    
    
    return render(request, "catalog/movie/add_movie.html", {"form": form})


@login_required
def add_show(request):
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
            
            return redirect('index')
                
    else:
        form = ShowForm()
    
    
    return render(request, "catalog/show/add_show.html", {"form": form})

