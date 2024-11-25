from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Pages
    path("", lambda request: redirect("home/", permanent=True)),
    path("home/", views.index, name="index"),
    path("about-us/", views.about, name="about_us"),
    path("contact-us/", views.contact, name="contact_us"),
    path("succes/", views.succes, name="succes"),
    
    # Services
    path("services/", views.list_services, name="services"),
    path("services/create/", views.create_service, name="create_service"),
    path("services/<int:pk>/detail/", views.detail_service, name="detail_service"),
    path("services/<int:pk>/update/", views.update_service, name="update_service"),
    path("services/<int:pk>/delete/", views.delete_service, name="delete_service"),
    
    # Job
    path("jobs/", views.job_list, name="jobs"),
    path("jobs/create/", views.job_create, name="job_create"),
    path("jobs/<int:job_id>/", views.job_detail, name="job_detail"),
    path("jobs/<int:job_id>/edit/", views.job_update, name="job_update"),
    path("jobs/<int:job_id>/delete/", views.job_delete, name="job_delete"),
    
    # Candidat
    path("candidats/", views.candidat_list, name="candidats"),
    path("candidats/create/", views.candidat_create, name="candidat_create"),
    path("candidats/<int:candidat_id>/", views.candidat_detail, name="candidat_detail"),
    path("candidats/<int:candidat_id>/edit/", views.candidat_update, name="candidat_update"),
    path("candidats/<int:candidat_id>/delete/", views.candidat_delete, name="candidat_delete"),
]
