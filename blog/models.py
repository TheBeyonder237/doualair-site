from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    categorie = {"presse": _("Presse"), "actualité": _("Actualité")}

    Titre = models.CharField(
        max_length=100, verbose_name=_("Titre de l'article"), null=False
    )
    Statut = models.CharField(
        max_length=15,
        verbose_name=_("Catégorie de l'article"),
        choices=categorie.items(),
    )
    Image = models.ImageField(
        upload_to="article/", verbose_name=_("Image"), default="default/DOUALAIR.png"
    )
    Description = models.TextField(
        verbose_name=_("Description de l'article"), null=False
    )
    date_publiee = models.DateField(auto_now_add=True)
    date_mise_a_jour = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.Titre}"
