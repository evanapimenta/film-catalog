from django.contrib import admin
from .models import Movie, Show, Genre
from easy_select2 import select2_modelform

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Admin View for Movie'''
    form = select2_modelform(Movie)
    ordering = ('id',)

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    '''Admin View for Show'''
    ordering = ('id',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''Admin View for Genre'''

    ordering = ('name',)