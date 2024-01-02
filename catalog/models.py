from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Genre(models.Model):

    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return _(self.name)

    def get_absolute_url(self):
        return reverse("Genre_detail", kwargs={"pk": self.pk})


class Movie(models.Model):

    title = models.CharField(_("Title"), max_length=100)
    year = models.DateField(_("Release date"), auto_now=False, auto_now_add=False)
    genre = models.ManyToManyField(Genre, related_name='movie_genre')
    synopsis = models.TextField(_("Synopsis"),)
    poster = models.ImageField(_("Poster"), upload_to="static/images", max_length=None, blank=True)
    date_added = models.DateField(_("Date added"),auto_now_add=True)
    date_updated = models.DateField(_("Date updated"),auto_now=True)

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Movie_detail", kwargs={"pk": self.pk})
    
    

class Show(models.Model):
    title = models.CharField(_("Title"),max_length=50)
    year = models.DateField(_("Release date"),auto_now=False, auto_now_add=False)
    genre = models.ManyToManyField(Genre, related_name=_('show_genre'))
    synopsis = models.TextField(_("Synopsis"),)
    poster = models.ImageField(_("Poster"), upload_to='static/images', max_length=None, blank=True)
    date_added = models.DateField(_("Date added"),auto_now_add=True)
    date_updated = models.DateField(_("Date updated"),auto_now=True)

    class Meta:
        verbose_name = _("Show")
        verbose_name_plural = _("Shows")
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Show_detail", kwargs={"pk": self.pk})


class Catalog(models.Model):

    class Meta:
        verbose_name = _("Catalog")
        verbose_name_plural = _("Catalogs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Catalog_detail", kwargs={"pk": self.pk})
    