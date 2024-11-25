from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["Titre", "Statut", "Image", "Description"]
        widgets = {
            "Titre": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",  # Plusieurs classes
                    "id": "name",
                    "placeholder": "Entrez le titre de l'article",
                }
            ),
            "Statut": forms.Select(attrs={"class": "form-control form-select"}),
            "Image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control form-control-file",  # Pour le style des fichiers
                    "multiple": False,
                }
            ),
            "Description": forms.Textarea(
                attrs={
                    "class": "form-control form-control-textarea",  # Classe personnalisée
                    "rows": 4,
                    "id": "message",
                    "placeholder": "Entrez la description de l'article",
                }
            ),
        }
