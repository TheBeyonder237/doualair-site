from django import forms
from .models import Service, Job, Candidat
from django.core.mail import send_mail
from django.template.loader import render_to_string


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nom")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

    def send_email(self):
        # Récupérer les données du formulaire
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]

        # Préparer l'objet et le corps de l'email
        subject = f"Nouveau message de {name}"
        body = render_to_string(
            "pages/custom_contact.html",
            {
                "name": name,
                "email": email,
                "message": message,
            },
        )

        # Envoyer l'email
        send_mail(
            subject=subject,
            message=message,  # Utiliser le message brut ici si nécessaire
            from_email=email,  # L'expéditeur est l'adresse email de l'utilisateur
            recipient_list=["contact@orizonne.net"],
            html_message=body,
            fail_silently=False,
        )


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["Nom", "Image", "Description"]
        widgets = {
            "Nom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le nom du service",
                }
            ),
            "Image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control-file",
                }
            ),
            "Description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Entrez la description du service",
                }
            ),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["Nom", "Lieu", "Contrat", "Nombre", "Dateline"]
        widgets = {
            "Nom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le nom du poste",
                }
            ),
            "Lieu": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le lieu de travail",
                }
            ),
            "Contrat": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "Nombre": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre de postes",
                }
            ),
            "Dateline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }


class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ["Nom", "Prenom", "House", "Phone_number", "Email", "Profession", "CV"]
        widgets = {
            "Nom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez votre nom",
                }
            ),
            "Prenom": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez votre prénom",
                }
            ),
            "House": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Résidence",
                }
            ),
            "Phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: +237696704865",
                }
            ),
            "Email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez votre email",
                }
            ),
            "Profession": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Votre profession actuelle",
                }
            ),
            "CV": forms.ClearableFileInput(
                attrs={
                    "class": "form-control-file",
                    "multiple": False,
                }
            ),
        }
