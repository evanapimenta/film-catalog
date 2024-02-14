from django import forms
from django.utils.translation import gettext_lazy as _

from easy_select2.widgets import Select2, Select2Multiple

from catalog.models import Movie, Genre

default_poster = "catalog/no-image.jpg"

class MovieForm(forms.Form):
    movie_title = forms.CharField(label=_("Title"), max_length=100)
    movie_year = forms.IntegerField(label=_("Release date"))
    movie_genres = forms.ModelMultipleChoiceField(label=_("Genres"), queryset=Genre.objects.all(), required=False, widget=Select2Multiple(attrs={'data-width': '100%'}))
    movie_synopsis = forms.CharField(widget=forms.Textarea, label=_("Synopsis"))
    movie_poster = forms.ImageField(label=_("Poster"), required=False, initial=default_poster)


class ShowForm(forms.Form):
    show_title = forms.CharField(label=_("Show title"), max_length=100)
    show_year = forms.DateField(label=_("Release date"))
    show_genres = forms.ModelMultipleChoiceField(label=_("Genres"), queryset=Genre.objects.all(), required=False, widget=Select2Multiple(attrs={'data-width': '100%'}))
    show_synopsis = forms.CharField(widget=forms.Textarea, label=_("Synopsis"), max_length=None, required=False)
    show_poster = forms.ImageField(label=_("Poster"), required=False)