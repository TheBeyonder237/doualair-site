from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from blog.models import Article
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.http import HttpResponse


def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    services = Service.objects.all()[:3]
    jobs = Job.objects.all()[:3]
    articles = Article.objects.all()[:3]
    context = {
        "services": services,
        "jobs": jobs,
        "articles" : articles,
    }

    return render(request, "pages/custom_index.html", context=context)


def custom_404_view(request, exception):

    return render(request, "pages/errors/404.html", status=404)


def about(request):

    return render(request, "pages/custom_about.html")


def succes(request):
    return render(request, "pages/succes.html")



def contact(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.send_email()
                return render(request, "pages/succes.html")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return render(request, "pages/custom_contact.html", {'form': form, 'error': str(e)})
    else:
        form = ContactForm()
    return render(request, 'pages/custom_contact.html', {'form': form})


# CRUD pour Service
# Vue pour afficher la liste des services
def list_services(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    services = Service.objects.all()
    return render(request, "pages/services/list.html", {"services": services})


# Vue pour afficher les détails d'un service
def detail_service(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    service = get_object_or_404(Service, pk=pk)
    return render(request, "pages/services/detail.html", {"service": service})


# Vue pour créer un service
def create_service(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("services")
    else:
        form = ServiceForm()
    return render(request, "pages/services/form.html", {"form": form})


# Vue pour mettre à jour un service
def update_service(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect("services")
    else:
        form = ServiceForm(instance=service)
    return render(request, "pages/services/form.html", {"form": form})


# Vue pour supprimer un service
def delete_service(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect("services")


# CRUD pour Job
# Liste des emplois
def job_list(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    jobs = Job.objects.all()
    return render(request, "pages/careers/list.html", {"jobs": jobs})


# Détail d'un emploi
def job_detail(request, job_id):
    """_summary_

    Args:
        request (_type_): _description_
        job_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    job = get_object_or_404(Job, id=job_id)
    return render(request, "pages/careers/detail.html", {"job": job})


# Créer un emploi
def job_create(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jobs")
    else:
        form = JobForm()
    return render(request, "pages/careers/form.html", {"form": form})


# Modifier un emploi
def job_update(request, job_id):
    """_summary_

    Args:
        request (_type_): _description_
        job_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("job_detail", job_id=job.id)
    else:
        form = JobForm(instance=job)
    return render(request, "pages/careers/form.html", {"form": form})


# Supprimer un emploi
def job_delete(request, job_id):
    """_summary_

    Args:
        request (_type_): _description_
        job_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        job.delete()
        return redirect("jobs")
    # return render(request, 'careers/job_confirm_delete.html', {'job': job})
    return redirect("jobs")


# CRUD pour candidat
# Liste des candidatures
def candidat_list(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    candidats = Candidat.objects.all()
    return render(request, "pages/candidat/list.html", {"candidats": candidats})


# Détail d'un candidature
def candidat_detail(request, candidat_id):
    """_summary_

    Args:
        request (_type_): _description_
        candidat_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    candidat = get_object_or_404(Candidat, id=candidat_id)
    return render(request, "pages/candidat/detail.html", {"candidat": candidat})


# Créer une candidature
def candidat_create(request):
    """Création d'une instance de candidature à partir des données
    soumises via un formulaire
    
    Cette fonction traite les requêtes HTTP pour afficher un formulaire
    de création de candidat et pour enregistrer les données du candidat
    si le formulaire est valide

    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: _description_
    """
    if request.method == "POST":
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("about_us")
    else:
        form = CandidatForm()
    return render(request, "pages/candidat/form.html", {"form": form})


# Modifier une candidature
def candidat_update(request, candidat_id):
    """_summary_

    Args:
        request (_type_): _description_
        candidat_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    candidat = get_object_or_404(Candidat, id=candidat_id)
    if request.method == "POST":
        form = CandidatForm(request.POST, instance=candidat)
        if form.is_valid():
            form.save()
            return redirect("candidat_detail", candidat_id=candidat.id)
    else:
        form = CandidatForm(instance=candidat)
    return render(request, "pages/candidat/form.html", {"form": form})


# Supprimer une candidature
def candidat_delete(request, candidat_id):
    """_summary_

    Args:
        request (_type_): _description_
        candidat_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    candidat = get_object_or_404(Candidat, id=candidat_id)
    if request.method == "POST":
        candidat.delete()
        return redirect("candidats")
    # return render(request, 'candidat/candidat_confirm_delete.html', {'candidat': candidat})
    return redirect("candidats")


# Vue pour créer une candidature
def candidat(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("about_us")
    else:
        form = CandidatForm()
    return render(request, "pages/candidat/form.html", {"form": form})