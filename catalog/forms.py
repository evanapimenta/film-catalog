from django import forms

from easy_select2.widgets import Select2, Select2Multiple

from catalog.models import Movie, Genre

class MovieForm(forms.Form):
    movie_title = forms.CharField(label="Movie title", max_length=100)
    movie_year = forms.DateField(label="Year of release")
    movie_genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), required=False, widget=Select2Multiple(attrs={'data-width': '100%'}))
    movie_synopsis = forms.CharField(widget=forms.Textarea, label="Movie Synopsis")
    movie_poster = forms.ImageField(required=False)