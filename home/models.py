from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import os


class Service(models.Model):
    Nom = models.CharField(max_length=100, verbose_name=_("Nom du Service"), null=False)
    Image = models.ImageField(
        upload_to="services/",
        verbose_name=_("Représentation du Service"),
        default="default/DOUALAIR.png",
    )
    Description = models.TextField(verbose_name=_("Description du Service"), null=False)
    date_publiee = models.DateField(verbose_name=_("Date"), auto_now_add=True)
    date_mise_a_jour = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.Nom}"


class Job(models.Model):
    qualite = {
        "CDD": _("Contrat à durée déterminée"),
        "CDI": _("Contrat à durée indéterminée"),
        "Freelance": _("Freelance"),
    }

    Nom = models.CharField(max_length=200, verbose_name=_("Nom"))
    Lieu = models.CharField(max_length=150, verbose_name=_("Lieu de travail"))
    Contrat = models.CharField(
        max_length=15, verbose_name=_("Type de contrat"), choices=qualite.items()
    )
    Nombre = models.PositiveIntegerField(verbose_name=_("Nombre de postes"))
    Dateline = models.DateField()
    date_publiee = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.Nom}"


# fonction de validation de candidature
def validate_cv_file_extension(value):
    valid_extensions = [".pdf", ".doc", ".docx"]
    ext = os.path.splitext(value.name)[1]

    # Récupération de l'extension du fichier
    if ext.lower() not in valid_extensions:
        raise ValidationError("Le fichier doit être un PDF ou un document word.")


class Candidat(models.Model):
    # Vérification que le numéro sera ajouté normalement
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Le numéro de téléphone doit être au format : '+999999999'. Le numéro de téléphone doit contenir entre 9 et 15 chiffres.",
    )

    Nom = models.CharField(max_length=150, verbose_name=_("Nom"))
    Prenom = models.CharField(max_length=150, verbose_name=_("Prenom"), blank=True)
    House = models.CharField(max_length=150, verbose_name=_("Lieu de résidence"))
    Phone_number = models.CharField(
        max_length=30,
        validators=[phone_regex],
        blank=True,
        verbose_name=_("Numéro de téléphone"),
    )
    Email = models.EmailField(max_length=250, verbose_name=_("Email"), unique=True)
    Profession = models.CharField(max_length=100, verbose_name=_("Profession"))
    CV = models.FileField(
        upload_to="cvs/",
        validators=[validate_cv_file_extension],
        verbose_name=_("Curriculum Vitae"),
    )
    date_publiee = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.Nom} {self.Prenom}"
