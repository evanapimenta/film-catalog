from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .forms import MovieForm, ShowForm
from .models import Movie, Show, Genre


from django.db.models import Q

def show_all_movies(request):
    movies = Movie.objects.all()
    # series = Show.objects.all()

    # title = request.GET.get('title')
    # year = request.GET.get('year')
    # genres = request.GET.get('genre')

    # print(f"name: {title}")
    # print(f"year: {year}")
    # print(f"genres: {genres}")

    # filters = Q()

    # if filters:
    #     if title:
    #         filters &= Q(name__icontains=title)

    #     if year:
    #         filters &= Q(year=year)

    #     if genres:
    #         filters &= Q(genres__icontains=genres)

    #     movies = movies.filter(filters)

    context = {'movies': movies}

    return render(request, "movies/movie_catalog.html", context=context)


def show_movie(request):
    return render(request, "movies/display_movie.html")


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    genre_names = ', '.join(genre.name for genre in movie.genre.all())
    context = {
        'movie': movie,
        'genre_list': genre_names,
    }
    
    return render(request, 'movies/movie_details.html', context)

# add titles

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


@login_required
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


def filter_view(request):
    return render(request, 'movies/filter_sidebar.html', {})