from django.contrib import admin
from .models import Movie, Genre
from easy_select2 import select2_modelform

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Admin View for Movie'''
    form = select2_modelform(Movie)
    ordering = ('id',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''Admin View for Genre'''

    ordering = ('name',)