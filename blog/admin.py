from django.contrib import admin
from .models import Article
from .forms import ArticleForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm  # Utiliser le formulaire personnalisé
    list_display = ("Titre", "Statut", "date_publiee", "date_mise_a_jour")
    search_fields = ("Titre", "Statut")
    list_filter = ("Statut", "date_publiee")
    ordering = ("-date_publiee",)

    # Optionnel : Personnaliser l'affichage du formulaire d'édition
    fieldsets = ((None, {"fields": ("Titre", "Statut", "Image", "Description")}),)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
