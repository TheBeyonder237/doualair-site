from django.contrib import admin
from .models import Service, Job, Candidat


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("Nom", "date_publiee", "date_mise_a_jour")
    search_fields = ("Nom",)
    list_filter = ("date_publiee",)
    ordering = ("-date_publiee",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("Nom", "Lieu", "Contrat", "Nombre", "Dateline", "date_publiee")
    search_fields = ("Nom", "Lieu")
    list_filter = ("Contrat", "date_publiee")
    ordering = ("-date_publiee",)


@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ("Nom", "Prenom", "Email", "Phone_number", "date_publiee")
    search_fields = ("Nom", "Email")
    list_filter = ("date_publiee",)
    ordering = ("-date_publiee",)

    """
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Titre', 'Statut', 'date_publiee', 'date_mise_a_jour')
    search_fields = ('Titre', 'Statut')
    list_filter = ('Statut', 'date_publiee')
    ordering = ('-date_publiee',)
    """
