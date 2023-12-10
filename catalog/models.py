from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Genre(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Genre_detail", kwargs={"pk": self.pk})



class Movie(models.Model):

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.OneToOneField(Genre, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Movie_detail", kwargs={"pk": self.pk})



class Catalog(models.Model):

    

    class Meta:
        verbose_name = _("Catalog")
        verbose_name_plural = _("Catalogs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Catalog_detail", kwargs={"pk": self.pk})